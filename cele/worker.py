import datetime
import os

import requests
import telebot


def worker(task):
    token = os.getenv("TOKEN")
    host = os.getenv("BOT_BACKEND_HOST")
    port = os.getenv("BOT_BACKEND_PORT")

    bot = telebot.TeleBot(token)
    bot.send_message(
        task["user_id"],
        text=f"ВЫполни задачу {task['name']}")

    now = datetime.datetime.now()
    now_str = datetime.datetime.strftime(now, '%Y-%m-%dT%H:%M:%S.%f')

    body = {
        "last_notification": now_str
    }

    url = f"http://{host}:{port}/to_do_list"

    response = requests.patch(url, json=body)
    if response.status_code != 200:
        print("prishla sadknfksd")

    return "uspex"
