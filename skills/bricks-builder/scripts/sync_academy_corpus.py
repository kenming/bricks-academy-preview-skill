#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import mimetypes
import re
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urljoin, urlparse


SKILL_DIR = Path(__file__).resolve().parent.parent
INPUT_MANIFEST = SKILL_DIR / "index" / "academy_manifest.csv"
OUT_DIR = SKILL_DIR / "corpus" / "bricks-academy"
REPORT_DIR = SKILL_DIR / "index"
BASE_URL = "https://academy.bricksbuilder.io"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123 Safari/537.36"
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\((/assets/[^)]+)\)")
EXTERNAL_EMBED_RE = re.compile(
    r"(https?://(?:www\.)?(?:youtube\.com|youtu\.be|youtube-nocookie\.com|vimeo\.com|loom\.com)[^\s)]+)"
)


@dataclass
class SyncResult:
    doc_id: str
    title: str
    source_url: str
    local_path: str
    section: str
    subsection: str
    doc_kind: str
    asset_count: int
    external_embed_count: int
    status: str
    note: str


def fetch_text(url: str) -> str:
    result = subprocess.run(
        ["curl", "-fsSL", "-A", USER_AGENT, url],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def fetch_binary(url: str) -> bytes:
    result = subprocess.run(
        ["curl", "-fsSL", "-A", USER_AGENT, url],
        check=True,
        capture_output=True,
    )
    return result.stdout


def load_manifest() -> list[dict[str, str]]:
    with INPUT_MANIFEST.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    return [row for row in rows if row.get("source_url") and row.get("title", "").strip()]


def local_markdown_path(source_url: str) -> Path:
    rel = urlparse(source_url).path.strip("/")
    return OUT_DIR / f"{rel}.md"


def classify_doc(row: dict[str, str]) -> tuple[str, str, str]:
    rel = urlparse(row["source_url"]).path.strip("/")
    parts = rel.split("/")
    section = parts[0] if len(parts) >= 1 else ""
    subsection = "/".join(parts[:2]) if len(parts) >= 2 else section

    if rel.startswith("developer/hooks/"):
        doc_kind = "hook"
    elif rel.startswith("developer/schema/"):
        doc_kind = "schema"
    elif rel.startswith("builder/elements/"):
        doc_kind = "element"
    elif rel.startswith("developer/controls/"):
        doc_kind = "control"
    elif rel.startswith("integrations/"):
        doc_kind = "integration"
    else:
        doc_kind = "guide"

    return section, subsection, doc_kind


def safe_asset_name(asset_url: str) -> str:
    parsed = urlparse(asset_url)
    base = Path(parsed.path).name
    stem = Path(base).stem
    suffix = Path(base).suffix
    if not suffix:
        suffix = mimetypes.guess_extension("image/jpeg") or ".bin"
    digest = hashlib.sha1(asset_url.encode("utf-8")).hexdigest()[:10]
    return f"{stem}-{digest}{suffix}"


def rewrite_and_fetch_assets(markdown: str, md_path: Path) -> tuple[str, int]:
    assets = IMAGE_RE.findall(markdown)
    if not assets:
        return markdown, 0

    img_dir = md_path.parent / "imgs"
    img_dir.mkdir(parents=True, exist_ok=True)
    rewritten = markdown
    count = 0

    for alt_text, asset_path in assets:
        asset_url = urljoin(BASE_URL, asset_path)
        filename = safe_asset_name(asset_url)
        local_asset_path = img_dir / filename
        if not local_asset_path.exists():
            local_asset_path.write_bytes(fetch_binary(asset_url))
        relative_asset = Path("imgs") / filename
        old_ref = f"![{alt_text}]({asset_path})"
        new_ref = f"![{alt_text}]({relative_asset.as_posix()})"
        rewritten = rewritten.replace(old_ref, new_ref)
        count += 1

    return rewritten, count


def process_row(row: dict[str, str]) -> SyncResult:
    md_source_url = row["source_url"].rstrip("/") + ".md"
    md_path = local_markdown_path(row["source_url"])
    md_path.parent.mkdir(parents=True, exist_ok=True)
    section, subsection, doc_kind = classify_doc(row)

    try:
        markdown = fetch_text(md_source_url)
        external_embeds = sorted(set(EXTERNAL_EMBED_RE.findall(markdown)))
        rewritten, asset_count = rewrite_and_fetch_assets(markdown, md_path)
        md_path.write_text(rewritten.rstrip() + "\n", encoding="utf-8")
        note = ""
        if external_embeds:
            note = "external embeds preserved as links"
        return SyncResult(
            doc_id=row["doc_id"],
            title=row["title"],
            source_url=row["source_url"],
            local_path=md_path.relative_to(SKILL_DIR).as_posix(),
            section=section,
            subsection=subsection,
            doc_kind=doc_kind,
            asset_count=asset_count,
            external_embed_count=len(external_embeds),
            status="ok",
            note=note,
        )
    except Exception as exc:
        return SyncResult(
            doc_id=row["doc_id"],
            title=row["title"],
            source_url=row["source_url"],
            local_path=md_path.relative_to(SKILL_DIR).as_posix(),
            section=section,
            subsection=subsection,
            doc_kind=doc_kind,
            asset_count=0,
            external_embed_count=0,
            status="error",
            note=str(exc),
        )


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=list(rows[0].keys()),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    rows = load_manifest()
    results: list[SyncResult] = []

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(process_row, row) for row in rows]
        for future in as_completed(futures):
            results.append(future.result())

    results.sort(key=lambda item: item.source_url)
    report_rows = [
        {
            "doc_id": item.doc_id,
            "title": item.title,
            "source_url": item.source_url,
            "local_path": item.local_path,
            "section": item.section,
            "subsection": item.subsection,
            "doc_kind": item.doc_kind,
            "asset_count": item.asset_count,
            "external_embed_count": item.external_embed_count,
            "status": item.status,
            "note": item.note,
        }
        for item in results
    ]
    write_csv(REPORT_DIR / "academy_corpus_manifest.csv", report_rows)
    (REPORT_DIR / "academy_corpus_manifest.json").write_text(
        json.dumps(report_rows, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    ok_count = sum(1 for item in results if item.status == "ok")
    error_count = len(results) - ok_count
    asset_total = sum(item.asset_count for item in results)
    embed_total = sum(item.external_embed_count for item in results)
    print(
        f"synced docs={len(results)} ok={ok_count} error={error_count} "
        f"assets={asset_total} external_embeds={embed_total}"
    )
    print(f"corpus written to {OUT_DIR}")
    print(f"manifest written to {REPORT_DIR / 'academy_corpus_manifest.csv'}")


if __name__ == "__main__":
    main()
