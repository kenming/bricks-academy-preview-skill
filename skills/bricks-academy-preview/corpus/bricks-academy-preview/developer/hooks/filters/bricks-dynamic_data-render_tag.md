Filters the logic to resolve a single dynamic data tag to its value. This filter is called for each individual tag found in the content.

## Parameters

- `$tag` (*string*): The dynamic data tag string (without curly braces, e.g., `post_title:fallback`).
- `$post` (*WP_Post*): The post context.
- `$context` (*string*): The context where the tag is being rendered.

## Example usage

```php
add_filter( 'bricks/dynamic_data/render_tag', function( $tag, $post, $context ) {
    // Implement a custom tag '{my_custom_tag}'
    if ( $tag === 'my_custom_tag' ) {
        return 'My Custom Value';
    }

    return $tag; // Return original tag to let other providers handle it
}, 10, 3 );
```
