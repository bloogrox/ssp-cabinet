from .base import *


DEBUG = True

DATABASE_URL = os.environ['DATABASE_URL']

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, engine='django.db.backends.postgresql_psycopg2')
}

