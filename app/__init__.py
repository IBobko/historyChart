# app/__init__.py
from flask import Flask

from app.config import Config
from app.container import Container
from app.views.main import main

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Here we can initialize extensions, such as a database, logger, etc.
    # from app.extensions import db
    # db.init_app(app)

    # Registering blueprints
    app.register_blueprint(main)
    cont = Container()
    cont.config.from_dict(app.config)
    cont.wire(modules=["app.views.main"])  # Указываем модуль, где используется внедрение зависимостей

    return app
