import sys
import pygame as pg

pg.init()

font = pg.font.Font('Leaner-Thin.ttf', 60)

Board = [

    0,8,0,7,0,4,6,0,0,
    1,0,0,0,0,0,0,0,8,
    2,0,0,0,0,0,0,0,0,
    7,0,0,0,1,0,4,0,0,
    0,0,9,0,0,0,0,0,3,
    6,1,0,0,0,2,9,0,0,
    0,5,0,0,0,0,0,0,0,
    0,6,0,5,0,0,1,0,4,
    0,0,0,4,9,0,7,0,0

]

class SudokuBoard:
    def __init__(self, boardWidth, boardHeight, navBarHeight):
        self.boardWidth = boardWidth
        self.boardHeight = boardHeight
        self.navBarHeight = navBarHeight

        screen = pg.display.set_mode((boardWidth, boardHeight + navBarHeight))

        def draw_Board():
            screen.fill(pg.Color(255,255,255))
            pg.draw.rect(screen, pg.Color(0,0,0), pg.Rect(10, 10 + navBarHeight, 730, 730), 10)
            for i in range(80,720,80):
                pg.draw.line(screen, pg.Color(0,0,0), pg.Vector2(i + 15, 15 + navBarHeight), pg.Vector2(i + 15, 730 + navBarHeight), 5)
                pg.draw.line(screen, pg.Color(0,0,0), pg.Vector2(15, i + 15 + navBarHeight), pg.Vector2(730, i + 15 + navBarHeight), 5)


        def draw_numbers():
            for i in range(0,81,9):
                for j in range(0, 9):
                    output = Board[i + j]
                    if output != 0:
                        text = font.render(str(output), True, pg.Color(0,0,0))
                        screen.blit(text, pg.Vector2(((j * 80) + 40, (i/9 * 80) + navBarHeight + 20)))



        draw_Board()
        draw_numbers()
        pg.display.flip()



