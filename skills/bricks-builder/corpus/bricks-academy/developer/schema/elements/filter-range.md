---
title: "Filter - Range Schema"
description: "Schema for Bricks Filter - Range element"
canonical: "https://academy.bricksbuilder.io/developer/schema/elements/filter-range/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/elements/filter-range.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-08-04T12:13:33.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | filter-range |
| `category` | general |
| `tag` | div |
| `nestable` | false |

<SchemaJson path="elements/filter-range.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `disableAutoMinMax` | checkbox | Disable auto min/max value | — |
| `displayMode` | select | Mode | — |
| `step` | number | Step | — |
| `decimalPlaces` | number | Decimal places | — |
| `labelThousandSeparator` | checkbox | Thousand separator | — |
| `labelSeparatorText` | text | Separator | — |
| `labelMin` | text | Min | — |
| `labelMax` | text | Max | — |
| `labelDirection` | direction | Direction | `flex-direction` on `.min-max-wrap > *, .value-wrap > *` |
| `labelGap` | number | Gap | `gap` on `.value-wrap > span`, `gap` on `.min-max-wrap > div` |
| `labelTypography` | typography | Typography | `font` on `.label` |
| `placeholderMin` | text | Placeholder | — |
| `placeholderMax` | text | Placeholder | — |
| `inputBackgroundColor` | color | Background color | `background-color` on `.min-max-wrap input` |
| `inputBorder` | border | Border | `border` on `.min-max-wrap input` |
| `inputTypography` | typography | Typography | `font` on `.min-max-wrap input` |
| `inputWidth` | number | Width | `width` on `.min-max-wrap input` |
| `inputUseCustomStepper` | checkbox | Custom stepper | — |
| `inputCustomStepperButtonGap` | number | Gap | `gap` on `.min-max-wrap.has-custom-stepper .brx-stepper` |
| `inputCustomStepperInputGap` | number | Gap | `margin-inline-start` on `.min-max-wrap.has-custom-stepper .brx-stepper` |
| `inputCustomStepperButtonBackgroundColor` | color | Button | `background-color` on `.min-max-wrap.has-custom-stepper .brx-stepper-button` |
| `inputCustomStepperButtonBorder` | border | Button | `border` on `.min-max-wrap.has-custom-stepper .brx-stepper-button` |
| `inputCustomStepperButtonTypography` | typography | Button | `font` on `.min-max-wrap.has-custom-stepper .brx-stepper-button` |
| `sliderSpacing` | number | Spacing | `padding-top` on `.double-slider-wrap`, `margin-top` on `.double-slider-wrap .value-wrap` |
| `sliderBarHeight` | number | Bar | `border-width` on `.double-slider-wrap .slider-wrap .slider-base`, `border-width` on `.double-slider-wrap .slider-wrap .slider-track` |
| `sliderBarColor` | color | Bar | `border-color` on `.double-slider-wrap .slider-wrap .slider-base` |
| `sliderBarColorActive` | color | Bar | `border-color` on `.double-slider-wrap .slider-wrap .slider-track`, `border-color` on `.double-slider-wrap input[type="range"]::-moz-range-thumb`, `border-color` on `.double-slider-wrap input[type="range"]::-webkit-slider-thumb` |
| `sliderThumbSize` | number | Thumb | `width` on `.double-slider-wrap input[type="range"]::-moz-range-thumb`, `width` on `.double-slider-wrap input[type="range"]::-webkit-slider-thumb`, `height` on `.double-slider-wrap input[type="range"]::-moz-range-thumb`, `height` on `.double-slider-wrap input[type="range"]::-webkit-slider-thumb`, `border-radius` on `:scope > .double-slider-wrap input[type="range"]::-moz-range-thumb`, `border-radius` on `:scope > .double-slider-wrap input[type="range"]::-webkit-slider-thumb` |
| `sliderThumbBackgroundColor` | color | Thumb | `background-color` on `.double-slider-wrap input[type="range"]::-moz-range-thumb`, `background-color` on `.double-slider-wrap input[type="range"]::-webkit-slider-thumb` |
| `sliderThumbBorderFull` | border | Thumb | `border` on `.double-slider-wrap input[type="range"]::-moz-range-thumb`, `border` on `.double-slider-wrap input[type="range"]::-webkit-slider-thumb` |
| `sliderThumbBoxShadow` | box-shadow | Thumb | `box-shadow` on `.double-slider-wrap input[type="range"]::-moz-range-thumb`, `box-shadow` on `.double-slider-wrap input[type="range"]::-webkit-slider-thumb` |

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
