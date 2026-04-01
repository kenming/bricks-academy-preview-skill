Creates a checkbox filter interface for AJAX-powered content filtering. Users can select multiple options to narrow down query results. Supports taxonomy terms, WordPress fields, and custom fields as filter sources.

**Tip:** Perfect for allowing users to filter by multiple categories, tags, or custom attributes simultaneously.

## Settings

- **Target query** (query-list) - Select the query this filter should target. Only post queries are supported in this version.
- **URL parameter** (text) - Define a unique, more readable URL parameter name for this filter.
- **Apply on** (select) - Choose when to apply the filter. Options: Input (immediate), Submit (requires button click). Default: Input.
- **Source** (select) - Data source for filter options. Options: Taxonomy, WordPress field, Custom field.
- **Field type** (select) - Type of field when using WordPress field or custom field source. Options: Post, Term, User.
- **Field** (select) - Specific field to filter by (varies based on field type).
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
- **Auto toggle child terms** (checkbox) - Automatically toggle child term checkboxes when parent is clicked.
- **Indent: Prefix** (text) - Prefix text for hierarchical indentation. Default: —.
- **Indent: Gap** (number) - Gap spacing for hierarchical indentation.
- **Provider** (select) - Custom field provider for integration (ACF, Meta Box, etc.).
- **Meta key** (text) - Custom field key for filtering.
- **Compare** (select) - Comparison operator for filtering. Options: IN, NOT IN, BETWEEN, NOT BETWEEN.
- **Mode** (select) - Display mode for checkboxes. Options: Default (traditional checkboxes), Button (modern button style).
- **Active filter** - Settings for active filter display.
  - **Prefix** (text) - Text to display before filter value.
  - **Suffix** (text) - Text to display after filter value.
  - **Title** (text) - Custom title attribute for filter links.

:::tip[Developer reference]
See the [Filter - Checkbox Schema](/developer/schema/elements/filter-checkbox/) for the full JSON schema of this element's settings and controls.
:::
