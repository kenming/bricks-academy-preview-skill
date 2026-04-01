Filters the element settings before they are converted into query variables. This runs early in the query setup process, allowing you to modify the raw query settings of an element.

## Parameters

- `$settings` (*array*): The element settings array. The query settings are typically located in `$settings['query']`.
- `$element_id` (*string*): The ID of the element being queried.

## Example usage

```php
add_filter( 'bricks/query/prepare_query_vars_from_settings', function( $settings, $element_id ) {
    // Example: Force a specific post type for a query element with ID 'my_query_element'
    if ( $element_id === 'my_query_element' ) {
        $settings['query']['post_type'] = 'my_custom_post_type';
    }

    return $settings;
}, 10, 2 );
```
