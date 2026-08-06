---
title: "Filter: bricks/get_template_bundles"
description: "Filters the list of template bundles displayed in the Bricks template manager. Template bundles are a custom taxonomy used to categorize templates."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_template_bundles/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-get_template_bundles.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the list of template bundles displayed in the Bricks template manager. Template bundles are a custom taxonomy used to categorize templates.

## Parameters

- `$bundles` (*array*): Associative array of template bundles, where the key is the term slug and the value is the term name.

## Example usage

```php
add_filter( 'bricks/get_template_bundles', function( $bundles ) {
    // Example: Rename a specific bundle
    if ( isset( $bundles['my-bundle'] ) ) {
        $bundles['my-bundle'] = 'My Renamed Bundle';
    }

    return $bundles;
} );
```
