from litestar import Litestar
from litestar.plugins.sqlalchemy import SQLAlchemyInitPlugin
from litestar.openapi.plugins import RapidocRenderPlugin, SwaggerRenderPlugin, StoplightRenderPlugin, RedocRenderPlugin
from litestar.openapi import OpenAPIConfig

from app.api.routes import api_router

from app.db.database import sqlalchemy_config

app = Litestar(
    route_handlers=[api_router],
    plugins=[
        SQLAlchemyInitPlugin(config=sqlalchemy_config),
    ],
    openapi_config=OpenAPIConfig(
        title="Boundary API",
        version="1.0.0",
        description="API for cricket statistics and data",
        render_plugins=[
            RapidocRenderPlugin(path="/rapidoc"),
            SwaggerRenderPlugin(path="/swagger"),
            StoplightRenderPlugin(path="/stoplight"),
            RedocRenderPlugin(path="/redoc")
        ]
    ),
    debug=True
)