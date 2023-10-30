import datetime
from datetime import timedelta
# from time import strptime

from app.crud.last_notification import post_last_notification
from app.schemas.task import LastNotificationUpdate

response = [{'created_at': '2023-10-30T11:47:40.708941', 'description': 'string', 'id': 3, 'last_notification': None, 'name': '21', 'status': False, 'urgency': 'string', 'user_id': 1}]
for task in response:
    if task["last_notification"] is None:
        created_at = task.get("created_at")
        now = datetime.datetime.now()
        date_time_obj = datetime.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f')
        one_day = timedelta(1)
        day_after_created = date_time_obj + one_day
        day_after_created_str = datetime.datetime.strftime(date_time_obj, '%Y-%m-%dT%H:%M:%S.%f')
        schema: LastNotificationUpdate = LastNotificationUpdate(last_notification=day_after_created_str)

        if day_after_created > now:
            day_after_created_str = datetime.datetime.strftime(date_time_obj, '%Y-%m-%dT%H:%M:%S.%f')
            print("отправялем сообщение")
            post_last_notification(schema, task["id"])
        else:
            print("ничего")




# date += DT.timedelta(hours=2)
# print(date.strftime('%d/%m/%Y %H:%M:%S'))
# # 23/01/2020 17:19:55