from litestar import Litestar
from app.api.routes import api_router

app = Litestar(route_handlers=[api_router])