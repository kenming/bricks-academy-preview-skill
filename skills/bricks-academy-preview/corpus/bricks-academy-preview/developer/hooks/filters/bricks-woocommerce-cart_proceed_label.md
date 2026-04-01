Allows you to modify the text of the "Proceed to checkout" button in the WooCommerce Cart element.

## Parameters

- `$label` (string): The button text. Default is "Proceed to checkout".

## Example usage

```php
add_filter( 'bricks/woocommerce/cart_proceed_label', function( $label ) {
    return 'Go to Checkout';
} );
```
