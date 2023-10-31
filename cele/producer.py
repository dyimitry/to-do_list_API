import os

import requests
import datetime
from datetime import timedelta

host = os.getenv("BOT_BACKEND_HOST")
port = os.getenv("BOT_BACKEND_PORT")


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
            if task["last_notification"] is None:
                created_at = task.get("created_at")

                date_time_obj = datetime.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f')
                one_day = timedelta(1)
                day_after_created = date_time_obj + one_day

                if day_after_created < now:
                    print("отправялем сообщение")
                    list_tasks.append(task)

                    # now_str = datetime.datetime.strftime(now, '%Y-%m-%dT%H:%M:%S.%f')
                    # schema: LastNotificationUpdate = LastNotificationUpdate(last_notification=now_str)
                    # patch_last_notification(schema, task["id"])  # меняем время в поле last_notification
                else:
                    print("ничего")
                    continue

            if task["last_notification"]:
                last_notification = task.get("last_notification")
                now = datetime.datetime.now()
                date_time_obj = datetime.datetime.strptime(last_notification, '%Y-%m-%dT%H:%M:%S.%f')
                one_day = timedelta(1)
                day_after_last_notification = date_time_obj + one_day

                if day_after_last_notification < now:

                    print("отправялем сообщение")
                    list_tasks.append(task)

                    # now_str = datetime.datetime.strftime(now, '%Y-%m-%dT%H:%M:%S.%f')
                    # schema: LastNotificationUpdate = LastNotificationUpdate(last_notification=now_str)
                    # patch_last_notification(schema, task["id"])
                else:
                    print("ничего")
                    continue

        if task["urgency"] == "Срочно":  # СРОЧНО
            if task["last_notification"] is None:
                created_at = task.get("created_at")
                now = datetime.datetime.now()
                date_time_obj = datetime.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f')
                hours_twelve = timedelta(seconds=30)
                day_after_created = date_time_obj + hours_twelve

                if day_after_created < now:
                    print("отправялем сообщение")
                    list_tasks.append(task)

                    # now_str = datetime.datetime.strftime(now, '%Y-%m-%dT%H:%M:%S.%f')
                    # schema: LastNotificationUpdate = LastNotificationUpdate(last_notification=now_str)
                    # patch_last_notification(schema, task["id"])  # меняем время в поле last_notification
                else:
                    print("ничего")
                    continue

            if task["last_notification"]:
                last_notification = task.get("last_notification")
                now = datetime.datetime.now()
                date_time_obj = datetime.datetime.strptime(last_notification, '%Y-%m-%dT%H:%M:%S.%f')
                hours_ten = timedelta(hours=10)
                day_after_last_notification = date_time_obj + hours_ten

                if day_after_last_notification < now:  # <

                    print("отправялем сообщение")
                    list_tasks.append(task)

                    # now_str = datetime.datetime.strftime(now, '%Y-%m-%dT%H:%M:%S.%f')
                    # schema: LastNotificationUpdate = LastNotificationUpdate(last_notification=now_str)
                    # patch_last_notification(schema, task["id"])
                else:
                    print("ничего")
                    continue

        if task["urgency"] == "Очень срочно":  # ОЧЕНЬ СРОЧНО
            if task["last_notification"] is None:
                created_at = task.get("created_at")
                now = datetime.datetime.now()
                date_time_obj = datetime.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f')
                hours_five = timedelta(hours=5)
                day_after_created = date_time_obj + hours_five

                if day_after_created < now:
                    print("отправялем сообщение")
                    list_tasks.append(task)

                    # now_str = datetime.datetime.strftime(now, '%Y-%m-%dT%H:%M:%S.%f')
                    # schema: LastNotificationUpdate = LastNotificationUpdate(last_notification=now_str)
                    # patch_last_notification(schema, task["id"])  # меняем время в поле last_notification
                else:
                    print("ничего")
                    continue

            if task["last_notification"]:
                last_notification = task.get("last_notification")
                now = datetime.datetime.now()
                date_time_obj = datetime.datetime.strptime(last_notification, '%Y-%m-%dT%H:%M:%S.%f')
                hours_three = timedelta(hours=3)
                day_after_last_notification = date_time_obj + hours_three

                if day_after_last_notification < now:

                    print("отправялем сообщение")
                    list_tasks.append(task)

                    # now_str = datetime.datetime.strftime(now, '%Y-%m-%dT%H:%M:%S.%f')
                    # schema: LastNotificationUpdate = LastNotificationUpdate(last_notification=now_str)
                    # patch_last_notification(schema, task["id"])
                else:
                    print("ничего")
                    continue

    return list_tasks
