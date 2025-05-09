from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.constants.playing_roles import PlayingRoles, BattingStyles
from app.constants.bowling_styles import BowlingStyles
from app.models.player import Player, PlayingXI

class PlayerRepository(SQLAlchemyAsyncRepository[Player]):
    model_type = Player
    id_attribute = "player_id"

    async def list_players(
        self,
        name: str | None = None,
        role: PlayingRoles | None = None,
        national_team: str | None = None,
        batting_style: BattingStyles | None = None,
        bowling_style: BowlingStyles | None = None,
    ) -> list[Player]:
        query = select(Player)
        conditions = []

        if name:
            conditions.append(Player.name.ilike(f"%{name}%"))
        if role:
            conditions.append(Player.playing_role == role.value)
        if national_team:
            conditions.append(Player.national_team == national_team)
        if batting_style:
            conditions.append(Player.batting_styles.contains([batting_style.value]))
        if bowling_style:
            conditions.append(Player.bowling_styles.contains([bowling_style.value]))

        if conditions:
            query = query.where(and_(*conditions))

        result = await self.session.execute(query)
        return list(result.scalars().all())
    
    async def get_player_teams(self, player_id: str) -> list[str]:
        query = select(PlayingXI.team).where(PlayingXI.player_id == player_id).group_by(PlayingXI.team)
        result = await self.session.execute(query)
        return list(result.scalars().all())
    
    async def get_player_name(self, player_id: str) -> str:
        query = select(Player.name).where(Player.player_id == player_id)
        result = await self.session.execute(query)
        return result.scalars().one()

async def provide_player_repository(db_session: AsyncSession) -> PlayerRepository:
    return PlayerRepository(session=db_session)
