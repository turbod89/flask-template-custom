from flask import g, session, request

from flask_socketio import Namespace, emit

from .. import models, routes

def load_login_or_ignore(func):
    def wrapped_func(*args,**kwargs):
        routes.auth.load_logged_in_user()
        if g.me is None:
            return None

        return func(*args,**kwargs)

    return wrapped_func

class Chat(Namespace):

    '''
        Constructor
    '''
    def __init__(self, *args, **kwargs):
        self.connectedUsers = []
        super(Chat,self).__init__(*args,**kwargs)

    '''
        Helpers
    '''
    def emitUsers(self):
        print('\nemit\n')
        self.emit('connected_users',[{'email': user['email']} for user in self.connectedUsers])

    '''
        On connect
    '''
    @load_login_or_ignore
    def on_connect(self):


        connUser = None
        for conn in self.connectedUsers:
            if conn['email'] == g.me.email:
                connUser = conn

        if connUser is None:
            self.connectedUsers.append({
                'userId': g.me.id,
                'email': g.me.email,
                'sid': request.sid
            })
        
        self.emitUsers()

    
    '''
        On disconnect
    '''
    @load_login_or_ignore
    def on_disconnect(self):

        conn = next( x for x in self.connectedUsers if x['userId'] == g.me.id)
        self.connectedUsers.remove(conn)
        self.emitUsers()

    
    '''
        On custom events
    '''
    @load_login_or_ignore
    def on_send_message_to_user(self,email,message):

        conn = next( x for x in self.connectedUsers if x['email'] == email)
        self.emit('get_message_from_user',(g.me.email, message,), room=conn['sid'])