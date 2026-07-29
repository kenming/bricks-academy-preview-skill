---
title: "Filter: bricks/related_posts/query_vars"
description: "Since Bricks 1.3.5 you may manipulate the related posts element query vars before the query is performed like so:"
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-related_posts-query_vars/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-related_posts-query_vars.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Since Bricks 1.3.5 you may manipulate the **related posts** element query vars before the query is performed like so:

```php
add_filter( 'bricks/related_posts/query_vars', function( $query_vars, $settings, $element_id ) {
    $query_vars['post_type'] = [ 'post', 'project' ];

    return $query_vars;
}, 10, 3 );
```

The filter callback receives two arguments:

- `$query_vars` is an associative array used to feed the [WP_Query](https://developer.wordpress.org/reference/classes/wp_query/) class
- `$settings` is an associative array containing the element settings set in the builder
- `$element_id` is a string containing the element ID
