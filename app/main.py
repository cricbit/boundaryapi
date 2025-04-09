from litestar import Litestar
from litestar.plugins.sqlalchemy import SQLAlchemyInitPlugin
from litestar.openapi.plugins import RapidocRenderPlugin, SwaggerRenderPlugin, StoplightRenderPlugin, RedocRenderPlugin, ScalarRenderPlugin
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
        tags=[
            {
                "name": "Players",
                "description": "Operations related to cricket players"
            },
            {
                "name": "Series",
                "description": "Operations related to cricket series and tournaments"
            }
        ],
        render_plugins=[
            RapidocRenderPlugin(path="/rapidoc"),
            SwaggerRenderPlugin(path="/swagger"),
            StoplightRenderPlugin(path="/stoplight"),
            RedocRenderPlugin(path="/redoc"),
            ScalarRenderPlugin(path="/scalar")
        ]
    ),
    debug=True
)