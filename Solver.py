import Sudoku

SudokuBoard = Sudoku.Sudoku()

Board = [

        3,5,1,6,7,2,9,8,4,
        0,0,0,8,0,1,2,5,7,
        2,8,7,0,0,0,6,1,3,
        0,9,2,0,0,5,3,7,8,
        8,0,0,7,0,0,0,0,0,
        0,0,4,9,2,0,5,0,0,
        1,0,0,0,0,6,0,0,5,
        0,0,6,0,5,0,8,0,0,
        5,7,3,2,0,4,0,0,0

    ]

def printBoard(board):
    for i in range(0, 81, 9):
        print(board[i:i+9])

def validMove(board, number, position):
    if SudokuBoard.distinctInBox(board, number, position) and SudokuBoard.distinctInRow(board, number, position) and SudokuBoard.distinctInColumn(board, number, position):
        return True

    return False

def backtrackAlgo(board):
    position = -1
    solved = True

    for pos in range(0,81):
        if board[pos] == 0:
            position = pos

            solved = False
            break

    if solved:
        print("Solved!")
        printBoard(board)
        return True

    for num in range (1, 10):
        if validMove(board, num, position):
            board[position] = num
            if backtrackAlgo(board):
                return True
            else:
                board[position] = 0

    return False

if not backtrackAlgo(Board):
    print("gg")
 

#print(SudokuBoard.checkRows(Board))

""" 3,5,1,6,7,2,9,8,4,
    0,0,0,8,0,1,2,5,7,
    2,8,7,0,0,0,6,1,3,
    0,9,2,0,0,5,3,7,8,
    8,0,0,7,0,0,0,0,0,
    0,0,4,9,2,0,5,0,0,
    1,0,0,0,0,6,0,0,5,
    0,0,6,0,5,0,8,0,0,
    5,7,3,2,0,4,0,0,0
 """