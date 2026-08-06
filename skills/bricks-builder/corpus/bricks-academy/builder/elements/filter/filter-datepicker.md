---
title: "Filter datepicker"
description: "Provides a date picker interface for filtering content by date ranges. Supports single dates or date ranges with time selection. Can filter by post dates, user."
canonical: "https://academy.bricksbuilder.io/builder/elements/filter/filter-datepicker/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/filter/filter-datepicker.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-04T12:13:33.000Z"
---
Provides a date picker interface for filtering content by date ranges. Supports single dates or date ranges with time selection. Can filter by post dates, user registration dates, or custom date fields.

**Tip:** Ideal for filtering content by publication date, event dates, or any time-based data. Enable "Date range" for before/after date filtering, and "Enable time" for precise time-based queries.

## Settings

- **Target query** (query-list) - Select the query this filter should target. Only post queries are supported in this version.
- **URL parameter** (text) - Define a unique, more readable URL parameter name for this filter.
- **Apply on** (select) - Choose when to apply the filter. Options: Input (immediate), Submit (requires button click). Default: Input.
- **Source** (select) - Data source for filter options. Options: Taxonomy, WordPress field, Custom field.
- **Field type** (select) - Type of field when using WordPress field or custom field source. Options: Post, Term, User.
- **Field** (select) - Specific date field to filter by (post date, modified date, user registered date).
- **Provider** (select) - Custom field provider for integration (ACF, Meta Box, etc.).
- **Meta key** (text) - Custom field key containing date values.
- **Enable time** (checkbox) - Add time selection capability to the date picker.
- **Date range** (checkbox) - Enable selection of date ranges instead of single dates.
- **Date format** (text) - Date format matching the database storage format. Default: Y-m-d H:i:s. ACF uses Ymd format.
- **Min/max date** (checkbox) - Use minimum and maximum dates from the index table for date picker limits.
- **Compare** (select) - Comparison operator for date filtering. Options: == (is), < (before), > (after).
- **Input** - Settings for the date input field.
  - **Placeholder** (text) - Placeholder text for the input field. Default: Date.
  - **Placeholder typography** (typography) - Typography for placeholder text.
  - **Language** (text) - Language code for date picker localization (de, es, fr, etc.).
- **Active filter** - Settings for active filter display.
  - **Prefix** (text) - Text to display before filter value.
  - **Suffix** (text) - Text to display after filter value.
  - **Title** (text) - Custom title attribute for filter links.

:::tip[Developer reference]
See the [Filter - Datepicker Schema](/developer/schema/elements/filter-datepicker/) for the full JSON schema of this element's settings and controls.
:::
