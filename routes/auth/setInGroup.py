from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, abort, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

from ... import models


def append(bp,bp_api):

    @bp_api.route('/setInGroup', methods=('POST',))
    def api_setInGroup():
        if g.me is None:
            return abort(404)
        elif not g.me.belongsTo('admin'):
            return abort(404)
        
        userId = request.form['userId'] or None
        groupNames = request.form['groups'] if 'groups' in request.form else []
        print(request.get_data())
        print ([x for x in request.form])
        print(groupNames)
        
        if userId is None:
            return jsonify({'errors': [{
                'code': 1,
                'description': 'User id not provided',
            }]})

        user = models.auth.User.query.filter_by(id = userId).first()

        if user is None:
            return jsonify({'errors': [{
                'code': 1,
                'description': 'User id not valid',
            }]})
        
        groups = models.db.session.query(models.auth.Group).filter(models.auth.Group.name.in_(groupNames)).all()

        print(groups)
        

        return jsonify({'errors': []})

