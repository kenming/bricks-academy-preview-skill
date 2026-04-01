Filters the HTML tag used to wrap the comment author's name in the comments list.

## Parameters

- `$tag` (*string*): The HTML tag name. Defaults to `h5`.

## Example usage

```php
add_filter( 'bricks/comments/author_tag', function( $tag ) {
    // Change author name tag to 'span'
    return 'span';
} );
```
