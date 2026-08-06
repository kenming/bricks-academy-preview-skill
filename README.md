# Bricks Builder Skill

A local-first Agent Skill for researching, building, editing, and auditing Bricks Builder sites.

It combines three evidence layers:

1. a synchronized local mirror of the official Bricks Academy documentation;
2. concise, hand-maintained development workflows;
3. version-aware verification against an authorized active Bricks installation when exact implementation details matter.

The skill does not bundle or reproduce the licensed Bricks theme source.

## Repository layout

```text
skills/bricks-builder/
├── SKILL.md
├── agents/
├── references/
│   └── development/
├── corpus/
│   └── bricks-academy/
├── index/
└── scripts/
```

The Academy corpus and index are generated synchronization products. Development references are intentionally small and describe verification workflows rather than exhaustive snapshots of internal control keys.

## Capabilities

- Search official Bricks Academy guides, hooks, elements, controls, and schemas locally.
- Guide Bricks page and element JSON work without guessing stored shapes.
- Develop custom elements safely in a child theme or plugin.
- Work with responsive settings, Theme Styles, global classes, variables, and components.
- Route Dynamic Data, Query Loop, Forms, and hook work through the correct public and active-version sources.
- Validate changes in the Builder and on the frontend.

## Current Academy snapshot

- `764` synchronized documentation pages
- `614` downloaded local images
- `51` external embeds preserved as links

These numbers change as the official documentation evolves.

## Installation

Clone the repository and copy the inner `skills/bricks-builder/` directory to a skill location supported by your agent.

### User-level installation

```bash
git clone https://github.com/kenming/bricks-academy-skill.git /tmp/bricks-builder-skill
mkdir -p ~/.agents/skills
cp -R /tmp/bricks-builder-skill/skills/bricks-builder ~/.agents/skills/
```

### Project-level installation

```bash
git clone https://github.com/kenming/bricks-academy-skill.git /tmp/bricks-builder-skill
mkdir -p .agents/skills
cp -R /tmp/bricks-builder-skill/skills/bricks-builder .agents/skills/
```

Claude Code users can use the same pattern with `~/.claude/skills/` or `.claude/skills/`.

Invoke it explicitly with `$bricks-builder`, or ask a clearly Bricks-specific documentation or development question.

## Local corpus tools

From the repository root:

```bash
python3 skills/bricks-builder/scripts/search_corpus.py "query loop"
python3 skills/bricks-builder/scripts/search_corpus.py "bricks/query/before_loop" --kind hook
python3 skills/bricks-builder/scripts/show_doc.py "new:developer/hooks/actions/action-bricks-query-before_loop"
```

Check for upstream Academy changes without downloading the full corpus:

```bash
python3 skills/bricks-builder/scripts/check_academy_updates.py
```

Run a full synchronization only when needed:

```bash
bash skills/bricks-builder/scripts/run_academy_sync.sh
```

## Evidence and licensing boundaries

- Use the local Academy corpus first for official public documentation.
- Verify exact control keys, hook signatures, JSON shapes, and internal behavior against the user's authorized active Bricks version when available.
- Keep the Bricks parent theme read-only; place custom code in a child theme or plugin.
- Never publish licensed theme source, credentials, private site data, or local absolute paths.

## Documentation

- Traditional Chinese: [`README.zh-TW.md`](README.zh-TW.md)
- Changes: [`CHANGELOG.md`](CHANGELOG.md)

## License

This repository is licensed under the MIT License. See [`LICENSE`](LICENSE).
