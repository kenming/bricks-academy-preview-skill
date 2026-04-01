Runs at the start of the AJAX query page rendering process (`load_query_page` endpoint - used for infinite scroll/pagination). This action allows you to execute custom logic before the query page content is generated.

## Parameters

- `$request_data` (*array*): The request data parameters (e.g., queryElementId, postId, page, queryVars, etc.).

## Example usage

```php
add_action( 'bricks/render_query_page/start', function( $request_data ) {
    // Access request data
    // $page = $request_data['page'] ?? 1;
    
    // Example: Switch language for multilingual plugins
    // if ( isset( $request_data['lang'] ) ) {
    //     // Switch language logic
    // }
} );
```
