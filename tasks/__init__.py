from celery import Celery
import os
# import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ceshi.settings')
# django.setup()
broker = 'redis://127.0.0.1:6379/7'
backend = 'redis://127.0.0.1:6379/7'
app = Celery('my_ceshi', broker=broker, backend=backend)

