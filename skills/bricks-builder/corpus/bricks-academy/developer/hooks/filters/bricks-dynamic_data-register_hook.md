---
title: "Filter: bricks/dynamic_data/register_hook"
description: "Filters the WordPress action hook used to register Bricks dynamic data providers and tags."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-register_hook/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-register_hook.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the WordPress action hook used to register Bricks dynamic data providers and tags.

## Parameters

- `$hook` (*string*): The action hook name. Defaults to `init`.

## Example usage

```php
add_filter( 'bricks/dynamic_data/register_hook', function( $hook ) {
    // Register dynamic data on 'wp_loaded' instead of 'init'
    return 'wp_loaded';
} );
```
