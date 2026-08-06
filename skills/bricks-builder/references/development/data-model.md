# Bricks Data Model

Use the Academy element and content-area schemas as the canonical public shape. Verify saved values against the active version before mutation.

## Element tree

Bricks page areas contain an ordered flat array of element objects. Tree relationships are expressed with IDs:

```json
{
  "id": "abc123",
  "name": "container",
  "parent": 0,
  "children": ["def456"],
  "settings": {}
}
```

- `id` is unique within the content area.
- Root elements use numeric `0` as `parent` in the public schema.
- Child `parent` values reference a parent ID.
- A parent's `children` array preserves child order.
- `settings` combines element-specific controls, inherited CSS controls, and shared meta-settings.
- Optional top-level data can include `label`, `selectors`, and `themeStyles`.

## Shared meta-settings

Common settings include:

- `_cssGlobalClasses`: global class IDs.
- `_conditions`: element display-condition groups.
- `_interactions`: interaction records.
- `_hideElementBuilder` and `_hideElementFrontend`.
- `_attributes`: custom attribute records with stable row IDs.

Load the matching Academy schema before constructing any of these shapes.

## Storage

Bricks commonly stores complete content areas in post meta and global design data in WordPress options. Names and migration suffixes are version-sensitive. Prefer Bricks UI/export/public APIs; inspect actual keys and values read-only before any direct write.

## Integrity checks

- Every child ID exists exactly once.
- Every non-root element's parent exists and lists it as a child.
- No element is its own ancestor.
- Sibling order matches the parent's `children` array.
- Element names are registered in the active installation.
- Settings belong to the selected element/version.
