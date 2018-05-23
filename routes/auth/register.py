from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

from ... import models

def append(bp,bp_api):

    def logic():
        email = request.form['email']
        password = request.form['password']
        firstname = request.form['firstname'] or ''
        lastname = request.form['lastname'] or ''
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
            user = models.auth.User(email=email, password = generate_password_hash(password), firstname = firstname, lastname=lastname)
            group = models.auth.Group.query.filter_by(name='active').first()
            user.groups.append(group)
            models.db.session.add(user)
            models.db.session.commit()

            session.clear()
            session['user_id'] = user.id
            session['logged_in'] = True

        return error


    @bp.route('/register', methods=('GET', 'POST'))
    def register():
        if request.method == 'POST':
            error = logic()
            if error is not None:
                return redirect(url_for('index'))

            flash(error)

        return render_template('auth/register.html')



    @bp_api.route('/register', methods=('POST',))
    def api_register():
        error = logic()
        if error is not None:
            return jsonify({'errors': [{'description': error}]})


        return jsonify({'errors': []})