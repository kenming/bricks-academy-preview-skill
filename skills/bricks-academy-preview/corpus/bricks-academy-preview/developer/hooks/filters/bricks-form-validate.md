Filters the validation errors for a form submission. This allows you to implement custom validation logic (e.g., checking if an email is from a specific domain, or if a field value meets certain criteria).

## Parameters

- `$errors` (*array*): Array of validation error messages.
- `$form` (*object*): The Form integration instance.

## Example usage

```php
add_filter( 'bricks/form/validate', function( $errors, $form ) {
    $form_id = $form->get_element_id();
    $fields  = $form->get_fields();

    // Example: Only validate a specific form
    if ( $form_id === 'my_form_id' ) {
        // Check if email domain is allowed
        $email_field_id = 'form-field-email';
        if ( isset( $fields[ $email_field_id ] ) ) {
            $email = $fields[ $email_field_id ];
            if ( strpos( $email, '@example.com' ) === false ) {
                $errors[] = esc_html__( 'Please use an @example.com email address.', 'my-domain' );
            }
        }
    }

    return $errors;
}, 10, 2 );
```
