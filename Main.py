# Diego Enrique Jiménez Urgell
# This file contains the main method, which manages the game's user interface and the actions that have to be performed
# depending on their actions.

import pygame, sys
from pygame.locals import *
from Game import Game


pygame.init()

# Color definition
LIGHT_GREEN = (224, 230, 190)
DARK_BLUE = (46, 155, 255)
LIGHT_BLUE = (117, 189, 255)
DARK_ORANGE = (222, 125, 0)
LIGHT_ORANGE = (252, 161, 43)
BLACK = (0, 0, 0)
DARK = (210, 210, 210)
LIGHT = (155, 155, 155)
DARK_MAGENTA = (214, 35, 203)
LIGHT_MAGENTA = (240, 105, 231)
DARK_GOLD = (202, 166, 18)
LIGHT_GOLD = (253,208,23)
DARK_RED = (203,0,0)
LIGHT_RED = (254,0,1)

# In the main method, the Graphical User Interface was coded, along with the event listeners and handlers. The JavaFX
# concept of scenes was implemented by separating the code with 4 if-elif statements corresponding to a particular value
# of the "scene" variable. At the beginning, scene equals 0, and the initial menu is displayed. Depending on the user's
# actions, the scene is changed to a different value and different grpahical elements are displayed. Regarding the responsiveness
# of the interface, the buttons change color when the mouse hovers above them, and the chess pieces support drag and drop
# for the movement.

scene = 0 # Initial value of the scene
FPS = 240
fpsClock = pygame.time.Clock()

name_1 = ""
name_2 = ""
writing_1 = False
writing_2 = False

save = False

