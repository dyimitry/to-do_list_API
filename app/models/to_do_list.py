import datetime
from sqlalchemy import Column, String, Boolean, ForeignKey, Integer, DateTime
from app.core.db import Base


class To_do_list(Base):
    name = Column(String(100), nullable=False)
    description = Column(String(200))
    status = Column(Boolean, default=False)
    urgency = Column(String(100))
    created_at = Column(DateTime, default=datetime.datetime.now)
    last_notification = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
