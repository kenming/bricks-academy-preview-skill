---
title: "Filter: bricks/element/builder_setup_query"
description: "Filters the query arguments used to set up the preview context in the builder (e.g., when \"Populate Content\" is active)."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-element-builder_setup_query/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-element-builder_setup_query.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the query arguments used to set up the preview context in the builder (e.g., when "Populate Content" is active).

## Parameters

- `$query_args` (*array*): Array of arguments passed to `WP_Query`.
- `$post_id` (*int*): The ID of the template being edited.

## Example usage

```php
add_filter( 'bricks/element/builder_setup_query', function( $query_args, $post_id ) {
    // Example: If editing a specific template, force a specific post for preview
    if ( $post_id === 123 ) {
        $query_args['p'] = 456;
        $query_args['post_type'] = 'post';
    }

    return $query_args;
}, 10, 2 );
```
