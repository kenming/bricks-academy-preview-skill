The `bricks/builder/image_sizes` hook gives developers the ability to customize image size options in the builder.

By default, when working within a query loop and using dynamic data for image sources, Bricks Builder displays all the registered WordPress image sizes.

This hook allows you to modify this list if you know that certain sizes are not being used, helping you streamline your image size options to fit your needs.

```php
/**
 * $image_sizes Multidimensional array (key: image size name)
 */
add_filter( 'bricks/builder/image_size_options', function( $image_sizes ) {
  // Unset thumbnail, 1536x1536, 2048x2048
  unset( $image_sizes['thumbnail'] );
  unset( $image_sizes['1536x1536'] );
  unset( $image_sizes['2048x2048'] );

  return $image_sizes;
});
```
