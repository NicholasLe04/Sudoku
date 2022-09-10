import pygame as pg
import random
import Solver

pg.init()

font = pg.font.SysFont('verdana', 60)


class SudokuBoard:
    def __init__(self, boardWidth, boardHeight, navBarHeight):              #Constructor
        self.Board = [

            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,

        ]

        self.boardWidth = boardWidth
        self.boardHeight = boardHeight
        self.navBarHeight = navBarHeight

        screen = pg.display.set_mode((boardWidth, boardHeight + navBarHeight))
        
        screen.fill(pg.Color(255,255,255))

        def draw_Board():
            pg.draw.rect(screen, pg.Color(0,0,0), pg.Rect(10, 10 + navBarHeight, 730, 730), 10)
            for i in range(80,720,80):
                pg.draw.line(screen, pg.Color(0,0,0), pg.Vector2(i + 15, 15 + navBarHeight), pg.Vector2(i + 15, 730 + navBarHeight), 5)
                pg.draw.line(screen, pg.Color(0,0,0), pg.Vector2(15, i + 15 + navBarHeight), pg.Vector2(730, i + 15 + navBarHeight), 5)

        draw_Board()
        pg.display.flip()



    def generate_Board(self, numFilled):
            i = 0
            while i < numFilled:
                index = random.randint(0,80)
                num = random.randint(1,9)
                if self.Board[index] == 0 and Solver.validMove(self.Board, num, index):
                    self.Board[index] = num
                    i += 1


    def draw_numbers(self, screen):
        for i in range(0,81,9):
            for j in range(0, 9):
                output = self.Board[i + j]
                if output != 0:
                    text = font.render(str(output), True, pg.Color(0,0,0))
                    screen.blit(text, pg.Vector2(((j * 80) + 40, (i/9 * 80) + self.navBarHeight + 20)))
                else:
                    pg.draw.rect(screen, "White", pg.Rect(j*80 + 20, (i/9 * 80) + self.navBarHeight + 20, 70, 70))


    def clear_board(self, board):
        for i in range(len(board)):
            board[i] = 0

