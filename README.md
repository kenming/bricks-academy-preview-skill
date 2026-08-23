# Bricks Builder Skill

A local-first Agent Skill for researching, building, editing, and auditing Bricks Builder sites.

It combines three evidence layers:

1. a synchronized local mirror of the official Bricks Academy documentation;
2. concise, hand-maintained development workflows;
3. version-aware verification against an authorized active Bricks installation when exact implementation details matter.

![Bricks Builder Skill evidence workflow](screenshots/evidence-workflow.svg)

The skill starts with public documentation, loads only the development guidance relevant to the task, and checks an authorized active installation before making version-sensitive claims.

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

- `768` synchronized documentation pages
- `631` downloaded local images
- `51` external embeds preserved as links

These numbers change as the official documentation evolves.

## Versioning and compatibility

This repository follows Semantic Versioning for the installable Skill contract. Its version is independent of the Bricks product version, WordPress version, and Academy snapshot date. Bricks and Academy updates only change the Skill version when they change its published behavior, workflows, or bundled guidance.

Version-sensitive implementation details must still be verified against the user's authorized active Bricks installation. See [`CHANGELOG.md`](CHANGELOG.md) for snapshot and compatibility notes.

## Installation

Clone the repository and copy the inner `skills/bricks-builder/` directory to a skill location supported by your agent.

### User-level installation

```bash
git clone https://github.com/kenming/bricks-builder-skill.git /tmp/bricks-builder-skill
mkdir -p ~/.agents/skills
cp -R /tmp/bricks-builder-skill/skills/bricks-builder ~/.agents/skills/
```

### Project-level installation

```bash
git clone https://github.com/kenming/bricks-builder-skill.git /tmp/bricks-builder-skill
mkdir -p .agents/skills
cp -R /tmp/bricks-builder-skill/skills/bricks-builder .agents/skills/
```

Claude Code users can use the same pattern with `~/.claude/skills/` or `.claude/skills/`.

Invoke it explicitly with `$bricks-builder`, or ask a clearly Bricks-specific documentation or development question.

## Invocation examples

Ask a clearly Bricks-specific question to trigger the Skill implicitly:

![Implicit invocation for a Bricks Container question](screenshots/chat-container-query.svg)

Use `$bricks-builder` when you want to invoke it explicitly, especially for an exact hook, schema, or implementation question:

![Explicit invocation for a Bricks query hook](screenshots/chat-hook-query.svg)

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
