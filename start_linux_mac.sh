#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

PORT="${PORT:-8080}"

echo "=============================================================="
echo "  MEMULAI SERVER MAZEBOT EDUKIT LEARNING PORTAL (PORT: $PORT)"
echo "=============================================================="

if command -v python3 >/dev/null 2>&1; then
    exec python3 server.py --port "$PORT"
elif command -v python >/dev/null 2>&1; then
    exec python server.py --port "$PORT"
elif command -v npx >/dev/null 2>&1; then
    exec npx --yes serve -l "$PORT" .
else
    echo "Error: Python3 atau Node.js tidak ditemukan di sistem ini."
    exit 1
fi
