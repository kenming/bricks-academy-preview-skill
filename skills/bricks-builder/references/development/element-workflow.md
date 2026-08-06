# Element Development Workflow

Use this workflow for generated sections, page JSON, audits, and surgical element changes.

1. Identify the target content area and current Bricks version.
2. Search the Academy corpus for the element and related schema.
3. Inspect a minimal builder-created example when exact saved shape matters.
4. Select registered element names from the active installation.
5. Generate unique IDs and construct reciprocal parent/children relationships.
6. Add only verified control keys and value shapes.
7. Preserve unrelated element data, labels, selectors, component connections, and global-class references.
8. Prefer a supported import/UI path. Back up and perform a dry read before direct persistence.
9. Reopen the content in the builder and test frontend rendering.

## Control lookup

For an exact setting:

1. Open the element's Academy schema.
2. Check whether the setting is element-specific, inherited, or shared metadata.
3. If still ambiguous, inspect the active element class/control registration.
4. Reproduce a single setting through the UI and compare the saved result.

Do not infer keys from control labels or another element with similar behavior.

## Responsive and state settings

Supported variants remain in the same flat `settings` object:

```json
{
  "_padding": { "top": "48px" },
  "_padding:tablet_portrait": { "top": "32px" },
  "_typography:hover": { "color": { "raw": "#ffffff" } }
}
```

Use the literal active breakpoint key and only apply variants to controls that generate responsive/state CSS.
