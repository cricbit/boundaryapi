from litestar.plugins.sqlalchemy import AsyncSessionConfig, SQLAlchemyAsyncConfig
from dotenv import load_dotenv
import os

load_dotenv()

session_config = AsyncSessionConfig(expire_on_commit=False)

sqlalchemy_config = SQLAlchemyAsyncConfig(
    session_config=session_config,
    connection_string=os.getenv("DATABASE_URL")
)
