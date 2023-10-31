# import os
# import celery
# from dotenv import load_dotenv
# load_dotenv()
#
#
# REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
# REDIS_PORT = os.getenv("REDIS_PORT", "6379")
# CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
# CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
# app = celery.Celery("to_do_list_API",  broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
#
# # app.config_from_object("django.conf:settings", namespace="CELERY")
#
# app.autodiscover_tasks()

