# Responsive Settings and Global Design Data

## Breakpoints

Read active breakpoint records before generating variants. Records can include a key, label, widths, base/custom flags, and paused/edited state. Do not assume default labels, widths, or cascade direction.

Responsive and pseudo-state keys use flat colon suffixes when the control supports them:

```text
_padding
_padding:tablet_portrait
_typography:hover
_typography:mobile_portrait:hover
```

## Theme Styles

Theme Styles are global, condition-aware design records. Their settings are grouped by theme-style sections rather than being ordinary element objects. Use the Academy Theme Styles schema and inspect a UI-created style before automation.

## Global classes

Elements reference global classes by class ID, not display name. A class contains its own settings and can contain scoped selectors. Preserve IDs and existing metadata during updates.

## Variables and palettes

Global variable and color records have structured IDs and metadata. Do not reduce color objects to an assumed hex string or prepend/remove `--` from variable names without inspecting current storage and CSS output.

## Components

Components connect reusable element trees, properties, variants, and instances. Treat component connections as version-sensitive. Build one representative component in the UI and inspect its stored/exported shape before generation.

## Safety

Prefer Bricks UI/import paths for global design changes. Before a programmatic mutation, back up the entire target option, validate references, and test that generated CSS can be rebuilt through a supported Bricks workflow.
