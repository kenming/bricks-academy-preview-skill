---
title: "Filter: bricks/builder/state_group_definitions"
description: "Filters builder state group definitions used for WooCommerce modular element preview states."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-state_group_definitions/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-builder-state_group_definitions.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the builder state group definitions returned by `Woocommerce::get_builder_state_group_definitions()`.

Bricks sends these definitions to the builder as `stateGroupDefinitions`. The default definitions are currently for WooCommerce modular element states such as cart, checkout, and account page preview states.

## Parameters

- `$definitions` (array): State group definitions keyed by element name.

## Example usage

```php
add_filter( 'bricks/builder/state_group_definitions', function( $definitions ) {
    $definitions['my-group'] = [
        'label'  => 'My group',
        'states' => [],
    ];

    return $definitions;
} );
```
