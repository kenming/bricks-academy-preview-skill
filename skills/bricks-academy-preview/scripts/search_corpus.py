#!/usr/bin/env python3
from __future__ import annotations

import csv
import argparse
import re
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parent.parent
MANIFEST = SKILL_DIR / "index" / "preview_corpus_manifest.csv"

SYNONYMS = {
    "loop": ["query loop"],
    "query loops": ["query loop"],
    "dynamic tags": ["dynamic data"],
    "global classes": ["global css classes"],
    "global class": ["global css classes"],
    "global styles": ["theme styles"],
    "conditions": ["element conditions"],
    "template conditions": ["element conditions"],
    "hooks": ["hook"],
    "filters": ["hook"],
    "actions": ["hook"],
    "woocommerce": ["integration", "woocommerce"],
}


def normalize(text: str) -> str:
    text = text.lower().strip()
    text = text.replace("&", "and")
    text = text.replace("_", " ")
    text = text.replace("-", " ")
    text = re.sub(r"/{2,}", "/", text)
    text = re.sub(r"[^a-z0-9/ ]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def expand_terms(query: str) -> list[str]:
    normalized = normalize(query)
    terms = {term for term in normalized.split() if term}
    phrases = {normalized}

    for source, mapped in SYNONYMS.items():
        if source in normalized:
            phrases.update(mapped)
            for item in mapped:
                terms.update(item.split())

    if "/" in normalized:
        phrases.add(normalized)

    combined = list(phrases) + sorted(terms)
    seen = []
    for item in combined:
        item = item.strip()
        if item and item not in seen:
            seen.append(item)
    return seen


def score(row: dict[str, str], terms: list[str], raw_query: str) -> int:
    text_fields = {
        "title": normalize(row["title"]),
        "section": normalize(row["section"]),
        "subsection": normalize(row["subsection"]),
        "doc_kind": normalize(row["doc_kind"]),
        "url": normalize(row["source_url"]),
        "path": normalize(row["local_path"]),
    }
    score = 0
    for term in terms:
        if term in text_fields["title"]:
            score += 12
        if term in text_fields["subsection"]:
            score += 8
        if term in text_fields["section"]:
            score += 4
        if term in text_fields["url"] or term in text_fields["path"]:
            score += 6
        if term == text_fields["doc_kind"]:
            score += 8

    hook_like = "/" in raw_query or "filter" in raw_query or "action" in raw_query
    if hook_like and row["doc_kind"] == "hook":
        score += 10
    if "schema" in terms and row["doc_kind"] == "schema":
        score += 10
    if "element" in terms and row["doc_kind"] == "element":
        score += 8
    if any(term in raw_query for term in ["how", "why", "guide", "tutorial"]):
        if row["doc_kind"] == "guide":
            score += 10
    if any(term in raw_query for term in ["element", "button", "container", "section", "video", "form"]):
        if row["doc_kind"] == "element":
            score += 10
        if row["doc_kind"] == "schema":
            score -= 2
    if any(term in raw_query for term in ["hook", "filter", "action", "/"]):
        if row["doc_kind"] == "hook":
            score += 12
        if row["doc_kind"] == "guide":
            score -= 2
    return score


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="search query")
    parser.add_argument("--kind", dest="doc_kind", help="filter by doc_kind")
    parser.add_argument("--section", dest="section", help="filter by top-level section")
    parser.add_argument("--subsection", dest="subsection", help="filter by subsection prefix")
    parser.add_argument("--limit", dest="limit", type=int, default=15, help="max results")
    args = parser.parse_args()

    query = args.query
    terms = expand_terms(query)

    with MANIFEST.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))

    ranked = []
    for row in rows:
        if args.doc_kind and row["doc_kind"] != args.doc_kind:
            continue
        if args.section and row["section"] != args.section:
            continue
        if args.subsection and not row["subsection"].startswith(args.subsection):
            continue
        row_score = score(row, terms, query.lower())
        if row_score > 0:
            ranked.append((row_score, row))

    ranked.sort(key=lambda item: (-item[0], item[1]["source_url"]))

    for idx, (row_score, row) in enumerate(ranked[: args.limit], start=1):
        print(
            f"{idx:02d}. [{row_score}] {row['title']} | {row['doc_kind']} | "
            f"{row['subsection']} | {row['local_path']} | {row['doc_id']}"
        )


if __name__ == "__main__":
    main()
