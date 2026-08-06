---
title: "Filter: bricks/dynamic_data/register_providers"
description: "Filters the dynamic data providers registered by Bricks."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-register_providers/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-register_providers.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the dynamic data providers registered by Bricks. Use it to add, remove, or reorder provider keys before Bricks registers them.

## Parameters

- `$providers` (array): Provider keys such as cmb2, wp, woo, acf, pods, metabox, toolset, and jetengine.

## Example usage

```php
add_filter( 'bricks/dynamic_data/register_providers', function( $providers ) {
    $providers[] = 'my_provider';

    return $providers;
} );
```
