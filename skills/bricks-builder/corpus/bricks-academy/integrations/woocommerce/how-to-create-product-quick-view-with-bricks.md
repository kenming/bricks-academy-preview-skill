---
title: "How to Create Product Quick View with Bricks"
description: "Create a WooCommerce product quick view in Bricks so shoppers can preview products without leaving the current listing page."
canonical: "https://academy.bricksbuilder.io/integrations/woocommerce/how-to-create-product-quick-view-with-bricks/"
markdownUrl: "https://academy.bricksbuilder.io/integrations/woocommerce/how-to-create-product-quick-view-with-bricks.md"
pageType: "article"
section: "integrations"
category: "woocommerce"
lastmod: "2026-08-04T12:13:33.000Z"
---
## Step 1: Design a Popup Template for Quick View

Begin by designing the popup template that will be used for the Quick View functionality. Incorporate essential elements such as the Product Gallery, Product Rating, Product Price, and Add to Cart button.

Additionally, consider including a WooCommerce Notice element within the popup to display any notifications or confirmations directly to the user after an add-to-cart action.

It's crucial to implement the appropriate template hooks, similar to those used in a standard single product page. If you're unfamiliar with template hooks, we recommend reviewing [this article](/integrations/woocommerce/woocommerce-template-hooks/#single-product-template-hooks) for further guidance.

Below is an example of a WooCommerce Quick View Popup design:

![](imgs/woo-quick-view-design-example-5cb29bdac9.png)

## Step 2: Configure Popup settings

To proceed, ensure that you have enabled the **"WooCommerce Quick View"** (@since 1.10.2) and **"Fetch content via AJAX"** options in **Settings > Template Settings > Popup**.

Enabling the **AJAX loader** will enhance the user experience by providing a smoother interaction with the Quick View Popup.

:::note
Do not set any template condition for the popup template as we will embed it in the Products loop.
:::

![](imgs/woo-quick-view-popup-control-6bfaf6afe8.png)

## Step 3: Create a Product Query Loop

Proceed by creating a Product query loop on a new page or within your Shop page template. Insert the necessary elements according to your specific requirements.

Include the appropriate [template hooks](/integrations/woocommerce/product-archive-woocommerce/) within the loop to ensure that any WooCommerce third-party plugins can effectively apply their logic within your Product query loop.

![](imgs/woo-quick-view-query-loop-example-7d35830a9d.png)

## Step 4: Insert Popup template and Configure Interaction to Trigger Quick View Popup

Within the product query loop, insert a Template element and select the popup template you created in Step 1.

For a cleaner HTML structure, you may choose to enable the "Render without wrapper" option.

![](imgs/woo-quick-view-template-element-location-a9fb614a4e.png)

![](imgs/woo-quick-view-popup-template-element-094641e7d7.png)

Instead of using the Add to Cart element within the loop, utilize a Button element.

To ensure this button triggers the Quick View popup, configure the interaction as shown in the following screenshot:

![](imgs/woo-quick-view-button-interaction-dac55b91a6.png)

## Summary

By following these steps, you've successfully implemented a Quick View Popup feature using Bricks.

This enhancement not only improves the user experience by allowing visitors to quickly access product details without navigating away from the current page, but it also provides a seamless integration with WooCommerce.

Remember, fine-tuning the design and interaction settings can further optimize the effectiveness of the Quick View feature, ensuring it meets your specific needs and enhances your overall site performance.
