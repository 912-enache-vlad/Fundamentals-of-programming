import unittest

from domain.board import Board, EndGameException


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.__board = Board()

    def tearDown(self) -> None:
        self.__board = None

    def test_gravity_col(self):
        for i in range(0, 6):
            self.__board.move('🔴', self.__board.gravity_col(0), 0)
        self.assertEqual(self.__board.gravity_col(0), -1)

    def test_get_symbol(self):
        self.__board.move('🔴', self.__board.gravity_col(0), 0)
        self.assertEqual(self.__board.get_symbol(self.__board.gravity_col(0) + 1, 0), '🔴')
        self.__board.move('🔵', self.__board.gravity_col(0), 0)
        self.assertEqual(self.__board.get_symbol(self.__board.gravity_col(0) + 1, 0), '🔵')

    def test_move(self):
        self.__board.move('🔴', self.__board.gravity_col(0), 0)
        self.assertEqual(self.__board.get_symbol(self.__board.gravity_col(0) + 1, 0), '🔴')
        self.__board.move('🔵', self.__board.gravity_col(0), 0)
        self.assertEqual(self.__board.get_symbol(self.__board.gravity_col(0) + 1, 0), '🔵')

    def test_is_won(self):
        self.__board.move('🔴', self.__board.gravity_col(0), 0)
        self.__board.move('🔴', self.__board.gravity_col(1), 1)
        self.__board.move('🔴', self.__board.gravity_col(2), 2)
        self.__board.move('🔴', self.__board.gravity_col(3), 3)
        self.assertTrue(self.__board.is_won(self.__board.gravity_col(0) + 1, 0))

    def test_almoust_won(self):
        self.__board.move('🔴', self.__board.gravity_col(0), 0)
        self.__board.move('🔴', self.__board.gravity_col(1), 1)
        self.__board.move('🔴', self.__board.gravity_col(2), 2)
        self.assertEqual(self.__board.almoust_won(self.__board.gravity_col(2) + 1, 2), (self.__board.gravity_col(3), 3))

    def test_is_full(self):
        try:
            for i in range(0, 7):
                for j in range(0, 6):
                    self.__board.move('🔴', self.__board.gravity_col(i), i)
        except EndGameException as e:
            self.assertTrue(self.__board.is_full())

    def test_str(self):
        self.__board.move('🔴', self.__board.gravity_col(0), 0)
        self.__board.move('🔴', self.__board.gravity_col(1), 1)
        self.__board.move('🔴', self.__board.gravity_col(2), 2)
        self.__board.move('🔴', self.__board.gravity_col(3), 3)
        self.assertEqual(str(self.__board), "\n     A    B    C    D    E    F    G\n  +----+----+----+----+----+----+----+\n0 |    |    |    |    |    |    |    |\n  +----+----+----+----+----+----+----+\n1 |    |    |    |    |    |    |    |\n  +----+----+----+----+----+----+----+\n2 |    |    |    |    |    |    |    |\n  +----+----+----+----+----+----+----+\n3 |    |    |    |    |    |    |    |\n  +----+----+----+----+----+----+----+\n4 |    |    |    |    |    |    |    |\n  +----+----+----+----+----+----+----+\n5 | 🔴 | 🔴 | 🔴 | 🔴 |    |    |    |\n  +----+----+----+----+----+----+----+")

