from fastapi import APIRouter, HTTPException

from app.crud.user import create_user as create_user_controller, get_users, get_user_id
from app.schemas.user import UserCreateRequest, UserCreateResponse, UserResponse

router = APIRouter(prefix='/users', tags=['User'])


@router.post('/', response_model=UserCreateResponse, response_model_exclude_none=True)
def create_new_user(user: UserCreateRequest):
    new_user = create_user_controller(user)
    return new_user


@router.get('/', response_model=list[UserResponse], response_model_exclude_none=True)
def get_all_users():
    users = get_users()
    return users


@router.get('/{user_id}/', response_model=UserResponse, response_model_exclude_none=True)
def get_user(user_id: int):
    user = get_user_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail='Такого пользователя не существует!',
        )
    return user
