---
title: "Theme Styles Schema"
description: "Full schema for Bricks theme styles: per-section controls, types, CSS properties, and selectors."
canonical: "https://academy.bricksbuilder.io/developer/schema/global/theme-styles/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/global/theme-styles.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-08-04T12:13:33.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

Theme styles define global CSS defaults for element types (buttons, headings, typography, etc.) and site-wide settings (colors, links, spacing). They are stored in the `bricks_theme_styles` WordPress option.

## Data structure

Each theme style has a `label` and a `settings` object. The settings object is keyed by section name, and each section contains controls that map to CSS properties.

<SchemaJson path="global/theme-styles.json" />

## Storage

| Data | Option name | PHP constant |
|---|---|---|
| Theme styles | `bricks_theme_styles` | `BRICKS_DB_THEME_STYLES` |

The option value is an associative array keyed by theme style ID (e.g. `"flavor"`), with each entry being a `themeStyle` object.

## Responsive and state variants

Theme style control keys support the same colon syntax as element settings for breakpoint and pseudo-class variants:

```
typography                          → base breakpoint
typography:tablet_portrait          → tablet portrait
typography:mobile_portrait:hover    → mobile + hover
```

## Sections

### Accordion

Section key: `accordion`

Theme style controls for the "accordion" section. Default CSS selector: .brxe-accordion

| Key | Type | Label | CSS |
|---|---|---|---|
| `accordionIcon` | icon | Icon | — |
| `accordionIconExpanded` | icon | Icon expanded | — |
| `titleTypography` | typography | Title typography | `font` on `.accordion-title .title` |
| `subtitleTypography` | typography | Subtitle typography | `font` on `.accordion-subtitle` |
| `contentTypography` | typography | Content typography | `font` on `.accordion-content-wrapper` |

### Alert

Section key: `alert`

Theme style controls for the "alert" section. Default CSS selector: .brxe-alert

| Key | Type | Label | CSS |
|---|---|---|---|
| `padding` | spacing | Padding | `padding` |
| `typography` | typography | Typography | `font` |
| `border` | border | Border | `border` |
| `infoColor` | color | Text color | `color` on `&.info` |
| `infoBackground` | color | Background color | `background-color` on `&.info` |
| `infoBorder` | border | Border | `border` on `&.info` |
| `successColor` | color | Text color | `color` on `&.success` |
| `successBackground` | color | Background color | `background-color` on `&.success` |
| `successBorder` | border | Border | `border` on `&.success` |
| `warningColor` | color | Text color | `color` on `&.warning` |
| `warningBackground` | color | Background color | `background-color` on `&.warning` |
| `warningBorder` | border | Border | `border` on `&.warning` |
| `dangerColor` | color | Text color | `color` on `&.danger` |
| `dangerBackground` | color | Background color | `background-color` on `&.danger` |
| `dangerBorder` | border | Border | `border` on `&.danger` |
| `mutedColor` | color | Text color | `color` on `&.muted` |
| `mutedBackground` | color | Background color | `background-color` on `&.muted` |
| `mutedBorder` | border | Border | `border` on `&.muted` |

### Block

Section key: `block`

Theme style controls for the "block" section. Default CSS selector: .brxe-block

| Key | Type | Label | CSS |
|---|---|---|---|
| `_display` | select | Display | `display` on `.brxe-block:where(:not(.accordion-content-wrapper):not(.accordion-title-wrapper))` |
| `_direction` | direction | Direction | `flex-direction` on `.brxe-block` |
| `_justifyContent` | justify-content | Align main axis | `justify-content` on `.brxe-block` |
| `_alignItems` | align-items | Align cross axis | `align-items` on `.brxe-block` |
| `width` | number | Width | `width` on `.brxe-block` |
| `widthMin` | number | Min. width | `min-width` on `.brxe-block` |
| `widthMax` | number | Max. width | `max-width` on `.brxe-block` |
| `_columnGap` | number | Column gap | `column-gap` on `.brxe-block` |
| `_rowGap` | number | Row gap | `row-gap` on `.brxe-block` |
| `margin` | spacing | Margin | `margin` on `.brxe-block` |
| `padding` | spacing | Padding | `padding` on `.brxe-block` |

### Button

Section key: `button`

