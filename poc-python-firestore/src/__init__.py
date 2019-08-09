from flask import current_app, Flask, redirect, url_for
from .endpoint import endpoint

def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    app.register_blueprint(endpoint, url_prefix='/api')

    return app