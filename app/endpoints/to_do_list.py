from typing import List

from fastapi import APIRouter

from app.crud.to_do_list import create_new_task, get_task_id, update_task, task_delete, get_tasks_userid, \
    get_tasks_status_false

from app.schemas.to_do_list import TaskCreateResponse, TaskCreateRequest, TaskResponse, TaskUpdate, TaskUpdateRequest

router = APIRouter(prefix='/to_do_list', tags=['To_do_list'])

# class MyParams(BaseModel):
#     key: Optional[str] = "key"
#     value: Optional[str] = "value"
#     param1: Optional[int] = -1


@router.post('/', response_model=TaskCreateResponse)
def create_task(task: TaskCreateRequest):
    new_task = create_new_task(task)
    return new_task


@router.get('/user_id/{user_id}/', response_model=List[TaskResponse])
def get_all_tasks(user_id: int):
    tasks = get_tasks_userid(user_id)
    return tasks


@router.get('/{task_id}/', response_model=TaskResponse)
def get_task(task_id: int):
    task = get_task_id(task_id)
    return task


@router.put('/{task_id}/', response_model=TaskUpdate)
def put_task(task_id: int, task: TaskUpdateRequest):
    change_task = update_task(task_id, task)
    return change_task


@router.delete('/{task_id}/')
def delete_task(task_id: int):
    task_id = task_delete(task_id)
    return task_id


@router.get('/status')
def get_status_false():
    tasks = get_tasks_status_false()
    return tasks
