from __future__ import absolute_import, unicode_literals
# Django settings
import os
from django.conf import settings
# Celery app
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Somnium.settings')

app = Celery('Somnium')

# namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://redis:6379'
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
