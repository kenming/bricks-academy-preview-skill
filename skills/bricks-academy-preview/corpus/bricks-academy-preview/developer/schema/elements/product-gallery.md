import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | product-gallery |
| `category` | woocommerce_product |
| `tag` | div |
| `nestable` | false |

<SchemaJson path="elements/product-gallery.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `productImageSize` | select | Product | — |
| `thumbnailImageSize` | select | Thumbnail | — |
| `lightboxImageSize` | select | Lightbox | — |
| `thumbnailPosition` | select | Position | — |
| `itemWidth` | number | Item width | `width` on `&[data-pos="right"] .woocommerce-product-gallery .flex-control-nav`, `width` on `&[data-pos="left"] .woocommerce-product-gallery .flex-control-nav`, `width` on `&[data-pos="right"] .brx-product-gallery-thumbnail-slider`, `width` on `&[data-pos="left"] .brx-product-gallery-thumbnail-slider` |
| `columns` | number | Columns | `grid-template-columns` on `.flex-control-thumbs` |
| `gap` | number | Gap | `gap` on `.flex-control-thumbs`, `gap` on `.woocommerce-product-gallery`, `gap` on `&.thumbnail-slider` |
| `thumbnailOpacity` | number | Opacity | `opacity` on `.woocommerce-product-gallery .flex-control-thumbs img:not(.flex-active)`, `opacity` on `&.thumbnail-slider .brx-product-gallery-thumbnail-slider .woocommerce-product-gallery__image:not(.flex-active-slide) img` |
| `thumbnailActiveOpacity` | number | Opacity | `opacity` on `.woocommerce-product-gallery .flex-control-thumbs img.flex-active`, `opacity` on `&.thumbnail-slider .brx-product-gallery-thumbnail-slider .woocommerce-product-gallery__image.flex-active-slide img` |
| `thumbnailBorder` | border | Border | `border` on `.woocommerce-product-gallery .flex-control-thumbs img`, `border` on `&.thumbnail-slider .brx-product-gallery-thumbnail-slider .woocommerce-product-gallery__image img` |
| `thumbnailActiveBorder` | border | Border | `border` on `.woocommerce-product-gallery .flex-control-thumbs img.flex-active`, `border` on `&.thumbnail-slider .brx-product-gallery-thumbnail-slider .woocommerce-product-gallery__image.flex-active-slide img` |
| `thumbnailSlider` | checkbox | Slider | — |
| `thumbnailWrapperMaxHeight` | number | Slider | `max-height` on `&.thumbnail-slider .brx-product-gallery-thumbnail-slider` |
| `itemMargin` | number | Slider | `margin-inline-end` on `&.thumbnail-slider[data-pos="top"] .brx-product-gallery-thumbnail-slider .woocommerce-product-gallery__image`, `margin-inline-end` on `&.thumbnail-slider[data-pos="bottom"] .brx-product-gallery-thumbnail-slider .woocommerce-product-gallery__image`, `margin-bottom` on `&.thumbnail-slider[data-pos="right"] .brx-product-gallery-thumbnail-slider .woocommerce-product-gallery__image`, `margin-bottom` on `&.thumbnail-slider[data-pos="left"] .brx-product-gallery-thumbnail-slider .woocommerce-product-gallery__image` |
| `maxItems` | number | Max. items | — |
| `prevArrow` | icon | Prev arrow | — |
| `nextArrow` | icon | Next arrow | — |
| `arrowBackground` | color | Background | `background-color` on `.flex-direction-nav a` |
| `arrowBorder` | border | Border | `border` on `.flex-direction-nav a` |
| `arrowColor` | color | Color | `color` on `.flex-direction-nav a` |
| `arrowSize` | number | Size | `font-size` on `.flex-direction-nav a > *`, `height` on `.flex-direction-nav a > svg` |
| `arrowHeight` | number | Height | `height` on `.flex-direction-nav a` |
| `arrowWidth` | number | Width | `width` on `.flex-direction-nav a` |

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
