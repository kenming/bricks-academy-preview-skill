---
title: "Filter: bricks/handle_no_results_children_elements"
description: "Determines whether Bricks should run logic to handle children elements displayed when a query loop returns no results (e.g., ensuring scripts/styles are."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-handle_no_results_children_elements/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-handle_no_results_children_elements.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Determines whether Bricks should run logic to handle children elements displayed when a query loop returns no results (e.g., ensuring scripts/styles are enqueued for "No results" content).

## Parameters

- `$run` (*bool*): Whether to handle "No results" children logic. Defaults to `true` if Query Filters are enabled.

## Example usage

```php
add_filter( 'bricks/handle_no_results_children_elements', function( $run ) {
    // Example: Always enable this logic, even if native Query Filters are disabled
    return true;
} );
```
