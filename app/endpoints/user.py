from fastapi import APIRouter, HTTPException

from app.crud.user import create_user as create_user_controller, get_users, get_user
from app.schemas.user import UserCreateRequest, UserCreateResponse, UserDB

router = APIRouter()


@router.post('/users/', response_model=UserCreateResponse, response_model_exclude_none=True)
def create_new_user(user: UserCreateRequest):
    new_user = create_user_controller(user)
    return new_user


@router.get('/users/', response_model=list[UserDB], response_model_exclude_none=True)
def get_all_users():
    users = get_users()
    return users


@router.get('/users/{user_id}/', response_model=UserDB, response_model_exclude_none=True)
def get_user_bd(user_id: int):
    user = get_user(user_id)
    if user is None:
        raise HTTPException(
            status_code=422,
            detail='Такого пользователя не существует!',
        )
    return user
