"""
WSGI config for stdb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stdb.settings')

application = get_wsgi_application()

project_folder = os.path.expanduser('../stdb/')
load_dotenv(os.path.join(project_folder, '.env'))
