from .Base import Base
from sqlalchemy import Column, Integer, String, DateTime, Date, TIMESTAMP, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func

class User(Base):
    __tablename__ = 'users'

    id_gender = Column('id_gender', Integer, nullable = False)
    id_default_group = Column('id_default_group', Integer, nullable = False)
    firstname = Column('firstname', String(32), nullable = False)
    lastname = Column('lastname', String(32), nullable = False)
    email = Column('email', String(128), nullable = False)
    password = Column('passwd', String(32), nullable = False)
    last_passwd_gen = Column('last_passwd_gen', TIMESTAMP, nullable = False, default = func.now())
    birthday = Column('birthday', DateTime, nullable = True)
    secure_key = Column('secure_key', String(32), nullable = False)
    ekey_md5 = Column('ekey_md5', String(32), nullable = False)
    note = Column('note', String(128), nullable = True)
    active = Column('active', String(32), nullable = False)
    is_guest = Column('is_guest', Boolean, nullable = False, default = False)
    is_admin = Column('is_admin', Boolean, nullable = False, default = False)
    id_source = Column('id_source', Integer, nullable = False)
    

    def __repr__(self):
        return "<User(id='%s')>" % (self.id)

    def __str__(self):
        if self.is_admin:
            return "!! %s %s (%s)" % (self.firstname, self.lastname, self.email)
        else:
            return "%s %s (%s)" % (self.firstname, self.lastname, self.email)
