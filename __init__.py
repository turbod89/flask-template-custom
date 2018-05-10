from .create_app import create_app
from .config import Configuration

create_app(Configuration('devel'))