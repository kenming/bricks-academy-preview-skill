---
title: "Icon list"
description: "The Icon List element creates a list of social media icons or custom icons with customizable styling, labels, and links."
canonical: "https://academy.bricksbuilder.io/builder/elements/general/icon-list/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/general/icon-list.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-04T12:13:33.000Z"
---
The Icon List element creates a list of social media icons or custom icons with customizable styling, labels, and links.

## Settings

- **Icons** (repeater) - Add and configure icons. Each icon has:
  - **Icon** (icon) - Icon selection. Default: `ion-logo-twitter`.
  - **Icon: Color** (color) - Individual icon color.
  - **Icon: Size** (number with units) - Individual icon size.
  - **Label** (text) - Text label for the icon.
  - **Label: Size** (number with units) - Label text size.
  - **Color** (color) - Text color for the icon/label combination.
  - **Background** (color) - Background color for the icon item.
  - **Link** (link) - Link destination for the icon.

- **Icon: Color** (color) - Global icon color for all icons.

- **Icon: Size** (number with units) - Global icon size for all icons.

### Alignment

- **Direction** (direction) - Layout direction. Options: `row`, `column`.

- **Align items** (align-items) - Vertical alignment of icons. Options: `flex-start`, `center`, `flex-end`, `baseline`.

- **Justify content** (justify-content) - Horizontal alignment of icons. Options: `flex-start`, `center`, `flex-end`, `space-between`, `space-around`, `space-evenly`.

- **Spacing (Items)** (number with units) - Spacing between icon items. Default: 0.

- **Spacing (Item)** (number with units) - Internal spacing within each icon item. Default: 5px.

:::tip[Developer reference]
See the [Icon List Schema](/developer/schema/elements/social-icons/) for the full JSON schema of this element's settings and controls.
:::
