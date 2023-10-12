from typing import Optional

from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    first_name: str
    username: Optional[str]
    last_name: Optional[str]


class UserCreateResponse(BaseModel):
    first_name: str
    username: Optional[str]
    last_name: Optional[str]


class UserDB(UserCreateResponse):
    id: int

    class Config:
        orm_mode = True
