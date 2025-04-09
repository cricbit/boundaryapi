from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.series import Series
from app.repositories.player_repository import PlayerRepository

class SeriesRepository(SQLAlchemyAsyncRepository[Series]):
    model_type = Series
    id_attribute = "series_id"

    async def get_series_stats(self, series_id: str) -> Series:
        query = select(Series).where(Series.series_id == series_id)
        result = await self.session.execute(query)
        result = result.scalar_one_or_none()

        highest_scorer_id = result.highest_scorer
        highest_score = int(result.highest_score)
        highest_wicket_taker_id = result.highest_wicket_taker
        highest_wickets = int(result.highest_wickets)\

        result = {
            "highest_scorer": highest_scorer_id,
            "highest_score": highest_score,
            "highest_wicket_taker": highest_wicket_taker_id,
            "highest_wickets": highest_wickets,
        }

        return result



async def provide_series_repository(db_session: AsyncSession) -> SeriesRepository:
    return SeriesRepository(session=db_session)