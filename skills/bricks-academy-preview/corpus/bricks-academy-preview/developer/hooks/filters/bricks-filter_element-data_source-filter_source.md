Filters the data source (options) for a specific filter source. The `{$filter_source}` portion of the hook name should be replaced with the actual source name.

## Parameters

- `$data_source` (*array*): Array of filter options. Each option should be an associative array with keys like `value`, `text`, `class`, etc.
- `$element` (*object*): The filter element instance.

## Example usage

```php
// Populate options for a custom source 'my_source'
add_filter( 'bricks/filter_element/data_source_my_source', function( $data_source, $element ) {
    $data_source[] = [
        'value' => 'option_1',
        'text'  => 'Option 1',
    ];

    $data_source[] = [
        'value' => 'option_2',
        'text'  => 'Option 2',
    ];

    return $data_source;
}, 10, 2 );
```
