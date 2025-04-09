from litestar import Controller, get
from litestar.di import Provide
from litestar.exceptions import HTTPException
from litestar.params import Parameter

from app.constants.playing_roles import PlayingRoles, BattingStyles
from app.constants.bowling_styles import BowlingStyles

from app.models.player import PlayerResponse, PlayerDTO
from app.repositories.player_repository import PlayerRepository, provide_player_repository

class PlayerController(Controller):
    path = "/players"
    dto = PlayerDTO
    tags = ["Players"]
    description = "Operations related to cricket players"

    dependencies = {
        "player_repository": Provide(provide_player_repository)
    }

    @get("/", description="List all players with optional filtering")
    async def list_players(
        self,
        player_repository: PlayerRepository,
        name: str | None = Parameter(query="name", default=None, description="Filter by player name"),
        role: PlayingRoles | None = Parameter(query="role", default=None, description="Filter by playing role"),
        national_team: str | None = Parameter(query="national_team", default=None, description="Filter by national team"),
        batting_style: BattingStyles | None = Parameter(query="batting_style", default=None, description="Filter by batting style"),
        bowling_style: BowlingStyles | None = Parameter(query="bowling_style", default=None, description="Filter by bowling style"),
    ) -> list[PlayerResponse]:
        try:
            players = await player_repository.list_players(
                name=name,
                role=role,
                national_team=national_team,
                batting_style=batting_style,
                bowling_style=bowling_style
            )
            return [PlayerResponse(**player.to_dict()) for player in players]
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch players: {str(e)}"
            )
        
    @get("/{player_id:str}", description="Get detailed information about a specific player")
    async def get_player_by_id(self, player_id: str, player_repository: PlayerRepository) -> PlayerResponse:
        try:
            player = await player_repository.get(player_id)
            teams = await player_repository.get_player_teams(player_id)
            return PlayerResponse(**player.to_dict(), teams=teams)
        except Exception:
            raise HTTPException(status_code=404, detail=f"Player not found: {player_id}")
