from __future__ import absolute_import
from celery import Celery
app = Celery('test_celery',broker='redis://redis_db:6379/0',backend='redis://redis_db:6379/0',include=['test_celery.tasks'])

