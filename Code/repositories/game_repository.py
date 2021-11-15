from db.run_sql import run_sql

from models.player import Player
from models.game import Game


def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)

def save(game):
    sql = "INSERT INTO games (player1_id, player2_id, score1, score2, completed) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [game.player1.id, game.player2.id, game.score[0], game.score[1], game.completed]
    results = run_sql(sql, values)
    print(results)
    id = results[0]['id']
    game.id = id
    return game