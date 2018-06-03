import os
from flask import Flask

from .config import Configuration
from . import models, routes

from flask_socketio import SocketIO

def create_app(config_name):
    print('create_app.py create_app(config_name)')


    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='mysecretkey',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    app.config.from_object(Configuration(config_name))

    models.init_app(app)
    routes.init_app(app)

    socketio = SocketIO(app)

    @socketio.on('my event')
    def handle_message(message):
        print('received message: ' + str(message))
        socketio.emit('message','hello')

    return app
