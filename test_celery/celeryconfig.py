from kombu.serialization import registry

CELERY_ACCEPT_CONTENT = ['json','application/text']
CELERYD_POOL_RESTARTS = True  # Required for /worker/pool/restart API
registry.enable('json')
registry.enable('application/text')
