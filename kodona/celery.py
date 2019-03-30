import os
from celery import Celery
 
settings_module = 'kodona.settings.' + os.getenv('KODONA_ENV', 'dev')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
 
celery = Celery('kodona')
celery.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
celery.autodiscover_tasks()