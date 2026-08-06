# Changelog

## Unreleased

## v1.0.0 - 2026-08-06

### Added

- Added a concise development-guidance layer for Bricks data models, element
  workflows, custom elements, responsive/global design data, Dynamic Data,
  hooks, Query Loop, Forms, validation, and mutation safety.
- Added version-aware source and verification policies that keep licensed
  Bricks source and private installation paths outside the public skill.

### Breaking

- Renamed the installable skill from `bricks-academy` to `bricks-builder` and
  moved it from `skills/bricks-academy/` to `skills/bricks-builder/`.

### Changed

- Renamed the GitHub repository from `bricks-academy-skill` to
  `bricks-builder-skill` and updated installation URLs.
- Established `bricks-builder-skill` as the single maintained public Skill
  repository after retiring the separate legacy fork.
- Reworked the README visuals around the current `bricks-builder` invocation
  and three-layer evidence workflow, and removed outdated duplicate screenshots.
- Expanded the skill from documentation lookup to Bricks-specific research,
  implementation, and audit workflows while retaining the synchronized Academy
  corpus as its official documentation layer.
- Refreshed the 764-page Academy snapshot to the 2026-08-04 metadata baseline
  and incorporated the expanded `bricks/helpers/get_posts_args` example; the
  corpus remains at 764 documents, 614 local images, and 51 external embeds.

- Renamed the GitHub repository from `bricks-academy-preview-skill` to
  `bricks-academy-skill` and updated the installation examples.
- Migrated the Agent Skill from the retired Bricks Academy preview domain to
  the official `academy.bricksbuilder.io` documentation.
- Renamed the skill to `bricks-academy` and aligned its corpus, index, sync
  scripts, references, screenshots, and installation paths.
- Refreshed the Academy snapshot to `764` documents, `614` local images, and
  `51` external embeds.

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
