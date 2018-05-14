from .Base import Base, db
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = 'users'

    firstname = db.Column('firstname', db.String(32), nullable = True)
    lastname = db.Column('lastname', db.String(32), nullable = True)
    email = db.Column('email', db.String(128), nullable = False, unique = True)
    password = db.Column('password', db.String(32), nullable = False)
    is_admin = db.Column('is_admin', db.Boolean, nullable = False, default = False)
    

    def __repr__(self):
        return "<User(id='%s')>" % (self.id)

    def __str__(self):
        if self.is_admin:
            return "!! %s %s (%s)" % (self.firstname, self.lastname, self.email)
        else:
            return "%s %s (%s)" % (self.firstname, self.lastname, self.email)
