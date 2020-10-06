# Diego Enrique Jiménez Urgell
# This file contains classes related to the physical part of the game. It includes a Square class to represent each tile,
# a Board class (which is basically a collection of Square objects), a Piece class which represents a generic piece,
# and classes for every type of piece: Pawn, Rook, King, Queen, Bishop, Knight.

import pygame
from pygame.locals import *

# Some colors in RGB used in the GUI
DARK_BROWN = (138, 77, 3)
LIGHT_BROWN = (214, 194, 169)
ARMY_GREEN = (142, 198, 96)
BLACK = (0, 0, 0)
WHITE = (128, 128, 128)


# This class is designed to represent a tile in the chess board. It also stores the current piece.
class Square:

    # A constructor of the square class. It initializes the attributes of the object, which include the color, the color when the
    # tiles is pressed, the initial piece, and the coordinates of the tile.
    def __init__(self, color_normal, color_pressed, piece, i, j):
        self.color_normal = color_normal
        self.color_pressed = color_pressed
        self.curr_color = color_normal
        self.piece = [piece]
        self.pos = [i, j]

    # to get the color of the tile
    def get_curr_color(self):
        return self.curr_color

    # to set the tile's state to "pressed"
    def set_pressed(self):
        self.curr_color = self.color_pressed

    # to set the tile's state to not pressed
    def set_not_pressed(self):
        self.curr_color = self.color_normal

    # to get the piece currently positioned at the tile
    def get_piece(self):
        return self.piece

    # to place a piece in the tile
    def set_piece(self, piece):
        self.piece = [piece]


# This class represents a board. It is a matrix of tiles, and also includes a method to draw them on the GUI.
class Board:

    # Constructor that initializes the matrix of tiles. Depending on the position of the tile, different colors are
    # set in order to create the pattern.
    def __init__(self):
        self.squares = []

        for i in range(0, 8):
            tool = []
            for j in range(0, 8):
                if (i + 1) % 2 == 0:
                    if (j + 1) % 2 == 0:
                        tool.append(Square(DARK_BROWN, ARMY_GREEN, None, i, j))
                    else:
                        tool.append(Square(LIGHT_BROWN, ARMY_GREEN, None, i, j))
                else:
                    if (j + 1) % 2 == 0:
                        tool.append(Square(LIGHT_BROWN, ARMY_GREEN, None, i, j))
                    else:
                        tool.append(Square(DARK_BROWN, ARMY_GREEN, None, i, j))
            self.squares.append(tool)

    # To retrieve the piece placed in a partiuclar tile
    def get_piece_in_square(self, i, j):
        piece = self.squares[i][j].get_piece()
        return piece

    # To set a piece on a particular tile
    def set_piece_in_square(self, i, j, piece):
        self.squares[i][j].set_piece(piece)

    # To draw the board on the GUI. It draws a square for each tile in the matrix, and fills with the corresponding color.
    def render_board(self, display):
        x_pos = 200
        y_pos = 75
        back_rect = pygame.Rect(170, 45, 860, 860)
        pygame.draw.rect(display, WHITE, back_rect)
        for a in range(len(self.squares)):
            for b in range(len(self.squares[a])):
                square_rect = pygame.Rect(x_pos, y_pos, 100, 100)
                square_disp = pygame.draw.rect(display, self.squares[a][b].get_curr_color(), square_rect)
                y_pos += 100
            y_pos = 75
            x_pos += 100


# This is a super class to represent a generic chess piece. It includes all the methods that the particular types of pieces
# must have. Some of them must be overrided.
class Piece:

    # Must be overriden with the particular attributes of the subclasses.
    def __init__(self, player):
        self.pos = [None, None]

    # To set the position
    def set_square(self, i, j):
        self.pos = [i, j]

    # To get the position
    def get_square(self):
        return self.pos

    # To get the image file
    def get_image(self):
        return self.image

    # Must be overriden in every subclass. Otherwise, all the movements are valid.
    def validate_move(self, i, j, board, player, oponent):
        return True

    # To get the type of piece
    def get_type(self):
        return self.type


