import os
from celery import Celery
from django.conf import settings

# settings module Celery



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookmarks.settings')
os.environ.setdefault('C_FORCE_ROOT', 'true')
app = Celery('bookmarks')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
