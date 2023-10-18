from typing import Optional

from pydantic import BaseModel


class TaskCreateRequest(BaseModel):
    name: str
    description: str
    status: bool
    user_id: int


class TaskCreateResponse(BaseModel):
    name: str
    description: str
    status: bool
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
