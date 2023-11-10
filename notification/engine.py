from celery import Celery

from app.core.config import settings


app = Celery("notification", broker=settings.CELERY_BROKER_URL, backend='rpc://', include=['notification.tasks'])

app.conf.beat_schedule = {
    'refresh': {
        'task': 'producer',
        'schedule': 5.0
    }
}


