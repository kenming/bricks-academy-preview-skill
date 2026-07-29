---
title: "Filter: bricks/builder/post_title"
description: "Filters the post title displayed in the Bricks builder interface (e.g., in search results, dropdowns, and lists)."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-post_title/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-post_title.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the post title displayed in the Bricks builder interface (e.g., in search results, dropdowns, and lists).

## Parameters

- `$title` (*string*): The post title.
- `$post_id` (*int*): The ID of the post.

## Example usage

```php
add_filter( 'bricks/builder/post_title', function( $title, $post_id ) {
    // Example: Append the post ID to the title
    return $title . ' (ID: ' . $post_id . ')';
}, 10, 2 );
```
