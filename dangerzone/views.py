# DangerZone Version 0.0.1

import datetime
# Flask
from flask import request, redirect, url_for, render_template, flash
# Flask-TurboDuck
from flask_turboduck.utils import get_object_or_404, object_list
# DangerZone
from app import app
from auth import auth
from models import User, Movie, Cast, Person



@app.route('/status/')
def status():
    if auth.get_logged_in_user():
        return 'Logged In'
    else:
        return 'Not Logged In'

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


# Movie List
@app.route('/movie/')
def movie_list():
    movie = Movie.select().order_by(Movie.title)
    return object_list('movie_list.html', Movie, 'movie_list')

# Regular Route using Flask-Rum
@app.route('/sample')
def sample(title='Home '):
    return render_template('site/sample.html', title=title)

