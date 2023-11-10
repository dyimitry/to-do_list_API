import os

import requests
import datetime
from datetime import timedelta

host = os.getenv("BOT_BACKEND_HOST")
port = os.getenv("BOT_BACKEND_PORT")


def passed_time_creation(task, time_after_do_send_created, time_after_do_send_notification, now):
    if task["last_notification"] is None:
        created_at = task.get("created_at")

        date_time_obj = datetime.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f')
        # time_after_do_send_notification >= 5:

        time_after_do_send_notification = timedelta(hours=time_after_do_send_notification)
        # time_after_do_send_notification = timedelta(time_after_do_send_notification)
        day_after_created = date_time_obj + time_after_do_send_notification

        if day_after_created < now:
            return True

        return False

    if task["last_notification"]:
        last_notification = task.get("last_notification")
        now = datetime.datetime.now()
        date_time_obj = datetime.datetime.strptime(last_notification, '%Y-%m-%dT%H:%M:%S.%f')
        time_after_do_send_created = timedelta(time_after_do_send_created)
        day_after_last_notification = date_time_obj + time_after_do_send_created

        if day_after_last_notification < now:
            return True
        return False


def get_tasks_status_false():
    list_tasks = []
    params = {
        "status": False
    }
    url = f"http://{host}:{port}/to_do_list"

    response = requests.get(url, params=params)
    result_json = response.json()

    now = datetime.datetime.now()

    for task in result_json:
        if task["urgency"] == "Не срочно":  # Не срочно !!!!!!!!!!!!
            result = passed_time_creation(task=task, time_after_do_send_created=1, time_after_do_send_notification=1,
                                          now=now)
            if result:
                list_tasks.append(task)
            continue

        if task["urgency"] == "Срочно":  # СРОЧНО
            result = passed_time_creation(task=task, time_after_do_send_created=12, time_after_do_send_notification=10,
                                          now=now)
            if result:
                list_tasks.append(task)
            continue

        result = passed_time_creation(task=task, time_after_do_send_created=5, time_after_do_send_notification=5,
                                      now=now)
        if result:
            list_tasks.append(task)
        continue

    return list_tasks

# p = get_tasks_status_false()
# print(p)
