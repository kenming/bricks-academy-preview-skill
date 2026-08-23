---
title: "Filter: bricks/acf/filter_field_groups"
description: "Filters the ACF field groups available in the Bricks dynamic data picker. This allows you to exclude specific field groups from appearing in the builder's."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-acf-filter_field_groups/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-acf-filter_field_groups.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the ACF field groups available in the Bricks dynamic data picker. This allows you to exclude specific field groups from appearing in the builder's dynamic data dropdown.

## Parameters

- `$groups` (*array*): Array of ACF field groups retrieved via `acf_get_field_groups()`.

## Example usage

```php
add_filter( 'bricks/acf/filter_field_groups', function( $groups ) {
    // Loop through groups and unset the one you want to hide
    foreach ( $groups as $key => $group ) {
        // Example: Hide field group with key 'group_60f1234567890'
        if ( $group['key'] === 'group_60f1234567890' ) {
            unset( $groups[ $key ] );
        }
    }

    return $groups;
} );
```
