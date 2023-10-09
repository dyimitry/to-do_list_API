from fastapi import APIRouter

from app.crud.user import create_user
from app.schemas.user import UserCreate

router = APIRouter()


@router.post('/users/')
def create_user(
        user: UserCreate
):
    new_user = create_user(user)
    return new_user