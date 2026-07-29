---
title: "Filter: bricks/filter_element/count_source_wcField"
description: "Filters the count data specifically for WooCommerce field filters (e.g., price, rating). This allows you to customize the counts displayed next to filter."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-count_source_wcfield/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-count_source_wcfield.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the count data specifically for WooCommerce field filters (e.g., price, rating). This allows you to customize the counts displayed next to filter options.

## Parameters

- `$count_source` (*array*): Associative array where keys are filter values and values are their respective counts.
- `$element` (*object*): The filter element instance.

## Example usage

```php
add_filter( 'bricks/filter_element/count_source_wcField', function( $count_source, $element ) {
    // Example: Hide counts for rating filter by setting them to 0 (if logic hides 0 counts)
    // Or manipulate them for specific ratings
    return $count_source;
}, 10, 2 );
```
