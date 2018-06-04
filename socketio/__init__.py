from flask_socketio import SocketIO

from .chat import Chat

def init_app(app):

    socketio = SocketIO(app)
    
    socketio.on_namespace(Chat('/chat'))