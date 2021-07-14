from ... import db


def init():
    """init
    """
    db.create_all()
