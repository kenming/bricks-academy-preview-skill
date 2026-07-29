---
title: "Filter: bricks/combined_search/post_ids"
description: "Filters the list of post IDs returned by the combined search logic (used in AJAX search filters). This allows you to include or exclude posts from the search."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-combined_search-post_ids/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-combined_search-post_ids.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the list of post IDs returned by the combined search logic (used in AJAX search filters). This allows you to include or exclude posts from the search results after the initial search query has run.

## Parameters

- `$post_ids` (*array*): Array of found post IDs.
- `$search_fields` (*array*): Array of post fields being searched (e.g., `['title', 'content', 'excerpt']`).
- `$meta_fields` (*array*): Array of meta keys being searched.
- `$search_term` (*string*): The search term entered by the user.
- `$filter_id` (*string*): The ID of the filter element initiating the search.
- `$query_id` (*string*): The ID of the query loop being filtered.

## Example usage

```php
add_filter( 'bricks/combined_search/post_ids', function( $post_ids, $search_fields, $meta_fields, $search_term, $filter_id, $query_id ) {
    // Example: Always include a specific sticky post in search results
    $sticky_post_id = 123;
    if ( ! in_array( $sticky_post_id, $post_ids ) ) {
        $post_ids[] = $sticky_post_id;
    }

    return $post_ids;
}, 10, 6 );
```
