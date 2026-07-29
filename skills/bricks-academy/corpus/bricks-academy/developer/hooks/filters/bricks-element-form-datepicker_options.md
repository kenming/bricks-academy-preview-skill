---
title: "Filter: bricks/element/form/datepicker_options"
description: "Filters the Flatpickr options for the datepicker field in the Form element. This allows you to customize the behavior of the date picker (e.g., disable specific."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-element-form-datepicker_options/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-element-form-datepicker_options.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
Filters the Flatpickr options for the datepicker field in the Form element. This allows you to customize the behavior of the date picker (e.g., disable specific dates, change the date format, set min/max dates).

## Parameters

- `$datepicker_options` (*array*): Array of Flatpickr options.
- `$element` (*object*): The Form element instance.

## Example usage

```php
add_filter( 'bricks/element/form/datepicker_options', function( $datepicker_options, $element ) {
    // Example: Disable weekends (Saturday and Sunday)
    $datepicker_options['disable'] = [
        function( $date ) {
            // Return true to disable
            return ( $date->format( 'N' ) >= 6 );
        }
    ];

    // Example: Set minDate to today
    $datepicker_options['minDate'] = 'today';

    return $datepicker_options;
}, 10, 2 );
```
