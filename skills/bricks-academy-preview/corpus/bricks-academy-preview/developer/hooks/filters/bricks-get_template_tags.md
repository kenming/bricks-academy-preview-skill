Filters the list of template tags displayed in the Bricks template manager. Template tags are a custom taxonomy used to organize templates.

## Parameters

- `$tags` (*array*): Associative array of template tags, where the key is the term slug and the value is the term name.

## Example usage

```php
add_filter( 'bricks/get_template_tags', function( $tags ) {
    // Example: Remove the 'dark' tag from the list
    if ( isset( $tags['dark'] ) ) {
        unset( $tags['dark'] );
    }

    return $tags;
} );
```
