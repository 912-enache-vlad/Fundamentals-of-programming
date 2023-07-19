from texttable import Texttable

class BoardException(Exception):
    pass

class Board:
    def __init__(self):
        self.__xs = []
        self.__os = []
        self.__grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    @property
    def xs(self):
        return self.__xs

    @property
    def os(self):
        return self.__os

    @property
    def grid(self):
        return self.__grid

    def place(self, i:int, j: int,piece: str):
        if piece == "x":
            self.__xs.append((i, j))
            self.__grid[i][j] = "x"
        elif piece == "o":
            self.__os.append((i, j))
            self.__grid[i][j] = "o"
        else:
            raise BoardException("The piece you want to place is not 'x' or 'o'!")

    def __str__(self):
        table = Texttable()
        for i in [0, 1, 2]:
            row = []
            for j in [0, 1, 2]:
                if (i, j) in self.__xs:
                    row.append("x")
                elif (i, j) in self.__os:
                    row.append("o")
                else:
                    row.append(" ")
            table.add_row(row)
        return table.draw() + "\n"
    def __repr__(self):
        # display the board with x and o and _ for empty spaces
        string = ""
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                if (i, j) in self.__xs:
                    string += "x "
                elif (i, j) in self.__os:
                    string += "o "
                else:
                    string += "_ "
            string += "\n"
        return string


    def removePiece(self, i, j, piece: str):
        if piece == "x":
            self.__xs.remove((i, j))
            self.__grid[i][j] = " "
        elif piece == "o":
            self.__os.remove((i, j))
            self.__grid[i][j] = " "
        else:
            raise BoardException("The piece you want to remove is not 'x' or 'o'!")

    def move(self,iFrom, jFrom, iTo, jTo, piece: str):
        if piece == "x":
            self.__xs.remove((iFrom, jFrom))
            self.__xs.append((iTo, jTo))
            self.__grid[iFrom][jFrom] = " "
            self.__grid[iTo][jTo] = "x"
        elif piece == "o":
            self.__os.remove((iFrom, jFrom))
            self.__os.append((iTo, jTo))
            self.__grid[iFrom][jFrom] = " "
            self.__grid[iTo][jTo] = "o"
        else:
            raise BoardException("The piece you want to move is not 'x' or 'o'!")
