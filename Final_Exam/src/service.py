import unittest
from random import choice

from src.board import Board

class GameException(Exception):
    pass

class EndOfGame(Exception):
    pass

class EndOfPlacement(Exception):
    pass

class Game:
    def __init__(self, file):
        self.__board = Board()
        self.__file = file

    @property
    def board(self):
        return self.__board

    def saveGame(self, piece: str):
        with open(self.__file, "w") as file:
            file.write(self.__board.__repr__() + "\n")
            file.write(piece)

    def loadGame(self):
        with open(self.__file, "r") as fin:
            i = 0
            for line in fin:
                if len(line) == 1:
                    if line == "x":
                        return "x"
                    elif line == "o":
                        return "o"
                pieces = line.split(" ")
                for j in range(3):
                    if pieces[j] == "x":
                        self.__board.place(i, j, "x")
                    elif pieces[j] == "o":
                        self.__board.place(i, j, "o")
                i += 1

    def displayBoard(self):
        return str(self.__board)

    def place(self, i: int, j: int, piece: str):
        """
        Places a piece on the board
        :param i: the row
        :param j: the column
        :param piece: the piece to be placed
        :return: nothing
        """
        if (i, j) in self.__board.xs or (i, j) in self.__board.os:
            raise GameException("You cannot place there because is not an empty square.")
        self.__board.place(i, j, piece)
        if self.WonGame() != False:
            raise EndOfGame(f"Player with {self.WonGame()} won the game!")
        if len(self.__board.xs) == 4 and len(self.__board.os) == 4:
            raise EndOfPlacement()

    def compMove(self, piece: str):

        if piece == "x":
            # trying to block
            # looking for 2 in a row
            for i in range(3):
                # case x x _
                if self.__board.grid[i][0] == self.__board.grid[i][1] == "o" and self.__board.grid[i][2] == " ":
                    self.place(i, 2, piece)
                    return i, 2, piece
                # case x _ x
                if self.__board.grid[i][0] == self.__board.grid[i][2] == "o" and self.__board.grid[i][1] == " ":
                    self.place(i, 1, piece)
                    return i, 1, piece
                # case _ x x
                if self.__board.grid[i][1] == self.__board.grid[i][2] == "o" and self.__board.grid[i][0] == " ":
                    self.place(i, 0, piece)
                    return i, 0, piece
            # looking for 2 in a column
            for j in range(3):
                # case x x _
                if self.__board.grid[0][j] == self.__board.grid[1][j] == "o" and self.__board.grid[2][j] == " ":
                    self.place(2, j, piece)
                    return 2, j, piece
                # case x _ x
                if self.__board.grid[0][j] == self.__board.grid[2][j] == "o" and self.__board.grid[1][j] == " ":
                    self.place(1, j, piece)
                    return 1, j, piece
                # case _ x x
                if self.__board.grid[1][j] == self.__board.grid[2][j] == "o" and self.__board.grid[0][j] == " ":
                    self.place(0, j, piece)
                    return 0, j, piece
            # looking for 2 in a diagonal
            # case x x _
            if self.__board.grid[0][0] == self.__board.grid[1][1] == "o" and self.__board.grid[2][2] == " ":
                self.place(2, 2, piece)
                return 2, 2, piece
            # case x _ x
            if self.__board.grid[0][0] == self.__board.grid[2][2] == "o" and self.__board.grid[1][1] == " ":
                self.place(1, 1, piece)
                return 1, 1, piece
            # case _ x x
            if self.__board.grid[1][1] == self.__board.grid[2][2] == "o" and self.__board.grid[0][0] == " ":
                self.place(0, 0, piece)
                return 0, 0, piece
            # then placing randomly
            places = []
            for i in range(3):
                for j in range(3):
                    if self.__board.grid[i][j] == " ":
                        places.append((i, j))

            place = choice(places)
            self.__board.place(place[0], place[1], piece)
            return (place[0], place[1], piece)

        elif piece == "o":
            # trying to block
            # looking for 2 in a row
            for i in range(3):
                # case x x _
                if self.__board.grid[i][0] == self.__board.grid[i][1] == "x" and self.__board.grid[i][2] == " ":
                    self.place(i, 2, piece)
                    return i, 2, piece
                # case x _ x
                if self.__board.grid[i][0] == self.__board.grid[i][2] == "x" and self.__board.grid[i][1] == " ":
                    self.place(i, 1, piece)
                    return i, 1, piece
                # case _ x x
                if self.__board.grid[i][1] == self.__board.grid[i][2] == "x" and self.__board.grid[i][0] == " ":
                    self.place(i, 0, piece)
                    return i, 0, piece
            # looking for 2 in a column
            for j in range(3):
                # case x x _
                if self.__board.grid[0][j] == self.__board.grid[1][j] == "x" and self.__board.grid[2][j] == " ":
                    self.place(2, j, piece)
                    return 2, j, piece
                # case x _ x
                if self.__board.grid[0][j] == self.__board.grid[2][j] == "x" and self.__board.grid[1][j] == " ":
                    self.place(1, j, piece)
                    return 1, j, piece
                # case _ x x
                if self.__board.grid[1][j] == self.__board.grid[2][j] == "x" and self.__board.grid[0][j] == " ":
                    self.place(0, j, piece)
                    return 0, j, piece
            # looking for 2 in a diagonal
            # case x x _
            if self.__board.grid[0][0] == self.__board.grid[1][1] == "x" and self.__board.grid[2][2] == " ":
                self.place(2, 2, piece)
                return 2, 2, piece
            # case x _ x
            if self.__board.grid[0][0] == self.__board.grid[2][2] == "x" and self.__board.grid[1][1] == " ":
                self.place(1, 1, piece)
                return 1, 1, piece
            # case _ x x
            if self.__board.grid[1][1] == self.__board.grid[2][2] == "x" and self.__board.grid[0][0] == " ":
                self.place(0, 0, piece)
                return 0, 0, piece

            # then placing randomly
            places = []
            for i in range(3):
                for j in range(3):
                    if self.__board.grid[i][j] == " ":
                        places.append((i, j))

            place = choice(places)
            self.__board.place(place[0], place[1], piece)

    def compMoveMovementPhaseRandom(self, piece: str):
        # implementing a random movement
        # searching for the empty space
        place = None
        for i in range(3):
            for j in range(3):
                if self.__board.grid[i][j] == " ":
                    place = (i, j)
                    break

        # searching for an adiacent piece to move
        dirI = [1, 0, -1, 0, 1, 1, -1, -1]
        dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
        for k in range(8):
            try:
                if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                    self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                    if self.WonGame() != False:
                        raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                    break
            except IndexError:
                pass

    def compMoveMovementPhase(self, piece:str):
        # computer trying to win the game
        if piece == "x":
            # trying to block
            # looking for 2 in a row
            for i in range(3):
                # case x x _
                if self.__board.grid[i][0] == self.__board.grid[i][1] == "x" and self.__board.grid[i][2] == " ":
                    place = (i, 2)
                    dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                    dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                    for k in range(8):
                        try:
                            if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                                self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                                if self.WonGame() != False:
                                    raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                                break
                        except IndexError:
                            pass
                # case x _ x
                if self.__board.grid[i][0] == self.__board.grid[i][2] == "x" and self.__board.grid[i][1] == " ":
                    place = (i, 1)
                    dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                    dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                    for k in range(8):
                        try:
                            if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                                self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                                if self.WonGame() != False:
                                    raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                                break
                        except IndexError:
                            pass
                # case _ x x
                if self.__board.grid[i][1] == self.__board.grid[i][2] == "x" and self.__board.grid[i][0] == " ":
                    place = (i, 0)
                    dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                    dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                    for k in range(8):
                        try:
                            if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                                self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                                if self.WonGame() != False:
                                    raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                                break
                        except IndexError:
                            pass
            # looking for 2 in a column
            for j in range(3):
                # case x x _
                if self.__board.grid[0][j] == self.__board.grid[1][j] == "x" and self.__board.grid[2][j] == " ":
                    place = (2, j)
                    dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                    dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                    for k in range(8):
                        try:
                            if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                                self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                                if self.WonGame() != False:
                                    raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                                break
                        except IndexError:
                            pass
                # case x _ x
                if self.__board.grid[0][j] == self.__board.grid[2][j] == "x" and self.__board.grid[1][j] == " ":
                    place = (1, j)
                    dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                    dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                    for k in range(8):
                        try:
                            if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                                self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                                if self.WonGame() != False:
                                    raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                                break
                        except IndexError:
                            pass
                # case _ x x
                if self.__board.grid[1][j] == self.__board.grid[2][j] == "x" and self.__board.grid[0][j] == " ":
                    place = (0, j)
                    dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                    dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                    for k in range(8):
                        try:
                            if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                                self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                                if self.WonGame() != False:
                                    raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                                break
                        except IndexError:
                            pass
            # looking for 2 in a diagonal
            # case x x _
            if self.__board.grid[0][0] == self.__board.grid[1][1] == "x" and self.__board.grid[2][2] == " ":
                place = (2, 2)
                dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                for k in range(8):
                    try:
                        if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                            self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                            if self.WonGame() != False:
                                raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                            break
                    except IndexError:
                        pass

            # case x _ x
            if self.__board.grid[0][0] == self.__board.grid[2][2] == "x" and self.__board.grid[1][1] == " ":
                place = (1, 1)
                dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                for k in range(8):
                    try:
                        if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                            self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                            if self.WonGame() != False:
                                raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                            break
                    except IndexError:
                        pass
            # case _ x x
            if self.__board.grid[1][1] == self.__board.grid[2][2] == "x" and self.__board.grid[0][0] == " ":
                place = (0, 0)
                dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                for k in range(8):
                    try:
                        if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                            self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                            if self.WonGame() != False:
                                raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                            break
                    except IndexError:
                        pass

            # then placing randomly
            self.compMoveMovementPhaseRandom(piece)

        elif piece == "o":
            # looking for 2 in a row
            for i in range(3):
                # case x x _
                if self.__board.grid[i][0] == self.__board.grid[i][1] == "o" and self.__board.grid[i][2] == " ":
                    place = (i, 2)
                    dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                    dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                    for k in range(8):
                        try:
                            if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                                self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                                if self.WonGame() != False:
                                    raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                                break
                        except IndexError:
                            pass
                # case x _ x
                if self.__board.grid[i][0] == self.__board.grid[i][2] == "o" and self.__board.grid[i][1] == " ":
                    place = (i, 1)
                    dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                    dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                    for k in range(8):
                        try:
                            if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                                self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                                if self.WonGame() != False:
                                    raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                                break
                        except IndexError:
                            pass
                # case _ x x
                if self.__board.grid[i][1] == self.__board.grid[i][2] == "o" and self.__board.grid[i][0] == " ":
                    place = (i, 0)
                    dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                    dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                    for k in range(8):
                        try:
                            if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                                self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                                if self.WonGame() != False:
                                    raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                                break
                        except IndexError:
                            pass
            for j in range(3):
                # case x x _
                if self.__board.grid[0][j] == self.__board.grid[1][j] == "o" and self.__board.grid[2][j] == " ":
                    place = (2, j)
                    dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                    dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                    for k in range(8):
                        try:
                            if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                                self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                                if self.WonGame() != False:
                                    raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                                break
                        except IndexError:
                            pass
                # case x _ x
                if self.__board.grid[0][j] == self.__board.grid[2][j] == "o" and self.__board.grid[1][j] == " ":
                    place = (1, j)
                    dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                    dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                    for k in range(8):
                        try:
                            if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                                self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                                if self.WonGame() != False:
                                    raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                                break
                        except IndexError:
                            pass
                # case _ x x
                if self.__board.grid[1][j] == self.__board.grid[2][j] == "o" and self.__board.grid[0][j] == " ":
                    place = (0, j)
                    dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                    dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                    for k in range(8):
                        try:
                            if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                                self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                                if self.WonGame() != False:
                                    raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                                break
                        except IndexError:
                            pass

            # looking for 2 in a diagonal
            # case x x _
            if self.__board.grid[0][0] == self.__board.grid[1][1] == "o" and self.__board.grid[2][2] == " ":
                place = (2, 2)
                dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                for k in range(8):
                    try:
                        if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                            self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                            if self.WonGame() != False:
                                raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                            break
                    except IndexError:
                        pass

            # case x _ x
            if self.__board.grid[0][0] == self.__board.grid[2][2] == "o" and self.__board.grid[1][1] == " ":
                place = (1, 1)
                dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                for k in range(8):
                    try:
                        if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                            self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                            if self.WonGame() != False:
                                raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                            break
                    except IndexError:
                        pass

            # case _ x x
            if self.__board.grid[1][1] == self.__board.grid[2][2] == "o" and self.__board.grid[0][0] == " ":
                place = (0, 0)
                dirI = [1, 0, -1, 0, 1, 1, -1, -1]
                dirJ = [0, 1, 0, -1, 1, -1, 1, -1]
                for k in range(8):
                    try:
                        if self.__board.grid[place[0] + dirI[k]][place[1] + dirJ[k]] == piece:
                            self.move(place[0] + dirI[k], place[1] + dirJ[k], place[0], place[1], piece)
                            if self.WonGame() != False:
                                raise EndOfGame(f"Player with {self.WonGame()} won the game!")
                            break
                    except IndexError:
                        pass

            # then placing randomly
            self.compMoveMovementPhaseRandom(piece)

    def WonGame(self):
        """
        Checks if the game is won
        :return: the piece that won the game or False if the game is not won
        """
        for i in range(3):
            if self.__board.grid[i][0] == self.__board.grid[i][1] == self.__board.grid[i][2] and self.__board.grid[i][0] != " ":
                return self.__board.grid[i][0]
        for j in range(3):
            if self.__board.grid[0][j] == self.__board.grid[1][j] == self.__board.grid[2][j] and self.__board.grid[0][j] != " ":
                return self.__board.grid[0][j]

        if self.__board.grid[0][0] == self.__board.grid[1][1] == self.__board.grid[2][2] and self.__board.grid[0][0] != " ":
            return self.__board.grid[0][0]
        if self.__board.grid[0][2] == self.__board.grid[1][1] == self.__board.grid[2][0] and self.__board.grid[0][2] != " ":
            return self.__board.grid[0][2]
        return False

    def removePiece(self, i, j, piece):
        self.__board.removePiece(i, j, piece)

    def move(self, iFrom, jFrom, iTo, jTo, piece):
        if self.__board.grid[iTo][jTo] != " ":
            raise GameException("There is already a piece there")
        if self.__board.grid[iFrom][jFrom] != piece:
            raise GameException("You can't move that piece")
        if iFrom == iTo and jFrom == jTo:
            raise GameException("You can't move to the same place")
        if abs(iFrom - iTo) > 1 or abs(jFrom - jTo) > 1:
            raise GameException("You can't move that far")
        self.__board.move(iFrom, jFrom, iTo, jTo, piece)
        if self.WonGame() != False:
            raise EndOfGame(f"The player with {self.WonGame()} won the game")

class testGame(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Game("test.txt")

    def testPlace(self):
        self.game.place(0, 0, "x")
        self.assertEqual(self.game.board.grid[0][0], "x")
        self.game.place(1, 1, "o")
        self.assertEqual(self.game.board.grid[1][1], "o")
        self.game.place(2, 2, "x")
        self.assertEqual(self.game.board.grid[2][2], "x")

    def testWonGame(self):
        self.game.place(0, 0, "x")
        self.game.place(0, 1, "x")
        try:
            self.game.place(0, 2, "x")
            assert False
        except EndOfGame:
            assert True
        self.assertEqual(self.game.WonGame(), "x")

