#!/usr/bin/env bash
set -euo pipefail

echo "[smoke_test] docker compose ps"
docker compose ps

echo "[smoke_test] list topics"
docker exec -it kafka kafka-topics --bootstrap-server kafka:9092 --list

echo "[smoke_test] OK"
