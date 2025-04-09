from litestar import Controller, get
from litestar.di import Provide

from app.models.series import SeriesResponse, SeriesStatsResponse, SeriesDTO, SeriesStatsDTO
from app.repositories.series_repository import SeriesRepository, provide_series_repository
from app.repositories.player_repository import PlayerRepository, provide_player_repository

class SeriesController(Controller):
    path = "/series"
    dto = SeriesDTO
    tags = ["Series"]
    description = "Operations related to cricket series and tournaments"

    dependencies = {
        "series_repository": Provide(provide_series_repository),
        "player_repository": Provide(provide_player_repository)
    }

    @get("/", description="List all cricket series")
    async def list_series(self, series_repository: SeriesRepository) -> list[SeriesResponse]:
        return await series_repository.list()

    @get("/{series_id:str}", description="Get detailed information about a specific series")
    async def get_series(self, series_id: str, series_repository: SeriesRepository) -> SeriesResponse:
        return await series_repository.get(series_id)
    
    @get("/{series_id:str}/stats", dto=SeriesStatsDTO, description="Get statistics for a specific series")
    async def get_series_stats(self, series_id: str, series_repository: SeriesRepository, player_repository: PlayerRepository) -> SeriesStatsResponse:
        series = await series_repository.get(series_id)
        stats = await series_repository.get_series_stats(series_id)

        stats['highest_scorer'] = await player_repository.get_player_name(stats['highest_scorer'])
        stats['highest_wicket_taker'] = await player_repository.get_player_name(stats['highest_wicket_taker'])

        return SeriesStatsResponse(**series.to_dict(), stats=stats)
