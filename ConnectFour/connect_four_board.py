"""
connect_four_board.py -- a basic board class for managing a connect-4 game

Tony Brenes
CSC121 W24
3/14/24

"""

class Board:
    def __init__(self):
        self.columns = []
        self.numRows = 6
        self.numCols = 7
        for _ in range(self.numCols):
            theseRows = ["."] * self.numRows
            self.columns.append(theseRows)

    def __str__(self):
        outstr = ""
        for row in range(self.numRows):
            outstr += "| "
            for col in range(self.numCols):
                outstr += self.columns[col][row] + " "
            outstr += "|\n"
        return outstr

if __name__ == "__main__":
    bd = Board()
    print("my board:")
    print(bd)
