---
title: "Filter: bricks/element/settings"
description: "Bricks 1.5 adds the possibility to change the element settings before it is rendered."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-element-settings/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-element-settings.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Bricks 1.5 adds the possibility to change the element settings before it is rendered.

This allows you to change a text element content programmatically, or add styles based on a custom conditional logic, like so:

```php
add_filter( 'bricks/element/settings', function( $settings, $element ) {
    // Add "[online]" text to all the headings elements if the visitor is logged in
    if ( $element->name === 'heading' && is_user_logged_in() ) {
        $settings['text'] .= ' [online]';
    }

    return $settings;
}, 10, 2 );
```

In case you need to programmatically add an element conditional display logic, check the filter [`bricks/element/render`](/developer/hooks/filters/filter-bricks-element-render/).



##### Example: Dynamically set WooCommerce Product Filter (Price) max price from all products

![](imgs/bricks-products-filter-max-price-from-all-products-b2ee4f6128.png)

```php
add_filter('bricks/element/settings', function( $settings, $element ) {
  // Change the zyjhwa to your element ID
  if( $element->id !== 'zyjhwa' || ! isset( $settings['filters'] ) ) {
    return $settings;
  }

  // Get all products
  $products = wc_get_products(array(
    'status' => 'publish',
    'limit' => -1, // Retrieve all products
  ));

  $highest_price = max(array_map(function ($product) {
    return $product->get_price();
  }, $products));

  foreach( $settings['filters'] as $key => $filter ) {
    if( ! isset( $filter['otherFilter'] ) || $filter['otherFilter'] !== 'price' ) {
      continue;
    }

    $settings['filters'][$key]['sliderMax'] = $highest_price;
  }

  return $settings;
}, 10, 2);
```
