---
title: "Account - Downloads Schema"
description: "Schema for Bricks Account - Downloads element"
canonical: "https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-downloads/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-downloads.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-07-29T10:15:35.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | woocommerce-account-downloads |
| `category` | general |
| `tag` | div |
| `nestable` | false |

<SchemaJson path="elements/woocommerce-account-downloads.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `tableBackgroundColor` | color | Background color | `background-color` on `.woocommerce-table--order-downloads` |
| `tableBorder` | border | Border | `border` on `.woocommerce-table--order-downloads` |
| `tableBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.woocommerce-table--order-downloads` |
| `tableTypography` | typography | Typography | `font` on `.woocommerce-table--order-downloads` |
| `theadPadding` | spacing | Padding | `padding` on `thead th, tbody td::before` |
| `theadBackgroundColor` | color | Background color | `background-color` on `thead th, tbody td::before` |
| `theadBorder` | border | Border | `border` on `thead th, tbody td::before` |
| `theadTypography` | typography | Typography | `font` on `thead th, tbody td::before` |
| `tbodyPadding` | spacing | Padding | `padding` on `tbody td` |
| `tbodyBackgroundColor` | color | Background color | `background-color` on `tbody td` |
| `tbodyBorder` | border | Border | `border` on `tbody td` |
| `tbodyTypography` | typography | Typography | `font` on `tbody td` |
| `tbodyLinksMargin` | spacing | Margin | `margin` on `tbody td a:not(.woocommerce-MyAccount-downloads-file.button)` |
| `tbodyLinksPadding` | spacing | Padding | `padding` on `tbody td a:not(.woocommerce-MyAccount-downloads-file.button)` |
| `tbodyLinksBackgroundColor` | color | Background color | `background-color` on `tbody td a:not(.woocommerce-MyAccount-downloads-file.button)` |
| `tbodyLinksBorder` | border | Border | `border` on `tbody td a:not(.woocommerce-MyAccount-downloads-file.button)` |
| `tbodyLinksBoxShadow` | box-shadow | Box shadow | `box-shadow` on `tbody td a:not(.woocommerce-MyAccount-downloads-file.button)` |
| `tbodyLinksTypography` | typography | Typography | `font` on `tbody td a:not(.woocommerce-MyAccount-downloads-file.button)` |
| `buttonPadding` | spacing | Padding | `padding` on `.woocommerce-MyAccount-downloads-file.button` |
| `buttonBackgroundColor` | color | Background color | `background-color` on `.woocommerce-MyAccount-downloads-file.button` |
| `buttonBorder` | border | Border | `border` on `.woocommerce-MyAccount-downloads-file.button` |
| `buttonBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.woocommerce-MyAccount-downloads-file.button` |
| `buttonTypography` | typography | Typography | `font` on `.woocommerce-MyAccount-downloads-file.button` |

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
