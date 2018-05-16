import click
from flask import current_app, g
from flask.cli import with_appcontext

from .db import db
from . import auth

def init_app (app):
    print('models/__init__.py init_app(app)')

    db.init_app(app)
    auth.init_app(app,db)


    def get_db_session(config = None):

        if config is None:
            config = app.config
        
        if 'session' not in g:
            g.db_session = db

        return g.db_session


    def close_db_session(e=None):
        session = g.pop('db_session', None)

        if session is not None:
            session.close()

    def init_db():
        print ('Destroying database...')
        db.drop_all()
        print('Commiting...')
        db.session.commit()
        print('Creating all again...')
        db.create_all()
        print('Comminting...')
        db.session.commit()
        print('Generating auth module...')
        auth.generate(db)


    @app.cli.command('init-db')
    @with_appcontext
    def init_db_command():
        """Clear the existing data and create new tables."""
        init_db()
    app.cli.add_command(init_db_command)
 
    app.teardown_appcontext(close_db_session)

    app.get_db = get_db_session


    return app