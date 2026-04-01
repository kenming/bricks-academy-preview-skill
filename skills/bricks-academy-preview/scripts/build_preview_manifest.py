#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from html import unescape
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = SKILL_DIR / "index"
BASE_URL = "https://academy-preview.bricksbuilder.io"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123 Safari/537.36"


def fetch(url: str) -> str:
    result = subprocess.run(
        ["curl", "-fsSL", "-A", USER_AGENT, url],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def normalize_title(value: str) -> str:
    value = value.strip().lower()
    value = value.replace("&", "and")
    value = re.sub(r"/{2,}", "/", value)
    value = re.sub(r"^element:\s*", "", value)
    value = re.sub(r"\belement$", "", value)
    value = re.sub(r"[^a-z0-9/]+", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def normalize_slug(value: str) -> str:
    value = value.strip("/").lower()
    leaf = value.split("/")[-1] if value else ""
    leaf = re.sub(r"^(action|filter|function)-", "", leaf)
    leaf = re.sub(r"-element$", "", leaf)
    leaf = re.sub(r"[^a-z0-9/-]+", "-", leaf)
    leaf = re.sub(r"-{2,}", "-", leaf).strip("-")
    return leaf


def list_paths(homepage_html: str) -> list[str]:
    paths = sorted(set(re.findall(r'href="(/[^"]+/)"', homepage_html)))
    filtered = []
    for path in paths:
        if path.startswith("/_astro/"):
            continue
        if path == "/":
            continue
        filtered.append(path)
    return filtered


def extract_title(html: str) -> str:
    match = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
    if match:
        return strip_tags(match.group(1))
    match = re.search(r"<title>(.*?)</title>", html, re.S | re.I)
    if match:
        title = strip_tags(match.group(1))
        return title.replace("| Bricks Academy", "").strip()
    return ""


def build_row(path: str) -> dict[str, str]:
    html = fetch(f"{BASE_URL}{path}")
    title = extract_title(html)
    segments = path.strip("/").split("/")
    row = {
        "doc_id": f"new:{path.strip('/')}",
        "origin": "preview",
        "title": title,
        "normalized_title": normalize_title(title),
        "source_url": f"{BASE_URL}{path}",
        "source_slug": segments[-1] if segments else "",
        "fallback_slug": segments[-1] if segments else "",
        "canonical_slug": normalize_slug(path),
        "section_or_category": "/".join(segments[:2]) if len(segments) >= 2 else segments[0],
        "local_path": "",
    }
    return row


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    homepage = fetch(BASE_URL + "/")
    paths = list_paths(homepage)
    rows: list[dict[str, str]] = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(build_row, path): path for path in paths}
        for future in as_completed(futures):
            path = futures[future]
            try:
                row = future.result()
                if row["title"].strip():
                    rows.append(row)
            except Exception:
                continue
    rows.sort(key=lambda row: row["source_url"])
    write_csv(OUT_DIR / "preview_manifest.csv", rows)
    (OUT_DIR / "preview_manifest.json").write_text(
        json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"wrote {len(rows)} preview docs to {OUT_DIR / 'preview_manifest.csv'}")


if __name__ == "__main__":
    main()
