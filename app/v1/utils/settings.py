import os

from pydantic.v1 import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):

    db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: int = os.getenv('DB_PORT')

    secret_key: str = os.getenv('SECRET_KEY')
    token_expire: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    