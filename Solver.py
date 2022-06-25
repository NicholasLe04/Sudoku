import math
import pygame
import time

SubBoxes = [
 
        [0,  1,  2,
        9,  10, 11, 
        18, 19, 20],

        [27, 28, 29,
        36, 37, 38,
        45, 46, 47],

        [54, 55, 56,
        63, 64, 65,
        72, 73, 74],

        [3,  4,  5,
        12, 13, 14,
        21, 22, 23],

        [30, 31, 32,
        39, 40, 41,
        48, 49, 50],

        [57, 58, 59,
        66, 67, 68,
        75, 76, 77],

        [6,  7,  8,
        15, 16, 17,
        24, 25, 26],

        [33, 34, 35,
        42, 43, 44,
        51, 52, 53],

        [60, 61, 62,
        69, 70, 71,
        78, 79, 80],

    ]

def areDistinct(self, array):
        n = len(array)

        s = set()
        for i in range(0, n):
            s.add(array[i])

        return(len(s) == len(array))


def distinctInRow(board, num, position):
        start = 9 * math.floor(position/9)
        for i in range(start, start + 9):
            if board[i] == num:
                return False
        return True 


def distinctInColumn(board, num, position):
        for i in range(position % 9, 81, 9):
            if board[i] == num:
                return False
        return True


def distinctInBox(board, num, position):
        check = -1

        for i in range(0,9):
            for j in SubBoxes[i]:
                if j == position:
                    check = i
                    break

        for k in SubBoxes[check]:
            if board[k] == num:
                return False

        return True


def checkBoard(board):

        #check for missing numbers
        for num in board:
            if num == 0: 
                return False

        #check rows
        for i in range(0, 81, 9):
            if not areDistinct(board[i:i+9]):
                return False

        #check columns
        col = []
        for j in range(0, 9):
            for k in range(0, 81, 9):
                col.append(board[j+k])

            if not areDistinct(col):
                return False

            col.clear()

        #check boxes
        box = []
        for subbox in SubBoxes:
            for pos in subbox:
                box.append(board[pos])

            if not areDistinct(box):
                return False

            box.clear()

        return True


def printBoard(board):
    for i in range(0, 81, 9):
        print(board[i:i+9])

def validMove(board, number, position):
    if distinctInBox(board, number, position) and distinctInRow(board, number, position) and distinctInColumn(board, number, position):
        return True

    return False

def backtrack(board):
    position = -1
    solved = True

    for pos in range(0,81):
        if board[pos] == 0:
            position = pos
            solved = False
            break

    if solved:
        print("Solved!")
        return True

    for num in range (1, 10):
        if validMove(board, num, position):
            board[position] = num
            if backtrack(board):
                return True

            board[position] = 0

    return False

#EXECUTE






""" x = input("Input the board in a long string (ex: 1234567892345...): ")
for i in range(0,81):
    Board[i] = int(x[i]) """

 

#print(SudokuBoard.checkRows(Board))



""" 
Easy:
    3,5,1,6,7,2,9,8,4,
    0,0,0,8,0,1,2,5,7,
    2,8,7,0,0,0,6,1,3,
    0,9,2,0,0,5,3,7,8,
    8,0,0,7,0,0,0,0,0,
    0,0,4,9,2,0,5,0,0,
    1,0,0,0,0,6,0,0,5,
    0,0,6,0,5,0,8,0,0,
    5,7,3,2,0,4,0,0,0
 """

""" Expert:
    0,8,0,7,0,4,6,0,0,
    1,0,0,0,0,0,0,0,8,
    2,0,0,0,0,0,0,0,0,
    7,0,0,0,1,0,4,0,0,
    0,0,9,0,0,0,0,0,3,
    6,1,0,0,0,2,9,0,0,
    0,5,0,0,0,0,0,0,0,
    0,6,0,5,0,0,1,0,4,
    0,0,0,4,9,0,7,0,0 """