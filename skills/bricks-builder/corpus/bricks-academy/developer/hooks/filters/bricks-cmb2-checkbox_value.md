---
title: "Filter: bricks/cmb2/checkbox_value"
description: "Filters the output value of a CMB2 checkbox field when rendered via Bricks dynamic data. By default, Bricks converts 'on' to \"Yes\" and other values to \"No\"."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-cmb2-checkbox_value/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-cmb2-checkbox_value.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the output value of a CMB2 checkbox field when rendered via Bricks dynamic data. By default, Bricks converts 'on' to "Yes" and other values to "No".

## Parameters

- `$value` (*string*): The processed value (e.g., "Yes" or "No").
- `$original_value` (*string*): The raw value from the database (e.g., 'on').
- `$field` (*array*): The CMB2 field settings array.
- `$post` (*WP_Post*): The current post object.

## Example usage

```php
add_filter( 'bricks/cmb2/checkbox_value', function( $value, $original_value, $field, $post ) {
    // Example: Return "True" or "False" instead of "Yes" or "No"
    return $original_value === 'on' ? 'True' : 'False';
}, 10, 4 );
```
