# Changelog

## Unreleased

### Changed

- Renamed the GitHub repository from `bricks-academy-preview-skill` to
  `bricks-academy-skill` and updated the installation examples.

## v0.1.1

Maintenance update for checking whether the official Bricks Academy preview
knowledge base has changed without downloading the full corpus.

### Added

- Added `skills/bricks-academy-preview/scripts/check_preview_updates.py`
  for lightweight upstream update checks using official `.md` endpoint ETags.
- Added `skills/bricks-academy-preview/index/preview_remote_etags.json`
  as the cached ETag baseline for the current preview corpus snapshot.
- Documented the lightweight update-check workflow in
  `skills/bricks-academy-preview/references/sync-maintenance.md`.

### Changed

- Updated README installation guidance to distinguish Codex/Copilot,
  Claude Code, and other agent skill directories.

## v0.1.0

Initial public release of the `bricks-academy-preview` Agent Skill.

### Highlights

- Added a local-first Bricks Academy preview corpus packaged as an Agent Skill.
- Included `691` synced documentation pages from `academy-preview.bricksbuilder.io`.
- Downloaded and localized `569` referenced images.
- Preserved external embeds as links where local download is not appropriate.
- Added corpus lookup scripts for search and document display.
- Added sync scripts for refreshing the preview corpus as upstream docs evolve.
- Added English and Traditional Chinese repository documentation.
- Added explicit and implicit invocation examples with screenshots.

### Skill Capabilities

- Search Bricks Builder preview docs from a local corpus.
- Resolve hooks, elements, guides, schema docs, controls, and integrations.
- Prefer local documentation before falling back to live browsing.
- Support explicit invocation with `$bricks-academy-preview`.
- Support implicit invocation for clearly Bricks-specific queries.

### Notes

- This release tracks the Bricks Academy preview site, not a final stable
  documentation release.
- Upstream structure and content may continue to change.
- Future releases may rename the repository or skill once the official docs move
  beyond preview.
