# Sync Maintenance

Use this workflow when the Bricks Academy preview site changes and the local corpus needs to be refreshed.

## Standard Sync

1. Run:
   `scripts/run_preview_sync.sh`
2. Confirm the script reports:
   - generated `index/preview_manifest.csv`
   - generated `index/preview_corpus_manifest.csv`
   - zero sync errors
3. Spot-check a few known pages with:
   - `scripts/search_corpus.py "query loop"`
   - `scripts/search_corpus.py "bricks/query/before_loop"`
   - `scripts/show_doc.py <doc_id>`

## What Changes

- `index/preview_manifest.csv`
  - page inventory discovered from the site navigation
- `index/preview_corpus_manifest.csv`
  - synced local corpus metadata
- `corpus/bricks-academy-preview/`
  - markdown pages and downloaded local images

## If Sync Fails

Check in this order:

1. Preview navigation changed:
   - inspect `scripts/build_preview_manifest.py`
2. `.md` endpoint behavior changed:
   - inspect `scripts/sync_preview_corpus.py`
3. Asset URLs changed:
   - inspect markdown image paths and asset rewrite logic

## Maintenance Notes

- This skill mirrors the preview docs, not a final stable docs release.
- Treat structural changes in `builder/`, `developer/`, or `integrations/` as expected.
- Re-run sync before major skill updates or when answers appear stale.
