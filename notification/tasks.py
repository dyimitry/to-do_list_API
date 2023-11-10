import datetime
import os

import requests
import telebot
from dotenv import load_dotenv

from notification.engine import app
from notification.producer import get_tasks_status_false

load_dotenv()


@app.task(bind=True, queue="notification")
def worker(self, task):
    print("111111111111111111111111111111111111111111")
    print(task)
    token = os.getenv("TOKEN")
    host = os.getenv("BOT_BACKEND_HOST")
    port = os.getenv("BOT_BACKEND_PORT")

    bot = telebot.TeleBot(token)
    bot.send_message(
        task["user_id"],
        text=f"Не забудь выполнить задачу: {task['name']}")

    now = datetime.datetime.now()
    now_str = datetime.datetime.strftime(now, '%Y-%m-%dT%H:%M:%S.%f')

    body = {
        "last_notification": now_str
    }

    url = f"http://{host}:{port}/to_do_list/{task['id']}"

    response = requests.patch(url, json=body)
    if response.status_code != 200:
        print(response.status_code)
        print(response.text)
        raise Exception("Come answer no 200")

    return "uspex"


@app.task(name="producer")
def producer():
    result = get_tasks_status_false()
    print(f"received count task: {len(result)}")
    for task in result:
        print(f"send task: {task}")
        worker.apply_async(args=(task,))

# celery -A cele.engine:app_celery worker -Q notification -l info -P solo
