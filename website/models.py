# database models

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    dateOfBirth = db.Column(db.Date)
    currency = db.Column(db.Integer)
    points = db.Column(db.Integer)
    handsCorrect = db.Column(db.Integer)
    handsIncorrect = db.Column(db.Integer)
    dateCreated = db.Column(db.DateTime(timezone=True), default=func.now())
    dateLastLoggedIn = db.Column(db.DateTime(timezone=True), default=func.now())



# using foreign key to connect different models (user.id goes to User class and selects id field)
# user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# if there was a model called Note that stored users notes, 
# you could add this line to the User model to store all the Notes of the users
# notes = db.relationship('Note')

#class Note(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    data = db.Column(db.String(10000))
#    date = db.Column(db.DateTime(timezone=True), default=func.now())
#    user_id = user_id = db.Column(db.Integer, db.ForeignKey('user.id'))




