---
title: "Filter: bricks/database/content_type"
description: "Filters the content type determined by Bricks for the current page request. This affects which template conditions are checked (e.g., whether to look for a."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-database-content_type/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-database-content_type.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the content type determined by Bricks for the current page request. This affects which template conditions are checked (e.g., whether to look for a single template, archive template, or search results template).

## Parameters

- `$content_type` (*string*): The detected content type (e.g., `content`, `archive`, `search`, `error`, `header`, `footer`).
- `$post_id` (*int*): The current post ID.

## Example usage

```php
add_filter( 'bricks/database/content_type', function( $content_type, $post_id ) {
    // Example: Treat a specific page as a search results page
    if ( is_page( 'advanced-search' ) ) {
        return 'search';
    }

    return $content_type;
}, 10, 2 );
```
