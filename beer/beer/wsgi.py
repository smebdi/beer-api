"""
WSGI config for beer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# DjangoWhiteNoise for static files
from whitenoise.django import DjangoWhiteNoise
# from whitenoise import WhiteNoise

path = 'beer/settings/prod'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beer.settings.prod")

application = DjangoWhiteNoise(get_wsgi_application())
# application = get_wsgi_application()