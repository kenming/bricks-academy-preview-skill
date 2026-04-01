Determine which elements to use in Bricks by out-commenting the ones you don't want to use. There is a full example and list of all elements in the Bricks child theme that you can customize to your requirements.

```php
add_filter( 'bricks/builder/elements', function( $elements ) {
  // See Bricks child theme for a full list of all available elements
  // var_dump( $elements ); // To see all available elements

  return $elements;
} );
```
