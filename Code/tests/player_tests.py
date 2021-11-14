import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Martin", "Tau")
        self.player2 = Player("Fraz", "Death Guard")

    def test_player_has_name(self):
        self.assertEqual("Martin", self.player1.name)
        self.assertEqual("Fraz", self.player2.name)

    def test_player_has_army(self):
        self.assertEqual("Tau", self.player1.army)
        self.assertEqual("Death Guard", self.player2.army)
    
    def test_player_has_zero_values_on_setup(self):
        self.assertEqual(0, self.player1.wins)
        self.assertEqual(0, self.player2.wins)
        self.assertEqual(0, self.player1.losses)
        self.assertEqual(0, self.player2.losses)
        self.assertEqual(0, self.player1.pts_for)
        self.assertEqual(0, self.player2.pts_for)
        self.assertEqual(0, self.player1.pts_against)
        self.assertEqual(0, self.player2.pts_against)