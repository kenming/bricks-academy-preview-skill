---
title: "List"
description: "The List element creates customizable lists with icons, titles, meta information, descriptions, and optional highlight labels."
canonical: "https://academy.bricksbuilder.io/builder/elements/layout/list/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/layout/list.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-07-29T10:15:35.000Z"
---
The List element creates customizable lists with icons, titles, meta information, descriptions, and optional highlight labels.

## Settings

### List Items

- **List items** (repeater) - Add and configure list items. Each item has:
  - **Icon** (icon) - Optional icon for the list item
  - **Title** (text) - Main title text
  - **Link title** (link) - Make the title clickable
  - **Meta** (text) - Additional meta information (e.g., price, date)
  - **Description** (textarea) - Longer description text
  - **Highlight** (checkbox) - Mark this item as highlighted
  - **Highlight label** (text) - Custom label text for highlighted items. Only available when highlight is enabled.

### List Item

- **Justify content** (justify-content) - Horizontal alignment of list item content. Controls `justify-content` property for `.content` and `.description` selectors.

- **Align items** (align-items) - Vertical alignment of list item content. Options: `flex-start`, `center`, `flex-end`, `baseline`. Controls `align-items` property for `.content` and `.description` selectors. Excludes `stretch` option.

- **Margin** (spacing) - Margin around each list item. Controls `margin` property for `li` selector.

- **Padding** (spacing) - Padding inside each list item. Controls `padding` property for `li` selector.

- **Odd background** (color) - Background color for odd-numbered list items. Controls `background-color` property for `li:nth-child(odd)` selector.

- **Even background** (color) - Background color for even-numbered list items. Controls `background-color` property for `li:nth-child(even)` selector.

- **Border** (border) - Border styling for list items. Controls `border` property for `li` selector.

- **Auto width** (checkbox) - Enable automatic width for list items. Sets `justify-content` to `initial` for `.content` selector and `flex-grow` to `0` for `.separator` selector.

### Highlight

- **Block** (checkbox) - Display highlight label as block element. Controls `display` property for `li[data-highlight]::before` selector.

- **Padding** (spacing) - Padding for highlight label. Controls `padding` property for `li[data-highlight]::before` selector.

- **Background** (color) - Background color for highlight label. Controls `background-color` property for `li[data-highlight]::before` selector.

- **Border** (border) - Border styling for highlight label. Controls `border` property for `li[data-highlight]::before` selector.

- **Typography** (typography) - Typography settings for highlight label. Controls `font` property for `li[data-highlight]::before` selector.

- **Content** (separator) - Visual separator in the control panel.

- **Padding** (spacing) - Padding for highlighted item content. Controls `padding` property for `li[data-highlight] .content` selector.

- **Background** (color) - Background color for highlighted item content. Controls `background-color` property for `li[data-highlight] .content` selector.

- **Border** (border) - Border styling for highlighted item content. Controls `border` property for `li[data-highlight] .content` selector.

- **Text color** (color) - Text color for highlighted item content. Controls `color` property for `li[data-highlight] .content .title`, `li[data-highlight] .content .meta`, and `li[data-highlight] .content .description` selectors.

### Icon

- **Icon** (icon) - Default icon for all list items.

- **After title** (checkbox) - Position icon after the title instead of before.

- **Width** (number with units) - Width of the icon. Controls `width` property for `.icon` selector.

- **Height** (number with units) - Height of the icon. Controls `height` property for `.icon` selector.

- **Size** (number with units) - Font size of the icon. Controls `font-size` property for `.icon` selector, and `height`/`width` properties for `.icon svg` selector.

- **Color** (color) - Color of the icon. Controls `color` property for `.icon` selector.

- **Background color** (color) - Background color of the icon. Controls `background-color` property for `.icon` selector.

- **Border** (border) - Border styling for the icon. Controls `border` property for `.icon` selector.

- **Box shadow** (box-shadow) - Box shadow for the icon. Controls `box-shadow` property for `.icon` selector.

### Title

- **Margin** (spacing) - Margin around the title. Controls `margin` property for `.title` selector.

- **HTML tag** (text) - HTML tag for the title. Supports dynamic data. Default placeholder: `span`. Validates HTML tag format.

- **Typography** (typography) - Typography settings for the title. Controls `font` property for `.title` selector.

### Meta

- **Margin** (spacing) - Margin around the meta text. Controls `margin` property for `.meta` selector.

- **Typography** (typography) - Typography settings for the meta text. Controls `font` property for `.meta` selector.

### Description

- **Typography** (typography) - Typography settings for the description. Controls `font` property for `.description` selector.

### Separator

- **Disable** (checkbox) - Disable the separator line between items. Controls `display` property for `.separator` selector (sets to `none`). Triggers re-render.

- **Style** (select) - Border style for the separator. Options from border style control options. Controls `border-top-style` property for `.separator` selector. Only available when separator is not disabled.

- **Width** (number with units) - Width of the separator. Controls `flex-basis` property for `.separator` selector and sets `flex-grow` to `0`. Only available when separator is not disabled.

- **Height** (number with units) - Height/thickness of the separator. Controls `border-top-width` property for `.separator` selector. Only available when separator is not disabled.

- **Color** (color) - Color of the separator. Controls `border-top-color` property for `.separator` selector. Only available when separator is not disabled.

:::tip[Developer reference]
See the [List Schema](/developer/schema/elements/list/) for the full JSON schema of this element's settings and controls.
:::
