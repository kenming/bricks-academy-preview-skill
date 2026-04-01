#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 "$SKILL_DIR/scripts/build_preview_manifest.py"
python3 "$SKILL_DIR/scripts/sync_preview_corpus.py"
