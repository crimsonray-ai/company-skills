#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHON="${PYTHON:-python3}"
"$PYTHON" scripts/validate_library.py
"$PYTHON" -m unittest discover -s tests -v
