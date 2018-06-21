from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',broker='redis://172.168.1.102:6370/0',backend='redis://172.168.1.102:6370/0',include=['test_celery.tasks'])
app.config_from_object('test_celery.celeryconfig')

