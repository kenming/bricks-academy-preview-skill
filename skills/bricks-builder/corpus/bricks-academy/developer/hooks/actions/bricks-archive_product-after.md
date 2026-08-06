---
title: "Action: bricks/archive_product/after"
description: "Runs after the Bricks content is rendered on a WooCommerce product archive page when a Bricks template is used. This action is specific to WooCommerce archives."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-archive_product-after/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-archive_product-after.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
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
