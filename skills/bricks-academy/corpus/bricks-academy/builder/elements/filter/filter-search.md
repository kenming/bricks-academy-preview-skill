---
title: "Filter search"
description: "Provides a live AJAX search input for real-time content filtering. Searches through post content, titles, and custom fields without page refresh. Features."
canonical: "https://academy.bricksbuilder.io/builder/elements/filter/filter-search/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/filter/filter-search.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-07-29T10:15:35.000Z"
---
Provides a live AJAX search input for real-time content filtering. Searches through post content, titles, and custom fields without page refresh. Features debouncing, minimum character requirements, and optional clear functionality.

**Tip:** Perfect for creating instant search experiences. Use the debounce setting to control API call frequency, and minimum characters to improve performance.

## Settings

- **Target query** (query-list) - Select the query this filter should target. Only post queries are supported in this version.
- **URL parameter** (text) - Define a unique, more readable URL parameter name for this filter.
- **Apply on** (select) - Choose when to apply the filter. Options: Input (immediate), Submit (requires button click). Default: Input.
- **Debounce (ms)** (number) - Delay before triggering search after typing stops. Default: 500ms.
- **Min. characters** (number) - Minimum characters required to trigger search. Default: 3.
- **Input** - Settings for the search input field.
  - **Placeholder** (text) - Placeholder text for the search input. Default: Search.
  - **Placeholder typography** (typography) - Typography for placeholder text.
  - **Label** (text) - Optional label text above the input field.
  - **Label typography** (typography) - Typography for the label text.
- **Icon (Clear)** - Settings for the clear/reset icon.
  - **Icon** (icon) - Icon to display for clearing the search.
  - **Icon color** (color) - Color of the clear icon.
  - **Icon size** (number) - Size of the clear icon.
- **Active filter** - Settings for active filter display.
  - **Prefix** (text) - Text to display before filter value.
  - **Suffix** (text) - Text to display after filter value.
  - **Title** (text) - Custom title attribute for filter links.

:::tip[Developer reference]
See the [Filter - Search Schema](/developer/schema/elements/filter-search/) for the full JSON schema of this element's settings and controls.
:::
