from enum import Enum

class PlayingRoles(str, Enum):
    BATTER = "Batter"
    OPENING_BATTER = "Opening batter"
    TOP_ORDER_BATTER = "Top-order batter"
    MIDDLE_ORDER_BATTER = "Middle-order batter"
    BATTLING_ALLROUNDER = "Batting allrounder"
    WICKETKEEPER = "Wicketkeeper"
    WICKETKEEPER_BATTER = "Wicketkeeper batter"
    ALLROUNDER = "Allrounder"
    BOWLER = "Bowler"
    BOWLING_ALLROUNDER = "Bowling allrounder"
    UNKNOWN = "Unknown"


class BattingStyles(Enum):
    LEFT_HAND_BATTER = "Left-hand bat"
    RIGHT_HAND_BATTER = "Right-hand bat"
