import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    gmail_app_password: str
    gmail_email: str
    reciever_email: str

    class Config:
        env_file = ".env"  # for local dev
        case_sensitive = False
        # for local
        # @classmethod
        # def _env_file(cls, env_file):
        #     if os.path.isfile(env_file):
        #         return env_file
        #     return None


        # prod
        @classmethod
        def env(cls):
            env_vars = os.environ.copy()
            return env_vars

settings = Settings()
