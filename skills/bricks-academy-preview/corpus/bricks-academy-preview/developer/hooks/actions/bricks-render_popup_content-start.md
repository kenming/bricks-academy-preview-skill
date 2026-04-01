Runs at the start of the AJAX popup content rendering process (`load_popup_content` endpoint). This action allows you to execute custom logic before the popup content is generated and returned.

## Parameters

- `$request_data` (*array*): The request data parameters (e.g., postId, popupId, etc.).

## Example usage

```php
add_action( 'bricks/render_popup_content/start', function( $request_data ) {
    // Access request data
    // $post_id = $request_data['postId'] ?? 0;
    
    // Example: Switch language for multilingual plugins (Polylang/WPML integration uses this)
    // if ( isset( $request_data['lang'] ) ) {
    //     // Switch language logic
    // }
} );
```
