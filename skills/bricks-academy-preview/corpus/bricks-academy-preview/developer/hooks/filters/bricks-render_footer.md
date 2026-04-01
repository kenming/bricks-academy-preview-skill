Filters the rendered HTML of the Bricks footer template. This allows you to wrap the footer in custom markup or modify its output before it is echoed to the page.

## Parameters

- `$footer_html` (*string*): The rendered HTML of the footer.

## Example usage

```php
add_filter( 'bricks/render_footer', function( $footer_html ) {
    // Example: Wrap the footer in a custom container
    return '<div class="custom-footer-wrapper">' . $footer_html . '</div>';
} );
```
