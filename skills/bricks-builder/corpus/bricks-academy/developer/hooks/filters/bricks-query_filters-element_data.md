---
title: "Filter: bricks/query_filters/element_data"
description: "Filters the data for a filter element before it is saved to the internal index table (bricksfilterelements). This allows plugins to attach extra metadata (like."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-element_data/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-element_data.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the data for a filter element before it is saved to the internal index table (`bricks_filter_elements`). This allows plugins to attach extra metadata (like language) to the filter configuration.

## Parameters

- `$element_data` (*array*): The data array to be saved (e.g., `filter_id`, `settings`, `post_id`, `language`).
- `$element` (*array*): The raw element data from the builder.
- `$post_id` (*int*): The ID of the post/template containing the element.

## Example usage

```php
add_filter( 'bricks/query_filters/element_data', function( $element_data, $element, $post_id ) {
    // Example: Add a custom property to the saved data
    $element_data['my_custom_prop'] = 'value';

    return $element_data;
}, 10, 3 );
```
