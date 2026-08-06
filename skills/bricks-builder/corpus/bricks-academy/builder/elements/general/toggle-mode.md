---
title: "Toggle - Mode"
description: "The Toggle - Mode element (toggle-mode) lets visitors switch between light and dark color modes on the front end. It relies on dark variants defined in the."
canonical: "https://academy.bricksbuilder.io/builder/elements/general/toggle-mode/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/general/toggle-mode.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-04T12:13:33.000Z"
---
The **Toggle - Mode** element (`toggle-mode`) lets visitors switch between **light** and **dark** color modes on the front end. It relies on **dark variants** defined in the Bricks **color manager**; if no dark colors exist, the builder toolbar sun/moon control does not appear, and the same idea applies to how the front end behaves.

The element renders a **button** containing two icon areas (`.toggle.light` and `.toggle.dark`); CSS shows the correct icon for the active mode.

## Settings

An **info** control explains that in the **builder**, you switch light/dark using the toolbar icon when dark colors are configured.

### Mode: Light

- **Icon** (icon) — Optional; default is the built-in light-mode graphic.
- **Color** (color) — Icon color/fill for the light icon.
- **Size** (number with units) — Icon size for the light icon.

### Mode: Dark

- **Icon Dark** (icon) — Optional; default is the built-in dark-mode graphic.
- **Color** (color) — Icon color/fill for the dark icon.
- **Size** (number with units) — Icon size for the dark icon.

### Accessibility

- **aria-label** (text) — Defaults to “Toggle mode” if empty.

:::tip[Developer reference]
See the [Toggle Mode Schema](/developer/schema/elements/toggle-mode/) for the full JSON schema of this element's settings and controls.
:::
