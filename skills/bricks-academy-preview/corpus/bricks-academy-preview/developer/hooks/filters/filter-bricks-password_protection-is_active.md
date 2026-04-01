Use this filter to add custom rules that determine whether a [password protection template](/builder/features/password-protection/) should be active. By default, the template’s visibility is controlled by settings such as logged-in status, valid password cookies, and scheduling through the password protection template settings in the builder. This filter allows you to extend those checks, adding more dynamic criteria once the default settings have been applied.

## Example Usage:

```php
add_filter( 'bricks/password_protection/is_active', function( $is_active, $template_id, $settings ) {
    // Bypass password protection for users with the 'manage_options' capability
    if ( current_user_can( 'manage_options' ) ) {
        return false;
    }

    // Maintain default logic for other cases
    return $is_active;
}, 10, 3 );
```

In this example, any user with the `manage_options` capability (typically administrators) will bypass the password protection, while other users will follow the default settings.

**Parameters:**

- `$is_active` (bool): The initial status of whether the password protection is active.
- `$template_id` (int): The ID of the password protection template.
- `$settings` (array): The template settings.

**Return:**

- (bool): `true` to keep the template active, `false` to disable it.
