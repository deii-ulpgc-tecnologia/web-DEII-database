"""
WSGI config for web_deii_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""
from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_path = BASE_DIR / '.venv' / '.pgsql' / '.env'

print("DOTENV PATH:", dotenv_path)
print("EXISTS:", dotenv_path.exists())
load_dotenv(dotenv_path)
print("PGPASSFILE AFTER LOAD:", os.environ.get("PGPASSFILE"))

load_dotenv(dotenv_path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_deii_project.settings')

application = get_wsgi_application()
