import click
from flask import current_app, g
from flask.cli import with_appcontext

from .DB import DB

from .Base import Base
from .User import User

def init_app (app):

    print ('__init__.py models init_app')
    print (''+str('DATABASE_URI' in app.config)+'\n')

    def get_db(config = None):

        if config is None:
            config = app.config

        config = app.config
        
        if 'db' not in g:
            g.db = DB.getSession(config)

        return g.db


    def close_db(e=None):
        db = g.pop('db', None)

        if db is not None:
            db.close()

    def init_db(config):
        db = get_db()
        Base.metadata.create_all(db.engine)



    @click.command('init-db')
    @click.argument('config')
    @with_appcontext
    def init_db_command(config = None):
        """Clear the existing data and create new tables."""
        init_db(config)
        click.echo('Initialized the database.')

    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


    pass