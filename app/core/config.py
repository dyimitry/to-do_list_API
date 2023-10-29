from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    postgres_db: str
    postgres_user: str
    postgres_password: str
    bot_backend_host: str
    token: str
    bot_backend_port: int

    redis_host: str
    redis_port: str
    # CELERY

    celery_task_serializer: str
    celery_result_serializer: str


    class Config:
        env_file = '.env'


settings = Settings()
