Allows you to modify the timeout duration (in seconds) for webhook requests triggered by the Form element.

## Parameters

- `$timeout` (int): The timeout duration in seconds. Default is `15`.

## Example usage

```php
add_filter( 'bricks/webhook/timeout', function( $timeout ) {
    // Increase timeout to 30 seconds
    return 30;
} );
```
