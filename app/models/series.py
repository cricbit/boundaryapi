from sqlalchemy import Column, Integer, String, Date, ARRAY, Boolean
from pydantic.dataclasses import dataclass
from litestar.dto import DataclassDTO

from app.models.base import Base


class Series(Base):
    __tablename__ = "series"

    series_id = Column(String, primary_key=True)
    series_name = Column(String, nullable=False)
    season = Column(String, nullable=False)
    format = Column(String, nullable=False)
    teams = Column(ARRAY(String), nullable=False)
    has_knockouts = Column(Boolean)
    series_winner = Column(String)
    num_matches = Column(Integer, nullable=False)
    highest_scorer = Column(String)
    highest_score = Column(Integer)
    highest_wicket_taker = Column(String)
    highest_wickets = Column(Integer)


    def to_dict(self) -> dict:
        return {
            "series_id": self.series_id,
            "series_name": self.series_name,
            "season": self.season,
            "format": self.format,
            "teams": self.teams,
            "has_knockouts": self.has_knockouts,
            "series_winner": self.series_winner,
            "num_matches": self.num_matches,
            "highest_scorer": self.highest_scorer,
            "highest_score": self.highest_score,
            "highest_wicket_taker": self.highest_wicket_taker,
            "highest_wickets": self.highest_wickets,
        }


@dataclass
class SeriesResponse:
    series_id: str
    series_name: str
    season: str
    format: str
    teams: list[str]
    has_knockouts: bool
    series_winner: str
    num_matches: int

@dataclass
class SeriesStatsResponse:
    series_id: str
    series_name: str
    season: str
    format: str
    teams: list[str]
    has_knockouts: bool
    series_winner: str
    num_matches: int
    stats: dict

SeriesDTO = DataclassDTO[SeriesResponse]
SeriesStatsDTO = DataclassDTO[SeriesStatsResponse]
