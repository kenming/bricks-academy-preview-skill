---
title: "Toggle"
description: "The Toggle element outputs a button used to open and close other UI—most often an Offcanvas menu. You can use a custom icon or the built-in animated “hamburger”."
canonical: "https://academy.bricksbuilder.io/builder/elements/general/toggle/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/general/toggle.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-07-29T10:15:35.000Z"
---
The **Toggle** element outputs a **button** used to open and close other UI—most often an [Offcanvas](/builder/elements/general/offcanvas/) menu. You can use a **custom icon** or the built-in animated “hamburger” bars (with optional **Animation** presets).

Bricks shows an inline hint: copy the **element ID** (or a valid CSS selector) of the target into **CSS selector**—for example `.brxe-offcanvas` for an Offcanvas.

## Settings

### Icon (optional)

If you add an **Icon**, the bar animation is hidden and the icon is used instead.

- **Icon** (icon)
- **Color** (color) — Icon color/fill.
- **Size** (number with units) — Icon size.

### Toggle

- **CSS selector** (text) — Target node to toggle (e.g. `.brxe-offcanvas`). Placeholder: `.brxe-offcanvas`.
- **Attribute** (text) — HTML attribute to change (default behavior uses `class`). Placeholder: `class`.
- **Value** (text) — Value applied when toggling (e.g. open-state class). Placeholder: `brx-open`.

### Bar (when no custom icon)

- **Animation** (select) — Preset hamburger animation: `close (x)`, `arrow`, `arrow-r`, `arrowalt`, `arrowalt-r`, `arrowturn`, `arrowturn-r`, `minus`, `spin`, `spring`, `squeeze`, `vortex`, or none.
- **Scale** (number) — Bar scale via `--brxe-toggle-scale`.
- **Height**, **Radius** (number with units) — Bar dimensions.
- **Color** (color) — Bar color.

### Accessibility

- **aria-label** (text) — Defaults to “Open” (or “Close” when used as the nested close control inside certain structures such as Nav).

:::tip[Developer reference]
See the [Toggle Schema](/developer/schema/elements/toggle/) for the full JSON schema of this element's settings and controls.
:::
