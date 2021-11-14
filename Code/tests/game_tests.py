import unittest
from models.player import Player
from models.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Martin", "Tau")
        self.player2 = Player("Fraz", "Death Guard")

        self.game = Game(self.player1, self.player2)

    def test_game_has_players(self):
        self.assertEqual("Martin",self.game.player1.name)
        self.assertEqual("Fraz",self.game.player2.name)
        self.assertEqual("Tau",self.game.player1.army)
        self.assertEqual("Death Guard",self.game.player2.army)
    
    def test_game_has_score(self):
        self.assertEqual([0,0], self.game.score)

    def test_input_game_score(self):
        self.game.input_score(70, 30)
        self.assertEqual([70,30], self.game.score)