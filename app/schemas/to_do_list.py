from typing import Optional

from datetime import datetime
from pydantic import BaseModel


class TaskCreateRequest(BaseModel):
    name: str
    description: str
    status: bool
    urgency: str
    user_id: int


class TasksRequest(BaseModel):
    user_id: Optional[int] = None
    task_id: Optional[int] = None
    status: Optional[bool] = None


class TaskCreateResponse(BaseModel):
    name: str
    description: str
    status: bool
    urgency: str
    created_at: datetime
    last_notification: Optional[datetime]
    user_id: int


class TaskResponse(TaskCreateResponse):
    id: int

    class Config:
        orm_mode = True


class TaskUpdateRequest(BaseModel):
    name: Optional[str]
    description: Optional[str]
    status: Optional[bool]


class TaskUpdate(TaskResponse):
    pass
