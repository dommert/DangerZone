# DangerZone Version 0.0.1
from hashlib import md5
import datetime
from peewee import *
from flask_turboduck.auth import Auth, BaseUser
from flask_turboduck import *
from peewee import *
import config
from app import db

# User Class (+Admin)
class User(db.Model, BaseUser):
    username = CharField()
    password = CharField()
    email = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)
    created = DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.username

# Movie Class
class Movie(db.Model):
    created = DateTimeField(default=datetime.datetime.now)
    title = TextField()
    description = BlobField()
    released = DateField()
    poster = TextField()

    def __unicode__(self):
        return 'Movie %s was created %s' % (self.title, self.released)

# Person Class
class Person(db.Model):
        created = DateTimeField(default=datetime.datetime.now)
        fname = TextField()
        lname = TextField()
        sex = TextField()

# Cast Memebers (relationship)
class Cast(db.Model):
    movie = ForeignKeyField(Movie, related_name='film')
    person = ForeignKeyField(Person, related_name='cast')
    created = DateTimeField(default=datetime.datetime.now)
    job = TextField()
    title = TextField()