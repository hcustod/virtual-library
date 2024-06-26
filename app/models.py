from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(100), nullable = False)
    isbn = db.Column(db.String(20), unique = True, nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

