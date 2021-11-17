from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import player_repository
from repositories import game_repository
from models.player import Player
from models.game import Game


players_blueprint = Blueprint("players", __name__)

# INDEX
@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", all_players=players)

# SHOW
@players_blueprint.route("/players/<id>", methods=['GET'])
def show_player(id):
    player = player_repository.select(id)
    games = game_repository.select_by_player(player)
    return render_template('players/player.html', player = player, player_games=games)

# EDIT
# GET '/players/<id>/edit'
@players_blueprint.route("/players/<id>/edit", methods=['GET'])
def edit_player(id):
    player = player_repository.select(id)
    return render_template('players/edit.html', player = player)

# UPDATE
# PUT '/players/<id>'
@players_blueprint.route("/players/<id>", methods=['POST'])
def update_player(id):
    name       = request.form['name']
    army       = request.form['army']
    wins       = request.form['wins']
    losses     = request.form['losses']
    pts_for    = request.form['pts_for']
    pts_against= request.form['pts_against']
    player = Player(name, army, wins, losses, pts_for, pts_against, id)
    player_repository.update(player)
    return redirect('/players')

# NEW
@players_blueprint.route("/players/new", methods=['GET']) 
def new_player(): 
    return render_template("players/new.html")

# CREATE
@players_blueprint.route("/players",  methods=['POST'])
def create_player():
    name   = request.form['name']
    army   = request.form['army']
    player = Player(name, army)
    player_repository.save(player)
    if request.form["action"] == "one":
        return redirect('/players')
    elif request.form["action"] == "two":
        return redirect('/players/new')
# Receives the data from the form to insert into the database

# DELETE
@players_blueprint.route("/players/<id>/delete", methods=['POST'])
def delete_player(id):
    player_repository.delete(id)
    return redirect('/players')