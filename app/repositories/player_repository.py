from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.player import Player
class PlayerRepository(SQLAlchemyAsyncRepository[Player]):
    model_type = Player
    id_attribute = "player_id"

async def provide_player_repository(db_session: AsyncSession) -> PlayerRepository:
    return PlayerRepository(session=db_session)
