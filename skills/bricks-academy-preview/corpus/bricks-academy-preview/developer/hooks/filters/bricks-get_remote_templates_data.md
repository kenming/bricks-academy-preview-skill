Filters the data retrieved from a remote template source (e.g., the Bricks Community Templates or a custom remote library). This allows you to modify, add, or remove templates before they are displayed in the template manager.

## Parameters

- `$remote_templates` (*array*): The decoded JSON response from the remote source, containing template data.

## Example usage

```php
add_filter( 'bricks/get_remote_templates_data', function( $remote_templates ) {
    // Example: Remove templates with a specific tag
    if ( ! empty( $remote_templates['templates'] ) ) {
        foreach ( $remote_templates['templates'] as $key => $template ) {
            if ( isset( $template['tags'] ) && in_array( 'deprecated', $template['tags'] ) ) {
                unset( $remote_templates['templates'][ $key ] );
            }
        }
    }

    return $remote_templates;
} );
```
