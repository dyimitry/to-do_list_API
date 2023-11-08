from celery import Celery

from app.core.config import settings


app_celery = Celery("cele", broker=settings.CELERY_BROKER_URL, backend='rpc://', include=['cele.tasks'])
