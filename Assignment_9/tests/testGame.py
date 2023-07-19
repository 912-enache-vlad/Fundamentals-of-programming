import unittest

from game.game import Game


class testGame(unittest.TestCase):
    def setUp(self) -> None:
        self.__game = Game()

    def test_get_board(self):
        self.assertEqual(self.__game.get_board(), self.__game.get_board())

    def test_gravity_col(self):
        self.assertEqual(self.__game.gravity_col(0), 5)

    def test_human_move(self):
        self.__game.human_move(5, 0)
        self.assertEqual(self.__game.get_board().get_symbol(5, 0), '🔴')

    def test_computer_move(self):
        row, col = self.__game.computer_move()
        self.assertEqual(self.__game.get_board().get_symbol(row, col), '🔵')

