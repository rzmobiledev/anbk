import os
from dotenv import dotenv_values
from pathlib import Path

env: dict = dotenv_values(".env")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEBUG = bool(env.get('DEBUG'))
SECRET_KEY = env.get('DJANGO_SECRET_KEY')
ALLOWED_HOSTS: list = str(env.get('ALLOWED_HOSTS')).split(',')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static_files')
CALLBACK_URL = env.get('CALLBACK_URL')

POSTGRES: dict = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.get('POSTGRES_DB', 'anbk'),
        'USER': env.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': env.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': 'db',
        'PORT': int(env.get('POSTGRES_PORT', 5432))
    }
}


SQLITE: dict = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
