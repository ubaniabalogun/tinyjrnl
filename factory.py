"""
factory.py
"""

from flask import Flask
from core import db, api
from flask.ext.restful import Api

def create_app(app_name,config_obj):
    """
    Create the flask application
    """
    # Initialize app object
    app = Flask(app_name)
    # Configure app object
    app.config.from_object(config_obj)
    # Initialize database
    db.init_app(app)
    app.db = db

    # Initialize Api
    api.app = app
    api.init_app(app)
    app.api = api
    return app

def register_blueprints(app,*blueprints):
    """
    Registers blueprints for the application
    """
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
