---
title: "Filter: bricks/dynamic_data/allowed_keys"
description: "Filter which argument keys Bricks accepts inside dynamic data tags, so you can support custom modifiers and parsing behavior."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-allowed_keys/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-dynamic_data-allowed_keys.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the allowed argument keys (modifiers) that can be parsed in dynamic data tags (e.g., `{post_title:my_key}`). This allows you to introduce custom arguments for your dynamic tags.

## Parameters

- `$allowed_keys` (*array*): Array of allowed argument keys. Defaults include `fallback`, `fallback-image`, `sanitize`, `exclude`, `start-at`, `pad`, `key`, `is-array`, `date`, `from`, `to`.

## Example usage

```php
add_filter( 'bricks/dynamic_data/allowed_keys', function( $allowed_keys ) {
    // Add 'limit' as an allowed argument key
    $allowed_keys[] = 'limit';

    return $allowed_keys;
} );
```
