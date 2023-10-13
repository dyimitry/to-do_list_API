from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, Text

from app.core.db import Base


class To_do_list(Base):
    name = Column(String(100), nullable=False)
    description = Column(String(200))
    status = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'))
