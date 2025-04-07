from litestar import Controller, get
from litestar.di import Provide
from litestar.exceptions import HTTPException
from litestar.params import Parameter

from app.constants.playing_roles import PlayingRoles, BattingStyles
from app.constants.bowling_styles import BowlingStyles

from app.models.player import Player, PlayerDTO
from app.repositories.player_repository import PlayerRepository, provide_player_repository

class PlayerController(Controller):
    path = "/players"
    dto = PlayerDTO

    dependencies = {
        "player_repository": Provide(provide_player_repository)
    }

    @get("/")
    async def list_players(
        self,
        player_repository: PlayerRepository,
        name: str | None = Parameter(query="name", default=None),
        role: PlayingRoles | None = Parameter(query="role", default=None),
        national_team: str | None = Parameter(query="national_team", default=None),
        is_active: bool | None = Parameter(query="is_active", default=None),
        batting_style: BattingStyles | None = Parameter(query="batting_style", default=None),
        bowling_style: BowlingStyles | None = Parameter(query="bowling_style", default=None),
    ) -> list[Player]:
        try:
            players = await player_repository.list(
                name=name,
                role=role,
                national_team=national_team,
                is_active=is_active,
                batting_style=batting_style,
                bowling_style=bowling_style.value if bowling_style else None
            )
            return players
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch players: {str(e)}"
            )
        
    @get("/{player_id:str}")
    async def get_player_by_id(self, player_id: str, player_repository: PlayerRepository) -> Player:
        try:
            player = await player_repository.get(player_id)
            return player
        except Exception:
            raise HTTPException(status_code=404, detail=f"Player not found: {player_id}")