Theme style controls for the "button" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `typography` | typography | Typography | `font` on `.bricks-button` |
| `background` | color | Background color | `background-color` on `.bricks-button:not([class*="bricks-background-"]):not([class*="bricks-color-"]):not(.outline)` |
| `border` | border | Border | `border` on `.bricks-button` |
| `boxShadow` | box-shadow | Box shadow | `box-shadow` on `.bricks-button` |
| `transition` | text | Transition | `transition` on `.bricks-button` |
| `outlineBackground` | color | Outline | `background-color` on `.bricks-button.outline` |
| `outlineBorder` | border | Outline | `border` on `.bricks-button.outline` |
| `outlineBoxShadow` | box-shadow | Outline | `box-shadow` on `.bricks-button.outline` |
| `outlineTypography` | typography | Outline | `font` on `.bricks-button.outline` |
| `primaryTypography` | typography | Typography | `font` on `:root .bricks-button[class*="primary"]` |
| `primaryBackground` | color | Background color | `background-color` on `:root .bricks-button[class*="primary"]:not(.outline)` |
| `primaryBorder` | border | Border | `border` on `:root .bricks-button[class*="primary"]` |
| `primaryBoxShadow` | box-shadow | Box shadow | `box-shadow` on `:root .bricks-button[class*="primary"]` |
| `primaryOutlineBackground` | color | Outline | `background-color` on `:root .bricks-button[class*="primary"].outline` |
| `primaryOutlineBorder` | border | Outline | `border` on `:root .bricks-button[class*="primary"].outline` |
| `primaryOutlineBoxShadow` | box-shadow | Outline | `box-shadow` on `:root .bricks-button[class*="primary"].outline` |
| `primaryOutlineTypography` | typography | Outline | `font` on `:root .bricks-button[class*="primary"].outline` |
| `secondaryTypography` | typography | Typography | `font` on `:root .bricks-button[class*="secondary"]` |
| `secondaryBackground` | color | Background color | `background-color` on `:root .bricks-button[class*="secondary"]:not(.outline)` |
| `secondaryBorder` | border | Border | `border` on `:root .bricks-button[class*="secondary"]` |
| `secondaryBoxShadow` | box-shadow | Box shadow | `box-shadow` on `:root .bricks-button[class*="secondary"]` |
| `secondaryOutlineBackground` | color | Outline | `background-color` on `:root .bricks-button[class*="secondary"].outline` |
| `secondaryOutlineBorder` | border | Outline | `border` on `:root .bricks-button[class*="secondary"].outline` |
| `secondaryOutlineBoxShadow` | box-shadow | Outline | `box-shadow` on `:root .bricks-button[class*="secondary"].outline` |
| `secondaryOutlineTypography` | typography | Outline | `font` on `:root .bricks-button[class*="secondary"].outline` |
| `lightTypography` | typography | Typography | `font` on `:root .bricks-button[class*="light"]:not(.bricks-lightbox)` |
| `lightBackground` | color | Background color | `background-color` on `:root .bricks-button[class*="light"]:not(.outline):not(.bricks-lightbox)` |
| `lightBorder` | border | Border | `border` on `:root .bricks-button[class*="light"]:not(.bricks-lightbox)` |
| `lightBoxShadow` | box-shadow | Box shadow | `box-shadow` on `:root .bricks-button[class*="light"]:not(.bricks-lightbox)` |
| `lightOutlineBackground` | color | Outline | `background-color` on `:root .bricks-button[class*="light"].outline` |
| `lightOutlineBorder` | border | Outline | `border` on `:root .bricks-button[class*="light"].outline` |
| `lightOutlineBoxShadow` | box-shadow | Outline | `box-shadow` on `:root .bricks-button[class*="light"].outline` |
| `lightOutlineTypography` | typography | Outline | `font` on `:root .bricks-button[class*="light"].outline` |
| `darkTypography` | typography | Typography | `font` on `:root .bricks-button[class*="dark"]` |
| `darkBackground` | color | Background color | `background-color` on `:root .bricks-button[class*="dark"]:not(.outline)` |
| `darkBorder` | border | Border | `border` on `:root .bricks-button[class*="dark"]` |
| `darkBoxShadow` | box-shadow | Box shadow | `box-shadow` on `:root .bricks-button[class*="dark"]` |
| `darkOutlineBackground` | color | Outline | `background-color` on `:root .bricks-button[class*="dark"].outline` |
| `darkOutlineBorder` | border | Outline | `border` on `:root .bricks-button[class*="dark"].outline` |
| `darkOutlineBoxShadow` | box-shadow | Outline | `box-shadow` on `:root .bricks-button[class*="dark"].outline` |
| `darkOutlineTypography` | typography | Outline | `font` on `:root .bricks-button[class*="dark"].outline` |
| `mutedTypography` | typography | Typography | `font` on `:root .bricks-button[class*="muted"]` |
| `mutedBackground` | color | Background color | `background-color` on `:root .bricks-button[class*="muted"]:not(.outline)` |
| `mutedBorder` | border | Border | `border` on `:root .bricks-button[class*="muted"]` |
| `mutedBoxShadow` | box-shadow | Box shadow | `box-shadow` on `:root .bricks-button[class*="muted"]` |
| `mutedOutlineBackground` | color | Outline | `background-color` on `:root .bricks-button[class*="muted"].outline` |
| `mutedOutlineBorder` | border | Outline | `border` on `:root .bricks-button[class*="muted"].outline` |
| `mutedOutlineBoxShadow` | box-shadow | Outline | `box-shadow` on `:root .bricks-button[class*="muted"].outline` |
| `mutedOutlineTypography` | typography | Outline | `font` on `:root .bricks-button[class*="muted"].outline` |
| `infoTypography` | typography | Typography | `font` on `:root .bricks-button[class*="info"]` |
| `infoBackground` | color | Background color | `background-color` on `:root .bricks-button[class*="info"]:not(.outline)` |
| `infoBorder` | border | Border | `border` on `:root .bricks-button[class*="info"]` |
| `infoBoxShadow` | box-shadow | Box shadow | `box-shadow` on `:root .bricks-button[class*="info"]` |
| `infoOutlineBackground` | color | Outline | `background-color` on `:root .bricks-button[class*="info"].outline` |
| `infoOutlineBorder` | border | Outline | `border` on `:root .bricks-button[class*="info"].outline` |
| `infoOutlineBoxShadow` | box-shadow | Outline | `box-shadow` on `:root .bricks-button[class*="info"].outline` |
| `infoOutlineTypography` | typography | Outline | `font` on `:root .bricks-button[class*="info"].outline` |
| `successTypography` | typography | Typography | `font` on `:root .bricks-button[class*="success"]` |
| `successBackground` | color | Background color | `background-color` on `:root .bricks-button[class*="success"]:not(.outline)` |
| `successBorder` | border | Border | `border` on `:root .bricks-button[class*="success"]` |
| `successBoxShadow` | box-shadow | Box shadow | `box-shadow` on `:root .bricks-button[class*="success"]` |
| `successOutlineBackground` | color | Outline | `background-color` on `:root .bricks-button[class*="success"].outline` |
| `successOutlineBorder` | border | Outline | `border` on `:root .bricks-button[class*="success"].outline` |
| `successOutlineBoxShadow` | box-shadow | Outline | `box-shadow` on `:root .bricks-button[class*="success"].outline` |
| `successOutlineTypography` | typography | Outline | `font` on `:root .bricks-button[class*="success"].outline` |
| `warningTypography` | typography | Typography | `font` on `:root .bricks-button[class*="warning"]` |
| `warningBackground` | color | Background color | `background-color` on `:root .bricks-button[class*="warning"]:not(.outline)` |
| `warningBorder` | border | Border | `border` on `:root .bricks-button[class*="warning"]` |
| `warningBoxShadow` | box-shadow | Box shadow | `box-shadow` on `:root .bricks-button[class*="warning"]` |
| `warningOutlineBackground` | color | Outline | `background-color` on `:root .bricks-button[class*="warning"].outline` |
| `warningOutlineBorder` | border | Outline | `border` on `:root .bricks-button[class*="warning"].outline` |
| `warningOutlineBoxShadow` | box-shadow | Outline | `box-shadow` on `:root .bricks-button[class*="warning"].outline` |
| `warningOutlineTypography` | typography | Outline | `font` on `:root .bricks-button[class*="warning"].outline` |
| `dangerTypography` | typography | Typography | `font` on `:root .bricks-button[class*="danger"]` |
| `dangerBackground` | color | Background color | `background-color` on `:root .bricks-button[class*="danger"]:not(.outline)` |
| `dangerBorder` | border | Border | `border` on `:root .bricks-button[class*="danger"]` |
| `dangerBoxShadow` | box-shadow | Box shadow | `box-shadow` on `:root .bricks-button[class*="danger"]` |
| `dangerOutlineBackground` | color | Outline | `background-color` on `:root .bricks-button[class*="danger"].outline` |
| `dangerOutlineBorder` | border | Outline | `border` on `:root .bricks-button[class*="danger"].outline` |
| `dangerOutlineBoxShadow` | box-shadow | Outline | `box-shadow` on `:root .bricks-button[class*="danger"].outline` |
| `dangerOutlineTypography` | typography | Outline | `font` on `:root .bricks-button[class*="danger"].outline` |
| `sizeDefaultPadding` | spacing | Padding | `padding` on `.bricks-button` |
| `sizeSmPadding` | spacing | Padding | `padding` on `.bricks-button.sm` |
| `sizeSmTypography` | typography | Typography | `font` on `.bricks-button.sm` |
| `sizeMdPadding` | spacing | Padding | `padding` on `.bricks-button.md` |
| `sizeMdTypography` | typography | Typography | `font` on `.bricks-button.md` |
| `sizeLgPadding` | spacing | Padding | `padding` on `.bricks-button.lg` |
| `sizeLgTypography` | typography | Typography | `font` on `.bricks-button.lg` |
| `sizeXlPadding` | spacing | Padding | `padding` on `.bricks-button.xl` |
| `sizeXlTypography` | typography | Typography | `font` on `.bricks-button.xl` |

