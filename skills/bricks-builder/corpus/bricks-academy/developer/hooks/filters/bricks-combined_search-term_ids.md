---
title: "Filter: bricks/combined_search/term_ids"
description: "Filters the list of term IDs returned by the combined search logic (used in AJAX search filters targeting terms). This allows you to include or exclude terms."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-combined_search-term_ids/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-combined_search-term_ids.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the list of term IDs returned by the combined search logic (used in AJAX search filters targeting terms). This allows you to include or exclude terms from the search results after the initial search query has run.

## Parameters

- `$term_ids` (*array*): Array of found term IDs.
- `$term_fields` (*array*): Array of term fields being searched (e.g., `['name', 'slug']`).
- `$meta_fields` (*array*): Array of meta keys being searched.
- `$search_term` (*string*): The search term entered by the user.
- `$filter_id` (*string*): The ID of the filter element initiating the search.
- `$query_id` (*string*): The ID of the query loop being filtered.

## Example usage

```php
add_filter( 'bricks/combined_search/term_ids', function( $term_ids, $term_fields, $meta_fields, $search_term, $filter_id, $query_id ) {
    // Example: Exclude 'uncategorized' term (ID: 1) from search results
    if ( ( $key = array_search( 1, $term_ids ) ) !== false ) {
        unset( $term_ids[ $key ] );
    }

    return $term_ids;
}, 10, 6 );
```
