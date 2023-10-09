from sqlalchemy import Column, String

from app.core.db import Base


class To_do_list(Base):
    name = Column(String(100), unique=True, nullable=False)