import pygame as pg
import Sudoku
import Solver
import button

screen = pg.display.set_mode((750, 850))
pg.display.set_caption('Sudoku')


image = pg.image.load('SolveSprite.png').convert_alpha()
clearImage = pg.image.load('ClearSprite.png').convert_alpha()

solveButton = button.Button(10, 10, image)
clearButton = button.Button(150, 10, clearImage)

run = True
while run:
    screen.fill([0,0,0])
    
    Sudoku.SudokuBoard(750, 750, 60)

    if solveButton.draw(screen):
        Solver.backtrack(Sudoku.Board)
        
    if clearButton.draw(screen):

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    pg.display.update()
    
pg.quit()

    