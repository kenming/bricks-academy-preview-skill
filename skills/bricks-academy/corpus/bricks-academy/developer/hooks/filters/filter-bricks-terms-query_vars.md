---
title: "Filter: bricks/terms/query_vars"
description: "Bricks terms query variables can be manipulated before the query runs like so:"
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-terms-query_vars/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-terms-query_vars.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Bricks terms query variables can be manipulated before the query runs like so:

```php
add_filter( 'bricks/terms/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    $query_vars['exclude'] = 23; // Exclude term id 23

    return $query_vars;
}, 10, 4 );
```

The filter callback receives three arguments:

- `$query_vars` an associative array used to feed the [WP_Term_Query](https://developer.wordpress.org/reference/classes/wp_term_query/) class
- `$settings` an associative array containing the element settings set in the builder
- `$element_id` is a string containing the unique element ID
- `$element_name` is a string containing the element name (`@since 1.11.1`)

## Example 1: Exclude the current term from the query {#exclude-current-term}

Inside a term archive page, to exclude the current term from the query:

```php
// Exclude current term from the terms query loop on term archive pages.
add_filter( 'bricks/terms/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    if ( $element_id !== 'uxtkgn' ) {
        return $query_vars;
    }

    $query_vars['exclude'] = get_queried_object_id();

    return $query_vars;
}, 10, 4 );
```

where `uxtkgn` is the Bricks ID of the element on which query loop is enabled.

## Example 2: Get terms assigned to a post {#get-terms-assigned-to-a-post}

In this example, we would like to get only the terms assigned to a specific post ID (the same as the WordPress function [`wp_get_object_terms()`](https://developer.wordpress.org/reference/functions/wp_get_object_terms/) output):

```php
add_filter( 'bricks/terms/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    if ( $element_id !== 'mjvhur' ) {
        return $query_vars;
    }

    $query_vars['object_ids'] = get_the_ID();

    return $query_vars;
}, 10, 4 );
```
