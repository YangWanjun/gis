import os

DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY', '')
STRIPE_API_KEY = os.getenv('STRIPE_API_KEY', '')

SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{db_name}'.format(**{
    'user': os.environ['POSTGRES_ENV_POSTGRES_USER'],
    'password': os.environ['POSTGRES_ENV_POSTGRES_PASSWORD'],
    'host': os.environ['POSTGRES_PORT_5432_TCP_ADDR'],
    'port': os.environ['POSTGRES_PORT_5432_TCP_PORT'],
    'db_name': os.environ['POSTGRES_ENV_POSTGRES_DB']
})
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
