from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from pytz import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsmart.settings')

app = Celery('newsmart')
app.conf.enable_utc = True

#app.conf.update(timezone = 'Asia/Karachi')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')