import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    database_url: str = Field(..., env='DATABASE_URL')
    db_name: str = Field(..., env='POSTGRES_DB')
    user: str = Field(..., env='POSTGRES_USER')
    password: str = Field(..., env='POSTGRES_PASSWORD')
    host: str = Field(..., env='HOST')


    class Config:
        env_file = '.env'


settings = Settings()
