from fastapi import APIRouter

from app.crud.user import create_user as create_user_controller
from app.schemas.user import UserCreateRequest, UserCreateResponse

router = APIRouter()


@router.post('/users/', response_model=UserCreateResponse)
def create_new_user(user: UserCreateRequest):
    new_user = create_user_controller(user)
    return new_user
