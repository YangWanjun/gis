from sqlalchemy import types

from .. import db


class BaseModel(db.Model):
    __abstract__ = True

    created_dt = db.Column(db.DateTime, nullable=False, default=db.func.now)
    updated_dt = db.Column(db.DateTime, nullable=False, default=db.func.now, onupdate=db.func.now)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)
    deleted_dt = db.Column(db.DateTime, nullable=True)


class ChoiceType(types.TypeDecorator):

    impl = types.String

    def __init__(self, choices, **kw):
        self.choices = dict(choices)
        super(ChoiceType, self).__init__(**kw)

    def process_bind_param(self, value, dialect):
        return [k for k, v in self.choices.items() if v == value][0]

    def process_result_value(self, value, dialect):
        return self.choices[value]


class IntChoiceType(ChoiceType):
    impl = types.Integer
