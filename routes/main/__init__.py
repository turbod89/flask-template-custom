from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from .. import models

from . import index

bp = Blueprint('main', __name__, url_prefix='/')

index.append(bp)