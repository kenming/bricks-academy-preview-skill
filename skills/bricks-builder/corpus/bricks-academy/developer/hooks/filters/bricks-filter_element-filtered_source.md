---
title: "Filter: bricks/filter_element/filtered_source"
description: "Filters the data retrieved from the index representing the available filter options and their counts based on the current query results."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-filtered_source/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-filtered_source.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the data retrieved from the index representing the available filter options and their counts based on the current query results.

## Parameters

- `$filtered_source` (*array*): Associative array where keys are filter values and values are their respective counts (based on the current filtered query).
- `$element` (*object*): The filter element instance.

## Example usage

```php
add_filter( 'bricks/filter_element/filtered_source', function( $filtered_source, $element ) {
    // Example: Ensure a specific value is always present with a count of 0 if missing
    if ( ! isset( $filtered_source['some_value'] ) ) {
        $filtered_source['some_value'] = 0;
    }

    return $filtered_source;
}, 10, 2 );
```
