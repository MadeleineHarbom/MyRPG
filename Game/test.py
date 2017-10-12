import unittest

from main import get_monsters


class GameTest(unittest.TestCase):
    def test_get_mosters(self):
        monsters = get_monsters(6, 1)


if __name__ == '__main__':
    unittest.main()
