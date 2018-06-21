from __future__ import absolute_import
from celery import Celery
app = Celery('test_celery',broker='amqp://cbim_admin:rabbitmq_VA1916w%23@172.168.1.201:5672/celery-debug',backend='file:///app/test_celery/_runtime/celery',include=['test_celery.tasks'])

