---
title: "Filter: bricks/get_terms_options/enable_limit"
description: "Enables a limit on the number of taxonomies queried when fetching terms for builder controls. This is useful for sites with a very large number of taxonomies to."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_terms_options-enable_limit/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_terms_options-enable_limit.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Enables a limit on the number of taxonomies queried when fetching terms for builder controls. This is useful for sites with a very large number of taxonomies to prevent memory exhaustion.

## Parameters

- `$enable_limit` (*bool*): Whether to limit the number of queried taxonomies. Default is `false`.

## Example usage

```php
add_filter( 'bricks/get_terms_options/enable_limit', function( $enable_limit ) {
    // Enable the limit to improve performance on sites with many taxonomies
    return true;
} );
```
