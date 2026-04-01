If you are creating a custom query loop or a custom plugin, you might want to perform some additional tasks like setting/resetting specific data before the loop runs. (`@since 1.7.2`)

```php
// Perform certain action before the loop of query element oklvcq
add_action( 'bricks/query/before_loop', function( $query, $args ) {
  if ( $query->element_id !== 'oklvcq' ) {
    return;
  }
  // $args is an array of the element settings
  // Perform your own logic here

}, 10, 2 );
```
