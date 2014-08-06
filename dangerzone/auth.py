# DangerZone Version 0.0.1
# Auth.py

from flask_turboduck.auth import Auth
from flask_turboduck.db import Database
from app import app, db
from models import User

auth = Auth(app, db, user_model=User)
