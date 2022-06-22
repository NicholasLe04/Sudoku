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

    #methods

    def areDistinct(self, array):
        n = len(array)

        s = set()
        for i in range(0, n):
            s.add(array[i])

        return(len(s) == len(array))


    def checkRows(self, board):
        row = []
        for i in range(0, 81, 9):
            for j in range(0, 9):
                row.append(board[i + j])

                if not self.areDistinct(row):
                    return False

            row.clear()

        return True 


    def checkColumns(self, board):
        column = []
        for j in range(0, 9):
            for i in range(0, 81, 9):
                column.append(board[i + j])

                if not self.areDistinct(column):
                    return False

            column.clear()

        return True
        
        
    def checkBoxes(self, board):
        box = []

        for subbox in self.SubBoxes:
            for index in subbox:
                box.append(board[index])

            if not self.areDistinct(box):
                return False

            box.clear()

        return True


    def checkBoard(self, board):
        if self.checkRows(board) and self.checkColumns(board) and self.checkBoxes(board):
            return True

        return False
