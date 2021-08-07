from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import flash
from flask_login import login_required, current_user
import json
from sqlalchemy.util.langhelpers import portable_instancemethod
from . import db
from .models import User
from sqlalchemy import desc, func

# this file is a blueprint of our application, meaning it have a lot of routes inside it
# blueprints organize the app so everything isnt in one place

# render templates call the HTML files, and can also pass variables such as
# dictionaries, lists, and python objects to the HTML file
# the HTML file can use they variables with a library called Jinja2
# which also allows for loops, conditional statements, and more

# will get imported into init.py to access all roots located in this file
views = Blueprint('views', __name__)

# these routes are called endpoints and link the URLs with the HTML templates
# runs whenever we go to sdblackjack.com/
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        numDecks = request.form.get('numDecks')
        deckPen = request.form.get('deckPen')
        numPlayers = request.form.get('numPlayers')
        modeSelect = request.form.get('modeSelect')
        numDecks = request.form.get('countMethod')

        flash('Game Start!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/Leaderboard/')
@login_required #look into redirecting
def leaderboard():
    # get top 100 users, and pass their username + points to the leaderboard
    users = User.query.order_by(User.points.desc()).limit(100).all()

    # this is a list
    rank = User.query.order_by(User.points.desc()).all()

    # gives the rank of the current user
    spot = rank.index(current_user) + 1

    # new_player = Player(_id=current_user.id, stack_size=10000, betting_unit_in_dollars=40)

    return render_template("leaderboard.html", user=current_user, users=users, rank=spot)

@views.route('/Information/')
@login_required
def information():
    return render_template("information.html", user=current_user)

#@views.route('/setting-slider', methods=['POST'])
#def setting_slider():
#    settings = json.loads(request.data)
#    numDecks = settings['numDecks']
#    deckPen = settings['deckPen']
#    numPlayers = settings['numPlayers']
#    modeSelect = settings['modeSelect']
#    numDecks = settings['numDecks']


