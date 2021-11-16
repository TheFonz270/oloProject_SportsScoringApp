import pdb
from models.player import Player
from models.game import Game

import repositories.game_repository as game_repository
import repositories.player_repository as player_repository

# game_repository.delete_all()
# player_repository.delete_all()

# player1 = Player("Martin", "Tau")
# player_repository.save(player1)
# player2 = Player("Fraz", "Death Guard")
# player_repository.save(player2)

# game1 = Game(player1, player2)
# game_repository.save(game1)

# print(player_repository.select_all())

print(game_repository.select_by_both_players(player_repository.select(24), player_repository.select(25)))
print(game_repository.select_by_both_players(player_repository.select(26), player_repository.select(27)))
