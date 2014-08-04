# DangerZone Version 0.0.1
# App.py

from flask import Flask
from flask_turboduck.db import Database

app= Flask(__name__)
app.config.from_object('config.Configuration')

db = Database(app)

def create_tables():
    User.create_table()
    Movie.create_table()
    Person.create_table()
    Cast.create_table()