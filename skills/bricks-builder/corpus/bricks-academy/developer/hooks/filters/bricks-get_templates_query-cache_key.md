---
title: "Filter: bricks/get_templates_query/cache_key"
description: "Filters the cache key used by Templates::gettemplatesquery() to store and retrieve template queries. Use this to create unique cache entries when modifying the."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_templates_query-cache_key/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_templates_query-cache_key.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the cache key used by `Templates::get_templates_query()` to store and retrieve template queries. Use this to create unique cache entries when modifying the template query arguments based on custom context (e.g., user role, language).

## Parameters

- `$cache_key` (*string*): The unique cache key string.

## Example usage

```php
add_filter( 'bricks/get_templates_query/cache_key', function( $cache_key ) {
    // Example: Append current user role to cache key
    $user = wp_get_current_user();
    $role = ( array ) $user->roles;
    
    return $cache_key . '_' . implode( '-', $role );
} );
```
