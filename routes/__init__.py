from flask import current_app, g, jsonify, Blueprint, session
from .. import models
from . import auth, main, admin

def init_app(app):
    print('routes/__init__.py init_app(app)')

    '''
        Identify username
    '''
    @auth.bp.before_app_request
    @main.bp.before_app_request
    @admin.bp.before_app_request
    @admin.bp_api.before_app_request
    def load_logged_in_user():
        auth.load_logged_in_user()

    '''
        Register modules
    '''
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(auth.bp_api)
    app.register_blueprint(admin.bp)
    app.register_blueprint(admin.bp_api)

    '''
        Error handlers
    '''
    app.register_error_handler(404, main.page_not_found)

    '''
        Special endpoints
    '''
    app.add_url_rule('/', endpoint='index')

    return app