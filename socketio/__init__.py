from flask import g, session, request
from flask_socketio import SocketIO

from .. import models, routes

def generateToken(user):
    return str(user.email)

def checkUserWithToken(user,token):
    if str(user.email) == token:
        return True

    return False

def init_app(app):

    socketio = SocketIO(app)
    connectedUsers = []

    def emitUsers():
        socketio.emit('message',[email for email in connectedUsers])

    @socketio.on('connect')
    def connect():
        routes.auth.load_logged_in_user()
        
        if g.me is not None:
            connUser = None
            for conn in connectedUsers:
                if conn['email'] == g.me.email:
                    connUser = conn

            if connUser is None:
                connectedUsers.append({
                    'email': g.me.email,
                    'sid': request.sid
                })
                emitUsers()

    @socketio.on('disconnect')
    def disconnect():
        routes.auth.load_logged_in_user()

        if g.me is not None:
            connectedUsers.remove(g.me.email)
            emitUsers()
