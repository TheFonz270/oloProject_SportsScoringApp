from db.run_sql import run_sql

from models.player import Player
from models.game import Game


def save(player):
    sql = "INSERT INTO players (name, army, wins, losses, pts_for, pts_against) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [player.name, player.army, player.wins, player.losses, player.pts_for, player.pts_against]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id
    return player

def select_all():
    players = []

    sql = "SELECT * FROM players"
    results = run_sql(sql)

    for row in results:
        player = Player(row['name'], row['army'], row['wins'], row['losses'], row['pts_for'], row['pts_against'], row['id'] )
        players.append(player)
    return players


def select(id):
    player = None
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        player = Player(result['name'], result['army'], result['wins'], result['losses'], result['pts_for'], result['pts_against'], result['id'] )
    return player

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)