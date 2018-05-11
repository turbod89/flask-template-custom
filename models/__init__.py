import click
from flask import current_app, g
from flask.cli import with_appcontext

from .DB import DB

from .Base import Base
from .User import User

def init_app (app):

    def get_db(config = None):

        if config is None:
            config = app.config
        
        if 'db' not in g:
            g.db = DB.getSession(config)

        return g.db


    def close_db(e=None):
        db = g.pop('db', None)

        if db is not None:
            db.close()

    def init_db():
        print ('\nInit Db\n')
        db = get_db()
        Base.metadata.create_all(db.engine)


    @app.cli.command('init-db')
    #@with_appcontext
    def init_db_command():
        """Clear the existing data and create new tables."""
        init_db()
        click.echo('Initialized the database.')
    app.cli.add_command(init_db_command)
 
    app.teardown_appcontext(close_db)


    return app