from flask import Flask, render_template, request, redirect
from flask import Blueprint
# from repositories import player_repository
# from repositories import game_repository
from models.player import Player
from models.game import Game


players_blueprint = Blueprint("players", __name__)

# INDEX
@players_blueprint.route("/players")
def players():
    # players = player_repository.select_all()
    return render_template("players/index.html")