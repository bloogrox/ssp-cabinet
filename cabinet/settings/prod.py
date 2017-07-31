from .base import *  # noqa
import os
import dj_database_url


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'UTC'

DATABASE_URL = os.environ['DATABASE_URL']

DATABASES = {
    'default': dj_database_url.config(
        default=DATABASE_URL,
        engine='django.db.backends.postgresql_psycopg2')
}
