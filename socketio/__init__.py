from flask import g, session, request
from flask_socketio import SocketIO

from .. import models, routes

def init_app(app):

    socketio = SocketIO(app)
    connectedUsers = []

    def emitUsers():
        socketio.emit('connected users',[{'email': user['email']} for user in connectedUsers],json = True,namespace='/chat')

    @socketio.on('connect',namespace='/chat')
    def connect():
        routes.auth.load_logged_in_user()
        
        if g.me is not None:
            connUser = None
            for conn in connectedUsers:
                if conn['email'] == g.me.email:
                    connUser = conn

            if connUser is None:
                connectedUsers.append({
                    'userId': g.me.id,
                    'email': g.me.email,
                    'sid': request.sid
                })
            
            emitUsers()

    @socketio.on('disconnect',namespace='/chat')
    def disconnect():
        routes.auth.load_logged_in_user()

        if g.me is not None:
            conn = next( x for x in connectedUsers if x['userId'] == g.me.id)
            connectedUsers.remove(conn)
            emitUsers()

            print(str(connectedUsers))

    @socketio.on('send message to user', namespace='/chat')
    def send_message_to_user(email,message):
        
        routes.auth.load_logged_in_user()
        
        if g.me is not None:
            conn = next( x for x in connectedUsers if x['email'] == email)
            socketio.emit('get message from user',(g.me.email, message,), room=conn['sid'],namespace ='/chat')