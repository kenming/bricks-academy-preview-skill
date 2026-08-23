---
title: "Text basic"
description: "The Basic Text element displays simple text content with basic formatting options. Use this element for paragraphs, small text blocks, or any content that."
canonical: "https://academy.bricksbuilder.io/builder/elements/basic/text-basic/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/basic/text-basic.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-20T13:12:40.000Z"
---
The Basic Text element displays simple text content with basic formatting options. Use this element for paragraphs, small text blocks, or any content that doesn't require rich text formatting.

## Settings

- **Text** (textarea) - The text content to display. Select text on canvas to access the formatting toolbar for styling options like bold, italic, and links. Line breaks are rendered as `<br>` tags.

- **HTML tag** (select) - The HTML tag to wrap the text content. Options: `div`, `p`, `span`, `figcaption`, `address`, `figure`, `custom`. Default: `div`.

- **Custom tag** (text) - Specify a custom HTML tag name without attributes. Only available when HTML tag is set to "custom".

- **Link to** (link) - Make the entire text element clickable by adding a link.

- **Words limit** (number) - Limit the number of words displayed. Minimum value: 1.

- **Read more** (text) - Text to display after the truncated content when using words limit. Only available when words limit is set.

:::tip[Developer reference]
See the [Basic Text Schema](/developer/schema/elements/text-basic/) for the full JSON schema of this element's settings and controls.
:::
