import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()  # loads .env if present

@dataclass(frozen=True)
class Settings:
    bootstrap_servers: str = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092")
    topic: str = os.getenv("KAFKA_TOPIC", "sport.events")
    consumer_group: str = os.getenv("KAFKA_CONSUMER_GROUP", "sport-consumer")
    events_per_second: int = int(os.getenv("EVENTS_PER_SECOND", "3"))
    match_count: int = int(os.getenv("MATCH_COUNT", "5"))

settings = Settings()
