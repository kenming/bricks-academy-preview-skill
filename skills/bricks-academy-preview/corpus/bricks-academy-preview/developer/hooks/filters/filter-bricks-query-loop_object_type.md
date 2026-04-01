Bricks will use `\Bricks\Query::get_loop_object_type()` to retrieve the looping iteration's object type. This static function is used in many places. It plays an important role in many conditions. The possible return object_type should be 'post', 'term', or 'user' only.

```php
// This is the example when Bricks set the object_type in woo cart query, so inside each iteration, it will be treat as a post/product object_type
add_filter( 'bricks/query/loop_object_type', function( $object_type, $object, $query_id ) {
    $query_object_type = \Bricks\Query::get_query_object_type( $query_id );

    if ( $query_object_type !== 'wooCart' ) {
	return $object_type;
    }

    return 'post';
}, 10, 3 );
```
