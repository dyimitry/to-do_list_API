import os

import requests
from telegram_bot.client import TodoCleint
from bot import clientDB

host = os.getenv("BOT_BACKEND_HOST")
port = os.getenv("BOT_BACKEND_PORT")

#

class Producer:
    def __init__(self, host: str, port: int):
        self.url = f'http://{host}:{port}/status_false'

    def get_tasks_status_false(self):
        response = requests.get(self.url)
        result_json = response.json()
        for i in result_json:
            if i.get("urgency") == "Не срочно":
                # то ко времени из базы сейчас добавялем час
                pass
        return result_json

p = Producer()
p.get_tasks_status_false()


# def tasks_status_false(user_id):
#     url = f"http://{host}:{port}/to_do_list/user_id/{user_id}/"
#     response = requests.get(url)
#     result_json = response.json()
#     return result_json



