# README: The Game Of Life

This project is a visual representation of John Conway's 'Game Of Life'. More information about the Game Of Life can be found [here](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

## How the game is played

### Background information

When the program is run a window pops up with a 2D board of squares. Each square in the board is known as a cell, and it can have two states: dead (coloured black) or alive (coloured white).

At the beginning of the game, whether a cell is dead or alive is assigned at random. At each frame of the game the state of each cell is updated according to Conway's [rules](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Rules).

### Interaction with the game

While the game is a zero player game, interaction with the program is possible. The following actions can be performed:

* SPACE BAR: Restarts the game by randomising the state of each cell
* P: Pauses the game. Pressing P again will resume the game if it is paused.
* MOUSE CLICK: Changes the state of a dead cell to a live cell.

To experiment with the possible patterns that are formed in the Game Of Life it is recommended to pause the game by pressing P and then changing the state of dead cells by clicking on them with the mouse.

A GIF of the project is attached below:

![The Game Of Life](https://github.com/Javierfg02/The-Game-Of-Life/blob/master/game%20of%20life.gif)
