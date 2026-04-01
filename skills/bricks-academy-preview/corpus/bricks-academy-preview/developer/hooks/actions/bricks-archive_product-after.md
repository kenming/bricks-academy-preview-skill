Runs after the Bricks content is rendered on a WooCommerce product archive page when a Bricks template is used. This action is specific to WooCommerce archives rendered by Bricks.

## Parameters

- `$bricks_data` (*array*): The Bricks data for the template being rendered.
- `$post_id` (*int*): The ID of the post/archive being rendered.

## Example usage

```php
add_action( 'bricks/archive_product/after', function( $bricks_data, $post_id ) {
    // Output custom content after the product archive
    echo '<div class="custom-archive-footer">End of product list</div>';
} );
```
