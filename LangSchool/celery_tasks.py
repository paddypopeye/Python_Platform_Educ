from __future__ import absolute_import
import os 
from django.conf import settings
from celery import Celery


#default module for celery program

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LangSchool.settings')

app = Celery('LangSchool')

app.config_from_object('django.conf.settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)