### Carousel

Section key: `carousel`

No typed controls extracted for this section. It uses the generic theme style control map.

### Code

Section key: `code`

Theme style controls for the "code" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `prettify` | select | Theme | — |

### Colors

Section key: `colors`

Theme style controls for the "colors" section. Default CSS selector: :where(:root)

| Key | Type | Label | CSS |
|---|---|---|---|
| `colorPrimary` | color | Primary color | `color` on `.bricks-color-primary`, `background-color` on `.bricks-background-primary` |
| `colorSecondary` | color | Secondary color | `color` on `.bricks-color-secondary`, `background-color` on `.bricks-background-secondary` |
| `colorLight` | color | Light color | `color` on `.bricks-color-light`, `background-color` on `.bricks-background-light` |
| `colorDark` | color | Dark color | `color` on `.bricks-color-dark`, `background-color` on `.bricks-background-dark` |
| `colorMuted` | color | Muted color | `color` on `.bricks-color-muted`, `background-color` on `.bricks-background-muted` |
| `colorBorder` | color | Border color | `border-color` on `*` |
| `colorInfo` | color | Info color | `color` on `.bricks-color-info`, `background-color` on `.bricks-background-info` |
| `colorSuccess` | color | Success color | `color` on `.bricks-color-success`, `background-color` on `.bricks-background-success` |
| `colorWarning` | color | Warning color | `color` on `.bricks-color-warning`, `background-color` on `.bricks-background-warning` |
| `colorDanger` | color | Danger color | `color` on `.bricks-color-danger`, `background-color` on `.bricks-background-danger` |

### Conditions

Section key: `conditions`

Theme style controls for the "conditions" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `conditions` | repeater | Style conditions | — |

### Container

Section key: `container`

Theme style controls for the "container" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `_display` | select | Display | `display` on `.brxe-container` |
| `_direction` | direction | Direction | `flex-direction` on `.brxe-container` |
| `_justifyContent` | justify-content | Align main axis | `justify-content` on `.brxe-container` |
| `_alignItems` | align-items | Align cross axis | `align-items` on `.brxe-container` |
| `width` | number | Width | `width` on `.brxe-container`, `width` on `.woocommerce main.site-main`, `width` on `#brx-content.wordpress` |
| `widthMin` | number | Min. width | `min-width` on `.brxe-container`, `min-width` on `#brx-content.wordpress` |
| `widthMax` | number | Max. width | `max-width` on `.brxe-container`, `max-width` on `#brx-content.wordpress` |
| `_columnGap` | number | Column gap | `column-gap` on `.brxe-container` |
| `_rowGap` | number | Row gap | `row-gap` on `.brxe-container` |
| `margin` | spacing | Margin | `margin` on `.brxe-container` |
| `padding` | spacing | Padding | `padding` on `.brxe-container` |

### Content

Section key: `content`

Theme style controls for the "content" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `contentMargin` | spacing | Margin | `margin` on `#brx-content`, `margin` on `.content-area` |
| `contentBlockquoteMargin` | spacing | Margin | `margin` on `blockquote` |
| `contentBlockquotePadding` | spacing | Padding | `padding` on `blockquote` |
| `contentBlockquoteBorder` | border | Border | `border` on `blockquote` |
| `contentBlockquoteTypography` | typography | Typography | `font` on `blockquote` |

### Contextual-spacing

Section key: `contextual-spacing`

No typed controls extracted for this section. It uses the generic theme style control map.

### Contextual Spacing

Section key: `contextualSpacing`

Theme style controls for the "contextualSpacing" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `contextualSpacingRemoveDefaultMargins` | select | Remove default margins | — |
| `contextualSpacingRemoveDefaultPadding` | select | Remove default padding | — |
| `contextualSpacingHeading` | number | Heading | `margin-block-start` |
| `contextualSpacingParagraph` | number | Paragraph | `margin-block-start` |
| `contextualSpacingFallback` | number | Fallback spacing | `margin-block-start` |
| `contextualSpacingCustomTarget` | repeater | Selector | `margin-block-start` |
| `contextualSpacingApplyTo` | text | contextualSpacingApplyTo | — |

### Counter

Section key: `counter`

Theme style controls for the "counter" section. Default CSS selector: .brxe-counter

| Key | Type | Label | CSS |
|---|---|---|---|
| `typography` | typography | Typography | `font` |

### Css

Section key: `css`

No typed controls extracted for this section. It uses the generic theme style control map.

