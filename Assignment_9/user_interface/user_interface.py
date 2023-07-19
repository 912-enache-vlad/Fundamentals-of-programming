from domain.board import Board, BoardException, EndGameException
from game.game import Game


def user_input_validator(option:str):
    if len(option) != 1:
        return False

    col = option

    if col.lower() not in "abcdefg":
        return False

    return True

def coordonateParser(cols:str):

    return ord(cols.lower()) - ord("a")

class User_interface:
    def __init__(self, game: Game):
        self.__game = game

    def __call__(self):
        print("\n-------Welcome to Connect 4-------\n")
        print(self.__game)

        last_computer_move = (None, None)

        while True:
            # getting the input from the user
            colStr = input("\nChoose a column:").strip()

            # validating the input
            if not user_input_validator(colStr):
                print("You have not entered a valid move. Please try again.")
                continue

            # parsing the input
            col = coordonateParser(colStr)
            row = self.__game.gravity_col(col)
            # making the human move
            try:
                self.__game.human_move(row, col)
            except BoardException as be:
                print(be)
                continue
            except EndGameException as ege:
                print(self.__game)
                print(ege)
                break

            # making the computer move
            try:
                self.__game.computer_move()
            except BoardException as be:
                print(be)
                continue
            except EndGameException as ege:
                print(self.__game)
                print(ege)
                break

            print(self.__game)
