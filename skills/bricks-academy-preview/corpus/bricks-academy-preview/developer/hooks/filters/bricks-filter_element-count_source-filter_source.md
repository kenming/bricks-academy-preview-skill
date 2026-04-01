Filters the count data for a specific filter source. The `{$filter_source}` portion of the hook name should be replaced with the actual source name (e.g., `taxonomy`, `custom_field`, `wcField`).

## Parameters

- `$count_source` (*array*): Associative array where keys are filter values and values are their respective counts.
- `$element` (*object*): The filter element instance.

## Example usage

```php
// Filter counts for a custom field filter source
add_filter( 'bricks/filter_element/count_source_custom_field', function( $count_source, $element ) {
    // Example: Override the count for a specific value
    if ( isset( $count_source['featured'] ) ) {
        $count_source['featured'] = 999;
    }

    return $count_source;
}, 10, 2 );
```
