Filters the result returned when a honeypot field is triggered (spam detection). This allows you to customize the error message shown to potential bots (or users who accidentally filled the hidden field).

## Parameters

- `$result` (*array*): The result array, typically containing `['type' => 'error', 'message' => '...']`.
- `$field_id` (*string*): The ID of the honeypot field that was filled.
- `$form` (*object*): The Form integration object.

## Example usage

```php
add_filter( 'bricks/element/form/honeypot/result', function( $result, $field_id, $form ) {
    // Customize the error message
    $result['message'] = esc_html__( 'Spam detected. Please do not fill out the hidden fields.', 'my-domain' );

    return $result;
}, 10, 3 );
```
