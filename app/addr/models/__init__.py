from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init():
    """init
    """
    db.create_all()


class BaseModel(db.Model):
    __abstract__ = True

    created_dt = db.Column(db.DateTime, nullable=False, default=db.func.now)
    updated_dt = db.Column(db.DateTime, nullable=False, default=db.func.now, onupdate=db.func.now)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)
    deleted_dt = db.Column(db.DateTime, nullable=True)
