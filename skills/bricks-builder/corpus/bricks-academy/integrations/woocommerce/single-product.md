---
title: "Single Product (WooCommerce)"
description: "Build WooCommerce single product templates in Bricks and customize the main product layout, data, and related elements."
canonical: "https://academy.bricksbuilder.io/integrations/woocommerce/single-product/"
markdownUrl: "https://academy.bricksbuilder.io/integrations/woocommerce/single-product.md"
pageType: "article"
section: "integrations"
category: "woocommerce"
lastmod: "2026-08-20T13:12:40.000Z"
---
:::note
The template type "WooCommerce - Single Product" is only visible if WooCommerce is installed & active.
:::

Create a template of type "WooCommerce - Single product" in Bricks to design an individual layout for the single products page.

To create this template, go to the Bricks templates screen and add a new template. Then select the template type **"WooCommerce - Single Product"** from the top-right dropdown:

![](imgs/WooCommerce-Template-Type-Single-Product-6a104ad675.png)

Click "Publish" or "Save Draft". Then "Edit with Bricks" to open the builder.

It is also possible to create/edit this and other templates in the Bricks editor interface by clicking on the Folders icon or pressing CMD / CTRL + SHIFT + L.

:::note
Please remember to add [template hooks](/integrations/woocommerce/woocommerce-template-hooks/#single-product-template-hooks) if you are using third-party plugins.
:::

## Single Product Elements {#elements}

When editing a "Single Product" template you'll find the "Products" elements at the very top of the elements panel:

![](imgs/woocommerc-single-product-elements-379x1024-90f2db9f5d.png)

### Product title

The product title renders the title of the product.

### Product gallery

The product gallery element displays the product images defined in the product image and in the product gallery meta boxes.

*To disable the image zoom or lightbox, go to "Bricks > Settings > WooCommerce > Single Product".*

### Product short description

Renders the content of the Product short description editor.

### Product price

Renders the product price. If the product is on sale, you could hide the regular price.

### Product stock

Displays the number of products in stock. You can replace the number of products in stock with a custom message for "in", "low", or "out of stock".

### Product meta

Use the product meta element to display product data like the SKU, the product categories or tags, or any other WooCommerce metadata. Use [Dynamic Data](/builder/dynamic-content/dynamic-data/) to pull the values.

### Product rating

Shows the product's rating on a scale of 1 to 5 stars.

### Product content

Renders the product's main content as written in the WordPress editor.

### Add to cart

This element adds an "Add to cart" button to trigger the addition of this element to the cart. With this element, you may style the product variations inputs, the product stock, the quantity input, and the look & feel of the button itself.

### Related products

Shows a list of products that have the same product categories and tags of the main product displayed in the page.

### Product reviews

Renders the product reviews and review form as a standalone element. Do not use the Product reviews element together with the Product tabs element on the same page, as Product tabs can also output reviews.

### Product additional information

Renders the list of product attributes. This information will also be part of the product tabs element.

### Product tabs

Renders a section with the default tabs: Description, Additional Information, and Reviews. Other tabs might be added by third-party plugins.

### Product up/cross-sells

The product up/cross-sells element renders linked product recommendations. You can set it to show **Up-sells**, **Cross-sells**, or **Cart Cross-sells** (by default, it lists up-sell products).



![](imgs/woocommerce-product-upsells-87edfd163b.png)

<figcaption>

WooCommerce product editor screen - Linked Products

</figcaption>
