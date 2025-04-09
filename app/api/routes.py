from litestar import Router
from app.api.v1.controllers.player_controller import PlayerController
from app.api.v1.controllers.series_controller import SeriesController

api_router = Router(path="/v1", route_handlers=[PlayerController, SeriesController])