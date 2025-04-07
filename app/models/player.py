from sqlalchemy import ARRAY, Boolean, Column, Date, String
from litestar.dto import DTOConfig
from litestar.contrib.sqlalchemy.dto import SQLAlchemyDTO

from app.models.base import Base


class Player(Base):
    __tablename__ = "player_info"

    player_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    dob = Column(Date)
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


class PlayerDTO(SQLAlchemyDTO[Player]):
    config = DTOConfig()
