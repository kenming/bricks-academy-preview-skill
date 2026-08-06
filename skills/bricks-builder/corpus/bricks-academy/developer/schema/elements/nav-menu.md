---
title: "Nav Menu Schema"
description: "Schema for Bricks Nav Menu element"
canonical: "https://academy.bricksbuilder.io/developer/schema/elements/nav-menu/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/elements/nav-menu.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-08-04T12:13:33.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | nav-menu |
| `category` | wordpress |
| `tag` | div |
| `nestable` | false |

<SchemaJson path="elements/nav-menu.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `menu` | select | Menu | — |
| `menuAlignment` | direction | Alignment | `flex-direction` on `.bricks-nav-menu` |
| `menuJustifyContent` | justify-content | Justify content | `justify-content` on `.bricks-nav-menu > li > a`, `justify-content` on `.bricks-nav-menu > li > .brx-submenu-toggle` |
| `menuGap` | number | Gap | `gap` on `.bricks-nav-menu` |
| `menuMargin` | spacing | Margin | `margin` on `.bricks-nav-menu > li` |
| `menuPadding` | spacing | Padding | `padding` on `.bricks-nav-menu > li > a`, `padding` on `.bricks-nav-menu > li > .brx-submenu-toggle > *` |
| `menuBackground` | background | Background | `background` on `.bricks-nav-menu > li\{pseudo\} > a`, `background` on `.bricks-nav-menu > li\{pseudo\} > .brx-submenu-toggle` |
| `menuBorder` | border | Border | `border` on `.bricks-nav-menu > li\{pseudo\} > a`, `border` on `.bricks-nav-menu > li\{pseudo\} > .brx-submenu-toggle` |
| `menuTypography` | typography | Typography | `font` on `.bricks-nav-menu > li\{pseudo\} > a`, `font` on `.bricks-nav-menu > li\{pseudo\} > .brx-submenu-toggle > *` |
| `menuActiveBackground` | background | Active background | `background` on `.bricks-nav-menu > .current-menu-item > a`, `background` on `.bricks-nav-menu > .current-menu-item > .brx-submenu-toggle`, `background` on `.bricks-nav-menu > .current-menu-parent > a`, `background` on `.bricks-nav-menu > .current-menu-parent > .brx-submenu-toggle`, `background` on `.bricks-nav-menu > .current-menu-ancestor > a`, `background` on `.bricks-nav-menu > .current-menu-ancestor > .brx-submenu-toggle` |
| `menuActiveBorder` | border | Active border | `border` on `.bricks-nav-menu .current-menu-item > a`, `border` on `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle`, `border` on `.bricks-nav-menu > .current-menu-parent > a`, `border` on `.bricks-nav-menu > .current-menu-parent > .brx-submenu-toggle`, `border` on `.bricks-nav-menu > .current-menu-ancestor > a`, `border` on `.bricks-nav-menu > .current-menu-ancestor > .brx-submenu-toggle` |
| `menuActiveTypography` | typography | Active typography | `font` on `.bricks-nav-menu .current-menu-item > a`, `font` on `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle > *`, `font` on `.bricks-nav-menu > .current-menu-parent > a`, `font` on `.bricks-nav-menu > .current-menu-parent > .brx-submenu-toggle > *`, `font` on `.bricks-nav-menu > .current-menu-ancestor > a`, `font` on `.bricks-nav-menu > .current-menu-ancestor > .brx-submenu-toggle > *` |
| `menuIcon` | icon | Icon | `—` on `.bricks-nav-menu > li.menu-item > .brx-submenu-toggle svg` |
| `menuIconTransform` | transform | Icon transform | `transform` on `.bricks-nav-menu button[aria-expanded="false"] > *` |
| `menuIconTransformOpen` | transform | Icon transform | `transform` on `.bricks-nav-menu button[aria-expanded="true"] > *` |
| `menuIconTypography` | typography | Icon typography | `font` on `.bricks-nav-menu > li.menu-item-has-children > .brx-submenu-toggle\{pseudo\} button[aria-expanded]` |
| `menuIconPosition` | select | Icon position | — |
| `menuIconMargin` | spacing | Icon margin | `margin` on `.bricks-nav-menu .brx-submenu-toggle button` |
| `menuIconPadding` | spacing | Icon padding | `padding` on `.bricks-nav-menu .brx-submenu-toggle button` |
| `submenuStatic` | checkbox | Position | — |
| `subMenuBackgroundList` | background | Background | `background` on `.bricks-nav-menu .sub-menu` |
| `subMenuBorder` | border | Border | `border` on `.bricks-nav-menu .sub-menu` |
| `subMenuBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.bricks-nav-menu .sub-menu` |
| `subMenuTransform` | transform | Transform | `transform` on `.bricks-nav-menu > li > .sub-menu`, `transform` on `.bricks-nav-menu > li > .brx-megamenu` |
| `subMenuTransformOpen` | transform | Transform | `transform` on `.bricks-nav-menu > li.open > .sub-menu`, `transform` on `.bricks-nav-menu > li.open > .brx-megamenu` |
| `caretSize` | number | Size | `border-width` |
| `caretColor` | color | Color | `border-bottom-color` |
| `caretTransform` | transform | Transform | `transform` |
| `caretPosition` | dimensions | Position | — |
| `subMenuJustifyContent` | justify-content | Justify content | `justify-content` on `.bricks-nav-menu .sub-menu a`, `justify-content` on `.bricks-nav-menu .sub-menu button` |
| `subMenuPadding` | spacing | Padding | `padding` on `.bricks-nav-menu .sub-menu a`, `padding` on `.bricks-nav-menu .sub-menu button` |
| `subMenuBackground` | background | Background | `background` on `.bricks-nav-menu .sub-menu .menu-item` |
| `subMenuItemBorder` | border | Border | `border` on `.bricks-nav-menu .sub-menu > li` |
| `subMenuTypography` | typography | Typography | `font` on `.bricks-nav-menu .sub-menu > li\{pseudo\} > a`, `font` on `.bricks-nav-menu .sub-menu > li\{pseudo\} > .brx-submenu-toggle > *` |
| `subMenuActiveBackground` | background | Active background | `background` on `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `background` on `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle`, `background` on `.bricks-nav-menu .sub-menu > .current-menu-ancestor > a`, `background` on `.bricks-nav-menu .sub-menu > .current-menu-ancestor > .brx-submenu-toggle` |
| `subMenuActiveBorder` | border | Active border | `border` on `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `border` on `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle`, `border` on `.bricks-nav-menu .sub-menu > .current-menu-ancestor > a`, `border` on `.bricks-nav-menu .sub-menu > .current-menu-ancestor > .brx-submenu-toggle` |
| `subMenuActiveTypography` | typography | Active typography | `font` on `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `font` on `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle > *`, `font` on `.bricks-nav-menu .sub-menu > .current-menu-ancestor > a`, `font` on `.bricks-nav-menu .sub-menu > .current-menu-ancestor > .brx-submenu-toggle > *` |
| `subMenuIcon` | icon | Icon | `—` on `.bricks-nav-menu .sub-menu .brx-submenu-toggle\{pseudo\} svg` |
| `subMenuIconSize` | number | Icon size | `height` on `.bricks-nav-menu .sub-menu .brx-submenu-toggle svg`, `width` on `.bricks-nav-menu .sub-menu .brx-submenu-toggle svg`, `font-size` on `.bricks-nav-menu .sub-menu .brx-submenu-toggle i` |
| `subMenuIconTransform` | transform | Icon transform | `transform` on `.bricks-nav-menu .sub-menu button > *` |
| `subMenuIconTransformOpen` | transform | Icon transform | `transform` on `.bricks-nav-menu .sub-menu button[aria-expanded="true"] > *` |
| `subMenuIconTypography` | typography | Icon typography | `font` on `.bricks-nav-menu .sub-menu .brx-submenu-toggle > a\{pseudo\} + button` |
| `subMenuIconPosition` | select | Icon position | — |
| `subMenuIconMargin` | spacing | Icon margin | `margin` on `.bricks-nav-menu .sub-menu .brx-submenu-toggle button` |
| `subMenuIconPadding` | spacing | Icon padding | `padding` on `.bricks-nav-menu .sub-menu .brx-submenu-toggle button` |
| `mobileMenu` | select | mobileMenu | — |
| `mobileMenuCustomBreakpoint` | number | Custom breakpoint | — |
| `mobileMenuPosition` | select | Position | — |
| `mobileMenuTop` | number | Top | `top` on `.bricks-mobile-menu-wrapper` |
| `mobileMenuWidth` | number | Width | `width` on `.bricks-mobile-menu-wrapper` |
| `mobileMenuHeight` | number | Height | `height` on `.bricks-mobile-menu-wrapper` |
| `mobileMenuFadeIn` | checkbox | Fade in | — |
| `mobileMenuAlignment` | justify-content | Vertical | `justify-content` on `.bricks-mobile-menu-wrapper` |
| `mobileMenuAlignItems` | align-items | Horizontal | `align-items` on `.bricks-mobile-menu-wrapper`, `justify-content` on `.bricks-mobile-menu-wrapper .brx-submenu-toggle`, `width` on `.bricks-mobile-menu-wrapper a` |
| `mobileMenuTextAlign` | text-align | Text align | `text-align` on `.bricks-mobile-menu-wrapper` |
| `mobileMenuBackground` | background | Background | `background` on `.bricks-mobile-menu-wrapper:before` |
| `mobileMenuBackgroundFilters` | filters | Background filters | `filter` on `.bricks-mobile-menu-wrapper:before` |
| `mobileMenuBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.bricks-mobile-menu-wrapper:before` |
| `mobileMenuOverlay` | background | Overlay | `background` on `.bricks-mobile-menu-overlay` |
| `mobileMenuPadding` | spacing | Padding | `padding` on `.bricks-mobile-menu > li > a`, `padding` on `.bricks-mobile-menu > li > .brx-submenu-toggle > *` |
| `mobileMenuItemBackground` | color | Background | `background-color` on `.bricks-mobile-menu > li > a`, `background-color` on `.bricks-mobile-menu > li > .brx-submenu-toggle` |
| `mobileMenuItemBackgroundActive` | color | Background | `background-color` on `.bricks-mobile-menu > li > a[aria-current="page"]`, `background-color` on `.bricks-mobile-menu > .current-menu-item > .brx-submenu-toggle` |
| `mobileMenuBorder` | border | Border | `border` on `.bricks-mobile-menu > li > a`, `background-color` on `.bricks-mobile-menu > li > .brx-submenu-toggle` |
| `mobileMenuActiveBorder` | border | Border | `border` on `.bricks-mobile-menu > .current-menu-item > a`, `border` on `.bricks-mobile-menu > .current-menu-item > .brx-submenu-toggle`, `border` on `.bricks-mobile-menu > .current-menu-ancestor > .brx-submenu-toggle` |
| `mobileMenuTypography` | typography | Typography | `font` on `.bricks-mobile-menu > li > a`, `font` on `.bricks-mobile-menu > li > .brx-submenu-toggle > *` |
| `mobileMenuActiveTypography` | typography | Typography | `font` on `.bricks-mobile-menu [aria-current="page"]`, `font` on `.bricks-mobile-menu [aria-current="page"] + button`, `font` on `.bricks-mobile-menu > .current-menu-item > a`, `font` on `.bricks-mobile-menu > .current-menu-parent > a`, `font` on `.bricks-mobile-menu > .current-menu-item > .brx-submenu-toggle > *`, `font` on `.bricks-mobile-menu > .current-menu-parent > .brx-submenu-toggle > *` |
| `mobileMenuIcon` | icon | Icon | `—` on `.bricks-mobile-menu-wrapper .brx-submenu-toggle svg` |
| `mobileMenuCloseIcon` | icon | Close icon | `—` on `.bricks-mobile-menu-wrapper .brx-submenu-toggle svg.close` |
| `mobileMenuIconTypography` | typography | Icon typography | `font` on `.bricks-mobile-menu > .menu-item-has-children .brx-submenu-toggle button` |
| `mobileMenuIconPosition` | select | Icon position | — |
| `mobileMenuIconMargin` | spacing | Icon margin | `margin` on `.bricks-mobile-menu .menu-item-has-children .brx-submenu-toggle button` |
| `mobileSubMenuPadding` | spacing | Padding | `padding` on `.bricks-mobile-menu .sub-menu > .menu-item > a`, `padding` on `.bricks-mobile-menu .sub-menu > .menu-item > .brx-submenu-toggle > *` |
| `mobileSubMenuItemBackground` | color | Background | `background-color` on `.bricks-mobile-menu .sub-menu > .menu-item > a`, `background-color` on `.bricks-mobile-menu .sub-menu > .menu-item > .brx-submenu-toggle` |
| `mobileSubMenuItemBackgroundActive` | color | Background | `background-color` on `.bricks-mobile-menu .sub-menu > .menu-item > a[aria-current="page"]`, `background-color` on `.bricks-mobile-menu .sub-menu .current-menu-item > .brx-submenu-toggle` |
| `mobileSubMenuBorder` | border | Border | `border` on `.bricks-mobile-menu .sub-menu > .menu-item` |
| `mobileSubMenuBorderActive` | border | Border | `border` on `.bricks-mobile-menu .sub-menu > .current-menu-item > a`, `border` on `.bricks-mobile-menu .sub-menu > .current-menu-item > .brx-submenu-toggle`, `border` on `.bricks-mobile-menu .sub-menu > .current-menu-ancestor > .brx-submenu-toggle` |
| `mobileSubMenuTypography` | typography | Typography | `font` on `.bricks-mobile-menu .sub-menu > li > a`, `font` on `.bricks-mobile-menu .sub-menu > li > .brx-submenu-toggle > *` |
| `mobileSubMenuActiveTypography` | typography | Active typography | `font` on `.bricks-mobile-menu .sub-menu > .current-menu-item > a`, `font` on `.bricks-mobile-menu .sub-menu > .current-menu-item > .brx-submenu-toggle > *` |
| `mobileMenuToggleAriaLabel` | text | aria-label | — |
| `mobileMenuToggleWidth` | number | Toggle width | `width` on `.bricks-mobile-menu-toggle`, `width` on `.bricks-mobile-menu-toggle .bar-top`, `width` on `.bricks-mobile-menu-toggle .bar-center`, `width` on `.bricks-mobile-menu-toggle .bar-bottom` |
| `mobileMenuToggleColor` | color | Color | `color` on `.bricks-mobile-menu-toggle` |
| `mobileMenuToggleHide` | checkbox | Hide close | `display` on `&.show-mobile-menu .bricks-mobile-menu-toggle` |
| `mobileMenuToggleColorClose` | color | Color close | `color` on `&.show-mobile-menu .bricks-mobile-menu-toggle` |
| `mobileMenuToggleClosePosition` | dimensions | Close position | `—` on `&.show-mobile-menu .bricks-mobile-menu-toggle` |
| `megaMenu` | checkbox | Enable | — |
| `megaMenuSelector` | text | CSS selector | — |
| `megaMenuToggleOn` | select | Toggle on | — |
| `megaMenuTransition` | text | Transition | `transition` on `.brx-megamenu` |
| `megaMenuTransform` | transform | Transform | `transform` on `.bricks-nav-menu > .brx-has-megamenu > .brx-megamenu` |
| `megaMenuTransformOpen` | transform | Transform | `transform` on `.bricks-nav-menu > .brx-has-megamenu.open > .brx-megamenu`, `transform` on `.bricks-nav-menu > .brx-has-megamenu.open > .brx-megamenu` |
| `multiLevel` | checkbox | Enable | — |
| `multiLevelBackText` | text | Back | — |
| `multiLevelBackTypography` | typography | Back | `font` on `.brx-multilevel-back` |
| `multiLevelBackground` | color | Back | `background-color` on `.brx-multilevel-back` |

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