### Div

Section key: `div`

Theme style controls for the "div" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `_display` | select | Display | `display` on `.brxe-div:where(:not(.brx-dropdown-content))` |
| `_direction` | direction | Direction | `flex-direction` on `.brxe-div` |
| `_justifyContent` | justify-content | Align main axis | `justify-content` on `.brxe-div` |
| `_alignItems` | align-items | Align cross axis | `align-items` on `.brxe-div` |
| `width` | number | Width | `width` on `.brxe-div` |
| `widthMin` | number | Min. width | `min-width` on `.brxe-div` |
| `widthMax` | number | Max. width | `max-width` on `.brxe-div` |
| `_columnGap` | number | Column gap | `column-gap` on `.brxe-div` |
| `_rowGap` | number | Row gap | `row-gap` on `.brxe-div` |
| `margin` | spacing | Margin | `margin` on `.brxe-div` |
| `padding` | spacing | Padding | `padding` on `.brxe-div` |

### Divider

Section key: `divider`

Theme style controls for the "divider" section. Default CSS selector: .brxe-divider

| Key | Type | Label | CSS |
|---|---|---|---|
| `height` | number | Height | `border-top-width` on `.line` |
| `color` | color | Color | `border-top-color` on `&.horizontal .line`, `border-right-color` on `&.vertical .line`, `color` on `.icon i` |

### Elements

Section key: `elements`

No typed controls extracted for this section. It uses the generic theme style control map.

### Form

Section key: `form`

Theme style controls for the "form" section. Default CSS selector: .brxe-form

| Key | Type | Label | CSS |
|---|---|---|---|
| `labelTypography` | typography | Label typography | `font` on `.form-group label`, `font` on `.form-group .label` |
| `placeholderTypography` | typography | Placeholder typography | `font` on `::placeholder`, `font` on `select` |
| `fieldTypography` | typography | Typography | `font` on `.form-group input`, `font` on `select`, `font` on `textarea` |
| `fieldBackgroundColor` | color | Background color | `background-color` on `.form-group input`, `background-color` on `.flatpickr`, `background-color` on `select`, `background-color` on `textarea` |
| `fieldBorder` | border | Border | `border` on `.form-group input`, `border` on `.flatpickr`, `border` on `select`, `border` on `textarea`, `border` on `.bricks-button`, `border` on `.choose-files` |
| `fieldMargin` | spacing | Spacing | `padding` on `.form-group` |
| `fieldPadding` | spacing | Padding | `padding` on `.form-group input`, `padding` on `.flatpickr`, `padding` on `select`, `padding` on `textarea` |
| `submitButtonPadding` | spacing | Padding | `padding` on `.bricks-button` |
| `submitButtonTypography` | typography | Typography | `font` on `.bricks-button` |
| `submitButtonBackgroundColor` | color | Background color | `background-color` on `.bricks-button` |
| `submitButtonBorder` | border | Border | `border` on `.bricks-button` |

### General

Section key: `general`

Theme style controls for the "general" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `siteLayout` | select | Site layout | — |
| `siteLayoutBoxedMaxWidth` | number | Boxed max. width | `max-width` on `.brx-boxed`, `max-width` on `.brx-boxed #brx-header.brx-sticky`, `margin-left` on `.brx-boxed #brx-header.brx-sticky`, `margin-right` on `.brx-boxed #brx-header.brx-sticky` |
| `contentBoxShadow` | box-shadow | Content box shadow | `box-shadow` on `.brx-boxed` |
| `contentBackground` | background | Content background | `background` on `.brx-boxed` |
| `siteBackground` | background | Site background | `background` on `html`, `background` on `body` |
| `siteBorder` | border | Site border | `border` on `.brx-boxed` |
| `elementMargin` | spacing | Element margin | `margin` on `[class*="brxe-"]:not(.brxe-section):not(.brxe-container):not(.brxe-div)` |
| `sectionMargin` | spacing | Root container margin | `margin` on `.brxe-container.root` |
| `sectionPadding` | spacing | Root container padding | `padding` on `.brxe-container.root:not(.stretch)`, `padding` on `.brxe-container.root.stretch > .brxe-container`, `padding` on `.brxe-container.root.stretch > .brxe-div` |
| `containerMaxWidth` | number | Root container width | `width` on `.brxe-container.root`, `width` on `.brxe-container.root.stretch > .brxe-container`, `width` on `.brxe-container.root.stretch > .brxe-div`, `width` on `.woocommerce main.site-main`, `width` on `#brx-content.wordpress` |
| `lightboxBackground` | background | Background | `background` on `.pswp .pswp__bg` |
| `lightboxCloseColor` | color | Close color | `color` on `.pswp.brx .pswp__top-bar button.pswp__button--close svg` |
| `lightboxCloseSize` | number | Close size | `width` on `.pswp.brx .pswp__top-bar button.pswp__button svg`, `height` on `.pswp.brx .pswp__top-bar button.pswp__button svg` |
| `lightboxWidth` | number | Width | — |
| `lightboxHeight` | number | Height | — |

### Heading

Section key: `heading`

Theme style controls for the "heading" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `tag` | select | HTML tag | — |
| `separator` | select | Separator | — |
| `separatorWidth` | number | Width | `width` on `.brxe-heading .separator`, `flex-grow` on `.brxe-heading .separator` |
| `separatorHeight` | number | Height | `border-top-width` on `.brxe-heading .separator` |
| `separatorSpacing` | number | Spacing | `gap` on `.brxe-heading.has-separator` |
| `separatorAlignItems` | align-items | Align | `align-items` on `.brxe-heading.has-separator` |
| `separatorStyle` | select | Style | `border-top-style` on `.brxe-heading .separator` |
| `separatorColor` | color | Color | `border-top-color` on `.brxe-heading .separator` |
| `separatorMargin` | spacing | Margin | `margin` on `.brxe-heading .separator` |

### Icon-box

Section key: `icon-box`

Theme style controls for the "icon-box" section. Default CSS selector: .brxe-icon-box