# Class to represent a Pawn piece. It is a subclass of the Piece class.
class Pawn(Piece):

    # Constructor which initializes the class attributes with the Pawn specific values
    def __init__(self, player):
        self.type = "pawn"
        self.first_move = True # This class has this attribute to allow a double tile movement on the first move of the piece.
        if player == 0:
            self.image = pygame.transform.scale(pygame.image.load("Resources/pawn_white.png"), (80, 80))
        else:
            self.image = pygame.transform.scale(pygame.image.load("Resources/pawn_black.png"), (80, 80))
        super().__init__(player) # Create a super class object to inherit the methods.


    # This method overrides the movement validation, and implements a specific algorithm to validate pawn movements.
    def validate_move(self, i, j, board, player, oponent):

        i_original = self.get_square()[0]
        j_original = self.get_square()[1]

        # Determining the direction of the movement of the piece, given the player number.
        if player.get_num() == 0:
            op = -1
        else:
            op = +1

        valid = False
        if (j_original + op) == j: # Validating for simple movements
            if i_original == i:
                if board.get_piece_in_square(i, j)[0] is None:
                    valid = True
                    self.first_move = False
                else:
                    None
            elif i_original + 1 == i or i_original - 1 == i:
                if board.get_piece_in_square(i, j)[0] is not None:
                    bool = True
                    for a in range(0, 8):
                        for each in player.get_chess_set()[a]:
                            if each == board.get_piece_in_square(i, j)[0]:
                                bool = False
                                break
                    valid = bool
                    if valid:
                        oponent.kill_piece(board.get_piece_in_square(i, j))
        elif j_original + (2 * op) == j and i_original == i: # Validating for double moves
            if self.first_move:
                if board.get_piece_in_square(i, j_original + op)[0] is None and board.get_piece_in_square(i, j)[0] is None:
                    self.first_move = False
                    valid = True
                else:
                    None
        else:
            None
        return valid


# Subclass to implement the Rock piece. It's super class is Piece
class Rook(Piece):

    # Constructor for the Rook objects
    def __init__(self, player):
        self.type = "rook"
        if player == 0:
            self.image = pygame.transform.scale(pygame.image.load("Resources/rook_white.png"), (80, 80))
        else:
            self.image = pygame.transform.scale(pygame.image.load("Resources/rook_black.png"), (80, 80))
        super().__init__(player)

# Subclass to implement the Bishop piece. It's super class is Piece
class Bishop(Piece):

    # Constructor for the Bishop objects
    def __init__(self, player):
        self.type = "bishop"
        if player == 0:
            self.image = pygame.transform.scale(pygame.image.load("Resources/bishop_white.png"), (80, 80))
        else:
            self.image = pygame.transform.scale(pygame.image.load("Resources/bishop_black.png"), (80, 80))
        super().__init__(player)


# Subclass to implement the King piece. It's super class is Piece
class King(Piece):

    # Constructor for the King objects
    def __init__(self, player):
        self.type = "king"
        if player == 0:
            self.image = pygame.transform.scale(pygame.image.load("Resources/king_white.png"), (80, 80))
        else:
            self.image = pygame.transform.scale(pygame.image.load("Resources/king_black.png"), (80, 80))
        super().__init__(player)


# Subclass to implement the Queen piece. It's super class is Piece
class Queen(Piece):

    # Constructor for the Queen objects
    def __init__(self, player):
        self.type = "queen"
        if player == 0:
            self.image = pygame.transform.scale(pygame.image.load("Resources/queen_white.png"), (80, 80))
        else:
            self.image = pygame.transform.scale(pygame.image.load("Resources/queen_black.png"), (80, 80))
        super().__init__(player)


# Subclass to implement the Knight piece. It's super class is Piece
class Knight(Piece):

    # Constructor for the Knight objects
    def __init__(self, player):
        self.type = "knight"
        if player == 0:
            self.image = pygame.transform.scale(pygame.image.load("Resources/kinght_white.png"), (80, 80))
        else:
            self.image = pygame.transform.scale(pygame.image.load("Resources/kinght_black.png"), (80, 80))
        super().__init__(player)

    # This method overrides the movement validation, and implements a specific algorithm to validate knight movements.
    def validate_move(self, i, j, board, player, oponent):

        i_original = self.get_square()[0]
        j_original = self.get_square()[1]

        if player.get_num() == 0: # Determining the direction of movement
            op = -1
        else:
            op = +1

        valid = False

        if i_original + 2 == i or i_original - 2 == i:
            if j_original + 1 == j or j_original - 1 == j:
                if board.get_piece_in_square(i, j)[0] is None:
                    valid = True
                else:
                    tool = True
                    for a in range(0, 8):
                        for each in player.get_chess_set()[a]:
                            if each == board.get_piece_in_square(i, j)[0]:
                                tool = False
                                break
                    valid = tool
                    if valid:
                        oponent.kill_piece(board.get_piece_in_square(i, j))
        elif i_original + 1 == i or i_original - 1 == i:
            if j_original + 2 == j or j_original - 2 == j:
                if board.get_piece_in_square(i, j)[0] is None:
                    valid = True
                else:
                    tool = True
                    for a in range(0, 8):
                        for each in player.get_chess_set()[a]:
                            if each == board.get_piece_in_square(i, j)[0]:
                                tool = False
                                break
                    valid = tool
                    if valid:
                        oponent.kill_piece(board.get_piece_in_square(i, j))
        return valid
