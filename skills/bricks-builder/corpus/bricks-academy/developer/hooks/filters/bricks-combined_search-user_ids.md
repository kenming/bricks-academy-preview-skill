---
title: "Filter: bricks/combined_search/user_ids"
description: "Filters the list of user IDs returned by the combined search logic (used in AJAX search filters targeting users). This allows you to include or exclude users."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-combined_search-user_ids/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-combined_search-user_ids.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the list of user IDs returned by the combined search logic (used in AJAX search filters targeting users). This allows you to include or exclude users from the search results after the initial search query has run.

## Parameters

- `$user_ids` (*array*): Array of found user IDs.
- `$user_fields` (*array*): Array of user fields being searched (e.g., `['display_name', 'user_email']`).
- `$meta_fields` (*array*): Array of meta keys being searched.
- `$search_term` (*string*): The search term entered by the user.
- `$filter_id` (*string*): The ID of the filter element initiating the search.
- `$query_id` (*string*): The ID of the query loop being filtered.

## Example usage

```php
add_filter( 'bricks/combined_search/user_ids', function( $user_ids, $user_fields, $meta_fields, $search_term, $filter_id, $query_id ) {
    // Example: Exclude administrator (ID: 1) from search results
    if ( ( $key = array_search( 1, $user_ids ) ) !== false ) {
        unset( $user_ids[ $key ] );
    }

    return $user_ids;
}, 10, 6 );
```
