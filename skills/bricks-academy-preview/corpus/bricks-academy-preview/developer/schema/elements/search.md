import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | search |
| `category` | wordpress |
| `tag` | div |
| `nestable` | false |

<SchemaJson path="elements/search.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `searchType` | select | Type | — |
| `ariaLabel` | text | aria-label | — |
| `actionURL` | text | Action URL | — |
| `additionalParams` | repeater | Additional parameters | — |
| `inputHeight` | number | Height | `height` on `input[type=search]` |
| `inputWidth` | number | Width | `width` on `input[type=search]`, `max-width` on `.bricks-search-overlay .bricks-search-form` |
| `placeholder` | text | Placeholder | — |
| `placeholderColor` | color | Placeholder color | `color` on `input[type=search]::placeholder` |
| `inputBackgroundColor` | color | Background color | `background-color` on `input[type=search]` |
| `inputBorder` | border | Border | `border` on `input[type=search]` |
| `inputBoxShadow` | box-shadow | Box shadow | `box-shadow` on `input[type=search]` |
| `inputTypography` | typography | Typography | `font` on `input[type=search]` |
| `showLabel` | checkbox | Show label | — |
| `labelText` | text | Label text | — |
| `labelTypography` | typography | Label typography | `typography` on `label` |
| `buttonAriaLabel` | text | aria-label | — |
| `buttonText` | text | Text | — |
| `icon` | icon | Icon | — |
| `buttonPadding` | spacing | Padding | `padding` on `button` |
| `iconHeight` | number | Height | `height` on `button` |
| `iconWidth` | number | Width | `width` on `button` |
| `iconBackgroundColor` | color | Background color | `background-color` on `button` |
| `iconBorder` | border | Border | `border` on `button` |
| `iconBoxShadow` | box-shadow | Box shadow | `box-shadow` on `button` |
| `iconTypography` | typography | Typography | `font` on `button` |
| `overlayFormDirection` | direction | Direction | `flex-direction` on `.bricks-search-overlay form` |
| `overlayFormGap` | number | Gap | `gap` on `.bricks-search-overlay form` |
| `searchOverlayTitle` | text | Title | — |
| `searchOverlayTitleTag` | text | Title tag | — |
| `searchOverlayTitleTypography` | typography | Title typography | `font` on `.title` |
| `searchOverlayBackground` | background | Background | `background` on `.bricks-search-overlay` |
| `searchOverlayBackgroundOverlay` | color | Background | `background-color` on `.bricks-search-overlay:after` |
| `overlayIconWidth` | number | Button | `width` on `.bricks-search-overlay button[type="submit"]` |
| `overlayButtonPadding` | spacing | Button | `padding` on `.bricks-search-overlay button[type="submit"]` |
| `overlayButtonBackground` | color | Button | `background-color` on `.bricks-search-overlay button[type="submit"]` |
| `overlayButtonBorder` | border | Button | `border` on `.bricks-search-overlay button[type="submit"]` |
| `overlayButtonTypography` | typography | Button | `font` on `.bricks-search-overlay button[type="submit"]` |

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
