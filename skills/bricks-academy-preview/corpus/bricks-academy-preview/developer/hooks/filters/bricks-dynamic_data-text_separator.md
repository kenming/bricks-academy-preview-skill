Filters the separator used when joining array values in a dynamic data tag (text context). The default separator is a comma and a space (`, `).

## Parameters

- `$sep` (*string*): The separator string.
- `$tag` (*string*): The dynamic data tag.
- `$post_id` (*int*): The ID of the post context.
- `$filters` (*array*): Array of modifiers applied to the tag.

## Example usage

```php
add_filter( 'bricks/dynamic_data/text_separator', function( $sep, $tag, $post_id, $filters ) {
    // Example: Use a line break separator for a specific custom field
    if ( $tag === 'my_repeater_field' ) {
        return '<br>';
    }

    return $sep;
}, 10, 4 );
```
