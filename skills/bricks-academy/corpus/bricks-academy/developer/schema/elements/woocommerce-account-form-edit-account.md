---
title: "Account - Edit Account Schema"
description: "Schema for Bricks Account - Edit account element"
canonical: "https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-form-edit-account/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-form-edit-account.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-07-29T10:15:35.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | woocommerce-account-form-edit-account |
| `category` | general |
| `tag` | div |
| `nestable` | false |

<SchemaJson path="elements/woocommerce-account-form-edit-account.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `labelTypography` | typography | Label typography | `font` on `label[for]` |
| `fieldsInputMargin` | spacing | Margin | `margin` on `input, .woocommerce-Input, .select2-selection.select2-selection--single` |
| `fieldsInputPadding` | spacing | Padding | `padding` on `input, .woocommerce-Input, .select2-selection.select2-selection--single` |
| `fieldsInputBackgroundColor` | color | Background color | `background-color` on `input, .woocommerce-Input, .select2-selection.select2-selection--single` |
| `fieldsInputBorder` | border | Border | `border` on `input, .woocommerce-Input, .select2-selection.select2-selection--single` |
| `fieldsInputBoxShadow` | box-shadow | Box shadow | `box-shadow` on `input, .woocommerce-Input, .select2-selection.select2-selection--single` |
| `fieldsInputTypography` | typography | Typography | `font` on `input, .woocommerce-Input, .select2-selection.select2-selection--single` |
| `submitButtonWidth` | number | Width | `width` on `button[type=submit]` |
| `submitButtonMargin` | spacing | Margin | `margin` on `button[type=submit]` |
| `submitButtonPadding` | spacing | Padding | `padding` on `button[type=submit]` |
| `submitButtonBackgroundColor` | color | Background color | `background-color` on `button[type=submit]` |
| `submitButtonBorder` | border | Border | `border` on `button[type=submit]` |
| `submitButtonBoxShadow` | box-shadow | Box shadow | `box-shadow` on `button[type=submit]` |
| `submitButtonTypography` | typography | Typography | `font` on `button[type=submit]` |
| `fieldsetGap` | number | Gap | `gap` on `fieldset` |
| `fieldsetMargin` | spacing | Margin | `margin` on `fieldset` |
| `fieldsetPadding` | spacing | Padding | `padding` on `fieldset` |
| `fieldsetBackgroundColor` | color | Background color | `background-color` on `fieldset` |
| `fieldsetBorder` | border | Border | `border` on `fieldset` |
| `fieldsetBoxShadow` | box-shadow | Box shadow | `box-shadow` on `fieldset` |
| `fieldsetTypography` | typography | Typography | `font` on `fieldset` |

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
