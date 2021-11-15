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
    print(results)
    id = results[0]['id']
    game.id = id
    return game


def select_all():
    games = []
    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for row in results:
        player1 = player_repository.select(row['player1_id'])
        player2 = player_repository.select(row['player2_id'])
        game = Game(player1, player2, [row['score1'], row['score2']], row['completed'], row['id'] )
        games.append(game)
    return games

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


# def delete_all():
#     sql = "DELETE  FROM tasks"
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE  FROM tasks WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


# def update(task):
#     sql = "UPDATE tasks SET (description, user_id, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
#     values = [task.description, task.user.id, task.duration, task.completed, task.id]
#     run_sql(sql, values)
