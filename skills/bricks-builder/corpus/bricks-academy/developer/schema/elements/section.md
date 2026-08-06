---
title: "Section Schema"
description: "Schema for Bricks Section element"
canonical: "https://academy.bricksbuilder.io/developer/schema/elements/section/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/elements/section.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-08-04T12:13:33.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | section |
| `category` | layout |
| `tag` | section |
| `nestable` | true |

<SchemaJson path="elements/section.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `link` | link | Link | — |
| `tag` | select | HTML tag | — |
| `customTag` | text | Custom tag | — |

## Inherited CSS controls

Shared CSS controls available on all elements. Keys are prefixed with `_` and support responsive/pseudo-class variants via colon syntax (e.g. `_typography:tablet_portrait:hover`).

| Key | Type | Label | CSS |
|---|---|---|---|
| `_gridItemColumnSpan` | text | Grid column | `grid-column` |
| `_gridItemRowSpan` | text | Grid row | `grid-row` |
| `_gridItemJustifySelf` | align-items | Justify self | `justify-self` |
| `_display` | select | Display | `display`, `align-items` |
| `_gridGap` | number | Gap | `grid-gap` |
| `_gridTemplateColumns` | text | Grid template columns | `grid-template-columns` |
| `_gridTemplateRows` | text | Grid template rows | `grid-template-rows` |
| `_gridAutoColumns` | text | Grid auto columns | `grid-auto-columns` |
| `_gridAutoRows` | text | Grid auto rows | `grid-auto-rows` |
| `_gridAutoFlow` | select | Grid auto flow | `grid-auto-flow` |
| `_justifyItemsGrid` | justify-content | Justify items | `justify-items` |
| `_alignItemsGrid` | align-items | Align items | `align-items` |
| `_justifyContentGrid` | justify-content | Justify content | `justify-content` |
| `_alignContentGrid` | align-items | Align content | `align-content` |
| `_flexWrap` | select | Flex wrap | `flex-wrap` |
| `_direction` | direction | Direction | `flex-direction` |
| `_alignSelf` | align-items | Align self | `align-self` |
| `_justifyContent` | justify-content | Align main axis | `justify-content` |
| `_alignItems` | align-items | Align cross axis | `align-items` |
| `_columnGap` | number | Column gap | `column-gap` |
| `_rowGap` | number | Row gap | `row-gap` |
| `_flexGrow` | number | Flex grow | `flex-grow` |
| `_flexShrink` | number | Flex shrink | `flex-shrink` |
| `_flexBasis` | text | Flex basis | `flex-basis` |
| `_order` | number | Order | `order` |
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
| `_visibility` | select | Visibility | `visibility` |
| `_overflow` | text | Overflow | `overflow` |
| `_opacity` | number | Opacity | `opacity` |
| `_cursor` | select | Cursor | `cursor` |
| `_isolation` | select | Isolation | `isolation` |
| `_mixBlendMode` | select | Mix blend mode | `mix-blend-mode` |
| `_pointerEvents` | text | Pointer events | `pointer-events` |
| `_perspective` | number | Perspective | `perspective` |
| `_perspectiveOrigin` | text | Perspective origin | `perspective-origin` |
| `_flexDirection` | direction | Direction | `flex-direction` |
| `_gap` | number | Gap | `gap` |
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
