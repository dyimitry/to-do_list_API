from app.core.db import session
from app.models.user import User
from app.schemas.user import UserCreate


def create_user(
        new_user: UserCreate
) -> User:
    new_user_data = new_user.dict()
    db_user = User(**new_user_data)
    session.add(db_user)
    session.commit()
    return db_user

