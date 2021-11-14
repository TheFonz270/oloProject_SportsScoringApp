from flask import Flask, render_template, request, redirect
from flask import Blueprint
# from repositories import book_repository
# from repositories import author_repository
from models.player import Player
from models.game import Game
# from models.task import Task 

# import repositories.author_repository as author_repository

players_blueprint = Blueprint("players", __name__)

# INDEX
# GET '/tasks'
@players_blueprint.route("/players")
def players():
    # books = book_repository.select_all()
    return render_template("players/index.html")