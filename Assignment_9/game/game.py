"""
Human and computer moves
"""
from random import choice

from domain.board import Board, EndGameException, BoardException


class Game:
    def __init__(self):
        self.__board = Board()

    def get_board(self):
        """
        Return the board
        :return:
        """
        return self.__board

    def gravity_col(self, col):
        """
        Return the row of the gravity of the column
        :param col: the column
        :return: the row of the gravity of the column
        """
        return self.__board.gravity_col(col)

    def human_move(self, row, col: int):
        """
        The user plays a move on the board
        :param row: the row of the position
        :param col: the column of the position
        :return:
        """
        try:
            self.__board.move('🔴', row, col)
            self.__board.humanMoves.append((row, col))
        except BoardException as be:
            raise BoardException(f"Human - {be}")

        if self.__board.is_won(row, col):
            raise EndGameException("Congratulations! You won!")


    def computer_move(self):
        """
        The computer plays a move on the board
        :return: the row and column of the computer move
        """

        # check if the computer can win and if it can play that move
        for computerMove in self.__board.computerMoves:
        # if lastCompRow is not None and lastCompCol is not None:
            row, col = self.__board.almoust_won(computerMove[0], computerMove[1])
            if row is not None:
                try:
                    self.__board.move('🔵', row, col)
                    self.__board.computerMoves.append((row, col))
                except BoardException as be:
                    raise BoardException(f"Computer - {be}")
                if self.__board.is_won(row, col):
                    raise EndGameException("The computer won!")

                return row, col

        # check if the human can win and if it can block that move
        for humanMove in self.__board.humanMoves:
            row, col = self.__board.almoust_won(humanMove[0], humanMove[1])
            if row in range(0, 6) and col in range(0, 7):
                try:
                    self.__board.move('🔵', row, col)
                    self.__board.computerMoves.append((row, col))
                except BoardException as be:
                    raise BoardException(f"Computer - {be}")
                if self.__board.is_won(row, col):
                    raise EndGameException("The computer won!")

                return row, col

        # if is not in the previous cases, it plays randomly
        positions = []
        for col in range(7):
            positions.append((self.__board.gravity_col(col), col))
        pos = choice(positions)
        row, col = pos
        try:
            self.__board.move('🔵', row, col)
            self.__board.computerMoves.append((row, col))
        except BoardException as be:
            raise BoardException(f"Computer - {be}")
        if self.__board.is_won(row, col):
            raise EndGameException("The computer won!")

        return row, col

    def __str__(self):
        """
        Return a string representation of the board
        :return:
        """
        return str(self.__board)