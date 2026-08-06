---
title: "Filter: bricks/filter_element/datepicker_db_date_format"
description: "Filters the database date format used by a Datepicker filter element."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-datepicker_db_date_format/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-filter_element-datepicker_db_date_format.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the database date format used by a Datepicker filter element. This is intended for custom field providers that store dates in a different format.

## Parameters

- `$db_format` (string): The database date format Bricks will use.
- `$provider` (string): The active custom field provider.
- `$element` (object): The Datepicker filter element instance.

## Example usage

```php
add_filter( 'bricks/filter_element/datepicker_db_date_format', function( $db_format, $provider, $element ) {
    if ( $provider === 'my_provider' ) {
        return 'Ymd';
    }

    return $db_format;
}, 10, 3 );
```
