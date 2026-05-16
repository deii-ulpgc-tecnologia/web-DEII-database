from .base import *

DEBUG = False

ALLOWED_HOSTS = []

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')