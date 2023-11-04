# app/__init__.py
from flask import Flask
from app.config import Config
from app.views.main import main
from flask_injector import FlaskInjector
from injector import Binder, singleton
from app.services.timeline_service import TimelineService
from injector import Injector

def configure(binder: Binder):
    binder.bind(TimelineService, to=TimelineService, scope=singleton)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Here we can initialize extensions, such as a database, logger, etc.
    # from app.extensions import db
    # db.init_app(app)

    # Registering blueprints
    app.register_blueprint(main)

    injector = Injector([configure])

    # Initialize Flask-Injector with the configure function
    FlaskInjector(app=app, injector=injector)

    return app
