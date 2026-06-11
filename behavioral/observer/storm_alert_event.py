from dataclasses import dataclass
from enum import IntEnum


class WarningLevel(IntEnum):
    LOW = 1
    MODERATE = 2
    HIGH = 3
    EXTREME = 4


@dataclass(frozen=True)
class StormAlertEvent:
    message: str
    level: WarningLevel
