---
title: "Filter: bricks/acf/google_map/address_parts"
description: "Filters the parts of the address displayed when rendering an ACF Google Map field. You can use this to reorder or remove specific components of the address."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-acf-google_map-address_parts/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-acf-google_map-address_parts.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the parts of the address displayed when rendering an ACF Google Map field. You can use this to reorder or remove specific components of the address.

## Parameters

- `$address_parts` (*array*): Array of address part keys. Defaults: `[ 'street_name', 'street_number', 'city', 'state', 'post_code', 'country' ]`.
- `$value` (*array*): The raw value of the ACF Google Map field.
- `$field` (*array*): The ACF field settings.

## Example usage

```php
add_filter( 'bricks/acf/google_map/address_parts', function( $address_parts, $value, $field ) {
    // Example: Only show city and country, and change order
    return [ 'city', 'country' ];
}, 10, 3 );
```
