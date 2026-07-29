---
title: "Filter: bricks/woo_setup_wizard/register_presets"
description: "Filters Woo setup wizard presets."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woo_setup_wizard-register_presets/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woo_setup_wizard-register_presets.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters Woo setup wizard presets before Bricks registers them. Use it to add or override one-click setup JSON presets.

## Parameters

- `$presets` (array): Preset data grouped by area and preset ID.

## Example usage

```php
add_filter( 'bricks/woo_setup_wizard/register_presets', function( $presets ) {
    $presets['checkout']['my-preset'] = [
        'label' => 'My checkout preset',
    ];

    return $presets;
} );
```
