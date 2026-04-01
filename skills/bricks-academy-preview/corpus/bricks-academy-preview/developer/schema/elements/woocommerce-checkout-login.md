import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | woocommerce-checkout-login |
| `category` | general |
| `tag` | div |
| `nestable` | false |

<SchemaJson path="elements/woocommerce-checkout-login.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `location` | select | Location | — |
| `toggleableForm` | checkbox | Toggleable form | — |
| `toggleText` | text | Text | — |
| `toggleDivJustifyContent` | justify-content | Justify content | `justify-content` on `.login-toggle` |
| `toggleDivGap` | number | Gap | `gap` on `.login-toggle` |
| `toggleButtonNoText` | checkbox | Disable text | — |
| `toggleButtonText` | text | Text | — |
| `toggleIcon` | icon | Icon | — |
| `toggleIconTypography` | typography | Icon typography | `font` on `.login-toggle .showlogin i` |
| `disableLoginMessage` | checkbox | Disable login message | — |
| `loginMessage` | text | Login message | — |
| `rememberMeDisable` | checkbox | Disable | — |
| `rememberMeTypography` | typography | Typography | `font` on `.woocommerce-form-login__rememberme` |
| `lostPasswordDisable` | checkbox | Disable | — |
| `lostPasswordTypography` | typography | Typography | `font` on `.woocommerce-LostPassword a` |
| `toggleDivMargin` | spacing | Margin | `margin` on `.login-toggle` |
| `toggleDivPadding` | spacing | Padding | `padding` on `.login-toggle` |
| `toggleDivBackgroundColor` | color | Background color | `background-color` on `.login-toggle` |
| `toggleDivBorder` | border | Border | `border` on `.login-toggle` |
| `toggleDivBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.login-toggle` |
| `toggleDivTypography` | typography | Typography | `font` on `.login-toggle` |
| `toggleButtonMargin` | spacing | Margin | `margin` on `.login-toggle .showlogin` |
| `toggleButtonPadding` | spacing | Padding | `padding` on `.login-toggle .showlogin` |
| `toggleButtonBackgroundColor` | color | Background color | `background-color` on `.login-toggle .showlogin` |
| `toggleButtonBorder` | border | Border | `border` on `.login-toggle .showlogin` |
| `toggleButtonBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.login-toggle .showlogin` |
| `toggleButtonTypography` | typography | Typography | `font` on `.login-toggle .showlogin` |
| `formWrapperMargin` | spacing | Margin | `margin` on `.login-div` |
| `formWrapperPadding` | spacing | Padding | `padding` on `.login-div` |
| `formWrapperBackgroundColor` | color | Background color | `background-color` on `.login-div` |
| `formWrapperBorder` | border | Border | `border` on `.login-div` |
| `formWrapperBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.login-div` |
| `formWrapperTypography` | typography | Typography | `font` on `.login-div` |
| `fieldsAlignItems` | align-items | Align items | `align-items` |
| `fieldsGap` | number | Gap | `gap` |
| `labelTypography` | typography | Label typography | `font` on `label[for]` |
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
