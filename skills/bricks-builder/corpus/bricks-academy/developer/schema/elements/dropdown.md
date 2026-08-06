---
title: "Dropdown Schema"
description: "Schema for Bricks Dropdown element"
canonical: "https://academy.bricksbuilder.io/developer/schema/elements/dropdown/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/elements/dropdown.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-08-04T12:13:33.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | dropdown |
| `category` | general |
| `tag` | li |
| `nestable` | true |

<SchemaJson path="elements/dropdown.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `tag` | text | HTML tag | — |
| `text` | text | Text | — |
| `link` | link | Link to | — |
| `ariaLabel` | text | Attribute | — |
| `icon` | icon | Icon | `—` on `.brx-submenu-toggle button > svg` |
| `iconPadding` | spacing | Icon padding | `padding` on `.brx-submenu-toggle button` |
| `gap` | number | Gap | `gap` on `.brx-submenu-toggle` |
| `iconPosition` | select | Icon position | `flex-direction` on `.brx-submenu-toggle` |
| `iconSize` | number | Icon size | `font-size` on `.brx-submenu-toggle button` |
| `iconColor` | color | Icon color | `color` on `.brx-submenu-toggle button` |
| `iconTransform` | transform | Icon transform | `transform` on `.brx-submenu-toggle button` |
| `iconTransformOpen` | transform | Icon transform | `transform` on `.brx-submenu-toggle button[aria-expanded="true"]` |
| `iconTransition` | text | Icon transition | `transition` on `.brx-submenu-toggle button` |
| `caretSize` | number | Size | `border-width` on `> .brx-dropdown-content::before` |
| `caretColor` | color | Color | `border-bottom-color` on `> .brx-dropdown-content::before` |
| `caretTransform` | transform | Transform | `transform` on `> .brx-dropdown-content::before` |
| `caretPosition` | dimensions | Position | `—` on `> .brx-dropdown-content::before` |
| `static` | checkbox | Position | — |
| `toggleOn` | select | Toggle on | — |
| `contentWidth` | number | Min. width | `min-width` on `.brx-dropdown-content` |
| `contentTransition` | text | Transition | `transition` on `> .brx-dropdown-content` |
| `contentTransform` | transform | Transform | `transform` on `> .brx-dropdown-content` |
| `contentTransformOpen` | transform | Transform | `transform` on `&.open > .brx-dropdown-content` |
| `contentBackground` | background | Background | `background` on `.brx-dropdown-content` |
| `contentBorder` | border | Border | `border` on `.brx-dropdown-content` |
| `contentBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.brx-dropdown-content` |
| `contentTypography` | typography | Typography | `font` on `.brx-dropdown-content` |
| `contentItemJustifyContent` | justify-content | Justify content | `justify-content` on `.brx-dropdown-content > li > a`, `justify-content` on `.brx-submenu-toggle`, `width` on `.brx-dropdown-content > li > a`, `width` on `.brx-submenu-toggle a` |
| `contentItemPadding` | spacing | Padding | `padding` on `.brx-dropdown-content > li > a`, `padding` on `.brx-dropdown-content .brx-submenu-toggle > *`, `padding` on `&.brx-has-megamenu .brx-dropdown-content > *` |
| `contentItemBackground` | color | Background | `background-color` on `.brx-dropdown-content > li > a`, `background-color` on `.brx-dropdown-content .brx-submenu-toggle`, `background-color` on `&.brx-has-megamenu .brx-dropdown-content > *` |
| `contentItemBorder` | border | Border | `border` on `.brx-dropdown-content > li > a`, `border` on `.brx-dropdown-content .brx-submenu-toggle`, `border` on `&.brx-has-megamenu .brx-dropdown-content > *` |
| `contentItemTypography` | typography | Typography | `font` on `.brx-dropdown-content > li > a`, `font` on `.brx-dropdown-content .brx-submenu-toggle > *`, `font` on `&.brx-has-megamenu .brx-dropdown-content > *` |
| `contentItemTransition` | text | Transition | `transition` on `.brx-dropdown-content > li`, `transition` on `.brx-dropdown-content > li > a`, `transition` on `.brx-dropdown-content .brx-submenu-toggle`, `transition` on `&.brx-has-megamenu .brx-dropdown-content > *` |
| `contentItemBackgroundActive` | color | Background | `background-color` on `.brx-dropdown-content > li [aria-current="page"]`, `background-color` on `.brx-dropdown-content > li .aria-current`, `background-color` on `&.brx-has-megamenu .brx-dropdown-content [aria-current="page"]` |
| `contentItemBorderActive` | border | Border | `border` on `.brx-dropdown-content > li [aria-current="page"]`, `border` on `.brx-dropdown-content > li .aria-current`, `border` on `&.brx-has-megamenu .brx-dropdown-content [aria-current="page"]` |
| `contentItemTypographyActive` | typography | Typography | `font` on `.brx-dropdown-content > li [aria-current="page"]`, `font` on `.brx-dropdown-content > li .aria-current`, `font` on `&.brx-has-megamenu .brx-dropdown-content [aria-current="page"]` |
| `megaMenu` | checkbox | Enable | — |
| `megaMenuSelector` | text | CSS selector | — |
| `megaMenuSelectorVertical` | text | CSS selector | — |
| `multiLevel` | checkbox | Enable | — |
| `multiLevelBackText` | text | Back | — |
| `multiLevelBackTypography` | typography | Back | `font` on `.brx-multilevel-back` |
| `multiLevelBackBackground` | color | Back | `background-color` on `.brx-multilevel-back` |

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
