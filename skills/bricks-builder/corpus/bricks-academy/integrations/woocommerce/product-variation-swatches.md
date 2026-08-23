---
title: "Product Variation Swatches (WooCommerce)"
description: "Integrate WooCommerce product variation swatches with Bricks and understand how they behave inside builder templates."
canonical: "https://academy.bricksbuilder.io/integrations/woocommerce/product-variation-swatches/"
markdownUrl: "https://academy.bricksbuilder.io/integrations/woocommerce/product-variation-swatches.md"
pageType: "article"
section: "integrations"
category: "woocommerce"
lastmod: "2026-08-20T13:12:40.000Z"
---
Bricks 2.0 introduces **Product variation swatches**, giving you more control over how product attribute options (i.e. color, size, pattern) appear on the frontend.

Instead of dropdowns, you can now display your product variations as **color swatches, image buttons, or custom labels**, creating a more visual and intuitive shopping experience.

This feature integrates directly into the **Add to cart** element, letting you style variation swatches exactly how you want, without the need for extra plugins.

![](imgs/bricks-woo-variation-swatches-before-1024x637-f9de079b52.png)

<figcaption>

Before Product Variation Swatches

</figcaption>



![](imgs/bricks-woo-variation-swatches-after-1024x637-12132ecea0.png)

<figcaption>

After Product Variation Swatches

</figcaption>

## Enable product variation swatches

To get started, go to **Bricks > Settings > WooCommerce > Enable product variation swatches**.

![](imgs/bricks-woo-variation-swatches-enable-5b7ab9a920.png)

Once enabled, you’ll be able to customize variation swatches directly from your product attribute settings.

## Assign a swatch type to product attributes

Go to **Products > Attributes**, and click "Edit" on an existing attribute (or create a new one).

![](imgs/bricks-woo-variation-swatches-edit-attribute-ffb0468c4c.png)

You’ll see a new **Swatch type** setting with the following options:

- **None (default)**: Standard WooCommerce behavior (dropdowns)
- **Color**: Displays swatches using color values
- **Label**: Displays custom text labels for each term
- **Image**: Displays swatches using images from your media library

![](imgs/bricks-woo-variation-swatches-attribute-settings-ccd1493048.png)

**Example:** Use the "Color" swatch type to show red and blue color boxes, or choose "Label" for size options like S, M, L.

### Set a fallback value (optional)

While editing the attribute, you can also set a **Fallback value**. This fallback will be used if a specific term doesn't have its own swatch value.

For **Image** swatches, Bricks checks images in this order:

1. The image assigned to the individual term.
2. The matching product variation image, if **Use product variation image** is enabled for the attribute.
3. The attribute fallback image.

## Assign swatch values to individual terms

Next, click **Configure terms** for the attribute you just edited.

![](imgs/bricks-woo-variation-swatches-configure-terms-83ae6ecd09.png)

Then, click **Edit** on a specific term (like “Red” or “Large”).

![](imgs/bricks-woo-variation-swatches-edit-term-935e30cf24.png)

For each term, you’ll see a new input that matches the swatch type:

- **Color** → Choose a color
- **Image** → Select or upload an image
- **Label** → Add custom text

![](imgs/bricks-woo-variation-swatches-term-settings-a795331acc.png)

These values are what will be shown on the frontend in the Add to cart element.

## Style swatches in the Add to cart element

Variation swatches are rendered inside the **Add to cart** element, as long as your product uses attributes with a swatch type.

To style them:

1. Select the **Add to cart** element (e.g in your single product template)
2. Open the new **Variation swatches** group in the element settings

![](imgs/bricks-woo-variation-swatches-add-to-cart-cc0c233fdd.png)

From there, you can adjust the size, spacing, borders, active states, tooltips, and more.

## Unavailable variation options

Bricks follows the availability state of the hidden WooCommerce variation dropdown. When WooCommerce disables an option for the current attribute combination, Bricks adds the `disabled` class and `aria-disabled="true"` to the matching swatch.

You can style unavailable swatches with custom CSS:

```css
.bricks-variation-swatches li.disabled,
.bricks-variation-swatches li[aria-disabled="true"] {
  opacity: 0.45;
  text-decoration: line-through;
}
```

There is no separate Bricks setting that forces every out-of-stock option to be hidden or disabled. If a swatch does not receive the disabled state, check the product's stock settings and the exact variation combination in WooCommerce first.

That's it. With variation swatches, you can now turn standard variation dropdowns into polished, interactive product selectors, designed your way, directly in the Bricks builder.
