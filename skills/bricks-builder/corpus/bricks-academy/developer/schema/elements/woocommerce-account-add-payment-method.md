---
title: "Account - Add Payment Method Schema"
description: "Schema for Bricks Account - Add payment method element"
canonical: "https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-add-payment-method/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-add-payment-method.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-08-20T13:12:40.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | woocommerce-account-add-payment-method |
| `category` | general |
| `tag` | div |
| `nestable` | false |

<SchemaJson path="elements/woocommerce-account-add-payment-method.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `radioCheckedColor` | color | Color | `background-color` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentMethod input.input-radio:checked + label::before`, `border-color` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentMethod input.input-radio:checked + label::before` |
| `wrapperMargin` | spacing | Margin | `margin` on `ul.woocommerce-PaymentMethods` |
| `wrapperPadding` | spacing | Padding | `padding` on `ul.woocommerce-PaymentMethods` |
| `wrapperBackgroundColor` | color | Background color | `background-color` on `ul.woocommerce-PaymentMethods` |
| `wrapperBorder` | border | Border | `border` on `ul.woocommerce-PaymentMethods` |
| `wrapperBoxShadow` | box-shadow | Box shadow | `box-shadow` on `ul.woocommerce-PaymentMethods` |
| `wrapperTypography` | typography | Typography | `font` on `ul.woocommerce-PaymentMethods` |
| `listMargin` | spacing | Margin | `margin` on `ul.woocommerce-PaymentMethods` |
| `listPadding` | spacing | Padding | `padding` on `ul.woocommerce-PaymentMethods` |
| `listBackgroundColor` | color | Background color | `background-color` on `ul.woocommerce-PaymentMethods` |
| `listBorder` | border | Border | `border` on `ul.woocommerce-PaymentMethods` |
| `listBoxShadow` | box-shadow | Box shadow | `box-shadow` on `ul.woocommerce-PaymentMethods` |
| `listTypography` | typography | Typography | `font` on `ul.woocommerce-PaymentMethods` |
| `itemMargin` | spacing | Margin | `margin` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod` |
| `itemPadding` | spacing | Padding | `padding` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod` |
| `itemBackgroundColor` | color | Background color | `background-color` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod` |
| `itemBorder` | border | Border | `border` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod` |
| `itemBoxShadow` | box-shadow | Box shadow | `box-shadow` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod` |
| `itemTypography` | typography | Typography | `font` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod` |
| `labelMargin` | spacing | Margin | `margin` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod label` |
| `labelPadding` | spacing | Padding | `padding` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod label` |
| `labelBackgroundColor` | color | Background color | `background-color` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod label` |
| `labelBorder` | border | Border | `border` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod label` |
| `labelBoxShadow` | box-shadow | Box shadow | `box-shadow` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod label` |
| `labelTypography` | typography | Typography | `font` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod label` |
| `paymentBoxMargin` | spacing | Margin | `margin` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentBox` |
| `paymentBoxPadding` | spacing | Padding | `padding` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentBox` |
| `paymentBoxBackgroundColor` | color | Background color | `background-color` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentBox` |
| `paymentBoxBorder` | border | Border | `border` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentBox` |
| `paymentBoxBoxShadow` | box-shadow | Box shadow | `box-shadow` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentBox` |
| `paymentBoxTypography` | typography | Typography | `font` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentBox` |
| `buttonMargin` | spacing | Margin | `margin` on `.woocommerce-Payment .form-row .woocommerce-Button` |
| `buttonPadding` | spacing | Padding | `padding` on `.woocommerce-Payment .form-row .woocommerce-Button` |
| `buttonBackgroundColor` | color | Background color | `background-color` on `.woocommerce-Payment .form-row .woocommerce-Button` |
| `buttonBorder` | border | Border | `border` on `.woocommerce-Payment .form-row .woocommerce-Button` |
| `buttonBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.woocommerce-Payment .form-row .woocommerce-Button` |
| `buttonTypography` | typography | Typography | `font` on `.woocommerce-Payment .form-row .woocommerce-Button` |

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
