from flask import render_template, request, redirect
from app import app
from app.models.game import *
from app.models.player import *

@app.route('/')
def index():
  return render_template('index.html', title='Home', games = player)

@app.route('/', methods=["POST"])
def add_player1():
  # game_name = request.form["name1"]
  game_choice = request.form["choice1"]
  new_player = Player(game_choice)
  player.append(new_player)
  return redirect('/')


@app.route('/game')
def game():
  import random
  game_list = ['Rock', 'Paper', 'Scissors']
  computer_choice = random.choice(game_list)
  if player == computer_choice:
    return f"Player1 choice:{player}: {computer_choice}, Computer choice \nThis is a draw"

  elif player == 'Rock':
    if computer_choice == 'Scissors':
      return f"{player} Player1 is the Winner!!"
    else:
      return f"{computer_choice} Computer win is the Winner!!"

  elif player == "Paper":
    if computer_choice == "Rock":
      return f"{player}: Player1 is the Winner!!"
    else:
      return f"{computer_choice} Computer win is the Winner!!"

  elif player == 'Rock':
    if computer_choice == 'Scissors':
      return f"{player}:  Player1 is the Winner!!"
    else:
      return f"{computer_choice} Computer winsis the Winner!!"
  else:
    return "Wrong Command!"

