---
title: "Filter active filters"
description: "Displays the currently active or selected filters, allowing users to easily remove a filter with a single click for faster navigation. This element shows all."
canonical: "https://academy.bricksbuilder.io/builder/elements/filter/filter-active-filters/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/filter/filter-active-filters.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-07-29T10:15:35.000Z"
---
Displays the currently active or selected filters, allowing users to easily remove a filter with a single click for faster navigation. This element shows all active filters from the connected target query and provides quick access to clear individual filters.

**Tip:** Use this element alongside other filter elements to give users clear visibility of their current filter selections and easy ways to modify their search criteria.

## Settings

- **Target query** (query-list) - Select the query this filter should target. Only post queries are supported in this version.
- **Exclude filter IDs** (text) - Enter Bricks IDs, separated by comma, of filter elements to exclude from the active filters list.
- **URL parameter** (text) - Define a unique, more readable URL parameter name for this filter.
- **Apply on** (select) - Choose when to apply the filter. Options: Input (immediate), Submit (requires button click). Default: Input.
- **Button** - Settings for the remove filter buttons.
  - **Padding** (spacing) - Padding for filter remove buttons.
  - **Gap** (number) - Gap between filter buttons.
  - **Size** (select) - Button size preset. Options: Default, Small, Medium, Large, Extra Large.
  - **Style** (select) - Button style. Options: None, Primary, Secondary, Success, Info, Warning, Danger, Dark, Light.
  - **Circle** (checkbox) - Make buttons circular.
  - **Outline** (checkbox) - Use outline button style.
  - **Background color** (color) - Custom background color for buttons.
  - **Border** (border) - Border styling for buttons.
  - **Typography** (typography) - Typography settings for button text.
- **Icon** - Settings for filter remove icons.
  - **Icon** (icon) - Icon to display on filter buttons.
  - **Color** (color) - Icon color.
  - **Size** (number) - Icon size.
  - **Gap** (number) - Gap between icon and text.
  - **Position** (select) - Icon position. Options: Left, Right. Default: Right.
- **Active filter** - Settings for active filter display.
  - **Prefix** (text) - Text to display before filter value.
  - **Suffix** (text) - Text to display after filter value.
  - **Title** (text) - Custom title attribute for filter links.

:::tip[Developer reference]
See the [Filter - Active Filters Schema](/developer/schema/elements/filter-active-filters/) for the full JSON schema of this element's settings and controls.
:::
