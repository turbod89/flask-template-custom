import click
from flask import current_app, g
from flask.cli import with_appcontext

from .DB import DB

from .Base import Base
from .User import User

def init_app (app):
    print('models/__init__.py init_app(app)')

    def get_db_session(config = None):

        if config is None:
            config = app.config
        
        if 'session' not in g:
            g.db_session = DB.getSession(config)

        return g.db_session


    def close_db_session(e=None):
        session = g.pop('db_session', None)

        if session is not None:
            session.close()

    def init_db():
        print ('\nInit session\n')
        session = get_db_session()
        Base.metadata.create_all(session.bind)
        session.commit()


    @app.cli.command('init-db')
    @with_appcontext
    def init_db_command():
        """Clear the existing data and create new tables."""
        init_db()
        click.echo('Initialized the database.')
    app.cli.add_command(init_db_command)
 
    app.teardown_appcontext(close_db_session)

    app.get_db_session = get_db_session


    return app