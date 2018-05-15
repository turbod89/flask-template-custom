from flask import current_app, g, jsonify
from .. import models
from .auth import *

def init_app(app):
    print('routes/__init__.py init_app(app)')

    app.register_blueprint(auth.bp)

    return app
