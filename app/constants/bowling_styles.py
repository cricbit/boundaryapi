from enum import Enum

class BowlingType(str, Enum):
    FAST = "Fast"
    SPIN = "Spin"

class BowlingHand(str, Enum):
    RIGHT = "Right"
    LEFT = "Left"

class BowlingStyles(str, Enum):
    FAST = ("Right-arm fast", BowlingType.FAST, BowlingHand.RIGHT)
    FAST_MEDIUM = ("Right-arm fast-medium", BowlingType.FAST, BowlingHand.RIGHT)
    MEDIUM_FAST = ("Right-arm medium-fast", BowlingType.FAST, BowlingHand.RIGHT)
    MEDIUM = ("Right-arm medium", BowlingType.FAST, BowlingHand.RIGHT)
    SLOW_MEDIUM = ("Right-arm slow-medium", BowlingType.FAST, BowlingHand.RIGHT)
    LEFT_FAST = ("Left-arm fast", BowlingType.FAST, BowlingHand.LEFT)
    LEFT_FAST_MEDIUM = ("Left-arm fast-medium", BowlingType.FAST, BowlingHand.LEFT)
    LEFT_MEDIUM_FAST = ("Left-arm medium-fast", BowlingType.FAST, BowlingHand.LEFT)
    LEFT_MEDIUM = ("Left-arm medium", BowlingType.FAST, BowlingHand.LEFT)
    LEFT_SLOW_MEDIUM = ("Left-arm slow-medium", BowlingType.FAST, BowlingHand.LEFT)

    OFFBREAK = ("Right-arm offbreak", BowlingType.SPIN, BowlingHand.RIGHT)
    SLOW = ("Right-arm slow", BowlingType.FAST, BowlingHand.RIGHT)
    LEFT_SLOW = ("Left-arm slow", BowlingType.FAST, BowlingHand.LEFT)
    LEGBREAK = ("Legbreak", BowlingType.SPIN, BowlingHand.RIGHT)
    GOOGLY = ("Legbreak googly", BowlingType.SPIN, BowlingHand.RIGHT)
    LEFT_ORTHODOX = ("Slow left-arm orthodox", BowlingType.SPIN, BowlingHand.LEFT)
    LEFT_WRIST_SPIN = ("Left-arm wrist-spin", BowlingType.SPIN, BowlingHand.LEFT)

    def __new__(cls, label, bowling_type, bowling_hand):
        obj = str.__new__(cls)
        obj._value_ = label
        obj.bowling_type = bowling_type
        obj.bowling_hand = bowling_hand
        return obj
