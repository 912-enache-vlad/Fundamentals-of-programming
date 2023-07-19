class EndGameException(Exception):
    pass


class BoardException(Exception):
    pass


class Board:  # board for connect 4
    def __init__(self):
        """
        Initialize the board
        """
        self.__board = []
        self.computerMoves = []
        self.humanMoves = []
        self.__free_squares = 42
        self.__gravity_col = [5, 5, 5, 5, 5, 5, 5]
        for row in range(6):
            self.__board.append([])
            for col in range(7):
                self.__board[row].append(' ')

    def gravity_col(self, col):
        """
        Return the row of the gravity of the column
        :param col: the column
        :return: the row of the gravity of the column
        """
        return self.__gravity_col[col]

    def get_symbol(self, row, col):
        """
        Return the symbol at the given position
        :param row: the row of the position
        :param col: the column of the position
        :return: the symbol at the given position
        """
        symbol = self.__board[row][col]
        if symbol == ' ':
            return None
        else:
            return symbol

    def move(self, symbol, row: int, col: int):
        """
        Play a move on the board
        :param symbol: the symbol to be placed on the board
        :param row: the row of the position
        :param col: the column of the position
        :return: nothing
        """
        # check if the row and column are valid
        if row not in range(6) or col not in range(7):
            raise BoardException(f"Invalid position.{row} {col}")

        # check if the position is free
        if self.get_symbol(row, col) is not None:  # if the position is not free
            raise BoardException("Square already taken.")

        # place the symbol on the board
        if self.__gravity_col[col] != row:
            raise BoardException(f"Invalid position. Take into account the gravity.{self.__gravity_col}")

        self.__board[row][col] = symbol
        self.__free_squares -= 1
        self.__gravity_col[col] -= 1

        if self.is_full():
            raise EndGameException("The board is full.")

    def is_won(self, row, col):
        """
        Check if the game is won
        :param row: the row of the last move
        :param col: the column of the last move
        :return: bool
        """
        # check vertical
        if True:
            try:
                if self.__board[row][col] == self.__board[row + 1][col] == self.__board[row + 2][col] == \
                        self.__board[row + 3][col] != ' ':
                    return True
            except IndexError:
                pass

        # check horizontal
        if True:
            try:
                if self.__board[row][col] == self.__board[row][col - 1] == self.__board[row][col - 2] == \
                        self.__board[row][
                            col - 3] != ' ':
                    return True
            except IndexError:
                pass
            try:
                if self.__board[row][col] == self.__board[row][col + 1] == self.__board[row][col + 2] == \
                        self.__board[row][
                            col + 3] != ' ':
                    return True
            except IndexError:
                pass
            try:
                if self.__board[row][col] == self.__board[row][col - 1] == self.__board[row][col + 1] == \
                        self.__board[row][
                            col + 2] != ' ':
                    return True
            except IndexError:
                pass
            try:
                if self.__board[row][col] == self.__board[row][col - 2] == self.__board[row][col - 1] == \
                        self.__board[row][
                            col + 1] != ' ':
                    return True
            except IndexError:
                pass

        # checks on diagonal 2
        if True:
            try:
                if self.__board[row][col] == self.__board[row - 1][col - 1] == self.__board[row - 2][col - 2] == \
                        self.__board[row - 3][col - 3] != ' ':
                    return True
            except IndexError:
                pass
            try:
                if self.__board[row][col] == self.__board[row + 1][col + 1] == self.__board[row + 2][col + 2] == \
                        self.__board[row + 3][col + 3] != ' ':
                    return True
            except IndexError:
                pass
            try:
                if self.__board[row][col] == self.__board[row - 1][col - 1] == self.__board[row + 1][col + 1] == \
                        self.__board[row + 2][col + 2] != ' ':
                    return True
            except IndexError:
                pass
            try:
                if self.__board[row][col] == self.__board[row - 2][col - 2] == self.__board[row - 1][col - 1] == \
                        self.__board[row + 1][col + 1] != ' ':
                    return True
            except IndexError:
                pass

        # checks on diagonal 1
        if True:
            try:
                if self.__board[row][col] == self.__board[row - 1][col + 1] == self.__board[row - 2][col + 2] == \
                        self.__board[row - 3][col + 3] != ' ':
                    return True
            except IndexError:
                pass
            try:
                if self.__board[row][col] == self.__board[row + 1][col - 1] == self.__board[row + 2][col - 2] == \
                        self.__board[row + 3][col - 3] != ' ':
                    return True
            except IndexError:
                pass
            try:
                if self.__board[row][col] == self.__board[row - 1][col + 1] == self.__board[row + 1][col - 1] == \
                        self.__board[row + 2][col - 2] != ' ':
                    return True
            except IndexError:
                pass
            try:
                if self.__board[row][col] == self.__board[row - 2][col + 2] == self.__board[row - 1][col + 1] == \
                        self.__board[row + 1][col - 1] != ' ':
                    return True
            except IndexError:
                pass

        return False

    def almoust_won(self, row, col):
        """
        Check if the game is almost won
        :param row: the row of the last move
        :param col: the column of the last move
        :return: (row, col) of the position that will win the game
        """
        # check vertical
        if True:
            try:
                if self.__board[row][col] == self.__board[row + 1][col] == self.__board[row + 2][col] != ' ':
                    if self.get_symbol(row - 1, col) is None and row - 1 in range(6) and col in range(7):
                        return row - 1, col
            except IndexError:
                pass

        # check horizontal
        if True:
            try:  # the case x🟡🔵🔵x
                if self.__board[row][col] == self.__board[row][col + 1] == self.__board[row][col + 2] != ' ':
                    try:
                        if self.get_symbol(row, col + 3) is None and self.__gravity_col[col + 3] == row and row in range(6) and col + 3 in range(7):
                            return row, col + 3
                    except IndexError:
                        pass
                    if self.get_symbol(row, col - 1) is None and self.__gravity_col[col - 1] == row and row in range(6) and col - 1 in range(7):
                        return row, col - 1
            except IndexError:
                pass

            try:  # the case x🔵🟡🔵x
                if self.__board[row][col] == self.__board[row][col - 1] == self.__board[row][col + 1] != ' ':
                    try:
                        if self.get_symbol(row, col + 2) is None and self.__gravity_col[col + 2] == row and row in range(6) and col + 2 in range(7):
                            return row, col + 2
                    except IndexError:
                        pass
                    if self.get_symbol(row, col - 2) is None and self.__gravity_col[col - 2] == row and row in range(6) and col - 2 in range(7):
                        return row, col - 2
            except IndexError:
                pass

            try:  # the case x🔵🔵🟡x
                if self.__board[row][col] == self.__board[row][col - 1] == self.__board[row][col - 2] != ' ':
                    try:
                        if self.get_symbol(row, col - 3) is None and self.__gravity_col[col - 3] == row and row in range(6) and col - 3 in range(7):
                            return row, col - 3
                    except IndexError:
                        pass
                    if self.get_symbol(row, col + 1) is None and self.__gravity_col[col + 1] == row and row in range(6) and col + 1 in range(7):
                        return row, col + 1
            except IndexError:
                pass

            try:  # the case 🟡x🔵🔵
                if self.__board[row][col] == self.__board[row][col + 2] == self.__board[row][col + 3] != ' ':
                    if self.get_symbol(row, col + 1) is None and self.__gravity_col[col + 1] == row and row in range(6) and col + 1 in range(7):
                        return row, col + 1
            except IndexError:
                pass

            try:  # the case 🔵x🟡🔵
                if self.__board[row][col] == self.__board[row][col - 2] == self.__board[row][col + 1] != ' ':
                    if self.get_symbol(row, col - 1) is None and self.__gravity_col[col - 1] == row and row in range(6) and col - 1 in range(7):
                        return row, col - 1
            except IndexError:
                pass
            try:  # the case 🔵x🔵🟡
                if self.__board[row][col] == self.__board[row][col - 1] == self.__board[row][col - 3] != ' ':
                    if self.get_symbol(row, col - 2) is None and self.__gravity_col[col - 2] == row and row in range(6) and col - 2 in range(7):
                        return row, col - 2
            except IndexError:
                pass

            try:  # the case 🟡🔵x🔵
                if self.__board[row][col] == self.__board[row][col + 1] == self.__board[row][col + 3] != ' ':
                    if self.get_symbol(row, col + 2) is None and self.__gravity_col[col + 2] == row and row in range(6) and col + 2 in range(7):
                        return row, col + 2
            except IndexError:
                pass

            try:  # the case 🔵🟡x🔵
                if self.__board[row][col] == self.__board[row][col - 1] == self.__board[row][col + 2] != ' ':
                    if self.get_symbol(row, col + 1) is None and self.__gravity_col[col + 1] == row and row in range(6) and col + 1 in range(7):
                        return row, col + 1
            except IndexError:
                pass

            try:  # the case 🔵🔵x🟡
                if self.__board[row][col] == self.__board[row][col - 2] == self.__board[row][col - 3] != ' ':
                    if self.get_symbol(row, col - 1) is None and self.__gravity_col[col - 1] == row and row in range(6) and col - 1 in range(7):
                        return row, col - 1
            except IndexError:
                pass


        # checks on diagonal 2
        if True:
            try:        # the case x🔵🔵🟡x
                if self.__board[row][col] == self.__board[row - 1][col - 1] == self.__board[row - 2][col - 2] != ' ':
                    try:
                        if self.get_symbol(row - 3, col - 3) is None and self.__gravity_col[col - 3] == row - 3 and row - 3 in range(6) and col - 3 in range(7):
                            return row - 3, col - 3
                    except IndexError:
                        pass
                    if self.get_symbol(row + 1, col + 1) is None and self.__gravity_col[col + 1] == row + 1 and row + 1 in range(6) and col + 1 in range(7):
                        return row + 1, col + 1

            except IndexError:
                pass

            try:        # the case x🔵🟡🔵x
                if self.__board[row][col] == self.__board[row - 1][col - 1] == self.__board[row + 1][col + 1] != ' ':
                    try:
                        if self.get_symbol(row + 2, col + 2) is None and self.__gravity_col[col + 2] == row + 2 and row + 2 in range(6) and col + 2 in range(7):
                            return row + 2, col + 2
                    except IndexError:
                        pass
                    if self.get_symbol(row - 2, col - 2) is None and self.__gravity_col[col - 2] == row - 2 and row - 2 in range(6) and col - 2 in range(7):
                        return row - 2, col - 2
            except IndexError:
                pass

            try:        # the case x🟡🔵🔵x
                if self.__board[row][col] == self.__board[row + 1][col + 1] == self.__board[row + 2][col + 2] != ' ':
                    try:
                        if self.get_symbol(row + 3, col + 3) is None and self.__gravity_col[col + 3] == row + 3 and row + 3 in range(6) and col + 3 in range(7):
                            return row + 3, col + 3
                    except IndexError:
                        pass
                    if self.get_symbol(row - 1, col - 1) is None and self.__gravity_col[col - 1] == row - 1 and row - 1 in range(6) and col - 1 in range(7):
                        return row - 1, col - 1
            except IndexError:
                pass


            try:      # the case 🟡x🔵🔵
                if self.__board[row][col] == self.__board[row + 2][col + 2] == self.__board[row + 3][col + 3] != ' ':
                    if self.get_symbol(row + 1, col + 1) is None and self.__gravity_col[col + 1] == row + 1 and row + 1 in range(6) and col + 1 in range(7):
                        return row + 1, col + 1
            except IndexError:
                pass

            try:      # the case 🔵x🟡🔵
                if self.__board[row][col] == self.__board[row - 2][col - 2] == self.__board[row + 1][col + 1] != ' ':
                    if self.get_symbol(row - 1, col - 1) is None and self.__gravity_col[col - 1] == row - 1 and row - 1 in range(6) and col - 1 in range(7):
                        return row - 1, col - 1
            except IndexError:
                pass

            try:      # the case 🔵x🔵🟡
                if self.__board[row][col] == self.__board[row - 1][col - 1] == self.__board[row - 3][col - 3] != ' ':
                    if self.get_symbol(row - 2, col - 2) is None and self.__gravity_col[col - 2] == row - 2 and row - 2 in range(6) and col - 2 in range(7):
                        return row - 2, col - 2
            except IndexError:
                pass

            try:      # the case 🟡🔵x🔵
                if self.__board[row][col] == self.__board[row + 1][col + 1] == self.__board[row + 3][col + 3] != ' ':
                    if self.get_symbol(row + 2, col + 2) is None and self.__gravity_col[col + 2] == row + 2 and row + 2 in range(6) and col + 2 in range(7):
                        return row + 2, col + 2
            except IndexError:
                pass

            try:      # the case 🔵🟡x🔵
                if self.__board[row][col] == self.__board[row - 1][col - 1] == self.__board[row + 2][col + 2] != ' ':
                    if self.get_symbol(row + 1, col + 1) is None and self.__gravity_col[col + 1] == row + 1 and row + 1 in range(6) and col + 1 in range(7):
                        return row + 1, col + 1
            except IndexError:
                pass

            try:      # the case 🔵🔵x🟡
                if self.__board[row][col] == self.__board[row - 2][col - 2] == self.__board[row - 3][col - 3] != ' ':
                    if self.get_symbol(row - 1, col - 1) is None and self.__gravity_col[col - 1] == row - 1 and row - 1 in range(6) and col - 1 in range(7):
                        return row - 1, col - 1
            except IndexError:
                pass


        # checks on diagonal 1
        if True:
            try:    # the case x🟡🔵🔵x
                if self.__board[row][col] == self.__board[row - 1][col + 1] == self.__board[row - 2][col + 2] != ' ':
                    try:
                        if self.get_symbol(row - 3, col + 3) is None and self.__gravity_col[col + 3] == row - 3 and row - 3 in range(6) and col + 3 in range(7):
                            return row - 3, col + 3
                    except IndexError:
                        pass
                    if self.get_symbol(row + 1, col - 1) is None and self.__gravity_col[col - 1] == row + 1 and row + 1 in range(6) and col - 1 in range(7):
                        return row + 1, col - 1
            except IndexError:
                pass

            try:    #the case x🔵🟡🔵x
                if self.__board[row][col] == self.__board[row - 1][col + 1] == self.__board[row + 1][col - 1] != ' ':
                    try:
                        if self.get_symbol(row + 2, col - 2) is None and self.__gravity_col[col - 2] == row + 2 and row + 2 in range(6) and col - 2 in range(7):
                            return row + 2, col - 2
                    except IndexError:
                        pass
                    if self.get_symbol(row - 2, col + 2) is None and self.__gravity_col[col + 2] == row - 2 and row - 2 in range(6) and col + 2 in range(7):
                        return row - 2, col + 2
            except IndexError:
                pass

            try:    # the case x🔵🔵🟡x
                if self.__board[row][col] == self.__board[row + 1][col - 1] == self.__board[row + 2][col - 2] != ' ':
                    try:
                        if self.get_symbol(row - 1, col + 1) is None and self.__gravity_col[col + 1] == row - 1 and row - 1 in range(6) and col + 1 in range(7):
                            return row - 1, col + 1
                    except IndexError:
                        pass
                    if self.get_symbol(row + 3, col - 3) is None and self.__gravity_col[col - 3] == row + 3 and row + 3 in range(6) and col - 3 in range(7):
                        return row + 3, col - 3
            except IndexError:
                pass

            try:    # the case 🟡x🔵🔵
                if self.__board[row][col] == self.__board[row - 2][col + 2] == self.__board[row - 3][col + 3] != ' ':
                    if self.get_symbol(row - 1, col + 1) is None and self.__gravity_col[col + 1] == row - 1 and row - 1 in range(6) and col + 1 in range(7):
                        return row - 1, col + 1
            except IndexError:
                pass

            try:    # the case 🔵x🟡🔵
                if self.__board[row][col] == self.__board[row + 1][col - 1] == self.__board[row - 2][col + 2] != ' ':
                    if self.get_symbol(row - 1, col + 1) is None and self.__gravity_col[col + 1] == row - 1 and row - 1 in range(6) and col + 1 in range(7):
                        return row - 1, col + 1
            except IndexError:
                pass

            try:    # the case 🔵x🔵🟡
                if self.__board[row][col] == self.__board[row - 1][col + 1] == self.__board[row - 3][col + 3] != ' ':
                    if self.get_symbol(row - 2, col + 2) is None and self.__gravity_col[col + 2] == row - 2 and row - 2 in range(6) and col + 2 in range(7):
                        return row - 2, col + 2
            except IndexError:
                pass

            try:    # the case 🟡🔵x🔵
                if self.__board[row][col] == self.__board[row + 1][col - 1] == self.__board[row + 3][col - 3] != ' ':
                    if self.get_symbol(row + 2, col - 2) is None and self.__gravity_col[col - 2] == row + 2 and row + 2 in range(6) and col - 2 in range(7):
                        return row + 2, col - 2
            except IndexError:
                pass

            try:    # the case 🔵🟡x🔵
                if self.__board[row][col] == self.__board[row - 1][col + 1] == self.__board[row + 2][col - 2] != ' ':
                    if self.get_symbol(row + 1, col - 1) is None and self.__gravity_col[col - 1] == row + 1 and row + 1 in range(6) and col - 1 in range(7):
                        return row + 1, col - 1
            except IndexError:
                pass

            try:    # the case 🔵🔵x🟡
                if self.__board[row][col] == self.__board[row - 2][col + 2] == self.__board[row - 3][col + 3] != ' ':
                    if self.get_symbol(row - 1, col + 1) is None and self.__gravity_col[col + 1] == row - 1 and row - 1 in range(6) and col + 1 in range(7):
                        return row - 1, col + 1
            except IndexError:
                pass

        return None, None

    def is_full(self):
        """
        Check if the board is full
        :return:
        """
        return self.__free_squares == 0

    def __str__(self):
        """
        Return a string representation of the board
        :return: a string representation of the board
        """
        s = '\n     A    B    C    D    E    F    G'
        for row in range(6):
            s += '\n  +----+----+----+----+----+----+----+'
            s += f'\n{row} |'
            for col in range(7):
                if self.__board[row][col] == ' ':
                    s += '    |'
                else:
                    s += f' {self.__board[row][col]} |'
        s += '\n  +----+----+----+----+----+----+----+'
        return s



