import random
import time
from kafka import KafkaProducer
from rich.console import Console
from src.config import settings
from src.schemas import SportEvent, now_ms, new_event_id
from src.utils import dumps_json

SPORT = "football"
COMPETITION = "UEFA Champions League"

TEAMS = [
    ("Paris SG", "Real Madrid"),
    ("FC Barcelona", "Bayern Munich"),
    ("Inter", "Man City"),
    ("Arsenal", "AC Milan"),
    ("Liverpool", "Juventus"),
]

EVENT_TYPES = [
    "GOAL",
    "FOUL",
    "YELLOW_CARD",
    "SUBSTITUTION",
]

def make_event(match_id: str, home: str, away: str, minute: int) -> SportEvent:
    etype = random.choice(EVENT_TYPES)
    payload = {}

    if etype == "GOAL":
        scorer_team = random.choice([home, away])
        payload = {
            "scorer_team": scorer_team,
            "scorer": random.choice(["Player A", "Player B", "Player C", "Player D"]),
            "assist": random.choice(["Player X", "Player Y", "Player Z", None]),
            "xg": round(random.uniform(0.05, 0.8), 2),
        }
    elif etype == "FOUL":
        payload = {
            "team": random.choice([home, away]),
            "player": random.choice(["Player E", "Player F", "Player G"]),
            "severity": random.choice(["low", "medium", "high"]),
        }
    elif etype == "YELLOW_CARD":
        payload = {
            "team": random.choice([home, away]),
            "player": random.choice(["Player H", "Player I", "Player J"]),
            "reason": random.choice(["tackle", "time_wasting", "handball"]),
        }
    elif etype == "SUBSTITUTION":
        payload = {
            "team": random.choice([home, away]),
            "player_out": random.choice(["Player K", "Player L", "Player M"]),
            "player_in": random.choice(["Player N", "Player O", "Player P"]),
        }

    return SportEvent(
        event_id=new_event_id(),
        ts_ms=now_ms(),
        sport=SPORT,
        competition=COMPETITION,
        match_id=match_id,
        home_team=home,
        away_team=away,
        event_type=etype,
        minute=minute,
        payload=payload,
    )

def main() -> None:
    producer = KafkaProducer(
        bootstrap_servers=settings.bootstrap_servers,
        value_serializer=dumps_json,
        acks="all",
        retries=5,
        linger_ms=10,
    )

    matches = []
    for i in range(settings.match_count):
        home, away = TEAMS[i % len(TEAMS)]
        matches.append((f"match-{i+1}", home, away))

    console = Console()
    print(f"[producer] bootstrap={settings.bootstrap_servers} topic={settings.topic}")
    print(f"[producer] generating ~{settings.events_per_second} events/s across {len(matches)} matches")

    minute = 1
    try:
        while True:
            # produce N events each second
            for _ in range(settings.events_per_second):
                match_id, home, away = random.choice(matches)
                event = make_event(match_id, home, away, minute)
                producer.send(settings.topic, value=event.to_dict())
                
                # Style based on event type
                style = "white"
                if event.event_type == "GOAL":
                    style = "bold green"
                elif event.event_type == "red_card": 
                    style = "bold red"
                elif event.event_type == "YELLOW_CARD":
                    style = "yellow"
                elif event.event_type == "FOUL":
                    style = "dim"
                elif event.event_type == "SUBSTITUTION":
                    style = "blue"
                
                console.print(f"[{style}]{event.event_type}[/{style}] in {match_id} (min {event.minute}) [dim]{event.event_id}[/dim]")

            producer.flush(timeout=2)
            minute = 1 if minute >= 90 else minute + 1
            time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n[red][producer] stopping...[/red]")
    finally:
        producer.flush(timeout=2)
        producer.close()

if __name__ == "__main__":
    main()
