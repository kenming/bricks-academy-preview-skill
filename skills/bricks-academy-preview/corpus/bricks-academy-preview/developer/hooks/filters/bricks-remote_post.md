Filters the arguments passed to `wp_remote_post()` when Bricks performs a remote POST request (e.g., verifying license, submitting form data to webhook).

## Parameters

- `$args` (*array*): Array of arguments for `wp_remote_post()` (e.g., `body`, `timeout`, `sslverify`).
- `$url` (*string*): The URL being requested.

## Example usage

```php
add_filter( 'bricks/remote_post', function( $args, $url ) {
    // Example: Add custom headers to webhook requests
    if ( strpos( $url, 'webhook.example.com' ) !== false ) {
        $args['headers']['X-Custom-Header'] = 'my-value';
    }

    return $args;
}, 10, 2 );
```
