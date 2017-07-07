import os

DEBUG = os.getenv('FLASK_DEBUG') == '1'

EXTENSIONS = list(map(lambda e: 'extensions.' + e, [
    'io',
]))
