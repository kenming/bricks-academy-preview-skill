---
title: "Filter: bricks/filter_element/datepicker_date_format"
description: "Filters the PHP date format string used by the Filter: Datepicker element. This determines how dates are parsed and formatted for comparison with the database."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-datepicker_date_format/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-datepicker_date_format.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Filters the PHP date format string used by the Filter: Datepicker element. This determines how dates are parsed and formatted for comparison with the database values.

## Parameters

- `$date_format` (*string*): The PHP date format string (e.g., `Y-m-d`, `d/m/Y`).
- `$provider` (*string*): The data provider (e.g., `acf`, `metabox`, `pods`, `jetengine`).
- `$element` (*object*): The filter element instance.

## Example usage

```php
add_filter( 'bricks/filter_element/datepicker_date_format', function( $date_format, $provider, $element ) {
    // Example: Use a specific format for ACF date fields
    if ( $provider === 'acf' ) {
        return 'Ymd'; // ACF often stores dates as Ymd
    }

    return $date_format;
}, 10, 3 );
```
