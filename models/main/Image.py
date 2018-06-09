from ..Base import Base, db
from sqlalchemy.sql import func

class Image(Base):
    __abstract__ = True

    file_descriptor = db.Column('file_descriptor', db.String(128), nullable = False)
    file_mime = db.Column('file_mime', db.String(32), nullable = False)

    def __repr__(self):
        return "<Image(id='%s',fd='%s')>" % (self.id, self.file_mime)

    def __str__(self):
        return "%s" % (self.id, )

    def serialize(self):
        obj = super(Image,self).serialize()
        
        obj['file_descriptor'] = self.file_descriptor
        obj['file_mime'] = self.file_mime
        
        return obj
