---
title: "Filter radio"
description: "Creates a radio button filter interface for single-selection filtering. Users can select one option at a time to filter query results. Supports taxonomy terms,."
canonical: "https://academy.bricksbuilder.io/builder/elements/filter/filter-radio/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/filter/filter-radio.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-20T13:12:40.000Z"
---
Creates a radio button filter interface for single-selection filtering. Users can select one option at a time to filter query results. Supports taxonomy terms, WordPress fields, custom fields, and can also function as a sorting or results-per-page control.

**Tip:** Use radio buttons when users should select only one filter option. Combine with the "Action" setting to create sorting dropdowns or results-per-page selectors.

## Settings

- **Target query** (query-list) - Select the query this filter should target. Only post queries are supported in this version.
- **URL parameter** (text) - Define a unique, more readable URL parameter name for this filter.
- **Apply on** (select) - Choose when to apply the filter. Options: Input (immediate), Submit (requires button click). Default: Input.
- **Action** (select) - Filter behavior. Options: Filter (traditional filtering), Sort (sorting control), Results per page (pagination control).
- **Source** (select) - Data source for filter options. Options: Taxonomy, WordPress field, Custom field.
- **Field type** (select) - Type of field when using WordPress field or custom field source. Options: Post, Term, User.
- **Field** (select) - Specific field to filter/sort by (varies based on field type and action).
- **Taxonomy** (select) - Taxonomy to use for filtering when source is taxonomy.
- **Order by** (select) - How to order taxonomy terms. Options: Name, Slug, Term ID, Description, Parent, Count, Include, Menu Order, Meta Value, Meta Value Num.
- **Order meta key** (text) - Meta key for ordering when using meta value ordering.
- **Order** (select) - Sort direction. Options: ASC, DESC. Default: ASC.
- **Terms: Include** (select) - Specific taxonomy terms to include in filter options.
- **Terms: Exclude** (select) - Specific taxonomy terms to exclude from filter options.
- **Top level terms only** (checkbox) - Display only top-level terms (parent = 0) when source is taxonomy.
- **Hide count** (checkbox) - Hide the result count for each option.
- **Hide empty** (checkbox) - Hide options with zero results.
- **Hide count bracket** (checkbox) - Remove brackets around count values. Style count via .brx-option-count.
- **Hierarchical** (checkbox) - Display taxonomy terms in hierarchical structure.
- **Indent: Prefix** (text) - Prefix text for hierarchical indentation. Default: —.
- **Indent: Gap** (number) - Gap spacing for hierarchical indentation.
- **Provider** (select) - Custom field provider for integration (ACF, Meta Box, etc.).
- **Meta key** (text) - Custom field key for filtering.
- **Compare** (select) - Comparison operator for filtering. Default: Equal.
- **Mode** (select) - Display mode for radio buttons. Options: Default (traditional radio buttons), Button (modern button style).
- **Sort options** (repeater) - Configure sorting options when Action is set to Sort.
  - **Option source** (text) - Sort field and direction (e.g., post_date_DESC).
  - **Option label** (text) - Display label for the sort option.
  - **Option order** (select) - Sort direction override.
  - **Option meta key** (text) - Meta key for meta-based sorting.
- **Results per page options** (text) - Comma-separated list of results per page options when Action is set to Results per page. Default: 10, 20, 50, 100.
- **Active filter** - Settings for active filter display.
  - **Prefix** (text) - Text to display before filter value.
  - **Suffix** (text) - Text to display after filter value.
  - **Title** (text) - Custom title attribute for filter links.

:::tip[Developer reference]
See the [Filter - Radio Schema](/developer/schema/elements/filter-radio/) for the full JSON schema of this element's settings and controls.
:::
