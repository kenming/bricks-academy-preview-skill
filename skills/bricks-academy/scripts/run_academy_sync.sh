#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 "$SKILL_DIR/scripts/build_academy_manifest.py"
python3 "$SKILL_DIR/scripts/sync_academy_corpus.py"
