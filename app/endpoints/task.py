from typing import List, Optional, Union

from fastapi import APIRouter, Depends

from app.crud.task import create_new_task, get_task_id, update_task, task_delete, list_tasks

from app.schemas.task import (TaskCreateResponse, TaskCreateRequest, TaskResponse,
                              TaskUpdateRequest, TasksRequest, )

router = APIRouter(prefix='/to_do_list', tags=['To_do_list'])


@router.post('/', response_model=TaskCreateResponse)
def create_task(task: TaskCreateRequest):
    new_task = create_new_task(task)
    return new_task


@router.get('/', response_model=List[TaskResponse])
def get_tasks(params: TasksRequest = Depends()):
    tasks_models = list_tasks(params)
    return tasks_models


@router.patch('/{task_id}/', response_model=TaskResponse)
def put_task(task_id: int, task: TaskUpdateRequest):
    change_task = update_task(task_id, task)
    return change_task


@router.delete('/{task_id}/')
def delete_task(task_id: int):
    task_id = task_delete(task_id)
    return task_id
