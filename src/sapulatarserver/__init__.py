import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # default config
        SECRET_KEY='dev',
        UPLOAD_FOLDER='uploads/',
        ALLOWED_EXTENSIONS=['jpg', 'jpeg', 'png']
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # TODO load rembg lib

    from . import sapulatarserver
    app.register_blueprint(sapulatarserver.sapulatarserver_bp)

    return app
