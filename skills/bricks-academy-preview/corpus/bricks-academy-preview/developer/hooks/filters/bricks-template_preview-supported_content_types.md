Filters the list of content types available for selection in the "Populate Content" (Template Preview) setting. This allows you to add custom preview contexts.

## Parameters

- `$types` (*array*): Associative array where keys are the content type IDs and values are their labels.

## Example usage

```php
add_filter( 'bricks/template_preview/supported_content_types', function( $types ) {
    // Example: Add a custom preview type
    $types['my_custom_preview'] = esc_html__( 'My Custom Preview', 'my-plugin' );

    return $types;
} );
```
