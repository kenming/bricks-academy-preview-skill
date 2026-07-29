---
title: "Filter: bricks/query_filters/index_post/meta_exists"
description: "Determines if a custom field (meta key) exists for a specific post during the indexing process. This is used when a third-party provider (like ACF or Meta Box)."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-index_post-meta_exists/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-index_post-meta_exists.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Determines if a custom field (meta key) exists for a specific post during the indexing process. This is used when a third-party provider (like ACF or Meta Box) is selected, to avoid indexing empty or non-existent fields.

## Parameters

- `$exists` (*bool*): Whether the meta key exists. Default is `false`.
- `$post_id` (*int*): The ID of the post being checked.
- `$meta_key` (*string*): The meta key of the custom field.
- `$provider` (*string*): The data provider (e.g., `acf`, `metabox`).

## Example usage

```php
add_filter( 'bricks/query_filters/index_post/meta_exists', function( $exists, $post_id, $meta_key, $provider ) {
    // Example: Custom check for a serialized meta field
    if ( $meta_key === 'my_serialized_data' ) {
        $data = get_post_meta( $post_id, $meta_key, true );
        return ! empty( $data );
    }

    return $exists;
}, 10, 4 );
```
