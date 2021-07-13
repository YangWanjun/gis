import os

DEBUG = True
# SECRET_KEY is generated by os.urandom(24).
SECRET_KEY = '\x05\x95r\xf6\x8f\xfd8fA\x1d6;\xe0\xaf\xf4BD\xad\x80V>q\x16M'
STRIPE_API_KEY = ''

SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{db_name}'.format(**{
    'user': os.environ['POSTGRES_ENV_POSTGRES_USER'],
    'password': os.environ['POSTGRES_ENV_POSTGRES_PASSWORD'],
    'host': os.environ['POSTGRES_PORT_5432_TCP_ADDR'],
    'port': os.environ['POSTGRES_PORT_5432_TCP_PORT'],
    'db_name': os.environ['POSTGRES_ENV_POSTGRES_DB']
})
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True