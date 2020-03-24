from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # Global variable

def create_app():

    app = Flask(__name__, instance_relative_config=False) # We define our own.
    app.config.from_object("config.Config") # <filename>.<ClassName>

    db.init_app(app) # In-app

    with app.app_context():

        # import our routes
        from . import routes

        db.create_all() # In-context

        return app
