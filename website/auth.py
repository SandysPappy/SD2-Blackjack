from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date, datetime
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import time

# this file relates to all places the user can navigate to related to authentification

# this file is a blueprint of our application, meaning it have a lot of routes inside it
# blueprints organize the app so everything isnt in one place

# will get imported into init.py to access all roots located in this file
auth = Blueprint('auth', __name__)

# login page
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('userName')
        password = request.form.get('password')

        # searches database
        user = User.query.filter_by(username=username).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password', category='error')
        else:
            flash('Username does not exist', category='error')

    return render_template("login.html", user=current_user)

# logout button
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# create account page
@auth.route('/create-account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('userName')
        password = request.form.get('password1')
        confirmPassword = request.form.get('password2')
        dateOfBirth = request.form.get('dateOfBirth') # '2021-08-09' YYYY-MM-DD

        user = User.query.filter_by(username=username).first()
        user1 = User.query.filter_by(email=email).first()

        if user1:
            flash('Email already exists', category='error')
        elif user:
            flash('Username already exists', category='error')
        elif len(email) < 5:
            flash('Email is too short', category='error')
        elif len(password) < 8:
            flash('Password is too short', category='error')
        elif len(password) > 32:
            flash('Password is too long', category='error')
        elif password != confirmPassword:
            flash('Passwords do not match', category='error')
        else:
            # make a User object and initiialize it
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'), 
            dateOfBirth=datetime.strptime(dateOfBirth, '%Y-%m-%d'), currency=10000, points=0, handsCorrect=0, handsIncorrect=0)
            #dateCreated=datetime.strptime(str(datetime.now(), '%Y-%m-%d %H:%M:%S.%f')), 
            #dateLastLoggedIn=datetime.strptime(str(datetime.now(), '%Y-%m-%d %H:%M:%S.%f')))

            # add user to database
            db.session.add(new_user)
            db.session.commit()
            
            flash('Account created', category='success')
            login_user(new_user, remember=True)

            # redirect to home page
            return redirect(url_for('views.home'))

    return render_template("create_account.html", user=current_user)