---
title: "Filter: bricks/filter_element/data_source_wcField"
description: "Filters the data source (options) specifically for WooCommerce field filters. This allows you to customize the options displayed for WooCommerce filters like."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-data_source_wcfield/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-data_source_wcfield.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the data source (options) specifically for WooCommerce field filters. This allows you to customize the options displayed for WooCommerce filters like product visibility, stock status, etc.

## Parameters

- `$data_source` (*array*): Array of filter options.
- `$element` (*object*): The filter element instance.

## Example usage

```php
add_filter( 'bricks/filter_element/data_source_wcField', function( $data_source, $element ) {
    // Example: Add a custom option to a WooCommerce filter
    // Note: You might need to check $element->settings to target specific WC fields
    if ( isset( $element->settings['sourceFieldType'] ) && $element->settings['sourceFieldType'] === 'stock_status' ) {
         // Modify stock status options
    }

    return $data_source;
}, 10, 2 );
```
