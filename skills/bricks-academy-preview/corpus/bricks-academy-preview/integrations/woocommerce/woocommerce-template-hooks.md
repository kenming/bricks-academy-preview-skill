Bricks 1.7 introduces a new [`do_action`](/builder/dynamic-content/dynamic-data/#do_action) dynamic tag, which is designed to address the majority of compatibility issues between Bricks and third-party WooCommerce plugins. This new dynamic tag not only solves these compatibility issues but also enhances the flexibility of design by allowing users to place hooks anywhere they desire.

This article will guide you through the templates that need to be updated with the new `do_action` dynamic tag, though this step is optional if your Bricks-built WooCommerce website is already functioning properly.



Please note that when using the `do_action` dynamic tag with the specified hooks, Bricks will automatically remove certain native WooCommerce actions to prevent duplicate content.



As an example, consider using `{do_action:woocommerce_after_shop_loop_item_title}` dynamic tag in Bricks. This tag will automatically remove the `woocommerce_template_loop_rating` and `woocommerce_template_loop_price` actions. The reason for this is because the Product price and Product rating elements will be used to output the information in the desired location. At the same time, other plugins or codes will still be able to successfully hook onto the dynamic tag.



#### WooCommerce actions list removed by Bricks when using the do_action tag {#woo-special-actions-list}

| Hook | Actions removed by Bricks, Priority |
| --- | --- |
| woocommerce_before_shop_loop_item | woocommerce_template_loop_product_link_open, 10 |
| woocommerce_before_shop_loop_item_title | woocommerce_show_product_loop_sale_flash, 10
woocommerce_template_loop_product_thumbnail, 10 |
| woocommerce_shop_loop_item_title | woocommerce_template_loop_product_title,10 |
| woocommerce_after_shop_loop_item_title | woocommerce_template_loop_rating, 5
woocommerce_template_loop_price, 10 |
| woocommerce_after_shop_loop_item | woocommerce_template_loop_product_link_close, 5
woocommerce_template_loop_add_to_cart, 10 |
| woocommerce_before_single_product_summary | woocommerce_show_product_sale_flash, 10
woocommerce_show_product_images, 20 |
| woocommerce_single_product_summary | woocommerce_template_single_title, 5
woocommerce_template_single_rating, 10
woocommerce_template_single_price, 10
woocommerce_template_single_excerpt, 20
woocommerce_template_single_add_to_cart, 30
woocommerce_template_single_meta, 40
woocommerce_template_single_sharing, 50 |
| woocommerce_after_single_product_summary | woocommerce_output_product_data_tabs, 10
woocommerce_upsell_display, 15
woocommerce_output_related_products, 20 |
| woocommerce_before_main_content | woocommerce_output_content_wrapper,10
woocommerce_breadcrumb, 20 |
| woocommerce_archive_description | woocommerce_taxonomy_archive_description, 10
woocommerce_product_archive_description, 10 |
| woocommerce_before_shop_loop | woocommerce_result_count, 20
woocommerce_catalog_ordering, 30 |
| woocommerce_after_shop_loop | woocommerce_pagination, 10 |
| woocommerce_after_main_content | woocommerce_output_content_wrapper_end, 10 |
| woocommerce_cart_is_empty | wc_empty_cart_message, 10 |



:::note
Simply use a Basic Text element when applying the `{do_action:xxx}` dynamic tag within your template.
:::



## WooCommerce Single Product Template Hooks {#single-product-template-hooks}

For the WooCommerce Single Product template, the following hooks are recommended to be used with the `do_action` dynamic tag:

- `{do_action:woocommerce_before_single_product}` - Important (WooCommerce notice)
- `{do_action:woocommerce_before_single_product_summary}`
- `{do_action:woocommerce_single_product_summary}` - Important (Many third-party plugins using this hook to inject their code)
- `{do_action:woocommerce_after_single_product_summary}`
- `{do_action:woocommerce_after_single_product}`

Best to place all of these in your single product template if you are not sure which hook will be using by the third-party plugins.



![](imgs/bricks-standard-woocommerce-single-product-template-hooks-d63ef55cc9.png)

<figcaption>

Single product template hooks location

</figcaption>



## WooCommerce Product Archive Template Hooks {#product-archive-template-hooks}

For the WooCommerce Product Archive template, the following hooks are recommended to be used with the `do_action` dynamic tag:

- `{do_action:woocommerce_archive_description}`
- `{do_action:woocommerce_before_shop_loop}` - Important (WooCommerce notice)
- `{do_action:woocommerce_before_shop_loop_item}`
- `{do_action:woocommerce_before_shop_loop_item_title}`
- `{do_action:woocommerce_shop_loop_item_title}`
- `{do_action:woocommerce_after_shop_loop_item_title}`
- `{do_action:woocommerce_after_shop_loop_item}`
- `{do_action:woocommerce_after_shop_loop}`



![](imgs/bricks-standard-woocommerce-product-archive-template-hooks-0224c0d9e2.png)

<figcaption>

Product archive template hooks location (Custom Query Loop)

</figcaption>



In Bricks 1.7, the dynamic tag `do_action` hooks will be automatically included in the fields of the Products element (for newly inserted Products elements only).



![](imgs/Products-element-with-do_action-included-since-1_6_3-680f992a58.png)

<figcaption>

Default Products element with do_action hooks (Bricks 1.7+)

</figcaption>



## WooCommerce Empty Cart Template Hooks {#empty-cart-template-hooks}

For the WooCommerce Empty Cart template, the following hook is recommended to be used with the `do_action` dynamic tag:

- `{do_action:woocommerce_cart_is_empty}` - Important (WooCommerce notice)



![](imgs/bricks-standard-woocommerce-empty-cart-template-hooks-a04efc4fc9.png)

<figcaption>

Empty cart template hook location

</figcaption>



## WooCommerce Cart Template Hooks {#cart-template-hooks}

For the WooCommerce Cart template, the following hooks are recommended to be used with the `do_action` dynamic tag:

- `{do_action:woocommerce_before_cart}` - Important (WooCommerce notice)
- `{do_action:woocommerce_before_cart_collaterals}`
- `{do_action:woocommerce_after_cart}`



![](imgs/bricks-standard-woocommerce-cart-template-hooks-34955c9d90.png)

<figcaption>

Cart template hooks location

</figcaption>



## WooCommerce Pay Template {#pay-template-hooks}

For the WooCommerce Pay template, the following hooks are recommended to be used with the `do_action` dynamic tag:

- `{do_action:woocommerce_pay_order_before_payment}`



![](imgs/woo-pay-template-830e9211f3.png)

<figcaption>

Pay template hooks location

</figcaption>



By following this guide, you can ensure that the templates created in Bricks are fully compatible with WooCommerce and that all necessary actions and details are displayed as intended.
