# Diego Enrique Jiménez Urgell
# This file contains classes that manage the game logic. There is a Game class and a Player class.

import pygame, math, os, csv
from pygame.locals import *
from Board import *


class Game:

    ''' This constructor creates a Game Object given a slot folder in which the game is going to be stored,
        and a boolean indicating if a new game is to be created or if the file contains information to be fetched. The
        name arguments may be empty for a saved game or passed as a string for new games'''
    def __init__(self,folder, tool, name1 = None, name2 = None):
        if not tool: # If a new game is created
            self.player_1 = Player(0, self) # Creating the two players, with their corresponding indexes. These are parameters of the class.
            self.player_2 = Player(1, self)
            name_file = open(folder + '/name.txt', 'w') # Writing the names of the players in the corresponding file on the given slot
            name_file.write(name1 + "\n")
            name_file.write(name2)
            name_file.close()
        else: # If the game is to be fetched from the file
            self.player_1 = Player(0, self, folder + "/chess_set_0.csv") # Creating hte players with a folder argument to retreive the info
            self.player_2 = Player(1, self, folder + "/chess_set_1.csv")

        self.board = Board()  # Creating the board object
        self.check = False # Setting some variables
        self.check_mate = False
        self.turn = True # A true turn is for the whites, a false is for the blacks
        self.playing = False # If a turn is being performed, intially this is False. When the first player clicks a piece, then it will be True
        self.click = None
        self.folder = folder # Saving the folder which represents the slot.
        with open(self.folder + "/name.txt") as doc:
            lines = doc.readlines()
            self.name_1 = lines[0]
            self.name_2 = lines[1] #Setting the names of the players as attributes
        pygame.display.set_caption(self.name_1 + " v.s. " + self.name_2)
        self.pieces_assign_square(self.player_1.get_chess_set())# Setting the pieces in the corresponding square
        self.pieces_assign_square(self.player_2.get_chess_set())

    ''' This method saves the game in the files of the corresponding slot '''
    def save_game(self):
        self.player_1.save_chess_set(self.folder+"/chess_set_0.csv")
        self.player_2.save_chess_set(self.folder + "/chess_set_1.csv")


    def render_game(self, display):
        """" This function calls the render methods of the board and player objects in order to draw the board and
            blit the pieces' images. """
        self.board.render_board(display)
        if self.turn:
            self.player_2.render_chess_set(display, self.click)
            self.player_1.render_chess_set(display, self.click)
        else:
            self.player_1.render_chess_set(display, self.click)
            self.player_2.render_chess_set(display, self.click)

    def start_turn(self, pos):
        """" This function gets the i-j index of the square in which the user clicked at the beginning of a turn, gets
            piece located in that particular square and sends the information to the Player class in order to manage
            the movement of the piece. The playing boolean is changed to True, which means that a player is making a
            movement"""

        i_index = math.floor((pos[0]-200)/100)
        j_index = math.floor((pos[1]-65)/100)
        self.click = [(pos[0]-200) % 100, (pos[1]-65) % 100]

        piece = self.board.get_piece_in_square(i_index, j_index)[0]

        valid_starting = False

        if self.turn:
            if self.player_1.start_move(piece):
                valid_starting = True
        else:
            if self.player_2.start_move(piece):
                valid_starting = True

        if valid_starting:
            self.playing = True

    def finish_turn(self, pos):
        """ This function is called only when the playing boolean is already True, si it manages the end of a movement.
        Once the player clicks on a piece and starts dragging it around the board, the next click will be the new
        position of the piece if the movement is valid. If the movement turns out to be legal, it will change the value
        of the playing boolean to False and will flip the Turn boolean"""

        valid = False
        i_index = math.floor((pos[0] - 200) / 100)
        j_index = math.floor((pos[1] - 65) / 100)

        if self.turn:
            if self.player_1.valid_move(i_index, j_index, self.board, self.player_2):
                self.player_1.finish_move(i_index, j_index, self.board)
                valid = True
        else:
            if self.player_2.valid_move(i_index, j_index, self.board, self.player_1):
                self.player_2.finish_move(i_index, j_index, self.board)
                valid = True

        if valid:
            self.playing = False
            self.turn = not self.turn
            self.pieces_assign_square(self.player_1.get_chess_set())
            self.pieces_assign_square(self.player_2.get_chess_set())

    def pieces_assign_square(self, chess_set):
        """This method must be called at the beginning of the game in the init method, and every time a movement is
         finished. It basically sinchronizes the board object with the given chess set of a player, so that the
         get_piece_in_square method of the Board class gives the appropriate piece when called"""
        for a in range(8):
            for each in chess_set[a]:
                if each is not None:
                    square = each.get_square()
                    self.board.set_piece_in_square(square[0], square[1], each)
                else:
                    None

    def get_playing(self):
        """This method is useful to know if a turn is taking place at the moment. It is mainly used to manage the clicks
        on the main loop of the game"""
        return self.playing

# This variable manages the players directions.
player_indexing = [[-7, 1], [0, 8]]

