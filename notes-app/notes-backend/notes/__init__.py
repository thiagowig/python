import logging

from flask import current_app, Flask, redirect, url_for

def create_app(config, debug=False, testing=False, config_overrides=None):
    app = Flask(__name__)
    app.config.from_object(config)

    app.debug = debug
    app.testing = testing

    if config_overrides:
        app.config.update(config_overrides)

    if not app.testing:
        logging.basicConfig(level=logging.INFO)

    # Setup the data model.
    with app.app_context():
        model = get_model()
        model.init_app(app)

    from .crud import crud
    app.register_blueprint(crud, url_prefix='/api')    

    return app


def get_model():
    model_backend = current_app.config['DATA_BACKEND']

    if model_backend == 'datastore':
        from . import model_datastore
        model = model_datastore
    else:
        raise ValueError(
            "No appropriate databackend configured. "
            "Please specify datastore, cloudsql, or mongodb")

    return model