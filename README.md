# two-players-chess

A chess game for two players (in the same computer). It allows to save up to three games in order to finish them later. Movement validation is implemented for some pieces. Turn validation is implemented. All the buttons have different behaviour when the user hovers over them. To move the pieces in the chess board, drag and drop was developed. 

### Installing pygame library
In order to run the code, you must first install the Pygame library. Detailed instructions are available [here](https://www.pygame.org/wiki/GettingStarted).

### Acknowledgments 
The images of the pieces used for this game where created by JohnPablok, and are publicly available [here](https://opengameart.org/content/chess-pieces-and-board-squares) under a Creative Commons BY-SA 3.0 license. 

# How to play? 

## Main Menu
When you first run the code, the displayed window will show a main menu, in which you can either start a new game or load a saved game. Note that you can save up to three games. You cannot start a new game if all the three slots are already taken, and an alert sound will be played if you attempt to do so. The button "Nueva Partida" allows to create a new game, while the "Cargar Partida" should be clicked in order to load a game. The main menu looks like this: 

[![Chess-main-Menu.png](https://i.postimg.cc/0Qh4dywS/Chess-main-Menu.png)](https://postimg.cc/BLcNJsNZ)

## Load Game Menu
If you click the "Cargar Partida" button, then a new menu appears, containing the games saved in each one of the three available slots. To the left of each slot, there is a button which has the name of the players, in order to recognize the name. If you click in any of those buttons, the saved game will be fetched and you will be able to continue. However, if the button text is "Vacío" (Empty), an alert will sound. You can delete a saved game in order to free up a slot, by clicking on the button with the trash icon to the right of the slot. If you want to return to the main menu, you can click on the "Regresar" (return) button. 

[![Chess-load-Game.png](https://i.postimg.cc/j27HVzS8/Chess-load-Game.png)](https://postimg.cc/vxGgfx99)

## New Game Menu
If you were on the Main Menu and you click the "Nueva Partida" button, then another menu will be loaded, in which you can create a new game. In that menu, there is a textbox to type the name of the white pieces player ("Piezas blancas"), and another one to type the name of the black pieces player ("Piezas Negras"). Once you typed both names, you can click on the "Empezar" button in order to begin the game. If you want to return to the main menu, you can click on the "Regresar" (return) button. 

[![Chess-new-Game.png](https://i.postimg.cc/kXjbj1sn/Chess-new-Game.png)](https://postimg.cc/fJ9yyv1F)

## Game Scene
Once you either created a new game or loaded an existing one, the game scene will become visible. It will show the board with the pieces in their slots. To move a piece, you just have to click it, drag it to the desired slot, and drop it with a final click. The first player to move in a new game will always be the one with the white pieces. If the black pieces try to move on the first turn, and alert will sound and the piece will return to its original place. After the white pieces finish moving, the turn will be of the black pieces, and so on. There is movement validation for some pieces (currently the pawn and the horse), and if a player tries to move a piece to an invalid slot, an alert will sound and the piece will return to its original place. You can eat a piece from your oppnonet simply by dropping your piece in the same slot. At any moment, you can save the game by clicking on the blue button at the top right corner. 

[![Chess-start.png](https://i.postimg.cc/jdkhWdGQ/Chess-start.png)](https://postimg.cc/Vdntp1sd)

[![Chess-playing.png](https://i.postimg.cc/7Yp28CFc/Chess-playing.png)](https://postimg.cc/3dFR2wJC)
