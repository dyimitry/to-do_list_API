import logging
from datetime import timedelta

from celery import Celery

from app.core.config import settings

# Configure the logging for Celery Beat
beat_logger = logging.getLogger('celery.beat')
beat_logger.setLevel(logging.DEBUG)
beat_logger.addHandler(logging.StreamHandler())

app = Celery("notification", broker=settings.CELERY_BROKER_URL, backend='rpc://', include=['notification.tasks'])


app.conf.beat_schedule = {
    'refresh': {
        'task': 'producer',
        'schedule': timedelta(seconds=5),
        'options': {
            'queue': 'notification',
        }
    }
}
