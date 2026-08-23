---
title: "Tabs"
description: "The Tabs element creates tabbed content with horizontal or vertical layouts and responsive accordion fallback."
canonical: "https://academy.bricksbuilder.io/builder/elements/general/tabs/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/general/tabs.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-20T13:12:40.000Z"
---
The Tabs element creates tabbed content with horizontal or vertical layouts and responsive accordion fallback.

## Settings

- **Tabs** (repeater) - Add tab items. Each tab has:
  - **Icon** (icon) - Optional icon for the tab.
  - **Icon position** (select) - Position of the icon relative to text. Options from iconPosition control options. Default: `Left`. Requires icon to be set.
  - **Title** (text) - The tab title.
  - **ID** (text) - Anchor ID for linking to the tab.
  - **Content** (editor) - The content shown when the tab is active.

- **Layout** (select) - Tab orientation. Options: `horizontal`, `vertical`. Default: `horizontal`.

- **Accordion layout at breakpoint** (select) - Switch to accordion layout below this breakpoint. Options from available breakpoints.

- **Open tab on** (select) - Trigger for opening tabs. Options: `click`, `hover`. Default: `click`.

- **Open tab index** (text) - Index of the tab to expand on page load, starting at 0. Default: 0.

### Title

- **Stretch** (checkbox) - Make tab titles stretch to fill available space (horizontal layout only). Sets `flex-grow: 1` on `.tab-title`.

- **Align** (justify-content) - Horizontal alignment of tab titles (horizontal layout only). Controls `justify-content` on `.tab-menu`.

- **Padding** (spacing) - Padding inside tab titles. Default: `20px` (top, right, bottom, left).

- **Background** (color) - Background color of tab titles.

- **Border** (border) - Border styling for tab titles. Default: `1px solid #dedede` (top, right, left only, no bottom).

- **Typography** (typography) - Font styling for tab titles.

- **Active background** (color) - Background color of active tab titles.

- **Active border** (border) - Border styling for active tab titles.

- **Active typography** (typography) - Font styling for active tab titles.

### Content

- **Padding** (spacing) - Padding inside tab content. Default: `20px` (top, right, bottom, left).

- **Text align** (text-align) - Text alignment for tab content.

- **Text color** (color) - Text color of tab content.

- **Background color** (color) - Background color of tab content.

- **Border** (border) - Border styling for tab content. Default: `1px solid #dedede` (all sides).

:::tip[Developer reference]
See the [Tabs Schema](/developer/schema/elements/tabs/) for the full JSON schema of this element's settings and controls.
:::
