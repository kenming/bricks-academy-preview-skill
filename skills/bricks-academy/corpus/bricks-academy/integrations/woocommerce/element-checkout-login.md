---
title: "Element: Checkout Login"
description: "Use the Bricks Checkout Login element inside WooCommerce checkout templates to render and style the returning-customer login prompt."
canonical: "https://academy.bricksbuilder.io/integrations/woocommerce/element-checkout-login/"
markdownUrl: "https://academy.bricksbuilder.io/integrations/woocommerce/element-checkout-login.md"
pageType: "article"
section: "integrations"
category: "woocommerce"
lastmod: "2026-07-29T10:15:35.000Z"
---
The Checkout Login element allows for a convenient login option directly on the checkout page, enabling returning customers to sign in before completing their purchase.

This feature becomes available once you've enabled **`Enable log-in during checkout`** under **`WooCommerce > Settings > Accounts & Privacy`**.

In previous versions, the placement of the checkout login form was fixed, and styling options were limited, requiring custom CSS for adjustments. Now, you can control both placement and appearance.

![](imgs/woocommerce-enable-login-during-checkout-3dfde9635c.png)

To use this element, activate it under **`Bricks > Settings > WooCommerce`** by toggling on **`Enable Bricks WooCommerce "Checkout login" element`**.

![](imgs/woocommerce-checkout-login-setting-e3f12aac31.png)

:::note
When the Bricks Checkout Login element is enabled, the native WooCommerce checkout login form is removed. Add this element where you want the returning-customer login prompt to appear. The WooCommerce **`Enable log-in during checkout`** setting must stay enabled; on the frontend, the element does not render for users who are already logged in.
:::

:::note
**Note:** This element is specifically intended for the Checkout page. Place it within the **Checkout template** or directly on the Checkout page, depending on your design needs.
:::

**Key Controls**

**Location:**

- By default, the **Checkout Login** element will appear where it’s placed in the layout. However, you can choose alternative positions, such as: Before Order Review Heading, After Order Review Heading, Before Payment.
- Custom location settings only apply on the frontend. To ensure the login form appears in the desired location, add this element at the beginning of your Checkout template.

![](imgs/woocommerce-checkout-login-element-controls-5d267824cb.png)

![](imgs/element-location-example-0a76cc7e91.png)

You can set the form to be toggle-able, hiding it by default and revealing it only when the toggle is clicked, for a cleaner layout.
