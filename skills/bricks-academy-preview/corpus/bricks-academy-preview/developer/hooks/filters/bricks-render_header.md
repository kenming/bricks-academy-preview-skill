Filters the rendered HTML of the Bricks header template. This allows you to wrap the header in custom markup or modify its output before it is echoed to the page.

## Parameters

- `$header_html` (*string*): The rendered HTML of the header.

## Example usage

```php
add_filter( 'bricks/render_header', function( $header_html ) {
    // Example: Add a notification bar before the header
    $notification = '<div class="notification-bar">Welcome!</div>';
    
    return $notification . $header_html;
} );
```
