from db.run_sql import run_sql

from models.player import Player
from models.game import Game
from repositories import player_repository
from repositories import game_repository
import random
from random import shuffle
import pdb

def create_next_round():
    players = player_repository.select_all()
    temp_list = players.copy()
    
    for player in players:
        if player in temp_list:
            for p in temp_list:
                if len(game_repository.select_by_both_players(player, p)) == 0 and player.name is not p.name:
                    game = Game(player, p)
                    game_repository.save(game)
                    temp_list.remove(player)
                    temp_list.remove(p)
                    print(temp_list)
                    break
        
    
def create_random_round():
    players = player_repository.select_all()
    random.shuffle(players)
    temp_list = players.copy()
    
    for player in players:
        if player in temp_list:
            for p in temp_list:
                if len(game_repository.select_by_both_players(player, p)) == 0 and player.name is not p.name:
                    game = Game(player, p)
                    game_repository.save(game)
                    temp_list.remove(player)
                    temp_list.remove(p)
                    print(temp_list)
                    break
    # game = Game(players[0], players[1])
    # game_repository.save(game)
    # game = Game(players[2], players[3])
    # game_repository.save(game)
    # game = Game(players[4], players[5])
    # game_repository.save(game)
    # game = Game(players[6], players[7])
    # game_repository.save(game)
    