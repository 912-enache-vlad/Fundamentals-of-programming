from game.game import Game
# from user_interface.graphical_user_interface import Grafical_user_interface
from user_interface.user_interface import User_interface

if __name__ == "__main__":
    game = Game()
    # gui = Grafical_user_interface(game)
    ui = User_interface(game)

    ui()