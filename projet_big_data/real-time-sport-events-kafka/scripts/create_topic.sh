#!/usr/bin/env bash
set -euo pipefail

TOPIC="${1:-sport.events}"

echo "[create_topic] Creating topic: $TOPIC"

docker exec -it kafka kafka-topics \
  --bootstrap-server kafka:9092 \
  --create --if-not-exists \
  --topic "$TOPIC" \
  --partitions 1 \
  --replication-factor 1

echo "[create_topic] Listing topics:"
docker exec -it kafka kafka-topics --bootstrap-server kafka:9092 --list
