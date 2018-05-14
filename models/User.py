from .Base import Base, db
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = 'users'


    #id = db.Column('id_user', db.Integer, nullable = False, primary_key = True, autoincrement = True)
    id_gender = db.Column('id_gender', db.Integer, nullable = False)
    id_default_group = db.Column('id_default_group', db.Integer, nullable = False)
    firstname = db.Column('firstname', db.String(32), nullable = True)
    lastname = db.Column('lastname', db.String(32), nullable = True)
    email = db.Column('email', db.String(128), nullable = False, unique = True)
    password = db.Column('passwd', db.String(32), nullable = False)
    last_passwd_gen = db.Column('last_passwd_gen', db.DateTime, nullable = False, default = func.now())
    birthday = db.Column('birthday', db.DateTime, nullable = True)
    secure_key = db.Column('secure_key', db.String(32), nullable = False)
    ekey_md5 = db.Column('ekey_md5', db.String(32), nullable = False)
    note = db.Column('note', db.String(128), nullable = True)
    active = db.Column('active', db.String(32), nullable = False)
    is_guest = db.Column('is_guest', db.Boolean, nullable = False, default = False)
    is_admin = db.Column('is_admin', db.Boolean, nullable = False, default = False)
    id_source = db.Column('id_source', db.Integer, nullable = False)
    

    def __repr__(self):
        return "<User(id='%s')>" % (self.id)

    def __str__(self):
        if self.is_admin:
            return "!! %s %s (%s)" % (self.firstname, self.lastname, self.email)
        else:
            return "%s %s (%s)" % (self.firstname, self.lastname, self.email)
