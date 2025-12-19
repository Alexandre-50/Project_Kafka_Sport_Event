import os
import time
from collections import Counter
from kafka import KafkaConsumer
from rich.live import Live
from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel
from rich.console import Console
from src.config import settings
from src.utils import loads_json

OUTPUT_PATH = os.path.join("data", "sample_output.jsonl")
console = Console()

def main() -> None:
    os.makedirs("data", exist_ok=True)

    consumer = KafkaConsumer(
        settings.topic,
        bootstrap_servers=settings.bootstrap_servers,
        group_id=settings.consumer_group,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        value_deserializer=lambda b: loads_json(b),
    )

    per_match = Counter()
    per_type = Counter()
    last_event = "Waiting for events..."
    
    # Create the Live Dashboard
    def generate_dashboard() -> Table:
        table = Table(title="Real-time Sport Events Dashboard", style="bold green")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")
        table.add_column("Detail", style="white")

        # Top Stats
        table.add_row("Total Events Processed", str(sum(per_type.values())), "Global Counter")
        table.add_row("Last Event", last_event, "Real-time feed")
        table.add_section()

        # Match Stats
        sorted_matches = per_match.most_common(5)
        match_str = ", ".join([f"{m}: {c}" for m, c in sorted_matches])
        table.add_row("Top Matches (Activity)", match_str, "Events per Match")
        
        # Type Stats
        sorted_types = per_type.most_common(5)
        type_str = ", ".join([f"{t}: {c}" for t, c in sorted_types])
        table.add_row("Event Distribution", type_str, "Events by Type")
        
        return table

    print(f"[consumer] bootstrap={settings.bootstrap_servers} topic={settings.topic}")
    
    with open(OUTPUT_PATH, "a", encoding="utf-8") as f:
        with Live(generate_dashboard(), refresh_per_second=4) as live:
            try:
                for msg in consumer:
                    event = msg.value
                    match_id = event.get("match_id", "unknown")
                    etype = event.get("event_type", "unknown")
                    
                    per_match[match_id] += 1
                    per_type[etype] += 1
                    
                    # Formatting last event for display
                    minute = event.get("minute", "?")
                    last_event = f"[{minute}'] {etype} in {match_id}"

                    f.write(str(event).replace("'", '"') + "\n")
                    f.flush()

                    live.update(generate_dashboard())
            except KeyboardInterrupt:
                console.print("\n[red]Stopping consumer...[/red]")
            finally:
                consumer.close()

if __name__ == "__main__":
    main()
