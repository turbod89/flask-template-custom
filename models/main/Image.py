from ..Base import Base, db
from sqlalchemy.sql import func

from flask import current_app

import re
import os
import math
import base64
from io import BytesIO
from PIL import Image as PIL_Image
import time


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

    @staticmethod
    def save_from_urlData(data, filename = None):
        r = re.compile('data:(.+);base64,')
        match = re.search(r, data)
        file_mime = match.group(1)

        directory = os.path.join(current_app.config['UPLOADED_FILES_DEST'])
        try:
            os.stat(directory)
        except:
            os.mkdir(directory)
        
        if filename is None:
            filename = 'image_'+str(math.floor(1000*time.time()))

        file_descriptor = os.path.join(
            directory, filename)

        if file_mime == 'image/png':
            file_descriptor += '.png'
        elif file_mime == 'image/jpg':
            file_descriptor += '.jpg'

        image_data = bytes(re.sub(r, '', data), encoding='ascii')

        image = PIL_Image.open(BytesIO(base64.b64decode(image_data)))
        image.save(file_descriptor)

        return file_descriptor, file_mime
