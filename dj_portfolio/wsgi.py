"""
WSGI config for dj_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import dotenv

from django.core.wsgi import get_wsgi_application
import pathlib


CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
ENV_FILE_PATH = BASE_DIR / ".env"

dot_env = dotenv.load_dotenv(ENV_FILE_PATH)
# print(os.environ.get("NAME"))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_portfolio.settings')
application = get_wsgi_application()
