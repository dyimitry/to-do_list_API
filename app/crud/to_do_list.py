from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select

from app.models import User
from app.models.to_do_list import To_do_list
from app.schemas.to_do_list import TaskCreateResponse, TaskCreateRequest, TaskUpdateRequest, TaskUpdate
from app.core.db import session


def create_new_task(task: TaskCreateRequest) -> TaskCreateResponse:
    db_user_id = session.execute(
        select(User).where(User.user_id == task.user_id)
    )
    db_user = db_user_id.scalars().first()
    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail='Такого пользователя не существует!',
        )

    db_task_model = To_do_list(
        name=task.name,
        description=task.description,
        status=task.status,
        user_id=task.user_id
    )

    session.add(db_task_model)
    session.commit()

    created_task_data: TaskCreateResponse = TaskCreateResponse(
        name=db_task_model.name,
        description=db_task_model.description,
        status=db_task_model.status,
        user_id=db_task_model.user_id
    )
    return created_task_data


def get_tasks_userid(user_id):
    tasks = session.execute(
        select(To_do_list).where(To_do_list.user_id == user_id))
    all_tasks = tasks.scalars().all()
    return all_tasks


def get_task_id(task_id: int):
    task_db = session.execute(
        select(To_do_list).where(To_do_list.id == task_id)
    )
    task = task_db.scalars().first()
    if task is None:
        raise HTTPException(
            status_code=404,
            detail='Такой задачи не существует!',
        )
    return task


def update_task(task_id: int, task: TaskUpdateRequest) -> TaskUpdate:
    task_id = get_task_id(task_id)

    update_data = task.dict(exclude_unset=True)
    obj_data = jsonable_encoder(task_id)

    for field in obj_data:
        if field in update_data:
            setattr(task_id, field, update_data[field])

    session.add(task_id)
    session.commit()

    change_task: TaskUpdate = TaskUpdate(
        name=task_id.name,
        description=task_id.description,
        status=task_id.status,
        user_id=task_id.user_id,
        id=task_id.id
    )
    return change_task


def task_delete(task_id: int):
    task_id = get_task_id(task_id)
    if task_id is None:
        raise HTTPException(
            status_code=404,
            detail='Такой задачи не существует!',
        )
    session.delete(task_id)
    session.commit()
    return task_id
