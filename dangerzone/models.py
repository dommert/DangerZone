# DangerZone Version 0.0.1

import datetime
from flask import Flask
from peewee import *
from flask_turboduck.db import Database
from flask_turboduck.auth import Auth


DATABASE = {
    'name': 'dangerzone.db'
    'engine': 'peewee.SqliteDatabase'
}
SECRET_KEY = 'key213_test'

app = Flask(__name__)
app.config.from_object(__name__)

# DB wrapper
db = Database(app)


# User Class (+Admin)
class User(db.Model, BaseUser):
    username = CharField()
    password = CharField()
    email = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)
    created = DateTimeField(default=datetime.datetime.now)


# Movie Class
class Movie(db.Model):
    title = TextField()
    created = DateTimeField(default=datetime.datetime.now)
    release = DateField()
    description = BlobField()
    poster = TextField()

# Person Class
class Person(db.Model):
        fname = TextField()
        lname = TextField()
        sex = CharField()
        created = DateTimeField(default=datetime.datetime.now)

# Cast Memebers (relationship)
class Cast(db.Model):
    movie = ForeignKeyField(Movie, related_name='film')
    person = ForeignKeyField(Person, related_name='cast')
    created = DateTimeField(default=datetime.datetime.now)
    job = TextField()
    title = TextField()


# create an Auth object for use with our flask app and database wrapper
auth = Auth(app, db)

