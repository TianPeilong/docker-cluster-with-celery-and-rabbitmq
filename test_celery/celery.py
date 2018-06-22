from __future__ import absolute_import
from celery import Celery
import os

CELERY_BROKER = 'redis://redis_db:6379/0'
if 'CELERY_BROKER' in os.environ:
    CELERY_BROKER = os.environ['CELERY_BROKER']

CELERY_BACKEND = 'redis://redis_db:6379/0'
if 'CELERY_BACKEND' in os.environ:
    CELERY_BACKEND = os.environ['CELERY_BACKEND']

app = Celery('test_celery', broker=CELERY_BROKER, backend=CELERY_BACKEND, include=['test_celery.tasks'])
app.config_from_object('test_celery.celeryconfig')

