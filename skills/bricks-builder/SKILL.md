---
name: bricks-builder
description: Research, implement, modify, and audit behavior inside Bricks Builder sites using the bundled Bricks Academy corpus, stable development workflows, and version-aware verification against an authorized active Bricks installation. Use when the requested outcome concerns Bricks elements, controls, schema, hooks, templates, styling, responsive settings, dynamic data, queries, forms, interactions, custom elements, or page JSON. Do not use merely because Bricks Builder is mentioned, for generic WordPress, PHP, CSS, or JavaScript work, or for maintaining, naming, versioning, documenting, or releasing this Skill repository.
---

# Bricks Builder

Treat the bundled Academy corpus as the public documentation layer, the hand-written references as development guidance, and the user's authorized active installation as the final source for version-sensitive implementation facts.

Never edit the Bricks parent theme. Put custom code in an active child theme or plugin.

## Route the task

### Documentation lookup

For feature behavior, official setup, public hooks, schemas, and supported workflows:

1. Run `scripts/search_corpus.py "<query>"`.
2. Open 1 to 3 high-signal results with `scripts/show_doc.py <path-or-doc-id>`.
3. Prefer `hook`, `element`, `schema`, or `control` results for exact APIs; prefer `guide` results for concepts and UI workflows.
4. Browse the official Academy site only when the local corpus is missing, stale, or the user requests current online verification.

Read `references/query-workflow.md` for search details and `references/corpus-layout.md` for corpus organization.

### Development implementation

For building or modifying Bricks content or code:

1. Read only the task-relevant development reference below.
2. Search the Academy corpus for the related public contract.
3. Detect the active Bricks version before relying on internal keys, signatures, paths, or storage shapes.
4. Inspect the smallest relevant part of the authorized active theme or live WordPress state when available.
5. Implement outside the parent theme and validate in both the builder and frontend.

### Version-sensitive verification

Treat exact element names, control keys, hook arguments, JSON shapes, option/meta keys, internal classes, and version availability as version-sensitive.

- Prefer the active installation for claims about that installation.
- Cross-check the matching Academy schema or guide where possible.
- State the verified Bricks version when the answer or change depends on it.
- If no authorized installation is available, use public documentation and clearly identify unverified internal details.
- Never publish licensed source, credentials, private site data, or a developer's absolute local path.

Read `references/source-policy.md` and `references/version-verification.md` before making version-sensitive claims.

## Development references

- Bricks element tree and storage model: `references/development/data-model.md`
- Building or editing page/element JSON: `references/development/element-workflow.md`
- Registering and rendering custom elements: `references/development/custom-elements.md`
- Responsive settings, Theme Styles, globals, and components: `references/development/responsive-and-styles.md`
- Dynamic Data and hook implementation: `references/development/dynamic-data-and-hooks.md`
- Query Loop and Forms: `references/development/query-and-forms.md`
- Mutation safety and end-to-end validation: `references/development/validation-and-safety.md`

Do not load every development reference by default.

## Core invariants

- Do not invent control keys or stored shapes.
- Keep element IDs unique and preserve reciprocal `parent`/`children` relationships.
- Store responsive and pseudo-state variants as flat colon-suffixed setting keys when supported by the control.
- Reference global classes by their IDs, not display names.
- Prefer the Builder UI or supported public APIs over direct database mutation.
- Scope filters and queries so unrelated Bricks elements are not changed.

## Maintenance

Corpus and index files are generated synchronization products. Do not hand-edit them for ordinary development guidance. Read `references/sync-maintenance.md` only when checking or refreshing Academy content.

Available scripts:

- `scripts/search_corpus.py "<query>" [filters]`
- `scripts/show_doc.py <doc-id-or-path>`
- `scripts/check_academy_updates.py`
- `scripts/run_academy_sync.sh`
