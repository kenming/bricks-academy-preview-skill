# Custom Elements

Place custom elements in an active child theme or plugin. Never modify the Bricks parent theme.

## Workflow

1. Read the Academy custom-elements guide and current base-element API.
2. Resolve the active child/plugin path at runtime; do not hard-code a machine path.
3. Define one clearly prefixed element class extending `\Bricks\Element`.
4. Register its file after Bricks has loaded; verify the current registration API and hook timing.
5. Define stable control keys and use only supported control properties.
6. Render root attributes so Bricks IDs, classes, styles, conditions, and interactions remain connected.
7. Escape output for its final HTML context.
8. Test save/reload, builder canvas, frontend, responsive settings, and dynamic data when supported.

## Minimal responsibilities

A custom element normally supplies a stable element name, label, category/icon metadata, controls, and a render method. Nestable elements, scripts, actions, and custom control groups require additional current-version verification.

## Security

- Escape text, attributes, and URLs at output.
- Sanitize stored values according to their destination.
- Whitelist user-selectable HTML tags and attributes.
- Do not print raw dynamic data or user content merely because the builder previously saved it.
- Enqueue scripts/styles through WordPress and avoid project-specific asset assumptions in reusable guidance.

Do not publish copied Bricks parent classes or substantial licensed source examples. Document the extension contract and small original examples instead.
