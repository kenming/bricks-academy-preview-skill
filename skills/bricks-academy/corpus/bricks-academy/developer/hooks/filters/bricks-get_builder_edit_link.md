---
title: "Filter: bricks/get_builder_edit_link"
description: "Filters the \"Edit with Bricks\" URL generated for a post. This allows you to append custom query parameters or modify the link structure."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_builder_edit_link/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_builder_edit_link.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the "Edit with Bricks" URL generated for a post. This allows you to append custom query parameters or modify the link structure.

## Parameters

- `$url` (*string*): The "Edit with Bricks" URL.
- `$post_id` (*int*): The ID of the post.

## Example usage

```php
add_filter( 'bricks/get_builder_edit_link', function( $url, $post_id ) {
    // Example: Append a custom parameter to the builder URL
    return add_query_arg( 'my_param', 'value', $url );
}, 10, 2 );
```
