# DangerZone Version 0.0.1

import datetime

from flask import request, redirect, url_for, render_template, flash

from flask_turboduck.utils import get_object_or_404, object_list

from app import app
#from auth import auth
from models import User, Movie, Relationship

@app.route('/')
def homepage():
    if auth.get_logged_in_user():
        return private_timeline()
    else:
        return public_timeline()


# DangerZone Private Area
@app.route('/private/')
@auth.login_required
def private_timeline():
    user = auth.get_logged_in_user()

    messages = Message.select().where(
        Message.user << user.following()
    ).order_by(Message.pub_date.desc())

    return object_list('private_messages.html', messages, 'message_list')

# Movie List
@app.route('/movie/')
def movie_list():
    movie = User.select().order_by(movies.mname)
    return object_list('movie_list.html', movies, 'movie_list')

# Regular Route using Flask-Rum
@app.route('/sample')
def sample(title='Home '):
    return render_template('site/sample.html', title=title)

