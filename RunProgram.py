import pygame as pg
import Sudoku
import button
import Solver

#Screen 
screen = pg.display.set_mode((750, 850))
pg.display.set_caption('Sudoku')

#Buttons
solveButton = button.Button((200, 100, 250), 10, 10, 100, 50, 'Solve')
clearButton = button.Button((200, 100, 250), 130, 10, 100, 50, 'Clear')
generateButton = button.Button((200, 100, 250), 250, 10, 100, 50, 'Generate')

#Create SudokuBoard Object
gameboard = Sudoku.SudokuBoard(750, 750, 60)

run = True
while run:

    #Draw buttons to screen
    clearButton.draw(screen, (0,0,0))
    solveButton.draw(screen, (0,0,0))
    generateButton.draw(screen, (0,0,0))

    for event in pg.event.get():
        pos = pg.mouse.get_pos()

        if event.type == pg.QUIT:
            run = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if solveButton.isOver(pos):                     #Click Solve Button
                if not Solver.backtrack(gameboard.Board):
                    print("Unable to evaluate a solution")
            
            if clearButton.isOver(pos):                     #Click Clear Button
                gameboard.clear_board(gameboard.Board)

            if generateButton.isOver(pos):                  #Click Generate Button
                gameboard.generate_Board(17)

         
    gameboard.draw_numbers(screen)
    pg.display.update()
    
pg.quit()

    