When using the Bricks Post Comments element, the comment default timestamp text will show the time difference since it was published in a human-readable format such as "1 hour ago" or "2 days ago".

Since Bricks 1.5.1, you'll be able to customize the comment timestamp text, like so:

```php
add_filter( 'bricks/comments/timestamp', function( $timestamp, $comment ) {
  // Return the WordPress default comment timestamp
  return sprintf( __( '%1$s at %2$s' ),
    get_comment_date( '', $comment ),
    get_comment_time()
  );
}, 10, 2 );
```
