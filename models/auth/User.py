from ..Base import Base, db
from .Group import Group
from sqlalchemy.sql import func

relUsersGroups = db.Table('relUsersGroups',
    db.Column('user', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('group', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'

    firstname = db.Column('firstname', db.String(32), nullable = True)
    lastname = db.Column('lastname', db.String(32), nullable = True)
    email = db.Column('email', db.String(128), nullable = False, unique = True)
    password = db.Column('password', db.String(128), nullable = False)

    groups = db.relationship('Group', secondary=relUsersGroups,
        backref=db.backref('users', lazy='dynamic'))
    

    def __repr__(self):
        return "<User(id='%s',email='%s')>" % (self.id, self.email)

    def __str__(self):
        if self.is_admin:
            return "!! %s %s (%s)" % (self.firstname, self.lastname, self.email)
        else:
            return "%s %s (%s)" % (self.firstname, self.lastname, self.email)
