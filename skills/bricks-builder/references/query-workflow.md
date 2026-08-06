# Query Workflow

Use the local corpus first, and start with the search script rather than generic file scans.

1. Search the manifest with `scripts/search_corpus.py`.
2. Read only the top matches, usually 1 to 3 files.
3. Prefer exact `doc_kind` matches:
   - `hook` for action or filter questions
   - `element` for builder element questions
   - `schema` for technical structure questions
   - `guide` for task or feature explanations
4. If search returns mixed results, narrow by:
   - exact hook name
   - official element name
   - section such as `builder/styling` or `developer/hooks`
5. Avoid starting with `rg` over the corpus unless the search script cannot find the right page.
6. If the local corpus looks stale or missing, browse the official site and state that you are verifying against live docs.

Useful queries:

- `query loop`
- `dynamic data`
- `theme styles`
- `global css classes`
- `element conditions`
- `template library`
- `bricks/query/before_loop`
- `filter bricks builder elements`
