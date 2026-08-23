---
title: "Query results summary"
description: "The Query Results Summary element, introduced in version 1.12.2, allows you to display a dynamic count of results within a query, helping users understand which."
canonical: "https://academy.bricksbuilder.io/builder/elements/query/query-results-summary/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/query/query-results-summary.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-20T13:12:40.000Z"
---
The Query Results Summary element, introduced in version 1.12.2, allows you to display a dynamic count of results within a query, helping users understand which items they are currently viewing in relation to the total number of results. This is particularly useful for search results, archive pages, and paginated lists where users navigate through multiple pages of content. It can be found in the elements panel under the "Query" category.

**Note:** If a third-party plugin disables Bricks Query history via the [`bricks/query/force_run`](/developer/hooks/filters/filter-bricks-query-force_run/) hook, the results summary may display incorrect information.

## Compatibility

The **Query Results Summary** element works seamlessly with Bricks' native AJAX actions, including:

- AJAX Pagination
- Load More
- Infinite Scroll
- Query Filters

This ensures that the summary updates dynamically as users interact with query-based elements on the page.

Example:

![](imgs/query-results-summary-element-example-e530ccb1a7.png)

## Settings

![](imgs/query-results-summary-element-controls-f1c3bdc55a.png)

### Query

Select the **target query** for which the summary should be displayed.

### Format

Customize the summary text using placeholders:

- `%start%` – The index of the first item on the current page.
- `%end%` – The index of the last item on the current page.
- `%total%` – The total number of results.

Default format: `Results: %start% - %end% of %total% posts`

Example output: Results: 1 - 5 of 14 posts

### Text: One Result

Define a custom message when the query returns exactly **one** result to handle singular/plural differences.

Default text: One post found

### Text: No Results

Specify a custom message when the query returns **zero** results.

Default text: No posts found

:::tip[Developer reference]
See the [Query Results Summary Schema](/developer/schema/elements/query-results-summary/) for the full JSON schema of this element's settings and controls.
:::
