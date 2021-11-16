from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import player_repository
from repositories import game_repository
from models.player import Player
from models.game import Game
from models import tournament


games_blueprint = Blueprint("games", __name__)

# INDEX
@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/index.html", all_games=games)


# NEW
@games_blueprint.route("/games/new", methods=['GET']) 
def new_game(): 
    players = player_repository.select_all()
    return render_template("games/new.html", all_players = players)

# CREATE
@games_blueprint.route("/games",  methods=['POST'])
def create_game():
    player1_id = request.form['player1_id']
    player2_id = request.form['player2_id']
    score1     = request.form['score1']
    score2     = request.form['score2']
    completed  = request.form['completed']
    player1    = player_repository.select(player1_id)
    player2    = player_repository.select(player2_id)
    game       = Game(player1, player2, [score1, score2], completed)
    if completed == True:
        game.reconcile_game()
        player_repository.update(player1)
        player_repository.update(player2)
    game_repository.save(game)
    return redirect('/games')
# Receives the data from the form to insert into the database

# SHOW
@games_blueprint.route("/games/<id>", methods=['GET'])
def show_game(id):
    game = game_repository.select(id)
    return render_template('games/game.html', game = game)

# EDIT
# GET '/games/<id>/edit'
@games_blueprint.route("/games/<id>/edit", methods=['GET'])
def edit_game(id):
    game = game_repository.select(id)
    players = player_repository.select_all()
    return render_template('games/edit.html', game = game, all_players = players)

# UPDATE
# PUT '/games/<id>'
@games_blueprint.route("/games/<id>", methods=['POST'])
def update_game(id):
    player1_id = request.form['player1_id']
    player2_id = request.form['player2_id']
    score1     = request.form['score1']
    score2     = request.form['score2']
    completed  = request.form['completed']
    player1    = player_repository.select(player1_id)
    player2    = player_repository.select(player2_id)
    game       = Game(player1, player2, [score1, score2], completed, id)
    game_repository.update(game)
    if completed == "True":
        game.reconcile_game()
        player_repository.update(player1)
        player_repository.update(player2)
    return redirect('/games')

# DELETE
@games_blueprint.route("/games/<id>/delete", methods=['POST'])
def delete_task(id):
    game_repository.delete(id)
    return redirect('/games')

# GENERATE GAME ROUND
@games_blueprint.route("/games/generate", methods=['POST'])
def generate_round():
    tournament.create_next_round()
    return redirect('/games')