from flask import Flask, render_template, request, redirect
from flask import Blueprint
# from repositories import player_repository
# from repositories import game_repository
from models.player import Player
from models.game import Game


games_blueprint = Blueprint("games", __name__)

# INDEX
@games_blueprint.route("/games")
def games():
    # games = game_repository.select_all()
    return render_template("games/index.html")