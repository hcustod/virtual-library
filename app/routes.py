from flask import render_template, url_for, flash, redirect
from app import app, db
from app.models import User, Book
import os

@app.route('/')
@app.route('/home')
def home():
    print("Template folder path:", os.path.abspath('templates'))  # Debug statement
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/bookshelf')
def bookshelf():
    return render_template('bookshelf.html')



