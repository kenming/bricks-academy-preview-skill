import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | posts |
| `category` | wordpress |
| `tag` | div |
| `nestable` | false |

<SchemaJson path="elements/posts.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `query` | query | Query | — |
| `linkPost` | checkbox | Link entire post | — |
| `layout` | select | Layout | — |
| `direction` | direction | Direction | `flex-direction` on `.bricks-layout-wrapper[data-layout=list] .bricks-layout-inner` |
| `columns` | number | Columns | `--columns` on `.bricks-layout-wrapper` |
| `columnsMetro` | number | Columns | `grid-template-columns` on `.bricks-layout-wrapper`, `grid-column` on `.bricks-layout-item`, `grid-row` on `.bricks-layout-item` |
| `gutter` | number | Spacing | `--gutter` on `.bricks-layout-wrapper` |
| `firstPostFullWidth` | checkbox | First post full width | `grid-column` on `[data-layout="grid"] .bricks-layout-item:first-child`, `width` on `[data-layout="grid"] .bricks-layout-item:first-child` |
| `imageDisable` | checkbox | Disable image | — |
| `imageLink` | checkbox | Link image | — |
| `imageLinkAlt` | text | Image link alt text | — |
| `alternate` | checkbox | Alternate images | — |
| `imagePosition` | select | Image position | — |
| `width` | number | Image width | `max-width` on `.bricks-layout-wrapper[data-layout=list] .image-wrapper`, `max-width` on `.bricks-layout-wrapper[data-layout=grid] .image-wrapper`, `max-width` on `.bricks-layout-inner > a`, `max-width` on `.overlay-wrapper` |
| `height` | number | Image height | `height` on `.bricks-layout-wrapper[data-layout=list] img`, `height` on `.bricks-layout-wrapper[data-layout=grid] img`, `height` on `.overlay-wrapper` |
| `imageRatio` | text | Image ratio | `aspect-ratio` on `.image` |
| `imageSize` | select | Image size | — |
| `filter` | select | Taxonomy | — |
| `filterTextAlign` | text-align | Text align | `text-align` on `.bricks-isotope-filters` |
| `filterBackground` | color | Background | `background-color` on `.bricks-isotope-filters li` |
| `filterBackgroundActive` | color | Background active | `background` on `.bricks-isotope-filters .active` |
| `filterBorder` | border | Border | `border` on `.bricks-isotope-filters li` |
| `filterTypography` | typography | Typography | `font` on `.bricks-isotope-filters li` |
| `filterTypographyActive` | typography | Typography active | `font` on `.bricks-isotope-filters .active` |
| `filterMargin` | spacing | Margin | `margin` on `.bricks-isotope-filters li` |
| `filterPadding` | spacing | Padding | `padding` on `.bricks-isotope-filters li` |
| `postsNavigation` | checkbox | Show | — |
| `postsNavigationJustifyContent` | justify-content | Alignment | `justify-content` on `.bricks-pagination ul` |
| `postsNavigationHeight` | number | Height | `height` on `.bricks-pagination ul .page-numbers` |
| `postsNavigationWidth` | number | Width | `width` on `.bricks-pagination ul .page-numbers` |
| `postsNavigationGap` | number | Spacing | `gap` on `.bricks-pagination ul` |
| `postsNavigationBackground` | color | Background | `background` on `.bricks-pagination ul .page-numbers` |
| `postsNavigationBorder` | border | Border | `border` on `.bricks-pagination ul .page-numbers` |
| `postsNavigationTypography` | typography | Typography | `font` on `.bricks-pagination .page-numbers` |
| `postsNavigationBackgroundActive` | color | Background | `background` on `.bricks-pagination ul .page-numbers.current` |
| `postsNavigationBorderActive` | border | Border | `border` on `.bricks-pagination ul .page-numbers.current` |
| `postsNavigationTypographyActive` | typography | Typography | `font` on `.bricks-pagination ul .page-numbers.current` |

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
