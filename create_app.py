import os
from flask import Flask
from . import models

def create_app(config):

    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='mysecretkey',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    app.config.from_object(config)

    models.init_app(app)

    return app