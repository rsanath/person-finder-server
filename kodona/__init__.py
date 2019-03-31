# order of import matters
from .celery import celeryapp
from img_processor import tasks