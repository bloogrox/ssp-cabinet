import os
import dj_database_url
from .base import *  # noqa


DEBUG = True

DATABASE_URL = os.environ['DATABASE_URL']

DATABASES = {
    'default': dj_database_url.config(
        default=DATABASE_URL,
        engine='django.db.backends.postgresql_psycopg2')
}

REDIS_URI = os.environ['REDIS_URI']
