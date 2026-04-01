import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | slider-nested |
| `category` | media |
| `tag` | div |
| `nestable` | true |

<SchemaJson path="elements/slider-nested.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `optionsType` | select | Options type | — |
| `options` | code | Custom options | — |
| `type` | select | Type | — |
| `direction` | select | Direction | — |
| `keyboard` | select | Keyboard | — |
| `autoHeight` | checkbox | Auto height | — |
| `height` | number | Height | — |
| `gap` | number | Spacing | — |
| `start` | number | Start index | — |
| `perPage` | number | Items to show | — |
| `perMove` | number | Items to scroll | — |
| `speed` | number | Speed in ms | — |
| `focus` | number | Focus | — |
| `autoplay` | checkbox | Autoplay | — |
| `pauseOnHover` | checkbox | Pause on hover | — |
| `pauseOnFocus` | checkbox | Pause on focus | — |
| `interval` | number | Interval in ms | — |
| `rewind` | checkbox | Rewind | — |
| `rewindByDrag` | checkbox | Rewind by drag | — |
| `rewindSpeed` | number | Speed in ms | — |
| `slidePadding` | spacing | Padding | `padding` on `.splide__slide` |
| `slideAlignHorizontal` | align-items | Align horizontal | `align-items` on `.splide__slide` |
| `slideAlignVertical` | justify-content | Align vertical | `justify-content` on `.splide__slide` |
| `slideBackground` | background | Background | `background` on `.splide__slide` |
| `slideBorder` | border | Border | `border` on `.splide__slide` |
| `arrows` | checkbox | Show | — |
| `arrowHeight` | number | Height | `height` on `.splide__arrow` |
| `arrowWidth` | number | Width | `width` on `.splide__arrow` |
| `arrowBackground` | color | Background | `background-color` on `.splide__arrow` |
| `arrowBorder` | border | Border | `border` on `.splide__arrow` |
| `arrowColor` | color | Color | `color` on `.splide__arrow`, `fill` on `.splide__arrow svg` |
| `arrowSize` | number | Size | `font-size` on `.splide__arrow`, `height` on `.splide__arrow svg`, `width` on `.splide__arrow svg`, `min-height` on `.splide__arrow`, `min-width` on `.splide__arrow` |
| `arrowTextShadow` | text-shadow | Text shadow | `text-shadow` on `.splide__arrow` |
| `arrowDisabledBackground` | color | Background | `background-color` on `.splide__arrow:disabled` |
| `arrowDisabledBorder` | border | Border | `border` on `.splide__arrow:disabled` |
| `arrowDisabledColor` | color | Color | `color` on `.splide__arrow:disabled`, `fill` on `.splide__arrow:disabled svg` |
| `arrowDisabledOpacity` | number | Opacity | `opacity` on `.splide__arrow:disabled` |
| `prevArrow` | icon | Prev arrow | `—` on `.splide__arrow--prev > *` |
| `prevArrowTop` | number | Top | `top` on `.splide__arrow--prev` |
| `prevArrowRight` | number | Right | `right` on `.splide__arrow--prev` |
| `prevArrowBottom` | number | Bottom | `bottom` on `.splide__arrow--prev` |
| `prevArrowLeft` | number | Left | `left` on `.splide__arrow--prev` |
| `prevArrowTransform` | transform | Transform | `transform` on `.splide__arrow--prev` |
| `nextArrow` | icon | Next arrow | `—` on `.splide__arrow--next > *` |
| `nextArrowTop` | number | Top | `top` on `.splide__arrow--next` |
| `nextArrowRight` | number | Right | `right` on `.splide__arrow--next` |
| `nextArrowBottom` | number | Bottom | `bottom` on `.splide__arrow--next` |
| `nextArrowLeft` | number | Left | `left` on `.splide__arrow--next` |
| `nextArrowTransform` | transform | Transform | `transform` on `.splide__arrow--next` |
| `pagination` | checkbox | Show | — |
| `paginationSpacing` | spacing | Margin | `margin` on `.splide__pagination .splide__pagination__page` |
| `paginationHeight` | number | Height | `height` on `.splide__pagination .splide__pagination__page` |
| `paginationWidth` | number | Width | `width` on `.splide__pagination .splide__pagination__page` |
| `paginationColor` | color | Color | `color` on `.splide__pagination .splide__pagination__page`, `background-color` on `.splide__pagination .splide__pagination__page` |
| `paginationBorder` | border | Border | `border` on `.splide__pagination .splide__pagination__page` |
| `paginationHeightActive` | number | Height | `height` on `.splide__pagination .splide__pagination__page.is-active` |
| `paginationWidthActive` | number | Width | `width` on `.splide__pagination .splide__pagination__page.is-active` |
| `paginationColorActive` | color | Color | `color` on `.splide__pagination .splide__pagination__page.is-active`, `background-color` on `.splide__pagination .splide__pagination__page.is-active` |
| `paginationBorderActive` | border | Border | `border` on `.splide__pagination .splide__pagination__page.is-active` |
| `paginationTop` | number | Top | `top` on `.splide__pagination`, `bottom` on `.splide__pagination` |
| `paginationRight` | number | Right | `right` on `.splide__pagination`, `left` on `.splide__pagination`, `transform` on `.splide__pagination` |
| `paginationBottom` | number | Bottom | `bottom` on `.splide__pagination` |
| `paginationLeft` | number | Left | `left` on `.splide__pagination`, `right` on `.splide__pagination`, `transform` on `.splide__pagination` |

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
