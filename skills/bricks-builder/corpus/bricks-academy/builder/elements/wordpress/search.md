---
title: "Search"
description: "Displays a search form with input field and submit button, or an icon that opens an overlay search."
canonical: "https://academy.bricksbuilder.io/builder/elements/wordpress/search/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/wordpress/search.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-04T12:13:33.000Z"
---
Displays a search form with input field and submit button, or an icon that opens an overlay search.

## Settings

- **Type** (select) - Choose between Input or Icon & Overlay. Default: Input.
- **aria-label** (text) - Accessibility label for overlay type. Required for overlay.
- **Action URL** (text) - URL where search form submits. Default: home URL.
- **Additional parameters** (repeater) - Hidden input fields added to search form.

### Input
- **Height** (number) - Input field height.
- **Width** (number) - Input field width.
- **Placeholder** (text) - Placeholder text. Default: "Search ...".
- **Placeholder color** (color) - Color of placeholder text.
- **Background color** (color) - Input background color.
- **Border** (border) - Input border settings.
- **Box shadow** (box-shadow) - Input box shadow.
- **Typography** (typography) - Input text typography.
- **Show label** (checkbox) - Display label above input. Default: false.
- **Label text** (text) - Text for input label.
- **Label typography** (typography) - Typography for input label.

### Button / Icon
- **aria-label** (text) - Accessibility label for button.
- **Text** (text) - Button text.
- **Icon** (icon) - Button icon.
- **Padding** (spacing) - Button padding.
- **Height** (number) - Button height.
- **Width** (number) - Button width.
- **Background color** (color) - Button background color.
- **Border** (border) - Button border settings.
- **Box shadow** (box-shadow) - Button box shadow.
- **Typography** (typography) - Button text typography.

### Overlay
- **Direction (Form)** (direction) - Flex direction of overlay form.
- **Gap** (number) - Gap between form elements.
- **Title** (text) - Overlay title. Default: "Search site".
- **Title tag** (text) - HTML tag for title. Default: h4.
- **Title typography** (typography) - Typography for overlay title.
- **Background** (background) - Overlay background.
- **Background: Overlay** (color) - Overlay background overlay color.
- **Button: Width** (number) - Overlay button width.
- **Button: Padding** (spacing) - Overlay button padding.
- **Button: Background color** (color) - Overlay button background color.
- **Button: Border** (border) - Overlay button border.
- **Button: Typography** (typography) - Overlay button typography.

:::tip[Developer reference]
See the [Search Schema](/developer/schema/elements/search/) for the full JSON schema of this element's settings and controls.
:::
