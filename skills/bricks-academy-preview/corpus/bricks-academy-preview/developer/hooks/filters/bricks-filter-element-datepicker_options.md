Filters the Flatpickr options used by the Filter: Datepicker element. This allows you to customize the behavior of the date picker within query filters.

## Parameters

- `$datepicker_options` (*array*): Array of Flatpickr options.
- `$element` (*object*): The Filter: Datepicker element instance.

## Example usage

```php
add_filter( 'bricks/filter-element/datepicker_options', function( $datepicker_options, $element ) {
    // Example: Change the date format
    $datepicker_options['dateFormat'] = 'Y-m-d';

    // Example: Disable specific dates
    $datepicker_options['disable'] = [ '2023-12-25', '2024-01-01' ];

    return $datepicker_options;
}, 10, 2 );
```
