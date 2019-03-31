import os
from celery import Celery
 
settings_module = 'kodona.settings.' + os.getenv('KODONA_ENV', 'dev')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
 
celeryapp = Celery('kodona')
celeryapp.config_from_object('django.conf:settings')

celeryapp.autodiscover_tasks()