Runs before the Bricks content is rendered on a WooCommerce product archive page when a Bricks template is used. This action is specific to WooCommerce archives rendered by Bricks.

## Parameters

- `$bricks_data` (_array_): The Bricks data for the template being rendered.
- `$post_id` (_int_): The ID of the post/archive being rendered.

## Example usage

```php
add_action( 'bricks/archive_product/before', function( $bricks_data, $post_id ) {
    // Output custom content before the product archive
    echo '<div class="custom-archive-header">Welcome to our shop</div>';
} );
```
