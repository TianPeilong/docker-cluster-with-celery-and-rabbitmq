from kombu.serialization import registry

CELERY_ACCEPT_CONTENT = ['json','application/text']
registry.enable('json')
registry.enable('application/text')