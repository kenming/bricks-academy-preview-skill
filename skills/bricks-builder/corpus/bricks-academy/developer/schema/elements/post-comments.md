---
title: "Comments Schema"
description: "Schema for Bricks Comments element"
canonical: "https://academy.bricksbuilder.io/developer/schema/elements/post-comments/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/elements/post-comments.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-08-20T13:12:40.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | post-comments |
| `category` | single |
| `tag` | div |
| `nestable` | false |

<SchemaJson path="elements/post-comments.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `source` | select | Source | — |
| `title` | checkbox | Show title | — |
| `titleTag` | select | HTML tag | — |
| `titleTypography` | typography | Typography | `font` on `.comments-title` |
| `avatar` | checkbox | Show avatar | — |
| `avatarSize` | number | Size | `margin-left` on `.depth-2`, `margin-left` on `.depth-3` |
| `avatarBorder` | border | Border | `border` on `.avatar` |
| `avatarBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.avatar` |
| `commentAuthorTag` | select | Author | — |
| `commentAuthorTypography` | typography | Author | `font` on `.comment-author .fn` |
| `commentMetaTypography` | typography | Meta | `font` on `.comment-meta` |
| `commentContentTypography` | typography | Content | `font` on `.comment-content` |
| `formTitle` | checkbox | Show | — |
| `formTitleTag` | select | HTML tag | — |
| `formTitleText` | text | Text | — |
| `label` | checkbox | Show | — |
| `labelTypography` | typography | Typography | `font` on `label` |
| `placeholderTypography` | typography | Placeholder typography | `font` on `::placeholder` |
| `cookies` | checkbox | Show | — |
| `cookiesRequired` | checkbox | Required | — |
| `cookiesText` | text | Text | — |
| `fieldKeys` | select | fieldKeys | — |
| `fieldBackgroundColor` | color | Background color | `background-color` on `.form-group input`, `background-color` on `.form-group textarea` |
| `fieldBorder` | border | Border | `border` on `.form-group input`, `border` on `.form-group textarea` |
| `fieldTypography` | typography | Typography | `font` on `.form-group input`, `font` on `.form-group textarea` |
| `fieldResize` | select | Textarea | `resize` on `.form-group textarea` |
| `submitButtonText` | text | Text | — |
| `submitButtonSize` | select | Size | — |
| `submitButtonStyle` | select | Style | — |
| `submitButtonBackgroundColor` | color | Background | `background-color` on `.bricks-button` |
| `submitButtonBorder` | border | Border | `border` on `.bricks-button` |
| `submitButtonTypography` | typography | Typography | `font` on `.bricks-button` |

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
