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
    
    def test_player_win_and_player_lose(self):
        self.player1.winner()
        self.player2.loser()
        self.assertEqual(1, self.player1.wins)
        self.assertEqual(1, self.player2.losses)
    
    def test_player_pts_for_and_pts_against(self):
        self.player1.increase_pts_for(70)
        self.player1.increase_pts_against(30)
        self.player2.increase_pts_for(30)
        self.player2.increase_pts_against(70)
        self.assertEqual(70, self.player1.pts_for)
        self.assertEqual(30, self.player2.pts_for)
        self.assertEqual(30, self.player1.pts_against)
        self.assertEqual(70, self.player2.pts_against)