---
name: bricks-academy
description: Use only for Bricks Builder-specific questions about elements, hooks, schema, controls, templates, styling, dynamic content, setup, or integrations when the local Bricks Academy corpus should be checked first. Do not use for generic WordPress, PHP, CSS, JavaScript, or unrelated web development questions unless they are clearly about Bricks.
license: See repository license terms for this skill and bundled corpus.
compatibility: Requires Python 3, curl, network access for sync, and a repository checkout with this skill under skills/bricks-academy.
---

# Bricks Academy

Use this skill only for clearly Bricks-specific questions that require documentation lookup from the local Bricks Academy corpus.

Do not use this skill for:

- generic WordPress questions with no Bricks context
- generic PHP, CSS, JavaScript, or frontend questions
- unrelated plugin or framework questions

## Corpus

- Local corpus root: `corpus/bricks-academy/`
- Manifest: `index/academy_corpus_manifest.csv`
- Preferred doc kinds:
  - `hook` for actions and filters
  - `element` for builder elements
  - `schema` for technical data model pages
  - `control` for control APIs
  - `guide` for builder workflows and concepts
  - `integration` for third-party integrations

## Workflow

1. Start with `scripts/search_corpus.py "<query>"` for every triggered Bricks docs lookup.
2. Open 1 to 3 high-signal candidates with `scripts/show_doc.py <path-or-doc-id>`.
3. Prefer `hook`, `element`, or `schema` matches when the user asks for exact APIs or element behavior.
4. Prefer `guide` matches for conceptual questions such as query loop, theme styles, conditions, templates, responsive editing, or setup.
5. Do not start with generic `rg` or broad file scans across the corpus unless `search_corpus.py` is insufficient.
6. Only browse the live Bricks site if the local corpus does not contain the needed page or if the answer depends on a very recent docs change.

## Search Guidance

- Normalize the user’s wording to Bricks terms before searching.
- Search by official nouns when possible:
  - `query loop`
  - `dynamic data`
  - `global css classes`
  - `theme styles`
  - `element conditions`
  - `template library`
  - `bricks/query/before_loop`
  - `filter: bricks/...`
- For hook questions, search both the hook name and the exact slash form.
- For element questions, search the element name first, then refine by category if needed.

## References

- Query workflow and lookup rules: `references/query-workflow.md`
- Corpus structure and doc kinds: `references/corpus-layout.md`
- Sync and maintenance workflow: `references/sync-maintenance.md`

## Scripts

- `scripts/search_corpus.py "<query>" [--kind hook|element|schema|control|guide|integration] [--section builder|developer|getting-started|integrations] [--subsection PREFIX] [--limit N]`
- `scripts/show_doc.py <doc_id|local_path>`
- `scripts/run_academy_sync.sh`
