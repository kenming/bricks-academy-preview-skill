# Source Policy

Use the narrowest source that directly supports the claim.

## Priority

1. User-provided files and explicit instructions.
2. Target project rules, code, and saved Bricks data.
3. Authorized active Bricks installation or trusted live WordPress runtime for version-specific behavior.
4. Bundled Bricks Academy corpus and current official Bricks documentation.
5. Historical notes, community repositories, issues, and third-party material as discovery aids only.

## Public and private boundaries

- The Academy corpus and hand-written development guidance may be published.
- Licensed Bricks parent-theme source may be inspected when authorized, but must not be copied into the skill.
- Keep absolute paths, credentials, site data, tokens, cookies, and license material out of public output and repositories.
- Use portable terms such as `{template_dir}`, `{stylesheet_dir}`, `get_template_directory()`, and `get_stylesheet_directory()`.

## Conflicts

When sources disagree, compare Bricks version, documentation date, migrations, enabled integrations, and runtime context. Prefer the active installation for its observed behavior and the official schema for portable public contracts. Report unresolved differences instead of generalizing one observation.
