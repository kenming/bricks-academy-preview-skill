---
title: "Filter: bricks/woocommerce/ajax_render_post_id"
description: "Filters the post ID used for WooCommerce AJAX rendering."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-ajax_render_post_id/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-ajax_render_post_id.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
Filters the post ID Bricks uses as context for WooCommerce AJAX rendering.

## Parameters

- `$post_id` (int): The post ID Bricks resolved for the WooCommerce page.
- `$wc_page` (string): The WooCommerce page context being rendered.

## Example usage

```php
add_filter( 'bricks/woocommerce/ajax_render_post_id', function( $post_id, $wc_page ) {
    return $post_id;
}, 10, 2 );
```
