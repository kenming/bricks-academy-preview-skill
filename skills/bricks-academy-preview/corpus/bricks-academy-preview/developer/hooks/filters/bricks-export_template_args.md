Filters the URL arguments used for the "Export Template" link in the Bricks templates list table.

## Parameters

- `$args` (*array*): Array of query arguments for the export URL (e.g., `action`, `nonce`, `templateId`).
- `$post_id` (*int*): The ID of the template being exported.

## Example usage

```php
add_filter( 'bricks/export_template_args', function( $args, $post_id ) {
    // Example: Add a custom parameter to the export URL
    $args['my_param'] = 'value';

    return $args;
}, 10, 2 );
```
