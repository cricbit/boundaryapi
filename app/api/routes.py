from litestar import Router
from app.api.v1.controllers.player_controller import PlayerController

api_router = Router(path="/v1", route_handlers=[PlayerController])