from .base import *
from django.core.management.utils import get_random_secret_key


DEBUG = False

ALLOWED_HOSTS = ['*']

SECRET_KEY = get_random_secret_key()

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "OPTIONS": {
            "service": os.environ.get("PGSERVICE"),
            "passfile": os.environ.get("PGPASSFILE"),
        },
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'