import os

DEBUG = os.getenv('FLASK_DEBUG') == '1'

BLUEPRINTS = ['auth']
EXTENSIONS = list(map(lambda e: 'extensions.' + e, [
    'io',
    'db',
    'migrate',
    'glue',
    'ma',
    'security'
]))

PSYCOPG2_URI = 'postgresql+psycopg2://{user}:{passwd}@{host}/{name}'
SQLALCHEMY_DATABASE_URI = PSYCOPG2_URI.format(
    user=os.getenv('POSTGRES_USER'),
    passwd=os.getenv('POSTGRES_PASSWORD'),
    host='db',
    name=os.getenv('POSTGRES_DB')
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
