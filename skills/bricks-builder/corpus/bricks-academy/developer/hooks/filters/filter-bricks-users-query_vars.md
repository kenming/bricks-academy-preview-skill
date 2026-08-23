---
title: "Filter: bricks/users/query_vars"
description: "Bricks users query variables can be manipulated before the query runs like so:"
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-users-query_vars/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-users-query_vars.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Bricks users query variables can be manipulated before the query runs like so:

```php
add_filter( 'bricks/users/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    $query_vars['exclude'] = [ 2, 5 ]; // Exclude users id 2 and 5

    return $query_vars;
}, 10, 4 );
```

The filter callback receives three arguments:

- `$query_vars` an associative array used to feed the [WP_User_Query](https://developer.wordpress.org/reference/classes/wp_user_query/) class
- `$settings` an associative array containing the element settings set in the builder
- `$element_id` is a string containing the unique element ID
- `$element_name` is a string containing the element name (`@since 1.11.1`)
