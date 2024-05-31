import unittest
from ej1.jugador import Player, MAX_ENERGY, MIN_ENERGY
from ej2.game import Game


class Test(unittest.TestCase):

    def test1(self):
        player = Player(1, 'test')
        self.assertEqual(player.get_energy(), (MAX_ENERGY - MIN_ENERGY) / 2)

    def test2(self):
        player = Player(1, 'test')
        player.boost(-100)
        self.assertTrue(player.get_energy() == MIN_ENERGY)

    def test3(self):
        player = Player(1, 'test')
        player.boost(200)
        self.assertTrue(player.get_energy() == MAX_ENERGY)

    def test4(self):
        player1 = Player(1, 'a')
        player2 = Player(2, 'b')
        game = Game(player1, player2, 1)
        player1.boost(-10)
        self.assertEqual(game.winner(), player2)
if __name__ == '__main__':
    unittest.main()