# This class represents a player with her chess set. It manages
class Player:

    """ This contstructor manages the creation of a new Player object. It needs a player number and a game object as parameters
        the file argument is passed if the data of the player's pieces is going to be fetched from a file rather than created
        at the starting positions. """
    def __init__(self, num, game, file = None):
        self.game = game
        self.num = num
        self.j_zero = player_indexing[num][0] # Saving the vertical max and min values in the board. It represents the player's
        self.j_max = player_indexing[num][1] # vertical range of movement and indirectly stores their direction.
        self.piece_moving = [None] #No piece is moving at the beginning
        self.moving = False # The player is not moving at the beginning
        if file is None: # If there is not a file and the game is new, then create the chess set. It is stored in a 2x8 matrix
                         # representing the two rows and the 8 columns of pieces.
            self.chess_set = [[Rook(num), Pawn(num)], [Knight(num), Pawn(num)], [Bishop(num), Pawn(num)], [Queen(num), Pawn(num)],
                              [King(num), Pawn(num)], [Bishop(num), Pawn(num)], [Knight(num), Pawn(num)], [Rook(num), Pawn(num)]]
            j_counter = self.j_zero # Setting the initial squares of the pieces. To do this, the min vertical position is used.
            for a in range(0, 8):
                for b in range(0, 2):
                    self.chess_set[a][b].set_square(a, abs(j_counter))
                    j_counter += 1
                j_counter = self.j_zero
        else: # If there is a file and the game needs to be fetched
            self.chess_set = []
            chess_file = open(file)
            chess_reader = csv.reader(chess_file)
            chess_list = list(chess_reader)
            print(chess_list)
            # A list similar to the other case is created, but the pieces and positions are "manually" set given the info on the file
            for i in range(0, len(chess_list), 2):
                tool = []
                for lista in range(i, i+2):
                    type = chess_list[lista][0]
                    if type == "pawn":
                        piece = Pawn(num)
                    elif type == "rook":
                        piece = Rook(num)
                    elif type == "bishop":
                        piece = Bishop(num)
                    elif type == "knight":
                        piece = Knight(num)
                    elif type == "queen":
                        piece = Queen(num)
                    elif type == "king":
                        piece = King(num)
                    else:
                        piece = None # If the set is incomplete because some pieces have been eaten.
                    if piece is not None:
                        piece.set_square(int(chess_list[lista][1]), int(chess_list[lista][2])) # Setting the square
                    tool.append(piece)
                self.chess_set.append(tool)

    """ This method saves the chess set of a player in a given file."""
    def save_chess_set(self, file):
        chess_file = open(file, "w", newline = '') # Openinig the given file
        chess_writer = csv.writer(chess_file) # Using the csv library
        for i in range(0, 8):
            for each in self.chess_set[i]: # For each space on the player's set matrix, if it is not empty, write the info of the piece
                if each is not None: # The info is printed with type, and the position.
                    chess_writer.writerow([each.get_type(), each.get_square()[0], each.get_square()[1]])
                else:
                    chess_writer.writerow("None") # If the space is emtpy, print "None"
        chess_file.close()

    # To get the chess set of a player
    def get_chess_set(self):
        return self.chess_set

    # To get the number of the player. 0 for whites, 1 for blacks.
    def get_num(self):
        return self.num

    # To draw the chess set on the board. It is called on every iteration of the main method.
    def render_chess_set(self, display, click_point):
        mouse = pygame.mouse.get_pos()
        for a in range(0, 8):
            for each in self.chess_set[a]: # For each piece in the chess set, draw it in the board
                if self.moving: # If player is in an active turn
                    if each != self.piece_moving[0]: # For every piece that IS NOT moving,
                        if each is not None:
                            pos = each.get_square() #Draw the piece on the corresponding place depnding on the piece's info
                            display.blit(each.get_image(), (pos[0] * 100 + 210, pos[1] * 100 + 85))
                    else:
                        None
                else:
                    if each is not None: # If the player is not in a turn, draw ALL the pieces according to their info
                        pos = each.get_square()
                        display.blit(each.get_image(), (pos[0] * 100 + 210, pos[1] * 100 + 85))
        # If the player was moving, the piece that is moving is drawn according to the current position of the mouse
        # This idea implements the drag and drop for the pieces.
        if self.moving:
            display.blit(self.piece_moving[0].get_image(), (mouse[0] - click_point[0], mouse[1] - click_point[1]))

    # Method that manages the start of a turn. It is called on the first click of a player if it is her current turn.
    def start_move(self, piece):
        valid_starting = False # Determining if the clicked tile really contains a piece and it is a valid spot
        for a in range(0, 8):
            if piece in self.chess_set[a]:
                self.moving = True
                self.piece_moving[0] = piece # If piece that is moving is in the player's set, then it is valid
                valid_starting = True
        if not valid_starting: # If it is not valid, play an error sound.
            error = pygame.mixer.Sound("Resources/error.wav")
            error.play()
        return valid_starting

    # Validate a movement of the player depending on the clicked piece.
    def valid_move(self, i, j, board, oponent):
        # Call the method to validate a piece's move given the intended coordinates in which the player wants to put the piece.
        valid = self.piece_moving[0].validate_move(i, j, board, self, oponent)
        if not valid:
            error = pygame.mixer.Sound("Resources/error.wav") # If it is not a valid movement, play an error sound.
            error.play()
        return valid

    # To finish a turn. This method is called after the movement verification.
    def finish_move(self, i, j, board):
        pos = self.piece_moving[0].get_square() # Update all the info of the piece.
        board.set_piece_in_square(pos[0], pos[1], None)
        self.piece_moving[0].set_square(i, j)
        self.piece_moving[0] = None
        self.moving = False

    # Method to kill a piece from the player's set, given the reference to the piece object that is to be removed.
    def kill_piece(self, piece):
        for a in range(0, 8):
            for b in range(len(self.chess_set[a])):
                if self.chess_set[a][b] == piece[0]: # When te piece is found, its space in the chess set matrix is change to None.
                    self.chess_set[a][b] = None
