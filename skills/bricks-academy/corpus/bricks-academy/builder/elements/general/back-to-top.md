---
title: "Back to Top"
description: "The Back to Top element renders a button (default tag: button) that scrolls the visitor back to the top of the page. It is nestable: you typically place an Icon."
canonical: "https://academy.bricksbuilder.io/builder/elements/general/back-to-top/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/general/back-to-top.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-07-29T10:15:35.000Z"
---
The **Back to Top** element renders a button (default tag: `button`) that scrolls the visitor back to the top of the page. It is **nestable**: you typically place an **Icon** and/or **Text** element inside it (the defaults use an up-arrow icon and the label “Back to Top”).

## Settings

- **HTML tag** (text) — Root element tag. Default: `button`.

- **aria-label** (text) — Accessible name when the control has no visible descriptive text.

### Position

- **Position** (select) — CSS `position` (placeholder suggests `fixed`).
- **Top**, **Right**, **Bottom**, **Left** (number with units) — Position offsets.

### Misc

Bricks surfaces **z-index**, **gap** (space between nested children), and **CSS transition** on this element (moved from the default tabs).

- **Visible after** (number) — Show the button only after the user has scrolled this many pixels. If empty and **Visible on scroll up** is off, the button stays visible.
- **Visible on scroll up** (checkbox) — Show the button when the user scrolls upward.
- **Smooth scroll** (checkbox) — Smooth scroll to the top when activated.
- **Move focus to top** (checkbox) — Move keyboard focus to the top of the page after activation (accessibility).

:::tip[Developer reference]
See the [Back to Top Schema](/developer/schema/elements/back-to-top/) for the full JSON schema of this element's settings and controls.
:::
