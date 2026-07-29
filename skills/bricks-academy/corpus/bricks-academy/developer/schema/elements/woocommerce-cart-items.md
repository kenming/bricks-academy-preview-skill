---
title: "Cart Items Schema"
description: "Schema for Bricks Cart items element"
canonical: "https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-cart-items/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-cart-items.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-07-29T10:15:35.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | woocommerce-cart-items |
| `category` | woocommerce |
| `tag` | div |
| `nestable` | false |

<SchemaJson path="elements/woocommerce-cart-items.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `itemLinkDisable` | checkbox | Disable link | — |
| `headHide` | checkbox | Hide | `display` on `thead` |
| `headBackground` | color | Background | `background-color` on `thead` |
| `headBorder` | border | Border | `border` on `thead` |
| `headTypography` | typography | Typography | `font` on `thead th` |
| `bodyBackground` | color | Background | `background-color` on `tbody` |
| `bodyBorder` | border | Border | `border` on `tbody tr` |
| `imageDisable` | checkbox | Disable | — |
| `width` | number | Width | `width` on `.product-thumbnail img` |
| `imageHeight` | number | Height | `height` on `.product-thumbnail img` |
| `imageSize` | select | Size | — |
| `removeColor` | color | Color | `color` on `.product-remove a` |
| `removeSize` | number | Size | `font-size` on `.product-remove a` |
| `removePosition` | dimensions | Position | `—` on `.product-remove`, `position` on `.product-remove` |
| `buttonsTypography` | typography | Typography | `font` on `.button` |
| `buttonsBackground` | color | Background color | `background-color` on `.button` |
| `buttonsBorder` | border | Border | `border` on `.button` |
| `hideCoupon` | checkbox | Hide | — |
| `couponMargin` | spacing | Margin | `margin` on `.coupon` |
| `removeHide` | checkbox | Hide Remove | `display` on `.product-remove` |
| `thumbnailHide` | checkbox | Hide Thumbnail | `display` on `.product-thumbnail` |
| `nameHide` | checkbox | Hide Name | `display` on `.product-name` |
| `priceHide` | checkbox | Hide Price | `display` on `.product-price` |
| `quantityHide` | checkbox | Hide Quantity | `display` on `.product-quantity` |
| `subtotalHide` | checkbox | Hide Subtotal | `display` on `.product-subtotal` |
| `nameTypography` | typography | Name typography | `font` on `tbody .product-name` |
| `priceTypography` | typography | Price typography | `font` on `tbody .product-price` |
| `quantityTypography` | typography | Quantity typography | `font` on `tbody .product-quantity` |
| `subtotalTypography` | typography | Subtotal typography | `font` on `tbody .product-subtotal` |

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
