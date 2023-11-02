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
        from_attributes = True


class TaskUpdateRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[bool] = None
    last_notification: Optional[datetime] = None


# class TaskUpdate(TaskResponse):
#     pass


class LastNotificationUpdate(BaseModel):
    last_notification: datetime
