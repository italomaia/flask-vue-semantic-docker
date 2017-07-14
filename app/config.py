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

# Make sure SERVER_NAME contains the access port for
# the http server if it is not a default port (ex: dev:8080)
# Also, add "127.0.0.1 dev" to your /etc/hosts during development
SERVER_NAME = os.getenv('SERVER_NAME')

PSYCOPG2_URI = 'postgresql+psycopg2://{user}:{passwd}@{host}/{name}'
SQLALCHEMY_DATABASE_URI = PSYCOPG2_URI.format(
    user=os.getenv('POSTGRES_USER'),
    passwd=os.getenv('POSTGRES_PASSWORD'),
    host='db',
    name=os.getenv('POSTGRES_DB')
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
