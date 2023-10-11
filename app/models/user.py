from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class User(Base):
    first_name = Column(String(100), nullable=False)
    username = Column(String(100))
    last_name = Column(String(100))
    to_do_list = relationship("To_do_list", cascade="delete")
