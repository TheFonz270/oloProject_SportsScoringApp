from db.run_sql import run_sql

from models.player import Player
from models.game import Game
from repositories import player_repository

def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)

def save(game):
    sql = "INSERT INTO games (player1_id, player2_id, score1, score2, completed) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [game.player1.id, game.player2.id, game.score[0], game.score[1], game.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id
    # return game


def select_all():
    games = []
    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for row in results:
        player1 = player_repository.select(row['player1_id'])
        player2 = player_repository.select(row['player2_id'])
        game = Game(player1, player2, [row['score1'], row['score2']], row['completed'], row['id'] )
        games.append(game)
    return sorted(games, key=lambda game: game.id, reverse=True)

def select(id):
    game = None
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        player1 = player_repository.select(result['player1_id'])
        player2 = player_repository.select(result['player2_id'])
        game = Game(player1, player2, [result['score1'], result['score2']], result['completed'], result['id'] )
    return game

def select_by_player(player):
    games = []
    sql = "SELECT * FROM games WHERE player1_id = %s OR player2_id = %s"
    values = [player.id, player.id]
    results = run_sql(sql, values)

    if results is not None:
        for row in results:
            player1 = player_repository.select(row['player1_id'])
            player2 = player_repository.select(row['player2_id'])
            game = Game(player1, player2, [row['score1'], row['score2']], row['completed'], row['id'] )
            games.append(game)
    return games


def delete_all():
    sql = "DELETE  FROM games"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM games WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(game):
    sql = "UPDATE games SET (player1_id, player2_id, score1, score2, completed) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [game.player1.id, game.player2.id, game.score[0], game.score[1], game.completed, game.id]
    run_sql(sql, values)
