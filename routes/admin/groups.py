from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for,jsonify, abort
from werkzeug.security import check_password_hash, generate_password_hash

from ... import models


def append(bp,bp_api):

    def allowed():
        return (g.me is not None) and (g.me.belongsTo('admin'))


    @bp.route('/groups', methods=('GET',))
    def groups():
        if not allowed():
            return abort(404)
            

        return render_template('admin/groups.html', me = g.me, groups = models.auth.Group.query.all())



    @bp_api.route('/groups', methods=('GET',))
    def api_groups():
        if not allowed():
            return abort(404)
            
        groups = models.auth.Group.query.all()
        groups_json = [ group.serialize() for group in groups]
        return jsonify(groups_json)
