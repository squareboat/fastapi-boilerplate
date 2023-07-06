from .app import app
from .database import db

config = {
    "app": app,
    "db": db
}

from .utils.resolve import resolve