from enum import Enum

class FastBowlingStyles(str, Enum):
    FAST = "Right-arm fast"
    FAST_MEDIUM = "Right-arm fast-medium"
    MEDIUM_FAST = "Right-arm medium-fast"
    MEDIUM = "Right-arm medium"
    SLOW_MEDIUM = "Right-arm slow-medium"
    SLOW = "Right-arm slow"
    LEFT_FAST = "Left-arm fast"
    LEFT_FAST_MEDIUM = "Left-arm fast-medium"
    LEFT_MEDIUM_FAST = "Left-arm medium-fast"
    LEFT_MEDIUM = "Left-arm medium"
    LEFT_SLOW_MEDIUM = "Left-arm slow-medium"
    LEFT_SLOW = "Left-arm slow"

class SpinBowlingStyles(str, Enum):
    OFFBREAK = "Right-arm offbreak"
    LEGBREAK = "Legbreak"
    GOOGLY = "Legbreak googly"
    LEFT_ORTHODOX = "Slow left-arm orthodox"
    LEFT_WRIST_SPIN = "Left-arm wrist-spin"

class BowlingStyles(str, Enum):
    # Fast Bowling Styles
    FAST = FastBowlingStyles.FAST
    FAST_MEDIUM = FastBowlingStyles.FAST_MEDIUM
    MEDIUM_FAST = FastBowlingStyles.MEDIUM_FAST
    MEDIUM = FastBowlingStyles.MEDIUM
    SLOW_MEDIUM = FastBowlingStyles.SLOW_MEDIUM
    SLOW = FastBowlingStyles.SLOW
    LEFT_FAST = FastBowlingStyles.LEFT_FAST
    LEFT_FAST_MEDIUM = FastBowlingStyles.LEFT_FAST_MEDIUM
    LEFT_MEDIUM_FAST = FastBowlingStyles.LEFT_MEDIUM_FAST
    LEFT_MEDIUM = FastBowlingStyles.LEFT_MEDIUM
    LEFT_SLOW_MEDIUM = FastBowlingStyles.LEFT_SLOW_MEDIUM
    LEFT_SLOW = FastBowlingStyles.LEFT_SLOW
    
    # Spin Bowling Styles
    OFFBREAK = SpinBowlingStyles.OFFBREAK
    LEGBREAK = SpinBowlingStyles.LEGBREAK
    GOOGLY = SpinBowlingStyles.GOOGLY
    LEFT_ORTHODOX = SpinBowlingStyles.LEFT_ORTHODOX
    LEFT_WRIST_SPIN = SpinBowlingStyles.LEFT_WRIST_SPIN

    @classmethod
    def is_fast_bowling(cls, style: str) -> bool:
        return style in [s.value for s in FastBowlingStyles]

    @classmethod
    def is_spin_bowling(cls, style: str) -> bool:
        return style in [s.value for s in SpinBowlingStyles] 