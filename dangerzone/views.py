# DangerZone Version 0.0.1

import datetime
# Flask
from flask import request, redirect, url_for, render_template, flash
# Flask-TurboDuck
from flask_turboduck.utils import get_object_or_404, object_list
# DangerZone
from app import app
from auth import auth
from models import User, Movie, Cast





@app.route('/join/', methods=['GET', 'POST'])
def join():
    if request.method == 'POST' and request.form['username']:
        try:
            user = User.select().where(User.username==request.form['username']).get()
            flash('That username is already taken')
        except User.DoesNotExist:
            user = User(
                username=request.form['username'],
                email=request.form['email'],
                join_date=datetime.datetime.now()
            )
            user.set_password(request.form['password'])
            user.save()

            auth.login_user(user)
            return redirect(url_for('rum.frontpage'))

    return render_template('join.html')

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
    movie = User.select().order_by(Movie.title)
    return object_list('movie_list.html', Movie, 'movie_list')

# Regular Route using Flask-Rum
@app.route('/sample')
def sample(title='Home '):
    return render_template('site/sample.html', title=title)

