from sqlalchemy import Boolean, Column, Date, String
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import date
from litestar.dto import DataclassDTO
from pydantic.dataclasses import dataclass
from typing import Optional

from app.models.base import Base


class Player(Base):
    __tablename__ = "player_info"

    player_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    dob = Column(Date, nullable=True)
    gender = Column(String)
    batting_styles = Column(ARRAY(String))
    bowling_styles = Column(ARRAY(String))
    image_url = Column(String)
    national_team = Column(String)
    playing_role = Column(String)
    is_active = Column(Boolean)

    def to_dict(self) -> dict:
        return {
            "player_id": self.player_id,
            "name": self.name,
            "dob": self.dob,
            "gender": self.gender,
            "batting_styles": self.batting_styles,
            "bowling_styles": self.bowling_styles,
            "image_url": self.image_url,
            "national_team": self.national_team,
            "playing_role": self.playing_role,
            "is_active": self.is_active
        }

class PlayingXI(Base):
    __tablename__ = "playing_xi"

    match_id = Column(String, nullable=False, primary_key=True)
    player_id = Column(String, nullable=False, primary_key=True)
    team = Column(String, nullable=False)
    opponent = Column(String, nullable=False)

@dataclass
class PlayerResponse:
    player_id: str
    name: str
    dob: date | None
    gender: str
    batting_styles: list[str]
    bowling_styles: list[str]
    image_url: str
    national_team: str
    playing_role: str
    is_active: bool
    teams: Optional[list[str]] = None

PlayerDTO = DataclassDTO[PlayerResponse]