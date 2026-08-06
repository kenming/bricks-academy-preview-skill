# Version Verification

Run this workflow before asserting exact controls, hooks, internal APIs, storage keys, or version availability.

1. Resolve the active parent theme with WordPress (`get_template_directory()`) or an authorized filesystem mapping.
2. Read the version from both `style.css` and the `BRICKS_VERSION` definition.
3. Continue only when both values exist and agree.
4. Inspect only the files or runtime values needed for the task.
5. Cross-check the related Academy schema, hook page, or guide.
6. Record the version in the answer, test note, or change description when material.

If the version changes during the task, recheck every version-sensitive conclusion used by the implementation.

Do not assume that the skill release, corpus snapshot, repository commit, or filesystem path implies a Bricks product version. Integrations and feature flags can also change registered elements, controls, queries, template types, and database tables.

## Typical source routing

| Need | Inspect |
|---|---|
| Element registration or controls | Active element registry and `includes/elements/` |
| Shared element settings | Active `Element` base implementation and Academy element schema |
| Breakpoints | Runtime breakpoint data and Academy breakpoints schema |
| Query behavior | Active query implementation and official Query Loop/hooks docs |
| Dynamic Data | Active providers and official Dynamic Data docs |
| Forms | Active Form element/actions and official Form schema |
| Theme Styles/global data | Active handlers and Academy global schemas |
| Saved content | Trusted live WordPress post meta/options, read-only first |

Internal file names are navigation hints, not stable public APIs.
