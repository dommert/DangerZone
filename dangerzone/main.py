# DangerZone Version 0.0.1

from flask import Flask, render_template, Blueprint
from app import app, db
from auth import *
from admin import *
#from api import api
from models import *
from views import *
from flask_rum.main import rum

#Import in Rum Configs
import flask_rum.rum_config as rum_config
app.config.from_object(rum_config)
# Sample override of Theme
app.config.THEME_FOLDER='rum/banana/'

# Setup
admin.setup()

#api.setup()

if __name__ == '__main__':
    app.register_blueprint(rum) #  Flask-Rum Blueprint
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])