| Key | Type | Label | CSS |
|---|---|---|---|
| `verticalAlign` | align-items | Icon align | `align-self` on `.icon` |
| `iconMargin` | spacing | Icon margin | `margin` on `.icon` |
| `iconPadding` | spacing | Icon padding | `padding` on `.icon` |
| `textAlign` | text-align | Text align | `text-align`, `align-self` on `.icon` |
| `iconSize` | number | Icon size | `font-size` on `.icon i` |
| `iconHeight` | number | Icon height | `height` on `.icon`, `line-height` on `.icon` |
| `iconWidth` | number | Icon width | `min-width` on `.icon` |
| `iconColor` | color | Icon color | `color` on `.icon`, `color` on `.icon a` |
| `iconBackgroundColor` | color | Icon background | `background-color` on `.icon` |
| `iconBorder` | border | Icon border | `border` on `.icon` |
| `iconBoxShadow` | box-shadow | Icon box shadow | `box-shadow` on `.icon` |
| `typographyHeading` | typography | Heading typography | `font` on `h1`, `font` on `h2`, `font` on `h3`, `font` on `h4`, `font` on `h5`, `font` on `h6` |
| `typographyBody` | typography | Body typography | `font` on `.content` |
| `contentBackgroundColor` | color | Content background | `background-color` on `.content` |
| `contentBorder` | border | Content border | `border` on `.content` |
| `contentBoxShadow` | box-shadow | Content box shadow | `box-shadow` on `.content` |
| `contentMargin` | spacing | Content margin | `margin` on `.content` |
| `contentPadding` | spacing | Content padding | `padding` on `.content` |

### Image

Section key: `image`

Theme style controls for the "image" section. Default CSS selector: .brxe-image

| Key | Type | Label | CSS |
|---|---|---|---|
| `popupIcon` | icon | Icon | — |
| `popupIconBackgroundColor` | color | Icon background color | `background-color` on `.brxe-image .icon` |
| `popupIconBorder` | border | Icon border | `border` on `.brxe-image .icon` |
| `popupIconBoxShadow` | box-shadow | Icon box shadow | `box-shadow` on `.brxe-image .icon` |
| `popupIconHeight` | number | Icon height | `line-height` on `.brxe-image .icon` |
| `popupIconWidth` | number | Icon width | `width` on `.brxe-image .icon` |
| `popupIconTypography` | typography | Icon typography | `font` on `.brxe-image .icon` |
| `caption` | select | Caption type | — |
| `captionCustomStyles` | checkbox | Custom styles | — |
| `captionMargin` | spacing | Margin | `margin` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)` |
| `captionPadding` | spacing | Padding | `padding` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)` |
| `captionPosition` | select | Position | `position` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)`, `position` on `.wp-block-image:has(.wp-element-caption:not(.wp-block-gallery *))` |
| `captionPositions` | dimensions | Position | `—` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)` |
| `captionBackgroundColor` | color | Background color | `background` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)`, `text-shadow` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)` |
| `captionBorder` | border | Border | `border` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)` |
| `captionBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)` |
| `captionTypography` | typography | Typography | `font` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)` |

### Image-gallery

Section key: `image-gallery`

Theme style controls for the "image-gallery" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `layout` | select | Layout | — |
| `imageRatio` | text | Image ratio | `aspect-ratio` on `.image` |
| `columns` | number | Columns | — |
| `imageHeight` | number | Image height | `padding-top` on `.brxe-image-gallery .image` |
| `gutter` | number | Spacing | `--gutter` on `.brxe-image-gallery` |
| `captionMargin` | spacing | Margin | `margin` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption` |
| `captionPadding` | spacing | Padding | `padding` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption` |
| `captionPosition` | select | Position | `position` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption`, `flex` on `.wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption`, `display` on `.wp-block-gallery.has-nested-images figure.wp-block-image:has(figcaption):before` |
| `captionPositions` | dimensions | Position | `—` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption`, `width` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption` |
| `captionBackgroundColor` | color | Background color | `background` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption`, `text-shadow` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption` |
| `captionBorder` | border | Border | `border` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption` |
| `captionBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption` |
| `captionTypography` | typography | Typography | `font` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption` |

### Links

Section key: `links`

Theme style controls for the "links" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `cssSelectors` | textarea | Link | — |
| `typography` | typography | Typography | `font` |
| `background` | background | Background | `background` |
| `border` | border | Border | `border` |
| `padding` | spacing | Padding | `padding` |
| `textDecoration` | text-decoration | Text decoration | `text-decoration` |
| `transition` | text | Transition | `transition` |

### List

Section key: `list`

Theme style controls for the "list" section. Default CSS selector: .brxe-list

| Key | Type | Label | CSS |
|---|---|---|---|
| `itemMargin` | spacing | Margin | `margin` on `li` |
| `itemPadding` | spacing | Padding | `padding` on `li` |
| `itemOddBackground` | color | Odd background | `background-color` on `li:nth-child(odd)` |
| `itemEvenBackground` | color | Even background | `background-color` on `li:nth-child(even)` |
| `itemBorder` | border | Border | `border` on `li` |
| `itemAutoWidth` | checkbox | Auto width | `justify-content` on `.content`, `flex-grow` on `.separator` |
| `highlightBlock` | checkbox | Block | `display` on `li[data-highlight]::before` |
| `highlightLabelPadding` | spacing | Padding | `padding` on `li[data-highlight]::before` |
| `highlightLabelBackground` | color | Background | `background-color` on `li[data-highlight]::before` |
| `highlightLabelBorder` | border | Border | `border` on `li[data-highlight]::before` |
| `highlightLabelTypography` | typography | Typography | `font` on `li[data-highlight]::before` |
| `highlightContentPadding` | spacing | Padding | `padding` on `li[data-highlight] + div` |
| `highlightContentBackground` | color | Background | `background-color` on `li[data-highlight] + div` |
| `highlightContentBorder` | border | Border | `border` on `li[data-highlight] + div` |
| `highlightContentColor` | color | Text color | `color` on `li[data-highlight] + div .title`, `color` on `li[data-highlight] + div .meta`, `color` on `li[data-highlight] + div .description` |
| `titleMargin` | spacing | Margin | `margin` on `.title` |
| `titleTypography` | typography | Typography | `font` on `.title` |
| `metaMargin` | spacing | Margin | `margin` on `.meta` |
| `metaTypography` | typography | Typography | `font` on `.meta` |
| `descriptionTypography` | typography | Typography | `font` on `.description` |
| `separatorDisable` | checkbox | Disable | `display` on `.separator` |
| `separatorStyle` | select | Style | `border-top-style` on `.separator` |
| `separatorWidth` | number | Width | `flex-basis` on `.separator` |
| `separatorHeight` | number | Height | `border-top-width` on `.separator` |
| `separatorColor` | color | Color | `border-top-color` on `.separator` |

### Nav-menu

Section key: `nav-menu`

Theme style controls for the "nav-menu" section. Default CSS selector: .brxe-nav-menu

| Key | Type | Label | CSS |
|---|---|---|---|
| `menuMargin` | spacing | Margin | `margin` on `.bricks-nav-menu > li` |
| `menuPadding` | spacing | Padding | `padding` on `.bricks-nav-menu > li > a`, `padding` on `.bricks-nav-menu > li > .brx-submenu-toggle > *` |
| `menuAlignment` | direction | Alignment | `flex-direction` on `.bricks-nav-menu` |
| `menuTypography` | typography | Typography | `font` on `.bricks-nav-menu > li > a`, `font` on `.bricks-nav-menu > li > .brx-submenu-toggle` |
| `menuActiveTypography` | typography | Active typography | `font` on `.bricks-nav-menu .current-menu-item > a`, `font` on `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle` |
| `menuActiveBorder` | border | Active border | `border` on `.bricks-nav-menu .current-menu-item > a`, `border` on `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle` |
| `subMenuPadding` | spacing | Padding | `padding` on `.bricks-nav-menu .sub-menu a`, `padding` on `.bricks-nav-menu .sub-menu button` |
| `subMenuTypography` | typography | Typography | `font` on `.bricks-nav-menu .sub-menu > li` |
| `subMenuActiveTypography` | typography | Active typography | `font` on `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `font` on `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle` |
| `subMenuBackground` | background | Background | `background` on `.bricks-nav-menu .sub-menu .menu-item` |
| `subMenuBorder` | border | Border | `border` on `.bricks-nav-menu .sub-menu` |
| `subMenuBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.bricks-nav-menu .sub-menu` |

