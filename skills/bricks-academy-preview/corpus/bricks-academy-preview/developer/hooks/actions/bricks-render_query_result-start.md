Runs at the start of the AJAX query result rendering process (`query_result` endpoint - used for filters, live search, etc.). This action allows you to execute custom logic before the query result content is generated.

## Parameters

- `$request_data` (*array*): The request data parameters (e.g., queryElementId, postId, filters, etc.).

## Example usage

```php
add_action( 'bricks/render_query_result/start', function( $request_data ) {
    // Access request data
    // $filters = $request_data['filters'] ?? [];
    
    // Example: Switch language for multilingual plugins
    // if ( isset( $request_data['lang'] ) ) {
    //     // Switch language logic
    // }
} );
```
