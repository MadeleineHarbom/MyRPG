import unittest

from Game.fight import get_monsters


class GameTest(unittest.TestCase):
    def test_get_mosters(self):
        monsters = get_monsters(6, 1)
        self.assertEqual(6, len(monsters))

if __name__ == '__main__':
    unittest.main()
