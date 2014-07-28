from os import environ


DEBUG = bool(environ.get('DEBUG', False))
