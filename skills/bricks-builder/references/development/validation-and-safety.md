# Validation and Safety

Use checks proportional to the mutation risk.

## Before changes

- Confirm the target repository, WordPress site, post/template, and active Bricks version.
- Resolve parent and child theme paths; keep the parent read-only.
- Capture current content/options or create a recoverable backup before direct data changes.
- Inspect the smallest representative UI-created object.
- Separate task changes from unrelated working-tree or site changes.

## Static checks

- Validate PHP syntax and relevant WordPress coding/security rules.
- Validate JSON/PHP array shapes and unique IDs.
- Confirm every relative path and referenced script/reference exists.
- Confirm hook callback signatures match the installed version.
- Confirm no secret, absolute private path, or licensed source was added.

## Bricks checks

- Open the affected content in the Builder without control-panel errors.
- Save and reload it to detect normalization or dropped settings.
- Verify builder canvas and frontend output.
- Test configured breakpoints and pseudo states.
- Exercise conditions, interactions, queries, forms, and Dynamic Data branches involved.
- Regenerate CSS through the supported Bricks UI when required; do not guess an internal method.

## Direct persistence

Prefer the Builder UI, export/import, or documented public APIs. If direct post-meta or option mutation is unavoidable:

1. Read and back up the complete current value.
2. Modify the smallest subtree.
3. Validate all references before writing.
4. Write through WordPress APIs in a non-production or explicitly authorized environment first.
5. Re-read and compare the persisted value.
6. Keep a tested rollback path.
