# config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    gmail_app_password: str
    gmail_email: str
    reciever_email: str

    class Config:
        env_file = ".env"
