from app.core.db import session
from app.models.user import User
from app.schemas.user import UserCreateRequest, UserCreateResponse


def create_user(new_user: UserCreateRequest) -> UserCreateResponse:
    db_user_model = User(
        first_name=new_user.first_name,
        username=new_user.username,
        last_name=new_user.last_name
    )

    session.add(db_user_model)
    session.commit()

    created_user_data: UserCreateResponse = UserCreateResponse(
        first_name=db_user_model.first_name,
        username=db_user_model.username,
        last_name=db_user_model.last_name
    )

    return created_user_data

