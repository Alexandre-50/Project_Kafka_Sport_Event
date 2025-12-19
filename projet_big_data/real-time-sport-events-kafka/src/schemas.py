from dataclasses import dataclass, asdict
from typing import Literal, Optional, Dict, Any
import time
import uuid

EventType = Literal[
    "MATCH_START",
    "PERIOD_START",
    "GOAL",
    "FOUL",
    "YELLOW_CARD",
    "RED_CARD",
    "SUBSTITUTION",
    "PERIOD_END",
    "MATCH_END",
]

@dataclass
class SportEvent:
    event_id: str
    ts_ms: int
    sport: str
    competition: str
    match_id: str
    home_team: str
    away_team: str
    event_type: EventType
    minute: int
    payload: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

def now_ms() -> int:
    return int(time.time() * 1000)

def new_event_id() -> str:
    return str(uuid.uuid4())
