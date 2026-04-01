Programmatically add HTML attributes to the `header` tag.

```php
add_filter( 'bricks/header/attributes', function( $attributes ) {
  // Add custom class to header
  if ( isset( $attributes['class'] ) && is_array( $attributes['class'] ) ) {
    $attributes['class'][] = 'my-header-class';
  } else {
    $attributes['class'] = ['my-header-class'];
  }

  // Add 'data-is-header' HTML attribute to header with value 'y'
  $attributes['data-is-header'] = 'y';

  return $attributes;
} );
```

- [/developer/hooks/filters/filter-bricks-content-attributes/](/developer/hooks/filters/filter-bricks-content-attributes/)
- [/developer/hooks/filters/filter-bricks-footer-attributes/](/developer/hooks/filters/filter-bricks-footer-attributes/)
