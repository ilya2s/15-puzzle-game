# Jeu de Taquin
A fully functional implementation of the classic puzzle game "Taquin" using Python and the codeBoot library.

![Jeu du Taquin](https://user-images.githubusercontent.com/42526358/213894149-8d6d7ed5-fd12-455b-80cf-40cd1e5bdc75.png)

## Gameplay
The game is played on a square grid of tiles. Each tile is a small image of 16x16 pixels. The game begins with the tiles in a disordered state. The player can only slide a tile(s) towards the empty tile to change the position of the tiles and indirectly of the empty tile. The game ends when the tiles are in numerical order from left to right and top to bottom with the empty tile at the bottom right of the grid.

## Features

- Developed a fully functional version of the classic puzzle game "Taquin" using Python and codeBoot library.
- Utilized advanced programming concepts such as functions, procedures, algorithms and data structures to efficiently display and manipulate game elements.
- Implemented complex image processing techniques to display and manipulate game elements in real-time.
- Incorporated randomness and game logic to ensure a unique and challenging game experience for each playthrough.

## Requirements
- Python
- CodeBoot library
- tuiles.py file containing the images and color of the tiles

## Note
The game is not completely random because certain configurations of tiles are impossible to solve. To make sure the game is solvable, an algorithm is used for the initial placement of the tiles that ensures that the number of inversions, or the number of pairs of tiles that are out of order, is even. This ensures that the game is solvable and can be completed by the player.
