from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Date, TIMESTAMP, ForeignKey
from sqlalchemy.sql.expression import func

class Base(object):
    id = Column('id_user', Integer, nullable = False, primary_key = True, autoincrement = True)
    deleted = Column('deleted', Integer, nullable=False, default = 0)
    date_add = Column('date_add', Date, nullable=False, default = func.now())
    date_upd = Column('date_upd', Date, nullable=False, default = func.now())

Base = declarative_base(cls=Base)
