from flask import current_app, g, jsonify
from .. import models

def init_app(app):
    print('routes/__init__.py init_app(app)')

    @app.route('/')
    def index():
        
        print (g)
        db = models.db
        users = models.User.query.all()
        return jsonify(users)


    return app
