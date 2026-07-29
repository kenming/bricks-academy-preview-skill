---
title: "Instagram Feed Schema"
description: "Schema for Bricks Instagram feed element"
canonical: "https://academy.bricksbuilder.io/developer/schema/elements/instagram-feed/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/elements/instagram-feed.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-07-29T10:15:35.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | instagram-feed |
| `category` | media |
| `tag` | div |
| `nestable` | false |

<SchemaJson path="elements/instagram-feed.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `columns` | number | Columns | `grid-template-columns` on `ul` |
| `numberOfPosts` | number | Posts | — |
| `imageObjectFit` | select | Object fit | `object-fit` on `img` |
| `imageAspectRatio` | text | Aspect ratio | `aspect-ratio` on `img` |
| `imageHeight` | number | Height | `height` on `img` |
| `imageWidth` | number | Width | `width` on `img` |
| `imageGap` | number | Gap | `gap` on `ul` |
| `imageBorder` | border | Border | `border` on `img` |
| `imageLink` | checkbox | Link | — |
| `carouselIcon` | icon | Icon | — |
| `carouselIconColor` | color | Icon color | `color` on `.brx-icon.carousel` |
| `carouselIconSize` | number | Icon size | `height` on `.brx-icon.carousel svg`, `width` on `.brx-icon.carousel svg`, `font-size` on `.brx-icon.carousel` |
| `carouselIconPosition` | dimensions | Icon position | — |
| `videoIcon` | icon | Icon | — |
| `videoIconColor` | color | Icon color | `color` on `.brx-icon.video` |
| `videoIconSize` | number | Icon size | `height` on `.brx-icon.video svg`, `width` on `.brx-icon.video svg`, `font-size` on `.brx-icon.video` |
| `videoIconPosition` | dimensions | Icon position | — |
| `caption` | checkbox | Enable | — |
| `captionBackground` | color | Background color | `background-color` on `.caption` |
| `captionBorder` | border | Border | `border` on `.caption` |
| `captionTypography` | typography | Typography | `font` on `.caption` |
| `followText` | text | Text | — |
| `followPosition` | select | Position | — |
| `followIcon` | icon | Icon | `—` on `.follow-icon` |
| `followTypography` | typography | Typography | `font` on `.follow` |
| `cacheDuration` | select | Duration | — |

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
