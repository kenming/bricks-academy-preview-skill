---
title: "Button"
description: "The Button element creates clickable buttons with customizable styles, sizes, and optional icons."
canonical: "https://academy.bricksbuilder.io/builder/elements/basic/button/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/basic/button.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-07-29T10:15:35.000Z"
---
The Button element creates clickable buttons with customizable styles, sizes, and optional icons.

## Settings

- **Text** (text) - The button text label. Default: "I am a button".

- **HTML tag** (text) - The HTML tag to use for the button. Default: `span`. Changes to `a` automatically when a link is added.

- **Size** (select) - Predefined button size. Options vary based on theme settings (e.g., `sm`, `md`, `lg`). Default: Default size.

- **Style** (select) - Apply a predefined color style from your theme styles (e.g., `primary`, `secondary`, `success`, `danger`). Default: `primary`.

- **Circle** (checkbox) - Make the button circular (typically used for icon-only buttons).

- **Outline** (checkbox) - Apply an outline style instead of filled background.

### Link

- **Link type** (link) - Configure the button link behavior, URL, and attributes.

### Icon

- **Icon** (icon) - Add an icon to the button from the icon library.

- **Typography** (typography) - Style settings for the icon. Only available when an icon is selected.

- **Position** (select) - Icon placement relative to text. Options: `left`, `right`. Default: `right`.

- **Gap** (number with units) - Space between the icon and text.

- **Space between** (checkbox) - Distribute space between icon and text to push them to opposite ends of the button.

:::tip[Developer reference]
See the [Button Schema](/developer/schema/elements/button/) for the full JSON schema of this element's settings and controls.
:::
