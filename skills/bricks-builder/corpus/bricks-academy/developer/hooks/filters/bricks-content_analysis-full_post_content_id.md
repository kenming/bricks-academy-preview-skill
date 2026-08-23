---
title: "Filter: bricks/content_analysis/full_post_content_id"
description: "Filters the post ID Bricks treats as the full-content target during content analysis."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-content_analysis-full_post_content_id/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-content_analysis-full_post_content_id.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the post ID Bricks treats as the full-content target during content analysis. Return a post ID to let Bricks remove the More block only for that target post.

## Parameters

- `$post_id` (int): The content analysis target post ID. Defaults to 0.

## Example usage

```php
add_filter( 'bricks/content_analysis/full_post_content_id', function( $post_id ) {
    return defined( 'MY_CONTENT_ANALYSIS_POST_ID' ) ? MY_CONTENT_ANALYSIS_POST_ID : $post_id;
} );
```
