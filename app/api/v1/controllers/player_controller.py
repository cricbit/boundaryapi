from litestar import Controller, get
from litestar.di import Provide
from litestar.exceptions import HTTPException

from app.models.player import Player, PlayerDTO
from app.repositories.player_repository import PlayerRepository, provide_player_repository

class PlayerController(Controller):
    path = "/players"
    dto = PlayerDTO

    dependencies = {
        "player_repository": Provide(provide_player_repository)
    }

    @get("/")
    async def list_all_players(self, player_repository: PlayerRepository) -> list[Player]:
        try:
            players = await player_repository.list()
            return players
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch players: {str(e)}"
            )
        
    @get("/{player_id:str}")
    async def get_player(self, player_id: str, player_repository: PlayerRepository) -> Player:
        try:
            player = await player_repository.get(player_id)
            return player
        except Exception:
            raise HTTPException(status_code=404, detail=f"Player not found: {player_id}")