while True:

    if scene == 0: # Graphical Interface for the starting menu

        # Creating the graphical elements and customizing the window.
        DISPLAY = pygame.display.set_mode((600, 450), 0, 32)

        DISPLAY.fill((224, 230, 190))
        pygame.display.set_caption("Chess")

        # Menu title
        font = pygame.font.Font("freesansbold.ttf", 50)
        tile = font.render("Ajedrez", True, BLACK)
        title_rect = tile.get_rect(x=200, y=50)
        DISPLAY.blit(tile, title_rect)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        # New game button with its event listener
        slot2_rectangle = pygame.Rect(125, 160, 350, 80)
        if 125 <= mouse_pos[0] <= 475 and 160 <= mouse_pos[1] <= 240: # To manage the color of the button depending on the mouse position
            slot2_button = pygame.draw.rect(DISPLAY, LIGHT_BLUE, slot2_rectangle)
            if mouse_pressed[0]:
                scene = 1 # Change the scene if this button was pressed.
            else:
                None
        else:
            slot2_button = pygame.draw.rect(DISPLAY, DARK_BLUE, slot2_rectangle)

        return_text = pygame.font.Font("freesansbold.ttf", 35)
        slot2_button_text = return_text.render("Nueva Partida", True, BLACK) # Text of the button
        slot2_render = slot2_button_text.get_rect(x=180, y=185)
        DISPLAY.blit(slot2_button_text, slot2_render)

        # Get game button with its event listener
        charge_game_rectangle = pygame.Rect(125, 290, 350, 80)
        if 125 <= mouse_pos[0] <= 475 and 290 <= mouse_pos[1] <= 370: # To manage the color of the button depending on the mouse position
            charge_game_button = pygame.draw.rect(DISPLAY, LIGHT_ORANGE, charge_game_rectangle)
            if mouse_pressed[0]:
                scene = 3 # Change the scene if this button was pressed.
            else:
                None
        else:
            charge_game_button = pygame.draw.rect(DISPLAY, DARK_ORANGE, charge_game_rectangle)

        charge_game_text = pygame.font.Font("freesansbold.ttf", 35)
        charge_game_text_surface = charge_game_text.render("Cargar Partida", True, BLACK)  # Text of the button
        charge_game_text_rect = charge_game_text_surface.get_rect(x=170, y=310)
        DISPLAY.blit(charge_game_text_surface, charge_game_text_rect)

        # Managing the user quitting the game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    # Graphical User Interface for the menu of the new game creation.
    elif scene == 1:

        # Customizing the window
        DISPLAY = pygame.display.set_mode((600, 450), 0, 32)

        DISPLAY.fill((224, 230, 190))
        pygame.display.set_caption("Chess")
        font1 = pygame.font.Font("freesansbold.ttf", 35)

        title = font1.render("Nombres de los jugadores", True, BLACK)
        title_rect = title.get_rect(x=90, y=25)
        DISPLAY.blit(title, title_rect)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        # White pieces label
        font = pygame.font.Font("freesansbold.ttf", 30)

        player1_label = font.render("Piezas blancas:", True, BLACK)
        player1_label_rect = player1_label.get_rect(x=20, y=140)
        DISPLAY.blit(player1_label, player1_label_rect)

        # White pieces textbox for the player to write her name 
        player1_textbox = pygame.Rect(260, 120, 300, 65)
        if 260 <= mouse_pos[0] <= 560 and 120 <= mouse_pos[1] <= 185 or writing_1:
            player1_button = pygame.draw.rect(DISPLAY, LIGHT, player1_textbox) # Managinig the color of the textbox depending on the mouse
            if mouse_pressed[0]:
                writing_1 = True
                writing_2 = False # To determine in which textbox the user is writting
            else:
                None
        else:
            player1_button = pygame.draw.rect(DISPLAY, DARK, player1_textbox)
        slot2_button_text = font.render(name_1, True, BLACK)
        slot2_render = slot2_button_text.get_rect(x=280, y=140)
        DISPLAY.blit(slot2_button_text, slot2_render)

        # Black pieces label
        player2_label = font.render("Piezas negras: ", True, BLACK)
        player2_label_rect = player2_label.get_rect(x=20, y=250)
        DISPLAY.blit(player2_label, player2_label_rect)

        # Black pieces textbox for the user to write her name 
        player2_textbox = pygame.Rect(260, 230, 300, 65)
        if 260 <= mouse_pos[0] <= 560 and 230 <= mouse_pos[1] <= 295 or writing_2:
            player2_button = pygame.draw.rect(DISPLAY, LIGHT, player2_textbox)
            if mouse_pressed[0]:
                writing_1 = False
                writing_2 = True
            else:
                None
        else:
            player2_button = pygame.draw.rect(DISPLAY, DARK, player2_textbox)
        player2_text = font.render(name_2, True, BLACK)
        player2_render = player2_text.get_rect(x=280, y=250)
        DISPLAY.blit(player2_text, player2_render)

        # Start game button with its event listener and handler
        slot2_rectangle = pygame.Rect(50, 350, 200, 80)
        if 50 <= mouse_pos[0] <= 250 and 350 <= mouse_pos[1] <= 430:
            slot2_button = pygame.draw.rect(DISPLAY, LIGHT_BLUE, slot2_rectangle)
            if mouse_pressed[0]:
                if name_1 != "" and name_2 != "": # If the name texfields are not empty
                    directory = None
                    for i in range(1, 4): # Determining if there is an empty slot to play a new game
                        if directory is None:
                            with open("Slot" + str(i) + "/name.txt") as doc:
                                lines = doc.readlines()
                                if not lines:
                                    directory = "Slot" + str(i)
                    if directory is None:
                        error = pygame.mixer.Sound("Resources/error.wav")
                        error.play()
                    else:
                        scene = 2 # If there is a slot, change scene and create a new game.
                        game = Game( directory, False, name_1, name_2)
                else:
                    error = pygame.mixer.Sound("Resources/error.wav")
                    error.play()
            else:
                None
        else:
            slot2_button = pygame.draw.rect(DISPLAY, DARK_BLUE, slot2_rectangle)
        return_text = pygame.font.Font("freesansbold.ttf", 35)
        slot2_button_text = return_text.render("Empezar", True, BLACK)
        slot2_render = slot2_button_text.get_rect(x=75, y=370)
        DISPLAY.blit(slot2_button_text, slot2_render)

        # Return to main menu button with its event handler
        slot2_rectangle = pygame.Rect(330, 350, 200, 80)
        if 330 <= mouse_pos[0] <= 530 and 350 <= mouse_pos[1] <= 430:
            slot2_button = pygame.draw.rect(DISPLAY, LIGHT_ORANGE, slot2_rectangle)
            if mouse_pressed[0]:
                name_1 = "" # Cleaning the textboxes
                name_2 = ""
                writing_1 = False # Setting the writing status of both textboxes as false.
                writing_2 = False
                scene = 0
            else:
                None
        else:
            slot2_button = pygame.draw.rect(DISPLAY, DARK_ORANGE, slot2_rectangle)
        return_text = pygame.font.Font("freesansbold.ttf", 35)
        slot2_button_text = return_text.render("Regresar", True, BLACK)
        slot2_render = slot2_button_text.get_rect(x=350, y=370)
        DISPLAY.blit(slot2_button_text, slot2_render)

        # Managing a user quitting the game and typing
        for event in pygame.event.get():
            if event.type == QUIT: # Quitting the game
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE: # Deleting, depending on the booleans.
                    if writing_1:
                        name_1 = name_1[0:len(name_1) - 1]
                    elif writing_2:
                        name_2 = name_2[0:len(name_2) - 1]
                elif event.key == K_RETURN: # Pressing enter to start the game
                    if name_1 != "" and name_2 != "":
                        scene = 2
                        game = Game(name_1, name_2, DISPLAY)
                    else:
                        error = pygame.mixer.Sound("Resources/error.wav")
                        error.play()
                else: # Writing on the textbox, depending on the booleans.
                    if writing_1:
                        name_1 = name_1 + event.unicode
                    elif writing_2:
                        name_2 = name_2 + event.unicode

    # Graphical User interface for the scene of the game. This is the one in which the board is drawn and the pieces move. 
    elif scene == 2:
        
        # Customizing the window
        DISPLAY = pygame.display.set_mode((1200, 950), 0, 32)
        table = pygame.transform.scale(pygame.image.load("Resources/table.jpg"), (1200, 950)).convert()
        table.set_alpha(240)
        DISPLAY.blit(table, (0, 0))

        save_image = pygame.transform.scale(pygame.image.load("Resources/save.png"), (70, 70)).convert_alpha()
        mouse_pos = pygame.mouse.get_pos()

        # Save button and its event handler
        save_rectangle = pygame.Rect(20, 65, 80, 80)
        if 20 <= mouse_pos[0] <= 100 and 65 <= mouse_pos[1] <= 145:
            save_button = pygame.draw.rect(DISPLAY, LIGHT_BLUE, save_rectangle)
            if mouse_pressed[0]:
                save = True
                game.save_game()
            else:
                None
        else:
            save_button = pygame.draw.rect(DISPLAY, DARK_BLUE, save_rectangle)
        DISPLAY.blit(save_image, (25, 70))

        # Managing a player quitting the game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Managing a turn. This is closely related with the Game class
        if game.get_playing():
            if pygame.mouse.get_pressed()[0]: # THe second click ends a turn
                if 200 < pygame.mouse.get_pos()[0] < 1000 and 65 < pygame.mouse.get_pos()[1] < 865:
                    mouse_pos = pygame.mouse.get_pos()
                    game.finish_turn(mouse_pos)
        else:
            if pygame.mouse.get_pressed()[0]: # The first click starts a turn
                if 200 < pygame.mouse.get_pos()[0] < 1000 and 65 < pygame.mouse.get_pos()[1] < 865:
                    mouse_pos = pygame.mouse.get_pos()
                    game.start_turn(mouse_pos)
        game.render_game(DISPLAY)

    # Graphical Interface of the scene in which a saved game is fetched or deleted. This is managed by having three different slots. 
    elif scene == 3:
        DISPLAY = pygame.display.set_mode((600, 450), 0, 32)

        DISPLAY.fill((224, 230, 190))
        pygame.display.set_caption("Chess")

        return_text = pygame.font.Font("freesansbold.ttf", 35)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        #Slot 1 button and its handler
        slot1_rectangle = pygame.Rect(80, 35, 350, 70)
        if 80 <= mouse_pos[0] <= 430 and 35 <= mouse_pos[1] <= 105:
            slot1_button = pygame.draw.rect(DISPLAY, LIGHT_BLUE, slot1_rectangle)
            if mouse_pressed[0]:
                game = Game("Slot1", True) # If the user clicks on this button, then a game is created with the first slot as a parameter
                scene = 2 # Change the scene to the game board
            else:
                None
        else:
            slot2_button = pygame.draw.rect(DISPLAY, DARK_BLUE, slot1_rectangle)
        with open("Slot1/name.txt") as doc: # Setting the text on the buttton
            lines = doc.readlines()
            if not lines:
                slot1_button_text = return_text.render("Vacio", True, BLACK)  # If the slot is empty
                slot1_render = slot1_button_text.get_rect(x=190, y=50)
            else: # If there is a game saved in that slot
                slot1_button_text = return_text.render(str(lines[0])[:-1] + " v.s. " + str(lines[1]), True, BLACK)
                slot1_render = slot1_button_text.get_rect(x=100, y=50)

        DISPLAY.blit(slot1_button_text, slot1_render)

        # Slot 2 button and its handler
        slot2_rectangle = pygame.Rect(80, 140, 350, 70)
        if 80 <= mouse_pos[0] <= 430 and 140 <= mouse_pos[1] <= 230:
            slot2_button = pygame.draw.rect(DISPLAY, LIGHT_MAGENTA, slot2_rectangle)
            if mouse_pressed[0]:
                game = Game("Slot2", True) # Fetching the game if the user presses it.
                scene = 2
            else:
                None
        else:
            slot2_button = pygame.draw.rect(DISPLAY, DARK_MAGENTA, slot2_rectangle)
        with open("Slot2/name.txt") as doc: # Setting the text on the button
            lines = doc.readlines()
            if not lines:
                slot2_button_text = return_text.render("Vacio", True, BLACK) # If the slot file is empty
                slot2_render = slot2_button_text.get_rect(x=190, y=160)
            else: # If there is a saved game in the slot
                slot2_button_text = return_text.render(str(lines[0])[:-1] + " v.s. " + str(lines[1]), True, BLACK)
                slot2_render = slot2_button_text.get_rect(x=100, y=160)
        DISPLAY.blit(slot2_button_text, slot2_render)

        #Slot 3 button and its handler
        slot3_rectangle = pygame.Rect(80, 250, 350, 70)
        if 80 <= mouse_pos[0] <= 430 and 250 <= mouse_pos[1] <= 320:
            slot3_button = pygame.draw.rect(DISPLAY, LIGHT_GOLD, slot3_rectangle)
            if mouse_pressed[0]:
                game = Game("Slot3", True) # Fetching the game if the user presses it.
                scene = 2
            else:
                None
        else:
            slot3_button = pygame.draw.rect(DISPLAY, DARK_GOLD, slot3_rectangle)
        with open("Slot3/name.txt") as doc: # Setting the text on the button
            lines = doc.readlines()
            if not lines:
                slot3_button_text = return_text.render("Vacio", True, BLACK) # If the slot file is empty
                slot3_render = slot3_button_text.get_rect(x=190, y=265)
            else: # If there is a saved game in the slot
                slot3_button_text = return_text.render(str(lines[0])[:-1] + " v.s. " + str(lines[1]), True, BLACK)
                slot3_render = slot3_button_text.get_rect(x=100, y=265)
        DISPLAY.blit(slot3_button_text, slot3_render)

        trash_image = pygame.transform.scale(pygame.image.load("Resources/trash.png"), (60, 60)).convert_alpha()

        #Delete 1 button and its handler
        slot1_delete_rectangle = pygame.Rect(431, 35, 70, 70)
        if 431 <= mouse_pos[0] <= 502 and 35 <= mouse_pos[1] <= 105:
            slot1_delete_button = pygame.draw.rect(DISPLAY, LIGHT_RED, slot1_delete_rectangle)
            if mouse_pressed[0]:
                scene = 1
            else:
                None
        else:
            slot1_delete_button = pygame.draw.rect(DISPLAY, DARK_RED, slot1_delete_rectangle)
        DISPLAY.blit(trash_image, (436, 41))

        # Delete 2 button and its handler
        slot2_delete_rectangle = pygame.Rect(431, 140, 70, 70)
        if 431 <= mouse_pos[0] <= 502 and 140 <= mouse_pos[1] <= 210:
            slot2_delete_button = pygame.draw.rect(DISPLAY, LIGHT_RED, slot2_delete_rectangle)
            if mouse_pressed[0]:
                scene = 1
            else:
                None
        else:
            slot2_delete_button = pygame.draw.rect(DISPLAY, DARK_RED, slot2_delete_rectangle)
        DISPLAY.blit(trash_image, (436, 145))

        # Delete 3 button and its handler
        slot3_delete_rectangle = pygame.Rect(431, 250, 70, 70)
        if 431 <= mouse_pos[0] <= 502 and 250 <= mouse_pos[1] <= 320:
            slot3_delete_button = pygame.draw.rect(DISPLAY, LIGHT_RED, slot3_delete_rectangle)
            if mouse_pressed[0]:
                scene = 1
            else:
                None
        else:
            slot3_delete_button = pygame.draw.rect(DISPLAY, DARK_RED, slot3_delete_rectangle)
        DISPLAY.blit(trash_image, (436, 255))

        # Return to main menu button and its handler
        slot2_rectangle = pygame.Rect(180, 350, 200, 80)
        if 180 <= mouse_pos[0] <= 380 and 350 <= mouse_pos[1] <= 430:
            slot2_button = pygame.draw.rect(DISPLAY, LIGHT_ORANGE, slot2_rectangle)
            if mouse_pressed[0]:
                scene = 0
            else:
                None
        else:
            slot2_button = pygame.draw.rect(DISPLAY, DARK_ORANGE, slot2_rectangle)
        return_text = pygame.font.Font("freesansbold.ttf", 35)
        slot2_button_text = return_text.render("Regresar", True, BLACK)
        slot2_render = slot2_button_text.get_rect(x=200, y=370)
        DISPLAY.blit(slot2_button_text, slot2_render)

        # Managing the user quitting the game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    fpsClock.tick(FPS) # Setting the FPS
    pygame.display.update() # To update the GUI