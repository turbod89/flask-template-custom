import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from .. import models

from . import register,login,logout,setInGroup

#from libgravatar import Gravatar

bp = Blueprint('auth', __name__, url_prefix='/auth')
bp_api = Blueprint('api/auth', __name__, url_prefix='/api/auth')

def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.me = None
    else:
        g.me = models.auth.User.query.filter_by(id = user_id).first()
        #g.gravatar = Gravatar(g.me.email)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.me is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

register.append(bp,bp_api)
login.append(bp,bp_api)
logout.append(bp,bp_api)
setInGroup.append(bp,bp_api)
