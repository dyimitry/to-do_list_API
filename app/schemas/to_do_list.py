from pydantic import BaseModel


class Todo_list(BaseModel):
    name: str
    description: str
    status: bool
    user_id: int
