from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_CONNECT_STRING: str
    class Config:
        env_file = './app/.env'