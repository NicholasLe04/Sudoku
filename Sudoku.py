import math

class Sudoku:

    def __init__(self):

        self.SubBoxes = [

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

    #game rules

    def areDistinct(self, array):
        n = len(array)

        s = set()
        for i in range(0, n):
            s.add(array[i])

        return(len(s) == len(array))


    def distinctInRow(self, board, num, position):
        start = 9 * math.floor(position/9)
        for i in range(start, start + 9):
            if board[i] == num:
                return False
        return True 


    def distinctInColumn(self, board, num, position):
        for i in range(position % 9, 81, 9):
            if board[i] == num:
                return False
        return True
        
        
    def distinctInBox(self, board, num, position):
        check = -1

        for i in range(0,9):
            for j in self.SubBoxes[i]:
                if j == position:
                    check = i
                    break

        for k in self.SubBoxes[check]:
            if board[k] == num:
                return False

        return True


    def checkBoard(self, board):
        if self.checkRows(board) and self.checkColumns(board) and self.checkBoxes(board):
            return True

        return False
