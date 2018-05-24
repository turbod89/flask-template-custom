from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for,jsonify, abort
from werkzeug.security import check_password_hash, generate_password_hash

from ... import models


def append(bp,bp_api):

    def allowed():
        return (g.me is not None) and (g.me.belongsTo('admin'))


    @bp.route('/users', methods=('GET',))
    def users():
        if not allowed():
            return abort(404)
            

        return render_template('admin/users.html', me = g.me, groups = models.auth.Group.query.all())



    @bp_api.route('/users', methods=('GET',))
    def api_users():
        if not allowed():
            return abort(404)
            
        users = models.auth.User.query.all()
        users_json = [ user.serialize() for user in users]
        return jsonify(users_json)
