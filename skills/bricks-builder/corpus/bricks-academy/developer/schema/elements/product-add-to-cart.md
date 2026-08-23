---
title: "Add To Cart Schema"
description: "Schema for Bricks Add to cart element"
canonical: "https://academy.bricksbuilder.io/developer/schema/elements/product-add-to-cart/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/elements/product-add-to-cart.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-08-20T13:12:40.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | product-add-to-cart |
| `category` | woocommerce_product |
| `tag` | div |
| `nestable` | false |

<SchemaJson path="elements/product-add-to-cart.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `variationsTypography` | typography | Typography | `font` on `table.variations label` |
| `variationsBackgroundColor` | color | Background color | `background-color` on `table.variations tr` |
| `variationsBorder` | border | Border | `border` on `.cart .variations tr:not(:has(.reset_variations))` |
| `variationsMargin` | spacing | Margin | `margin` on `.cart table.variations` |
| `variationsPadding` | spacing | Padding | `padding` on `.cart table.variations td`, `padding` on `.cart table.variations th` |
| `variationsDescriptionTypography` | typography | Description typography | `font` on `.woocommerce-variation-description` |
| `variationsPriceTypography` | typography | Price typography | `font` on `.woocommerce-variation-price` |
| `variationsRegularPriceTypography` | typography | Regular price typography | `font` on `.woocommerce-variation-price .price del, .woocommerce-variation-price .price > span` |
| `variationsSalePriceTypography` | typography | Sale price typography | `font` on `.woocommerce-variation-price .price ins` |
| `swatchesWrap` | select | Wrap | `flex-wrap` on `.bricks-variation-swatches` |
| `swatchesDirection` | direction | Direction | `flex-direction` on `.bricks-variation-swatches` |
| `swatchesJustifyContent` | justify-content | Align main axis | `justify-content` on `.bricks-variation-swatches` |
| `swatchesAlignItems` | align-items | Align cross axis | `align-items` on `.bricks-variation-swatches` |
| `swatchesColumnGap` | number | Column gap | `column-gap` on `.bricks-variation-swatches` |
| `swatchesRowGap` | number | Row gap | `row-gap` on `.bricks-variation-swatches` |
| `colorSwatchSize` | number | Size | `width` on `.bricks-variation-swatches.bricks-swatch-color li`, `height` on `.bricks-variation-swatches.bricks-swatch-color li` |
| `colorSwatchBorder` | border | Border | `border` on `.bricks-variation-swatches.bricks-swatch-color li` |
| `colorSwatchActiveBorder` | border | Border | `border` on `.bricks-variation-swatches.bricks-swatch-color li.bricks-swatch-selected` |
| `labelSwatchPadding` | spacing | Padding | `padding` on `.bricks-variation-swatches.bricks-swatch-label li` |
| `labelSwatchTypography` | typography | Typography | `font` on `.bricks-variation-swatches.bricks-swatch-label li` |
| `labelSwatchActiveTypography` | typography | Typography | `font` on `.bricks-variation-swatches.bricks-swatch-label li.bricks-swatch-selected` |
| `labelSwatchBackgroundColor` | color | Background color | `background-color` on `.bricks-variation-swatches.bricks-swatch-label li` |
| `labelSwatchActiveBackgroundColor` | color | Background color | `background-color` on `.bricks-variation-swatches.bricks-swatch-label li.bricks-swatch-selected` |
| `labelSwatchBorder` | border | Border | `border` on `.bricks-variation-swatches.bricks-swatch-label li` |
| `labelSwatchActiveBorder` | border | Border | `border` on `.bricks-variation-swatches.bricks-swatch-label li.bricks-swatch-selected` |
| `imageSwatchWidth` | number | Width | `width` on `.bricks-variation-swatches.bricks-swatch-image li img` |
| `imageSwatchHeight` | number | Height | `height` on `.bricks-variation-swatches.bricks-swatch-image li img` |
| `imageSwatchBorder` | border | Border | `border` on `.bricks-variation-swatches.bricks-swatch-image li` |
| `imageSwatchActiveBorder` | border | Border | `border` on `.bricks-variation-swatches.bricks-swatch-image li.bricks-swatch-selected` |
| `swatchTooltipPadding` | spacing | Padding | `padding` on `.bricks-variation-swatches li[data-balloon]::after` |
| `swatchTooltip` | typography | Typography | `font` on `.bricks-variation-swatches li[data-balloon]::after` |
| `swatchTooltipBackground` | color | Background color | `background-color` on `.bricks-variation-swatches li[data-balloon]::after`, `border-top-color` on `.bricks-variation-swatches li[data-balloon]::before` |
| `swatchTooltipBorder` | border | Border | `border` on `.bricks-variation-swatches li[data-balloon]::after` |
| `hideStock` | checkbox | Hide stock | `display` on `.stock` |
| `stockTypography` | typography | Typography | `font` on `.stock` |
| `inStockTypography` | typography | Typography | `font` on `.stock.in-stock` |
| `outOfStockTypography` | typography | Typography | `font` on `.stock.out-of-stock` |
| `formDisplay` | select | Display | `display` on `form.cart:not(.variations_form), form.cart.variations_form .woocommerce-variation-add-to-cart` |
| `formFlexDirection` | direction | Direction | `flex-direction` on `form.cart:not(.variations_form), form.cart.variations_form .woocommerce-variation-add-to-cart` |
| `formAlignSelf` | align-items | Align self | `align-self` on `form.cart:not(.variations_form), form.cart.variations_form .woocommerce-variation-add-to-cart` |
| `formJustifyContent` | justify-content | Align main axis | `justify-content` on `form.cart:not(.variations_form), form.cart.variations_form .woocommerce-variation-add-to-cart` |
| `formAlignItems` | align-items | Align cross axis | `align-items` on `form.cart:not(.variations_form), form.cart.variations_form .woocommerce-variation-add-to-cart` |
| `formGap` | number | Gap | `gap` on `form.cart:not(.variations_form), form.cart.variations_form .woocommerce-variation-add-to-cart` |
| `formFlexGrow` | number | Flex grow | `flex-grow` on `form.cart:not(.variations_form), form.cart.variations_form .woocommerce-variation-add-to-cart` |
| `formFlexShrink` | number | Flex shrink | `flex-shrink` on `form.cart:not(.variations_form), form.cart.variations_form .woocommerce-variation-add-to-cart` |
| `formFlexBasis` | text | Flex basis | `flex-basis` on `form.cart:not(.variations_form), form.cart.variations_form .woocommerce-variation-add-to-cart` |
| `quantityWidth` | number | Width | `width` on `.cart .quantity` |
| `quantityBackground` | color | Background | `background-color` on `.cart .quantity` |
| `quantityBorder` | border | Border | `border` on `.qty`, `border` on `.minus`, `border` on `.plus` |
| `buttonText` | text | Simple product | — |
| `variableText` | text | Variable product | — |
| `groupedText` | text | Grouped product | — |
| `externalText` | text | External product | — |
| `buttonMargin` | spacing | Margin | `margin` on `.cart .single_add_to_cart_button, a.button[data-product_id]` |
| `buttonPadding` | spacing | Padding | `padding` on `.cart .single_add_to_cart_button, a.button[data-product_id]` |
| `buttonWidth` | number | Width | `min-width` on `.cart .single_add_to_cart_button, a.button[data-product_id]` |
| `buttonBackgroundColor` | color | Background color | `background-color` on `.cart .single_add_to_cart_button, a.button[data-product_id]` |
| `buttonBorder` | border | Border | `border` on `.cart .single_add_to_cart_button, a.button[data-product_id]` |
| `buttonTypography` | typography | Typography | `font` on `.cart .single_add_to_cart_button, a.button[data-product_id]` |
| `icon` | icon | Icon | — |
| `iconTypography` | typography | Icon typography | `font` on `.icon` |
| `iconOnly` | checkbox | Icon only | — |
| `iconPosition` | select | Icon position | — |
| `groupedProductTablePadding` | spacing | Table cell | `padding` on `.cart.grouped_form .group_table td` |
| `groupedProductQuantityWidth` | number | Width | `width` on `.cart.grouped_form .quantity` |
| `groupedProductQuantityBackground` | color | Background | `background-color` on `.cart.grouped_form .quantity` |
| `groupedProductQuantityBorder` | border | Border | `border` on `.cart.grouped_form .quantity .minus`, `border` on `.cart.grouped_form .quantity .plus`, `border` on `.cart.grouped_form .quantity .qty` |
| `groupedProductLabelTypography` | typography | Typography | `font` on `.cart.grouped_form .woocommerce-grouped-product-list-item__label a` |
| `groupedProductStockTypography` | typography | Typography | `font` on `.cart.grouped_form .stock` |
| `groupedProductInStockTypography` | typography | Typography | `font` on `.cart.grouped_form .stock.in-stock` |
| `groupedProductOutOfStockTypography` | typography | Typography | `font` on `.cart.grouped_form .stock.out-of-stock` |
| `groupedProductPriceTypography` | typography | Typography | `font` on `.cart.grouped_form .woocommerce-grouped-product-list-item__price .woocommerce-Price-amount` |
| `groupedProductSalePriceTypography` | typography | Sale price typography | `font` on `.cart.grouped_form .woocommerce-grouped-product-list-item__price ins .woocommerce-Price-amount` |
| `groupedProductRegularPriceTypography` | typography | Regular price typography | `font` on `.cart.grouped_form .woocommerce-grouped-product-list-item__price del .woocommerce-Price-amount` |
| `groupedProductButtonWidth` | number | Width | `min-width` on `.cart.grouped_form .group_table .button` |
| `groupedProductButtonPadding` | spacing | Padding | `padding` on `.cart.grouped_form .group_table .button` |
| `groupedProductButtonTypography` | typography | Typography | `font` on `.cart.grouped_form .group_table .button` |
| `groupedProductButtonBackground` | color | Background color | `background-color` on `.cart.grouped_form .group_table .button` |
| `addingButtonText` | text | Button text | — |
| `addingButtonIcon` | icon | Icon | — |
| `addingButtonIconOnly` | checkbox | Icon only | — |
| `addingButtonIconPosition` | select | Icon position | — |
| `addingButtonIconSpinning` | checkbox | Icon spinning | — |
| `addedButtonText` | text | Button text | — |
| `resetTextAfter` | number | Reset text after .. seconds | — |
| `addedButtonIcon` | icon | Icon | — |
| `addedButtonIconOnly` | checkbox | Icon only | — |
| `addedButtonIconPosition` | select | Icon position | — |
| `showNotice` | select | Show notice | — |
| `scrollToNotice` | select | Scroll to notice | — |
| `hideViewCart` | select | Hide "View cart" button | `display` on `.added_to_cart.wc-forward` |

