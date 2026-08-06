---
title: "Filter: bricks/query/force_loop_index"
description: "Forces Bricks\\Query::getloopindex() to return a specific value. This is useful for AJAX contexts (like popups) where you need to simulate a specific loop."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-force_loop_index/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-force_loop_index.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Forces `Bricks\Query::get_loop_index()` to return a specific value. This is useful for AJAX contexts (like popups) where you need to simulate a specific loop iteration to render correct data or styles.

## Parameters

- `$index` (*string|int*): The forced loop index. Default is `''` (empty string), meaning no override.

## Example usage

```php
add_filter( 'bricks/query/force_loop_index', function( $index ) {
    // Example: Force loop index to 0
    return 0;
} );
```
