import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | woocommerce-checkout-order-payment |
| `category` | woocommerce |
| `tag` | div |
| `nestable` | false |

<SchemaJson path="elements/woocommerce-checkout-order-payment.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `previewOrderId` | number | Preview order ID | — |
| `paymentMargin` | spacing | Margin | `margin` on `#payment` |
| `paymentPadding` | spacing | Padding | `padding` on `#payment` |
| `paymentBackground` | color | Background | `background-color` on `#payment` |
| `paymentBorder` | border | Border | `border` on `#payment` |
| `paymentMethodLabelTypography` | typography | Label typography | `font` on `#payment .payment_methods label` |
| `paymentDescriptionMargin` | spacing | Margin | `margin` on `#payment .payment_methods .payment_box` |
| `paymentDescriptionPadding` | spacing | Padding | `padding` on `#payment .payment_methods .payment_box` |
| `paymentDescriptionBackground` | color | Background | `background-color` on `#payment .payment_methods .payment_box` |
| `paymentMethodDescriptionTypography` | typography | Typography | `font` on `#payment .payment_methods .payment_box` |
| `privacyMargin` | spacing | Margin | `margin` on `.woocommerce-privacy-policy-text` |
| `privacyTypography` | typography | Typography | `font` on `.woocommerce-privacy-policy-text` |
| `buttonWidth` | number | Width | `width` on `button[type="submit"]` |
| `buttonAlign` | align-items | Align | `align-self` on `button[type="submit"]` |
| `buttonMargin` | spacing | Margin | `margin` on `button[type="submit"]` |
| `buttonPadding` | spacing | Padding | `padding` on `button[type="submit"]` |
| `buttonBackground` | color | Background | `background-color` on `button[type="submit"]` |
| `buttonBorder` | border | Border | `border` on `button[type="submit"]` |
| `buttonTypography` | typography | Typography | `font` on `button[type="submit"]` |

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
