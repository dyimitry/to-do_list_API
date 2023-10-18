from typing import Optional

from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    user_id: int
    first_name: str
    username: Optional[str]
    last_name: Optional[str]


class UserCreateResponse(BaseModel):
    user_id: int
    first_name: str
    username: Optional[str]
    last_name: Optional[str]


class UserResponse(UserCreateResponse):
    id: int

    class Config:
        orm_mode = True
