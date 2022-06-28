import pygame as pg
import Sudoku
import button
import Solver

screen = pg.display.set_mode((750, 850))
pg.display.set_caption('Sudoku')


solveButton = button.Button((200, 100, 250), 10, 10, 100, 50, 'Solve')
clearButton = button.Button((200, 100, 250), 130, 10, 100, 50, 'Clear')
generateButton = button.Button((200, 100, 250), 250, 10, 100, 50, 'Generate')


gameboard = Sudoku.SudokuBoard(750, 750, 60)

run = True
while run:

    clearButton.draw(screen, (0,0,0))
    solveButton.draw(screen, (0,0,0))
    generateButton.draw(screen, (0,0,0))

    for event in pg.event.get():
        pos = pg.mouse.get_pos()

        if event.type == pg.QUIT:
            run = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if solveButton.isOver(pos):
                if not Solver.backtrack(gameboard.Board):
                    print("Unable to evaluate a solution")
            
            if clearButton.isOver(pos):
                gameboard.clear_board(gameboard.Board)

            if generateButton.isOver(pos):
                gameboard.generate_Board(17)

         
    gameboard.draw_numbers(screen)
    pg.display.update()
    
pg.quit()

    