### Popup

Section key: `popup`

No typed controls extracted for this section. It uses the generic theme style control map.

### Popups

Section key: `popups`

No typed controls extracted for this section. It uses the generic theme style control map.

### Post-content

Section key: `post-content`

Theme style controls for the "post-content" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `typography` | typography | Typography | `font` on `.brxe-post-content` |

### Post-meta

Section key: `post-meta`

Theme style controls for the "post-meta" section. Default CSS selector: .brxe-post-meta

| Key | Type | Label | CSS |
|---|---|---|---|
| `padding` | spacing | Padding | `padding` on `.item` |
| `gutter` | number | Gap | `width` on `.separator` |
| `background` | color | Background | `background-color` on `.item` |
| `border` | border | Border | `border` on `.item` |
| `typography` | typography | Typography | `font` on `.item` |

### Post-navigation

Section key: `post-navigation`

Theme style controls for the "post-navigation" section. Default CSS selector: .brxe-post-navigation

| Key | Type | Label | CSS |
|---|---|---|---|
| `titleTypography` | typography | Title typography | `font` on `.title` |
| `labelTypography` | typography | Label typography | `font` on `label` |
| `imageBorder` | border | Image border | `border` on `.image` |

### Post-taxonomy

Section key: `post-taxonomy`

Theme style controls for the "post-taxonomy" section. Default CSS selector: .brxe-post-taxonomy

| Key | Type | Label | CSS |
|---|---|---|---|
| `margin` | spacing | Margin | `margin` on `.bricks-button` |
| `padding` | spacing | Padding | `padding` on `.bricks-button` |
| `background` | color | Background | `background-color` on `.bricks-button` |
| `border` | border | Border | `border` on `.bricks-button` |
| `typography` | typography | Typography | `font` on `.bricks-button` |

### Post-title

Section key: `post-title`

Theme style controls for the "post-title" section. Default CSS selector: .brxe-post-title

| Key | Type | Label | CSS |
|---|---|---|---|
| `typography` | typography | Typography | `font` |

### Pricing-tables

Section key: `pricing-tables`

Theme style controls for the "pricing-tables" section. Default CSS selector: .brxe-pricing-tables

| Key | Type | Label | CSS |
|---|---|---|---|
| `background` | background | Table background | `background` on `.pricing-table` |
| `headerPadding` | spacing | Padding | `padding` on `.pricing-table-header` |
| `headerBackgroundColor` | color | Background color | `background-color` on `.pricing-table-header` |
| `headerBorder` | border | Border | `border` on `.pricing-table-header` |
| `headerTitleTypography` | typography | Title typography | `font` on `.pricing-table-title` |
| `headerSubtitleTypography` | typography | Subtitle typography | `font` on `.pricing-table-subtitle` |
| `pricePadding` | spacing | Padding | `padding` on `.pricing-table-pricing` |
| `priceBackgroundColor` | color | Background color | `background-color` on `.pricing-table-pricing` |
| `priceBorder` | border | Border | `Border` on `.pricing-table-pricing` |
| `priceTypography` | typography | Price typography | `font` on `.pricing-table-price-prefix`, `font` on `.pricing-table-price`, `font` on `.pricing-table-price-suffix` |
| `priceMetaTypography` | typography | Meta typography | `font` on `.pricing-table-price-meta` |
| `priceOriginalTypography` | typography | Original price typography | `font` on `.pricing-table-original-price` |
| `featuresPadding` | spacing | Padding | `padding` on `.pricing-table-feature` |
| `featuresIconColor` | color | Icon color | `color` on `.pricing-table-feature i` |
| `featuresBackgroundColor` | color | Background color | `background-color` on `.pricing-table-feature` |
| `featuresBorder` | border | Border | `border` on `.pricing-table-feature` |
| `featuresTypography` | typography | Features typography | `font` on `.pricing-table-feature` |
| `footerPadding` | spacing | Padding | `padding` on `.pricing-table-footer` |
| `footerBackgroundColor` | color | Background color | `background-color` on `.pricing-table-footer` |
| `footerBorder` | border | Border | `border` on `.pricing-table-footer` |
| `buttonBackgroundColor` | color | Background color | `background-color` on `.bricks-button` |
| `buttonBorder` | border | Border | `border` on `.bricks-button` |
| `buttonTypography` | typography | Typography | `font` on `.bricks-button` |
| `additionalInfoTypography` | typography | Typography | `font` on `.pricing-table-additional-info` |
| `ribbonTextColor` | color | Text color | `color` on `.pricing-table-ribbon-title` |
| `ribbonBackgroundColor` | color | Background color | `background-color` on `.pricing-table-ribbon-title` |

