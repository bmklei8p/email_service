import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    gmail_app_password: str
    gmail_email: str
    reciever_email: str

    class Config:
        env_file = ".env"  # for local dev
        case_sensitive = False

        @classmethod
        def env(cls):
            env_vars = os.environ.copy()
            return env_vars

settings = Settings()
