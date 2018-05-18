from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from ... import models


def append(bp):
    @bp.route('/login', methods=('GET', 'POST'))
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            error = None
            user = models.auth.User.query.filter_by(email = email).first()
                

            if user is None:
                error = 'Incorrect email.'
            elif not check_password_hash(user.password, password):
                error = 'Incorrect password.'

            if error is None:
                session.clear()
                session['user_id'] = user.id
                session['logged_in'] = True
                return redirect(url_for('index'))

            flash(error)

        return render_template('auth/login.html')

