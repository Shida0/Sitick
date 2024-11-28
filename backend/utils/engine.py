from sqlalchemy.ext.asyncio import create_async_engine

from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "db_user": os.getenv("DB_USER"),
    "db_password": os.getenv("DB_PASSWORD"),
    "db_host": os.getenv("DB_HOST"),
    "db_port": os.getenv("DB_PORT"),
    "db_name": os.getenv("DB_NAME")
}

url = f"postgresql+asyncpg://{config['db_user']}:{config['db_password']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"

engine = create_async_engine(
    url,
    echo=True
)