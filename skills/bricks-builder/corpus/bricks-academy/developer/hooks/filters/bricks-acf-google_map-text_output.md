---
title: "Filter: bricks/acf/google_map/text_output"
description: "Filters the final HTML output of the ACF Google Map field dynamic data. This runs after the address parts or coordinates have been formatted."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-acf-google_map-text_output/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-acf-google_map-text_output.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the final HTML output of the ACF Google Map field dynamic data. This runs after the address parts or coordinates have been formatted.

## Parameters

- `$output` (*string*): The rendered HTML output string.
- `$value` (*array*): The raw value of the ACF Google Map field.
- `$field` (*array*): The ACF field settings.

## Example usage

```php
add_filter( 'bricks/acf/google_map/text_output', function( $output, $value, $field ) {
    // Example: Strip HTML tags to get plain text
    return wp_strip_all_tags( $output );
}, 10, 3 );
```