### Progress-bar

Section key: `progress-bar`

Theme style controls for the "progress-bar" section. Default CSS selector: .brxe-progress-bar

| Key | Type | Label | CSS |
|---|---|---|---|
| `height` | number | Height | `height` on `.bar` |
| `barColor` | color | Bar color | `background-color` on `.bar span` |
| `barBackgroundColor` | color | Bar background color | `background-color` on `.bar` |
| `barBorder` | border | Bar border | `border` on `.bar` |
| `labelTypography` | typography | Label typography | `font` on `.label` |
| `percentageTypography` | typography | Percentage typography | `font` on `.percentage` |

### Related-posts

Section key: `related-posts`

Theme style controls for the "related-posts" section. Default CSS selector: .brxe-related-posts

| Key | Type | Label | CSS |
|---|---|---|---|
| `contentBackground` | color | Content background | `background-color` on `.post-content` |
| `contentPadding` | spacing | Content padding | `padding` on `.post-content` |

### Search

Section key: `search`

Theme style controls for the "search" section. Default CSS selector: .brxe-search

| Key | Type | Label | CSS |
|---|---|---|---|
| `inputBackgroundColor` | color | Input background | `background-color` on `input[type=search]` |
| `inputBorder` | border | Input border | `border` on `input[type=search]` |
| `iconBackgroundColor` | color | Icon background | `background-color` on `button` |
| `iconTypography` | typography | Icon typography | `font` on `button` |
| `iconWidth` | number | Icon width | `width` on `button` |

### Section

Section key: `section`

Theme style controls for the "section" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `_display` | select | Display | `display` on `.brxe-section` |
| `_direction` | direction | Direction | `flex-direction` on `.brxe-section` |
| `_justifyContent` | justify-content | Align main axis | `justify-content` on `.brxe-section` |
| `_alignItems` | align-items | Align cross axis | `align-items` on `.brxe-section` |
| `width` | number | Width | `width` on `.brxe-section` |
| `widthMin` | number | Min. width | `min-width` on `.brxe-section` |
| `widthMax` | number | Max. width | `max-width` on `.brxe-section` |
| `_columnGap` | number | Column gap | `column-gap` on `.brxe-section` |
| `_rowGap` | number | Row gap | `row-gap` on `.brxe-section` |
| `margin` | spacing | Margin | `margin` on `.brxe-section` |
| `padding` | spacing | Padding | `padding` on `.brxe-section` |

### Sidebar

Section key: `sidebar`

Theme style controls for the "sidebar" section. Default CSS selector: .brxe-sidebar

| Key | Type | Label | CSS |
|---|---|---|---|
| `margin` | spacing | Widget margin | `margin` on `.bricks-widget-wrapper` |
| `titleTypography` | typography | Widget title | `font` on `.bricks-widget-title`, `font` on `h1`, `font` on `h2`, `font` on `h3`, `font` on `h4`, `font` on `h5`, `font` on `h6` |
| `contentTypography` | typography | Content typography | `font` |
| `searchBackground` | color | Search background color | `background-color` on `input[type=search]` |

### Slider

Section key: `slider`

Theme style controls for the "slider" section. Default CSS selector: .brxe-slider

| Key | Type | Label | CSS |
|---|---|---|---|
| `titleMargin` | spacing | Title margin | `margin` on `.title` |
| `titleTypography` | typography | Title typography | `font` on `.title` |
| `contentWidth` | number | Content width | `width` on `.slider-content` |
| `contentBackgroundColor` | color | Content background | `background-color` on `.slider-content` |
| `contentMargin` | spacing | Content margin | `margin` on `.slider-content` |
| `contentPadding` | spacing | Content padding | `padding` on `.slider-content` |
| `contentAlignHorizontal` | select | Content align horizontal | `justify-content` on `.swiper-slide` |
| `contentAlignVertical` | align-items | Content align vertical | `align-items` on `.swiper-slide` |
| `contentTextAlign` | text-align | Content text align | `text-align` on `.slider-content` |
| `contentTypography` | typography | Content typography | `font` on `.content` |
| `buttonStyle` | select | Style | — |
| `buttonSize` | select | Size | — |
| `buttonBackground` | color | Background | `background-color` on `.bricks-button` |
| `buttonBorder` | border | Border | `border` on `.bricks-button` |
| `buttonBoxshadow` | box-shadow | Box shadow | `box-shadow` on `.bricks-button` |
| `buttonTypography` | typography | Button typography | `color` on `.bricks-button` |
| `backgroundFilters` | filters | CSS Filters | `filter` on `.css-filter` |
| `backgroundPositionTop` | number | Top | `top` on `.image` |
| `backgroundPositionRight` | number | Right | `right` on `.image` |
| `backgroundPositionBottom` | number | Bottom | `bottom` on `.image` |
| `backgroundPositionLeft` | number | Left | `left` on `.image` |

### Social-icons

Section key: `social-icons`

Theme style controls for the "social-icons" section. Default CSS selector: .brxe-social-icons

| Key | Type | Label | CSS |
|---|---|---|---|
| `margin` | spacing | Margin | `margin` on `li` |
| `padding` | spacing | Padding | `padding` on `li` |
| `backgroundColor` | color | Background color | `background-color` on `li` |
| `border` | border | Border | `border` on `li` |
| `typography` | typography | Typography | `font` on `li` |

### Svg

Section key: `svg`

Theme style controls for the "svg" section. Default CSS selector: .brxe-svg

| Key | Type | Label | CSS |
|---|---|---|---|
| `height` | number | Height | `height` |
| `width` | number | Width | `width` |
| `strokeWidth` | number | Stroke width | `stroke-width` on `*` |
| `stroke` | color | Stroke color | `stroke` on `*` |
| `fill` | color | Fill | `fill` on `*` |

### Tabs

Section key: `tabs`

Theme style controls for the "tabs" section. Default CSS selector: .brxe-tabs

