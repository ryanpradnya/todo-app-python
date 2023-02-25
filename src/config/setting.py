from pydantic import BaseSettings


class Settings(BaseSettings):
    ENGINE_VERSION: str = '0.1.0'

    # == MongoDB ==
    MONGO_CONNECTION: str
    MONGO_DATABASE: str
    # mongo_username: str
    # mongo_password: str
    # mongo_bucket: str
    # mongo_timeout: int = 30
    # mongo_nlql_timeout: int = 300


    # == Redis ==
    # redis_connection: str

    class Config:
        env_file = '.env'


settings = Settings()
