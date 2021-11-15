import pdb
from models.player import Player
from models.game import Game

import repositories.game_repository as game_repository
import repositories.player_repository as player_repository

game_repository.delete_all()
player_repository.delete_all()

player1 = Player("Martin", "Tau")
player_repository.save(player1)
player2 = Player("Fraz", "Death Guard")
player_repository.save(player2)

game1 = Game(player1, player2)
game_repository.save(game1)

print(player_repository.select_all())