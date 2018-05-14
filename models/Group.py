from .Base import Base, db
from sqlalchemy.sql import func

class Group(Base):
    __tablename__ = 'groups'

    firstname = db.Column('name', db.String(32), nullable = False, unique = True)
    lastname = db.Column('description', db.String(128), nullable = True)
    

    def __repr__(self):
        return "<Group(id='%s')>" % (self.id)

    def __str__(self):
        return "{%s}" % (self.name)
