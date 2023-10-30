from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    postgres_db: str
    postgres_user: str
    postgres_password: str
    bot_backend_host: str
    token: str
    bot_backend_port: int


    # CELERY



    class Config:
        env_file = '.env'


settings = Settings()
