from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import declarative_base, Session, declared_attr
from app.core.config import settings


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)


Base = declarative_base(PreBase)

engine = create_engine(settings.db_url)

session = Session(engine)

