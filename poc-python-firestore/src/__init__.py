from flask import current_app, Flask, redirect, url_for
from .crud import crud

def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    app.register_blueprint(crud, url_prefix='/api')

    return app