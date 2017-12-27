import os
from utils import load_env

DEBUG = os.getenv('FLASK_DEBUG') == '1'
SECRET_KEY = load_env('FLASK_SECRET_KEY')

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
# the http server if it is not a default port (ex: dv:8080)
# Also, add "127.0.0.1 dv" to your /etc/hosts during development
SERVER_NAME = os.getenv('SERVER_NAME') + os.getenv('SERVER_NAME_EXTRA', '')

PSYCOPG2_URI = 'postgresql+psycopg2://{user}:{passwd}@{host}/{name}'
SQLALCHEMY_DATABASE_URI = PSYCOPG2_URI.format(
    user=load_env('POSTGRES_USER'),
    passwd=load_env('POSTGRES_PASSWORD'),
    host='db',
    name=load_env('POSTGRES_DB')
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
