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
    return render_template('players/player.html', player = player)

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
    return redirect('/players')
# Receives the data from the form to insert into the database

# UPDATE
# # PUT '/tasks/<id>'
# @tasks_blueprint.route("/tasks/<id>", methods=['POST'])
# def update_task(id):
#     description = request.form['description']
#     user_id     = request.form['user_id']
#     duration    = request.form['duration']
#     completed   = request.form['completed']
#     user        = user_repository.select(user_id)
#     task        = Task(description, user, duration, completed, id)
#     task_repository.update(task)
#     return redirect('/tasks')

# DELETE
@players_blueprint.route("/players/<id>/delete", methods=['POST'])
def delete_player(id):
    player_repository.delete(id)
    return redirect('/players')