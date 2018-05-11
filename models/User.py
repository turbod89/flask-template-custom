from .Base import Base
from sqlalchemy import Column, Integer, String, DateTime, Date, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column('id_user', Integer, nullable = False, primary_key = True, autoincrement = True)
    id_gender = Column('id_gender', Integer, nullable = False)
    id_default_group = Column('id_default_group', Integer, nullable = False)
    firstname = Column('firstname', String(32), nullable = False)
    lastname = Column('lastname', String(32), nullable = False)
    email = Column('email', String(128), nullable = False)
    password = Column('passwd', String(32), nullable = False)
    last_passwd_gen = Column('last_passwd_gen', TIMESTAMP, nullable = False)
    birthday = Column('birthday', DateTime, nullable = True)
    secure_key = Column('secure_key', String(32), nullable = False)
    ekey_md5 = Column('ekey_md5', String(32), nullable = False)
    note = Column('note', String(128), nullable = True)
    active = Column('active', String(32), nullable = False)
    is_guest = Column('is_guest', String(32), nullable = False)
    id_source = Column('id_source', Integer, nullable = False)
    deleted = Column('deleted', String(32), nullable = False)
    date_add = Column('date_add', Date, nullable = False)
    date_upd = Column('date_upd', Date, nullable = False)

    def __repr__(self):
        return "<User(id='%s')>" % (self.id)

    def __str__(self):
        return "%s %s (%s)" % (self.firstname, self.lastname, self.email)
