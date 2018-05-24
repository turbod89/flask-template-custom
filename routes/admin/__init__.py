import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from .. import models

from . import users

#from libgravatar import Gravatar

bp = Blueprint('admin', __name__, url_prefix='/admin')
bp_api = Blueprint('api/admin', __name__, url_prefix='/api/admin')

users.append(bp,bp_api)