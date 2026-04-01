Runs after the dynamic data `{do_action:my_hook}` tag is processed. This allows you to execute code after a specific `do_action` tag has been rendered.

## Parameters

- `$action` (*string*): The action name specified in the tag (e.g. `my_hook` in `{do_action:my_hook}`).
- `$filters` (*array*): Array of filters applied to the tag.
- `$context` (*string*): The context in which the tag is being rendered (e.g., 'text').
- `$post` (*WP_Post|null*): The current post object, or null.
- `$value` (*string*): The rendered output of the action (captured via output buffering).

## Example usage

```php
add_action( 'bricks/dynamic_data/after_do_action', function( $action, $filters, $context, $post, $value ) {
    if ( $action === 'my_custom_hook' ) {
        // Code to run after 'my_custom_hook' is processed via dynamic data
        error_log( 'Finished processing my_custom_hook' );
    }
}, 10, 5 );
```