## Inherited CSS controls

Shared CSS controls available on all elements. Keys are prefixed with `_` and support responsive/pseudo-class variants via colon syntax (e.g. `_typography:tablet_portrait:hover`).

| Key | Type | Label | CSS |
|---|---|---|---|
| `_content` | text | Content | `content` |
| `_margin` | spacing | Margin | `margin` |
| `_padding` | spacing | Padding | `padding` |
| `_width` | number | Width | `width` |
| `_widthMin` | number | Min. width | `min-width` |
| `_widthMax` | number | Max. width | `max-width` |
| `_height` | number | Height | `height` |
| `_heightMin` | number | Min. height | `min-height` |
| `_heightMax` | number | Max. height | `max-height` |
| `_aspectRatio` | text | Aspect ratio | `aspect-ratio` |
| `_position` | select | Position | `position` |
| `_top` | number | Top | `top` |
| `_right` | number | Right | `right` |
| `_bottom` | number | Bottom | `bottom` |
| `_left` | number | Left | `left` |
| `_zIndex` | number | Z-index | `z-index` |
| `_order` | number | Order | `order` |
| `_display` | select | Display | `display`, `align-items` |
| `_visibility` | select | Visibility | `visibility` |
| `_overflow` | text | Overflow | `overflow` |
| `_opacity` | number | Opacity | `opacity` |
| `_cursor` | select | Cursor | `cursor` |
| `_isolation` | select | Isolation | `isolation` |
| `_mixBlendMode` | select | Mix blend mode | `mix-blend-mode` |
| `_pointerEvents` | text | Pointer events | `pointer-events` |
| `_perspective` | number | Perspective | `perspective` |
| `_perspectiveOrigin` | text | Perspective origin | `perspective-origin` |
| `_gridItemJustifySelf` | align-items | Justify self | `justify-self` |
| `_flexDirection` | direction | Direction | `flex-direction` |
| `_alignSelf` | align-items | Align self | `align-self` |
| `_justifyContent` | justify-content | Align main axis | `justify-content` |
| `_alignItems` | align-items | Align cross axis | `align-items` |
| `_gap` | number | Gap | `gap` |
| `_flexGrow` | number | Flex grow | `flex-grow` |
| `_flexShrink` | number | Flex shrink | `flex-shrink` |
| `_flexBasis` | text | Flex basis | `flex-basis` |
| `_useMasonry` | checkbox | %s layout | — |
| `_masonryColumn` | number | Columns | `--columns` |
| `_masonryGutter` | number | Spacing | `--gutter` |
| `_masonryHorizontalOrder` | checkbox | Horizontal order | — |
| `_masonryTransitionDuration` | number | Transition | — |
| `_masonryTransitionMode` | select | Reveal animation | — |
| `_typography` | typography | _typography | `font` |
| `_background` | background | _background | `background` |
| `_shapeDividers` | repeater | Custom shape | — |
| `_gradient` | gradient | _gradient | `background-image` |
| `_border` | border | Border | `border` |
| `_boxShadow` | box-shadow | Box shadow | `box-shadow` |
| `_transform` | transform | Transform | `transform` |
| `_transformOrigin` | text | Transform origin | `transform-origin` |
| `_motionElementParallax` | checkbox | Element parallax | — |
| `_motionElementParallaxSpeedX` | number | Horizontal speed | `--brx-motion-parallax-speed-x` |
| `_motionElementParallaxSpeedY` | number | Vertical speed | `--brx-motion-parallax-speed-y` |
| `_motionBackgroundParallax` | checkbox | Background parallax | — |
| `_motionBackgroundParallaxSpeed` | number | Background speed | `--brx-motion-background-speed` |
| `_motionStartVisiblePercent` | number | Parallax start point | — |
| `_cssCustom` | code | Custom CSS | — |
| `_cssClasses` | text | CSS classes | — |
| `_cssId` | text | CSS ID | — |
| `_cssFilters` | filters | CSS Filters | `filter` |
| `_cssTransition` | text | Transition | `transition` |
| `_attributes` | repeater | Name | — |
| `_scrollSnapType` | select | Type | `scroll-snap-type` on `html`, `scroll-snap-align` on `.brxe-section` |
| `_scrollSnapAlign` | select | Align | `scroll-snap-align` on `.brxe-section` |
| `_scrollSnapStop` | select | Stop | `scroll-snap-stop` on `.brxe-section` |
