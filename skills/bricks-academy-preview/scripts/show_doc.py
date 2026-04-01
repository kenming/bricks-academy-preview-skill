#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parent.parent
MANIFEST = SKILL_DIR / "index" / "preview_corpus_manifest.csv"


def find_row(key: str) -> dict[str, str] | None:
    with MANIFEST.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    for row in rows:
        if key in {row["doc_id"], row["local_path"]}:
            return row
    return None


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: show_doc.py <doc_id|local_path>", file=sys.stderr)
        raise SystemExit(2)

    key = sys.argv[1]
    row = find_row(key)
    if not row:
        print(f"not found: {key}", file=sys.stderr)
        raise SystemExit(1)

    path = SKILL_DIR / row["local_path"]
    print(f"# {row['title']}")
    print(f"doc_id: {row['doc_id']}")
    print(f"doc_kind: {row['doc_kind']}")
    print(f"source_url: {row['source_url']}")
    print(f"local_path: {row['local_path']}")
    print()
    print(path.read_text(encoding='utf-8', errors='ignore'))


if __name__ == "__main__":
    main()
