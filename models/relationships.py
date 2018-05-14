from .User import User
from .Group import Group

def generateRelationships(db):
    db.Table('relUsersGroups',
        db.Column('user', db.Integer, db.ForeignKey('users.id'), primary_key=True),
        db.Column('group', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
    )