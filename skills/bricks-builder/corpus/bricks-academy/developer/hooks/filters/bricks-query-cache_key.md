---
title: "Filter: bricks/query/cache_key"
description: "Filters the cache key used for a Bricks query loop."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-cache_key/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-cache_key.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the cache key used for a Bricks query loop. Use it when external context, such as language, should split query cache entries.

## Parameters

- `$cache_key` (string): The generated query cache key.
- `$query` (Bricks\Query): The Bricks query instance.

## Example usage

```php
add_filter( 'bricks/query/cache_key', function( $cache_key, $query ) {
    if ( function_exists( 'pll_current_language' ) ) {
        $cache_key .= '_' . pll_current_language();
    }

    return $cache_key;
}, 10, 2 );
```
