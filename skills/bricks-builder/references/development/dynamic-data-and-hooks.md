# Dynamic Data and Hooks

## Dynamic Data

Available tags depend on the active providers and integrations. Use the Builder picker and official Dynamic Data docs to discover public tags; inspect the active provider only when exact parsing or return shape matters.

When adding a custom tag:

1. Register it through the documented tags-list extension point.
2. Preserve the renderer's post and output-context arguments.
3. Return untouched input for tags the callback does not own.
4. Escape or sanitize for the final context.
5. Test plain text, embedded content, builder preview, and frontend output.

Do not expose protected post, user, option, or integration data through a tag without an explicit authorization decision.

## Hooks

For every Bricks hook:

1. Search the corpus by exact slash-form name.
2. Open the official hook page when available.
3. Verify argument count, types, return contract, and timing against the active version if implementation depends on them.
4. Set the callback's accepted-argument count explicitly.
5. Scope mutations by element ID/name, post, query, or context as appropriate.

Do not treat internal actions/filters found in source as permanent public APIs. If no official contract exists, label the integration version-sensitive and provide a safe fallback.

Avoid recursion when a callback invokes Dynamic Data rendering or another filtered Bricks pipeline.
