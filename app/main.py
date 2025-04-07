from litestar import Litestar
from litestar.plugins.sqlalchemy import SQLAlchemyInitPlugin

from app.api.routes import api_router

from app.db.database import sqlalchemy_config

app = Litestar(
    route_handlers=[api_router],
    plugins=[SQLAlchemyInitPlugin(config=sqlalchemy_config)]
)