---
title: "Filter: bricks/query_filters/index_user/meta_exists"
description: "Determines if a custom field (meta key) exists for a specific user during the indexing process. This is used when a third-party provider (like ACF or Meta Box)."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-index_user-meta_exists/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query_filters-index_user-meta_exists.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Determines if a custom field (meta key) exists for a specific user during the indexing process. This is used when a third-party provider (like ACF or Meta Box) is selected, to avoid indexing empty or non-existent fields for users.

## Parameters

- `$exists` (*bool*): Whether the meta key exists. Default is `false`.
- `$user_id` (*int*): The ID of the user being checked.
- `$meta_key` (*string*): The meta key of the custom field.
- `$provider` (*string*): The data provider (e.g., `acf`, `metabox`).

## Example usage

```php
add_filter( 'bricks/query_filters/index_user/meta_exists', function( $exists, $user_id, $meta_key, $provider ) {
    // Example: Custom check for a serialized meta field on a user
    if ( $meta_key === 'user_custom_data' ) {
        $data = get_user_meta( $user_id, $meta_key, true );
        return ! empty( $data );
    }

    return $exists;
}, 10, 4 );
```
