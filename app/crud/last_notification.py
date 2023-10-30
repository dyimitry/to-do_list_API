from app.crud.task import get_task_id
from app.schemas.task import LastNotificationUpdate
from app.core.db import session
from fastapi.encoders import jsonable_encoder


def post_last_notification(update_dt: LastNotificationUpdate, task_id: int):
    update_data = update_dt.dict(exclude_unset=True)
    task_bd = get_task_id(task_id)
  #  obj_data = jsonable_encoder(task_bd)
    setattr(task_bd, "last_notification", update_data['last_notification'])

    session.add(task_bd)
    session.commit()
    return task_bd
