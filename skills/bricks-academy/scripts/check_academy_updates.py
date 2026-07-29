#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parent.parent
MANIFEST_PATH = SKILL_DIR / "index" / "academy_manifest.csv"
CACHE_PATH = SKILL_DIR / "index" / "academy_remote_etags.json"
BASE_URL = "https://academy.bricksbuilder.io"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123 Safari/537.36"


@dataclass
class RemoteDoc:
    doc_id: str
    title: str
    source_url: str
    md_url: str
    etag: str
    content_length: str
    content_type: str
    status: str
    note: str


def load_manifest() -> list[dict[str, str]]:
    with MANIFEST_PATH.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def load_cache() -> dict[str, object]:
    if not CACHE_PATH.exists():
        return {"docs": {}}
    return json.loads(CACHE_PATH.read_text(encoding="utf-8"))


def parse_headers(raw_headers: str) -> dict[str, str]:
    headers: dict[str, str] = {}
    for line in raw_headers.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        headers[key.strip().lower()] = value.strip()
    return headers


def fetch_text(url: str) -> str:
    result = subprocess.run(
        ["curl", "-fsSL", "-A", USER_AGENT, url],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def list_homepage_paths() -> set[str]:
    homepage = fetch_text(BASE_URL + "/")
    paths = set(re.findall(r'href="(/[^"]+/)"', homepage))
    return {
        path
        for path in paths
        if path != "/" and not path.startswith("/_astro/")
    }


def fetch_head(row: dict[str, str]) -> RemoteDoc:
    source_url = row["source_url"]
    md_url = source_url.rstrip("/") + ".md"
    try:
        result = subprocess.run(
            ["curl", "-fsSLI", "-A", USER_AGENT, md_url],
            check=True,
            capture_output=True,
            text=True,
        )
        headers = parse_headers(result.stdout)
        return RemoteDoc(
            doc_id=row["doc_id"],
            title=row["title"],
            source_url=source_url,
            md_url=md_url,
            etag=headers.get("etag", ""),
            content_length=headers.get("content-length", ""),
            content_type=headers.get("content-type", ""),
            status="ok",
            note="",
        )
    except Exception as exc:
        return RemoteDoc(
            doc_id=row.get("doc_id", ""),
            title=row.get("title", ""),
            source_url=source_url,
            md_url=md_url,
            etag="",
            content_length="",
            content_type="",
            status="error",
            note=str(exc),
        )


def markdown_exists_for_path(path: str) -> bool:
    md_url = BASE_URL + path.rstrip("/") + ".md"
    result = subprocess.run(
        ["curl", "-fsSLI", "-A", USER_AGENT, md_url],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def collect_remote(rows: list[dict[str, str]], workers: int) -> list[RemoteDoc]:
    docs: list[RemoteDoc] = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(fetch_head, row) for row in rows if row.get("source_url")]
        for future in as_completed(futures):
            docs.append(future.result())
    docs.sort(key=lambda item: item.source_url)
    return docs


def comparable_value(doc: RemoteDoc) -> str:
    return doc.etag or doc.content_length


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Lightweight Bricks Academy update check using remote .md ETags."
    )
    parser.add_argument(
        "--update-cache",
        action="store_true",
        help="write the current remote ETags as the new comparison baseline",
    )
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    parser.add_argument(
        "--skip-navigation",
        action="store_true",
        help="skip the homepage link inventory check",
    )
    args = parser.parse_args()

    rows = load_manifest()
    cache = load_cache()
    cached_docs = cache.get("docs", {})
    if not isinstance(cached_docs, dict):
        cached_docs = {}

    remote_docs = collect_remote(rows, args.workers)
    remote_by_url = {doc.source_url: doc for doc in remote_docs}
    manifest_paths = {
        "/" + row["source_url"].removeprefix(BASE_URL).strip("/") + "/"
        for row in rows
        if row.get("source_url", "").startswith(BASE_URL)
    }
    homepage_paths: set[str] = set()
    navigation_error = ""
    if not args.skip_navigation:
        try:
            homepage_paths = list_homepage_paths()
        except Exception as exc:
            navigation_error = str(exc)

    errors = [doc for doc in remote_docs if doc.status != "ok"]
    changed: list[RemoteDoc] = []
    unknown: list[RemoteDoc] = []

    for doc in remote_docs:
        if doc.status != "ok":
            continue
        cached = cached_docs.get(doc.source_url)
        current = comparable_value(doc)
        if not isinstance(cached, dict) or not cached.get("etag"):
            unknown.append(doc)
            continue
        if current and current != cached.get("etag"):
            changed.append(doc)

    removed = sorted(set(cached_docs) - set(remote_by_url))
    new_remote_path_candidates = sorted(homepage_paths - manifest_paths)
    new_remote_paths = [
        path for path in new_remote_path_candidates if markdown_exists_for_path(path)
    ]
    missing_remote_paths = sorted(manifest_paths - homepage_paths) if homepage_paths else []

    report = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "manifest_docs": len(rows),
        "checked_docs": len(remote_docs),
        "changed_docs": [asdict(doc) for doc in changed],
        "unknown_docs": [asdict(doc) for doc in unknown],
        "removed_docs": removed,
        "new_remote_paths": new_remote_paths,
        "missing_remote_paths": missing_remote_paths,
        "navigation_error": navigation_error,
        "errors": [asdict(doc) for doc in errors],
        "cache_path": str(CACHE_PATH),
    }

    if args.update_cache:
        payload = {
            "generated_at": report["checked_at"],
            "docs": {
                doc.source_url: {
                    "doc_id": doc.doc_id,
                    "title": doc.title,
                    "md_url": doc.md_url,
                    "etag": comparable_value(doc),
                    "raw_etag": doc.etag,
                    "content_length": doc.content_length,
                    "content_type": doc.content_type,
                }
                for doc in remote_docs
                if doc.status == "ok"
            },
        }
        CACHE_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(
            f"checked docs={len(remote_docs)} changed={len(changed)} "
            f"unknown={len(unknown)} removed={len(removed)} "
            f"new_paths={len(new_remote_paths)} missing_paths={len(missing_remote_paths)} "
            f"errors={len(errors)}"
        )
        if new_remote_paths:
            print("\nNew paths on the official Academy site:")
            for path in new_remote_paths[:30]:
                print(f"- {BASE_URL}{path}")
        if missing_remote_paths:
            print("\nManifest paths not found on the official Academy homepage:")
            for path in missing_remote_paths[:30]:
                print(f"- {BASE_URL}{path}")
        if changed:
            print("\nChanged:")
            for doc in changed[:30]:
                print(f"- {doc.title} ({doc.source_url})")
            if len(changed) > 30:
                print(f"- ... {len(changed) - 30} more")
        if unknown:
            print("\nNo cached baseline for some docs. Run with --update-cache after a trusted sync.")
        if removed:
            print("\nRemoved from current manifest:")
            for url in removed[:30]:
                print(f"- {url}")
        if errors:
            print("\nErrors:")
            for doc in errors[:30]:
                print(f"- {doc.source_url}: {doc.note}")
        if navigation_error:
            print(f"\nNavigation check error: {navigation_error}")
        if args.update_cache:
            print(f"\nupdated cache: {CACHE_PATH}")

    if errors or changed or removed or new_remote_paths or missing_remote_paths or navigation_error:
        return 1
    if unknown:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
