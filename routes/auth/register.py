from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from ... import models

def append(bp):
    @bp.route('/register', methods=('GET', 'POST'))
    def register():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            error = None

            if not email:
                error = 'Email is required.'
            elif not password:
                error = 'Password is required.'
            else:
                user = models.auth.User.query.filter_by(email = email).first()
                if user is not None:
                    error = 'User {} is already registered.'.format(email)

            if error is None:
                user = models.auth.User(email=email, password = generate_password_hash(password))
                models.db.session.add(user)
                models.db.session.commit()
                return redirect(url_for('auth.login'))

            flash(error)

        return render_template('auth/register.html')