from re import I

from pyparsing import col
import Sudoku

SudokuBoard = Sudoku.Sudoku()

Board = [
    
        1,2,3,6,7,8,9,4,5,
        5,8,4,2,3,9,7,6,1,
        9,6,7,1,4,5,3,2,8,
        3,7,2,4,6,1,5,8,9,
        6,9,1,5,8,3,2,7,4,
        4,5,8,7,9,2,6,1,3,
        8,3,6,9,2,4,1,5,7,
        2,1,9,8,5,7,4,3,6,
        7,4,5,3,1,6,8,9,2

    ]

def printBoard(board):
    for i in range(0, 81, 9):
        print(board[i:i+9])
        

def backtrackAlgo(board, position):
    if position == 81:
        return True

    if board[position] > 0:
        return backtrackAlgo(board, position + 1)

    for num in range (1, 10):
        board[position] = num
        if SudokuBoard.checkBoard(board):
            if backtrackAlgo(board, position + 1):
                return True

        board[position] = 0

    return False

if(backtrackAlgo(Board, 0)):
    printBoard(Board)
else:
    print("gg")


#print(SudokuBoard.checkRows(Board))