---
title: "Accordion (nestable)"
description: "The Nestable Accordion element allows creating hierarchical collapsible content with drag-and-drop nesting in the builder."
canonical: "https://academy.bricksbuilder.io/builder/elements/general/accordion-nested/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/general/accordion-nested.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-04T12:13:33.000Z"
---
The Nestable Accordion element allows creating hierarchical collapsible content with drag-and-drop nesting in the builder.

## Settings

- **Children** (nestable) - Drag and drop elements to create accordion items. Each item can contain nested content. Set "ID" on items to open via anchor link (no spaces, no pound sign).

- **Expand item indexes** (text) - Comma-separated indexes of items to expand on page load (starting at 0).

- **Independent toggle** (checkbox) - Allow multiple items to be open simultaneously. Enable to open & close an item without toggling other items.

- **Transition (ms)** (number) - Animation duration for expanding/collapsing in milliseconds. Default: 200.

- **FAQ schema** (checkbox) - Generate FAQPage structured data (JSON-LD) for search engines.

### Title

- **Min. height** (number with units) - Minimum height for title areas. Default: 50px.

- **Margin** (spacing) - Margin around title wrappers.

- **Padding** (spacing) - Padding inside title wrappers.

- **Background color** (color) - Background color for title wrappers.

- **Border** (border) - Border styling for title wrappers.

- **Typography** (typography) - Typography settings for title text and headings.

#### Active Title

- **Background color** (color) - Background color for active/expanded title wrappers.

- **Border** (border) - Border styling for active/expanded title wrappers.

- **Typography** (typography) - Typography settings for active/expanded title text and headings.

### Content

- **Margin** (spacing) - Margin around content wrappers.

- **Padding** (spacing) - Padding inside content wrappers. Default: 15px top/bottom, 0px left/right.

- **Background color** (color) - Background color for content wrappers.

- **Border** (border) - Border styling for content wrappers.

- **Typography** (typography) - Typography settings for content text.

:::tip[Developer reference]
See the [Accordion (Nestable) Schema](/developer/schema/elements/accordion-nested/) for the full JSON schema of this element's settings and controls.
:::
