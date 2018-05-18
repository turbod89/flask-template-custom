from flask import current_app, g, jsonify, Blueprint
from .. import models
from . import main, auth

def init_app(app):
    print('routes/__init__.py init_app(app)')

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    
    app.add_url_rule('/', endpoint='index')

    return app
