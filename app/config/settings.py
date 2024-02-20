from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_CONNECT_STRING: str
    DATABASE_NAME: str
    class Config:
        env_file = './app/.env'
        extra="allow"

class TestSettings(BaseSettings):
    TEST_MONGODB_CONNECT_STRING: str
    TEST_DATABASE_NAME: str
    class Config:
        env_file = './app/.env'
        extra="allow"