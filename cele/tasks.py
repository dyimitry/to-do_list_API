import requests
from app.core.celery import app
from app.models import To_do_list


@app.task
def processing_file(json_data):
    files = To_do_list.objects.get(file=json_data["urgency"])
    for file in files:
        if file == "Срочно":
            file.processed = True
            file.save()
