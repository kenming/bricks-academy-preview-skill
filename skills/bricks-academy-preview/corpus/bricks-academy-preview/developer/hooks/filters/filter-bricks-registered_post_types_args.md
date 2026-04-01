Available since version 1.6, this filter allows you to customise the post type args that are used to query the post type as shown in the Bricks settings & the builder (e.g. Query control post types, etc.)

```php
add_filter( 'bricks/registered_post_types_args', function( $args ) {
  // Default: Return only public post types
  // $args['public'] = true;

  // Custom: Return all registered post types
  unset( $args['public'] );

  // Available arguments: https://developer.wordpress.org/reference/functions/get_post_types/#comment-2184
  return $args;
} );
```
