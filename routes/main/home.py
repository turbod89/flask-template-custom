from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from ... import models
def append(bp):
    @bp.route('/', methods=('GET', 'POST'))
    def home():
        return render_template('main/home.html')