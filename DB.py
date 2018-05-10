import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker

class DB():

    
    session = None

    @staticmethod
    def getSession(config = {}):
        if DB.session is None:
            Session = sessionmaker()
            engine = sqlalchemy.create_engine(config['DATABASE_URI'], echo=False)
            Session.configure(bind=engine)

            session = Session()
            DB.session = session    

        return DB.session


    @staticmethod
    def closeSession():
        if DB.session is not None:
            DB.session.close()