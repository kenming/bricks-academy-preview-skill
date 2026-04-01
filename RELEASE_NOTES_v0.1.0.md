# v0.1.0

Initial public release of the `bricks-academy-preview` Agent Skill.

## Highlights

- Added a local-first Bricks Academy preview corpus packaged as an Agent Skill
- Included `691` synced documentation pages from `academy-preview.bricksbuilder.io`
- Downloaded and localized `569` referenced images
- Preserved external embeds as links where local download is not appropriate
- Added corpus lookup scripts for search and document display
- Added sync scripts for refreshing the preview corpus as upstream docs evolve
- Added English and Traditional Chinese repository documentation
- Added explicit and implicit invocation examples with screenshots

## Skill Capabilities

- Search Bricks Builder preview docs from a local corpus
- Resolve hooks, elements, guides, schema docs, controls, and integrations
- Prefer local documentation before falling back to live browsing
- Support both explicit invocation with `$bricks-academy-preview`
- Support implicit invocation for clearly Bricks-specific queries

## Notes

- This release tracks the Bricks Academy preview site, not a final stable documentation release
- Upstream structure and content may continue to change
- Future releases may rename the repository or skill once the official docs move beyond preview
