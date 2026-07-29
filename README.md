# Bricks Academy Skill

A local-first Agent Skill repository for querying the official Bricks Academy documentation.

This repository packages a maintained mirror of the docs published at
`https://academy.bricksbuilder.io/` and exposes it as a skill under
`skills/bricks-academy/`.

## What This Repository Contains

- A Bricks Academy corpus mirrored to local Markdown
- Downloaded local image assets referenced by the docs
- Search and lookup scripts for querying the corpus
- Sync scripts for refreshing the corpus when the official Academy site changes
- A skill definition compatible with the Agent Skills open specification

## Repository Layout

```text
skills/bricks-academy/
├── SKILL.md
├── corpus/
├── index/
├── references/
└── scripts/
```

Key paths:

- Skill entry: `skills/bricks-academy/SKILL.md`
- Local corpus: `skills/bricks-academy/corpus/bricks-academy/`
- Search index: `skills/bricks-academy/index/academy_corpus_manifest.csv`

## Current Corpus Snapshot

- `764` synced documentation pages
- `614` downloaded local images
- `51` external embeds preserved as links

These numbers reflect the current Academy snapshot in this repository and may
change as the official documentation evolves.

## Installation

This repository is structured as a skill repository with a nested `skills/` directory:

```text
bricks-academy-skill/
└── skills/
    └── bricks-academy/
        └── SKILL.md
```

When installing manually, copy the inner `skills/bricks-academy/` folder to a location your agent scans for skills.

Common skill locations:

- Codex/Copilot user-level: `~/.agents/skills/`
- Codex/Copilot project-level: `.agents/skills/`
- Claude Code user-level: `~/.claude/skills/`
- Claude Code project-level: `.claude/skills/`
- Other AI agents: check that agent's skill documentation for its supported global and project-level skill directories.

### Option 1: Codex/Copilot User-Level Installation

Install the skill globally for Codex/Copilot-style agents:

```bash
git clone https://github.com/kenming/bricks-academy-skill.git /tmp/bricks-academy-skill
mkdir -p ~/.agents/skills
cp -R /tmp/bricks-academy-skill/skills/bricks-academy ~/.agents/skills/
rm -rf /tmp/bricks-academy-skill
```

Result:

```text
~/.agents/skills/
└── bricks-academy/
    └── SKILL.md
```

### Option 2: Codex/Copilot Project-Level Installation

Install the skill only for one project:

```bash
git clone https://github.com/kenming/bricks-academy-skill.git /tmp/bricks-academy-skill
mkdir -p .agents/skills
cp -R /tmp/bricks-academy-skill/skills/bricks-academy .agents/skills/
rm -rf /tmp/bricks-academy-skill
```

Result:

```text
.agents/skills/
└── bricks-academy/
    └── SKILL.md
```

For Claude Code, use the same copy command pattern with `~/.claude/skills/`
or `.claude/skills/` as the destination.

### Verify Installation

Confirm the installed skill folder contains:

- `SKILL.md`
- `scripts/`
- `references/`
- `corpus/`
- `index/`

Then ask your agent a Bricks Builder question such as:

- `How does Bricks query loop work?`
- `Look up bricks/query/before_loop`
- `Find the docs for Theme Styles in Bricks`

## Triggering the Skill

This skill supports both explicit and implicit invocation.

### Explicit Invocation

Use the skill name directly when you want to force the agent to use this skill:

```text
$bricks-academy Find the docs for bricks/query/before_loop and answer briefly.
```

This is useful when:

- You want deterministic local-doc lookup
- You are testing the skill
- You want to avoid ambiguity with broader web or framework knowledge

### Implicit Invocation

Ask a clearly Bricks-specific question in natural language:

```text
In Bricks, what does bricks/query/before_loop do?
Where are Theme Styles configured in Bricks?
What is the Container element used for in Bricks?
```

The skill is designed so that clearly Bricks-specific queries can trigger local corpus lookup automatically, while unrelated generic topics should not trigger the skill.

Examples:

![Explicit invocation example](screenshots/chat-hook-query.png)

![Implicit invocation example: Theme Styles](screenshots/chat-theme-styles-query.png)

![Implicit invocation example: Container element](screenshots/chat-container-query.png)

## Usage

Search the corpus:

```bash
python3 skills/bricks-academy/scripts/search_corpus.py "query loop"
python3 skills/bricks-academy/scripts/search_corpus.py "bricks/query/before_loop" --kind hook
python3 skills/bricks-academy/scripts/search_corpus.py "theme styles" --section builder --subsection builder/styling --limit 5
```

Open a document:

```bash
python3 skills/bricks-academy/scripts/show_doc.py "new:developer/hooks/actions/action-bricks-query-before_loop"
```

Refresh the Academy corpus:

```bash
bash skills/bricks-academy/scripts/run_academy_sync.sh
```

Check whether the official Academy docs changed without downloading the full
corpus:

```bash
python3 skills/bricks-academy/scripts/check_academy_updates.py
```

After a trusted full sync, refresh the lightweight remote ETag baseline:

```bash
python3 skills/bricks-academy/scripts/check_academy_updates.py --update-cache
```

## Notes

- This repository tracks the official Bricks Academy documentation, which may
  continue to evolve.
- Structural and content changes are expected upstream.
- The skill is designed to answer from the local corpus first and only fall back to live browsing when needed.

## Documentation

- English: `README.md`
- Traditional Chinese: `README.zh-TW.md`
- Changelog: `CHANGELOG.md`

## License

This repository is licensed under the MIT License. See `LICENSE`.
