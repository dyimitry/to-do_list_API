import os

import requests

#
# host = os.getenv("BOT_BACKEND_HOST")
# port = os.getenv("BOT_BACKEND_PORT")


def get_tasks_status_false():

    # query = {
    #     "status": status
    # }
    params = {
        "status": False
    }
    url = f"http://127.0.0.1:8000/to_do_list"
    response = requests.get(url, params=params)
    # result_json = response.json()
    # for i in result_json:
    #     if i.get("urgency") == "Не срочно":
    #         # то ко времени из базы сейчас добавялем час
    #         pass
    return response

status=False
p = get_tasks_status_false()

print(p)
# def tasks_status_false(user_id):
#     url = f"http://{host}:{port}/to_do_list/user_id/{user_id}/"
#     response = requests.get(url)
#     result_json = response.json()
#     return result_json
