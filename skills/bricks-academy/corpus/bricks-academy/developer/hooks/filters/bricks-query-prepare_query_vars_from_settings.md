---
title: "Filter: bricks/query/prepare_query_vars_from_settings"
description: "Filters the element settings before they are converted into query variables. This runs early in the query setup process, allowing you to modify the raw query."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-prepare_query_vars_from_settings/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-prepare_query_vars_from_settings.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the element settings before they are converted into query variables. This runs early in the query setup process, allowing you to modify the raw query settings of an element.

## Parameters

- `$settings` (*array*): The element settings array. The query settings are typically located in `$settings['query']`.
- `$element_id` (*string*): The ID of the element being queried.

## Example usage

```php
add_filter( 'bricks/query/prepare_query_vars_from_settings', function( $settings, $element_id ) {
    // Example: Force a specific post type for a query element with ID 'my_query_element'
    if ( $element_id === 'my_query_element' ) {
        $settings['query']['post_type'] = 'my_custom_post_type';
    }

    return $settings;
}, 10, 2 );
```
