from flask import current_app, g, jsonify, Blueprint
from .. import models
from . import auth

def init_app(app):
    print('routes/__init__.py init_app(app)')

    app.register_blueprint(auth.bp)


    bp = Blueprint('/',__name__)
    
    @bp.route('/')
    def index():
        return ''
    
    app.add_url_rule('/', endpoint='index')

    return app