| Key | Type | Label | CSS |
|---|---|---|---|
| `titlePadding` | spacing | Padding | `padding` on `.tab-title` |
| `titleTypography` | typography | Typography | `font` on `.tab-title` |
| `titleBackgroundColor` | color | Background | `background-color` on `.tab-title` |
| `titleBorder` | border | Border | `border` on `.tab-title` |
| `titleActiveTypography` | typography | Active typography | `font` on `.tab-title.brx-open` |
| `titleActiveBackgroundColor` | color | Active background | `background-color` on `.tab-title.brx-open` |
| `titleActiveBorder` | border | Active border | `border` on `.tab-title.brx-open` |
| `contentPadding` | spacing | Padding | `padding` on `.tab-content` |
| `contentTextAlign` | select | Text align | `text-align` on `.tab-content` |
| `contentColor` | color | Text color | `color` on `.tab-content` |
| `contentBackgroundColor` | color | Background color | `background-color` on `.tab-content` |
| `contentBorder` | border | Border | `border` on `.tab-content` |

### Team-members

Section key: `team-members`

Theme style controls for the "team-members" section. Default CSS selector: .brxe-team-members

| Key | Type | Label | CSS |
|---|---|---|---|
| `memberGutter` | number | Gap | `gap` |
| `memberBorder` | border | Border | `border` on `.member` |
| `memberBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.member` |
| `memberTitleTypography` | typography | Title typography | `font` on `.title` |
| `memberSubtitleTypography` | typography | Subtitle typography | `font` on `.subtitle` |
| `memberDescriptionTypography` | typography | Description typography | `font` on `.description` |
| `imageBorder` | border | Image border | `border` on `.image` |
| `contentPadding` | spacing | Padding | `padding` on `.content` |
| `contentAlign` | select | Text align | `text-align` on `.content` |
| `contentBackgroundColor` | color | Background | `background-color` on `.member` |

### Testimonials

Section key: `testimonials`

Theme style controls for the "testimonials" section. Default CSS selector: .brxe-testimonials

| Key | Type | Label | CSS |
|---|---|---|---|
| `imageAlign` | select | Image align | `align-items` on `.repeater-item` |
| `imageSize` | number | Image size | `width` on `.image`, `height` on `.image` |
| `imageBorder` | border | Image border | `border` on `.image` |
| `typographyContent` | typography | Testimonial | `font` on `.testimonial-content-wrapper` |
| `typographyName` | typography | Name | `font` on `.testimonial-name` |
| `typographyTitle` | typography | Title | `font` on `.testimonial-title` |

### Text

Section key: `text`

Theme style controls for the "text" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `typography` | typography | Typography | `font` on `.brxe-text`, `font` on `.brxe-text-basic` |

### Text-basic

Section key: `text-basic`

Theme style controls for the "text-basic" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `tag` | select | HTML tag | — |

### Typography

Section key: `typography`

Theme style controls for the "typography" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `typographyHtml` | number | HTML: font-size | `font-size` on `html` |
| `typographyBody` | typography | Body | `font` on `body` |
| `typographyHeadings` | typography | All headings | `font` on `h1, h2, h3, h4, h5, h6` |
| `typographyHeadingH1` | typography | Typography | `font` on `h1` |
| `h1Margin` | spacing | Margin | `margin` on `h1` |
| `typographyHeadingH2` | typography | Typography | `font` on `h2` |
| `h2Margin` | spacing | Margin | `margin` on `h2` |
| `typographyHeadingH3` | typography | Typography | `font` on `h3` |
| `h3Margin` | spacing | Margin | `margin` on `h3` |
| `typographyHeadingH4` | typography | Typography | `font` on `h4` |
| `h4Margin` | spacing | Margin | `margin` on `h4` |
| `typographyHeadingH5` | typography | Typography | `font` on `h5` |
| `h5Margin` | spacing | Margin | `margin` on `h5` |
| `typographyHeadingH6` | typography | Typography | `font` on `h6` |
| `h6Margin` | spacing | Margin | `margin` on `h6` |
| `typographyHero` | typography | Hero | `font` on `.bricks-type-hero` |
| `typographyLead` | typography | Lead | `font` on `.bricks-type-lead` |
| `focusOutline` | text | Focus outline | `outline` on `body.bricks-is-frontend :focus-visible`, `outline` on `@supports not selector(:focus-visible) { body.bricks-is-frontend :focus` |
| `blockquoteMargin` | spacing | Blockquote margin | `margin` on `blockquote` |
| `blockquotePadding` | spacing | Blockquote padding | `padding` on `blockquote` |
| `blockquoteBorder` | border | Blockquote border | `border` on `blockquote` |
| `blockquoteTypography` | typography | Blockquote typography | `font` on `blockquote` |

### Video

Section key: `video`

Theme style controls for the "video" section. Default CSS selector: .brxe-video

| Key | Type | Label | CSS |
|---|---|---|---|
| `previewImageFallback` | image | Fallback preview image | — |
| `boxShadow` | box-shadow | Box shadow | `box-shadow` |
| `overlay` | background | Overlay | `background` on `.bricks-video-overlay` |
| `overlayIcon` | icon | Icon | `—` on `.bricks-video-overlay-icon` |
| `overlayIconTypography` | typography | Icon typography | `font` on `.bricks-video-overlay-icon` |
| `customPlayer` | checkbox | Custom video player | — |
| `fileRestart` | checkbox | Restart | — |
| `fileRewind` | checkbox | Rewind | — |
| `fileFastForward` | checkbox | Fast forward | — |
| `fileSpeed` | checkbox | Speed | — |
| `filePip` | checkbox | Picture in picture | — |

### Wordpress

Section key: `wordpress`

Theme style controls for the "wordpress" section. Default CSS selector: .brxe-wordpress

| Key | Type | Label | CSS |
|---|---|---|---|
| `titleBorder` | border | Widget title border | `border` on `.bricks-widget-title` |
| `titleTypography` | typography | Widget title typography | `font` on `.bricks-widget-title` |
| `contentTypography` | typography | Content typography | `font` on `ul` |
| `postsTitleTypography` | typography | Post title typography | `font` on `.post-title` |
| `postsMetaTypography` | typography | Post meta typography | `font` on `.post-meta` |
