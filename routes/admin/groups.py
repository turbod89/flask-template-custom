from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for,jsonify, abort
from werkzeug.security import check_password_hash, generate_password_hash

from ... import models
from .. import auth


def append(bp,bp_api):


    @bp.route('/groups', methods=('GET',))
    @auth.login_required
    @auth.group_required('active')
    @auth.group_required('admin')
    @auth.notin_group_required('blocked')
    def groups():
        return render_template('admin/groups.html', me = g.me, groups = models.auth.Group.query.all())



    @bp_api.route('/groups', methods=('GET',))
    @auth.login_required
    @auth.group_required('active')
    @auth.group_required('admin')
    @auth.notin_group_required('blocked')
    def api_groups():
            
        groups = models.auth.Group.query.all()
        groups_json = [ group.serialize() for group in groups]
        return jsonify(groups_json)
