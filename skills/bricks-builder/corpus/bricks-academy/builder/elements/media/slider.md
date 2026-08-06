---
title: "Slider"
description: "The Slider element creates a full-width image slider with customizable slides containing titles, content, and buttons, using the Swiper library."
canonical: "https://academy.bricksbuilder.io/builder/elements/media/slider/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/media/slider.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-04T12:13:33.000Z"
---
The Slider element creates a full-width image slider with customizable slides containing titles, content, and buttons, using the Swiper library.

## Security scanner reports

Bricks 2.4 patches the legacy Swiper build used by the classic Slider element. The bundled asset is a Bricks-patched vendored Swiper 8 legacy build with the CVE-2026-27212 / GHSA-hmx5-qpq5-p643 mitigation backported.

Bricks keeps the Swiper 8 runtime behavior so existing sliders continue to behave as before, including loop configurations that depend on Swiper 8 duplicate slides. The public `bricks-swiper` script version is `bricks-cve-2026-27212-p1`, and the bundled file no longer reports stock `Swiper 8.4.4` in its header.

Some security scanners may still fingerprint the underlying minified Swiper 8 code and flag it. Use this VEX or exception note: `Bricks-patched vendored Swiper 8 legacy build with CVE-2026-27212 backport.`

## Settings

- **Slides** (repeater) - Add slider slides. Each slide has:
  - **Title** (text) - Slide title.
  - **Title Tag** (select) - HTML tag for title. Options: `h1`-`h6`. Default: `h3`.
  - **Content** (rich text) - Slide content.
  - **Button text** (text) - Call-to-action button text.
  - **Button style** (select) - Button style. Default: `light`.
  - **Button size** (select) - Button size.
  - **Button width** (number with units) - Button width.
  - **Button link** (link) - Button destination.
  - **Button background** (color) - Button background color.
  - **Button border** (border) - Button border styling.
  - **Button box shadow** (box-shadow) - Button shadow.
  - **Button typography** (typography) - Button text styling.
  - **Background** (background) - Slide background (color, image, gradient).
  - **Overlay** (color) - Overlay color over the background.

- **Slides to show** (number) - Number of slides visible at once. Default: 1.

- **Slides to scroll** (number) - Number of slides to advance per transition. Default: 1.

- **Spacing** (number) - Spacing between slides in pixels. Default: 0.

- **Height** (number with units) - Slider height. Default: 300px.

- **Effect** (select) - Transition effect. Options: `slide`, `fade`, `cube`, `coverflow`, `flip`. Default: `slide`.

- **Loop** (select) - Enable infinite loop. Options: `enable`, `disable`. Default: `enable`.

- **Center mode** (checkbox) - Center the active slide.

- **Disable lazy load** (checkbox) - Load all images immediately.

- **Autoplay** (checkbox) - Enable automatic sliding.

- **Pause on hover** (checkbox) - Pause autoplay on hover.

- **Stop on last slide** (checkbox) - Stop autoplay on the last slide.

- **Autoplay delay in ms** (number) - Delay between slides in milliseconds. Default: 3000.

- **Animation speed in ms** (number) - Transition speed in milliseconds. Default: 300.

### Title

- **Title margin** (spacing) - Margin around slide titles.

- **Title typography** (typography) - Font settings for slide titles.

### Content

- **Content width** (number with units) - Maximum width of slide content.

- **Content background** (color) - Background color for slide content.

- **Content typography** (typography) - Font settings for slide content.

- **Content margin** (spacing) - Margin around slide content.

- **Content padding** (spacing) - Padding inside slide content. Default: 30px top, 60px right, 30px bottom, 60px left.

- **Content align horizontal** (justify-content) - Horizontal alignment of content within slides.

- **Content align vertical** (align-items) - Vertical alignment of content within slides.

- **Content text align** (text-align) - Text alignment within slide content.

### Button

- **Button style** (select) - Global button style. Default: `light`.

- **Button size** (select) - Global button size.

- **Button width** (number with units) - Global button width.

- **Background** (color) - Global button background color.

- **Border** (border) - Global button border styling.

- **Box shadow** (box-shadow) - Global button shadow.

- **Typography** (typography) - Global button text styling.

### Background

- **Top** (number with units) - Background image top position.

- **Right** (number with units) - Background image right position.

- **Bottom** (number with units) - Background image bottom position.

- **Left** (number with units) - Background image left position.

## Arrows

- **Show arrows** (checkbox) - Display navigation arrows. Default: true.

- **Height** (number with units) - Arrow button height. Default: 50px.

- **Width** (number with units) - Arrow button width. Default: 50px.

- **Background** (color) - Arrow button background color.

- **Border** (border) - Arrow button border styling.

- **Typography** (typography) - Arrow button text styling.

### Prev arrow

- **Prev arrow** (icon) - Previous arrow icon. Default: `ion-ios-arrow-back`.

- **Top** (number with units) - Previous arrow top position. Default: 50%.

- **Right** (number with units) - Previous arrow right position.

- **Bottom** (number with units) - Previous arrow bottom position.

- **Left** (number with units) - Previous arrow left position. Default: 50px.

- **Transform** (transform) - Previous arrow transformations.

### Next arrow

- **Next arrow** (icon) - Next arrow icon. Default: `ion-ios-arrow-forward`.

- **Top** (number with units) - Next arrow top position.

- **Right** (number with units) - Next arrow right position.

- **Bottom** (number with units) - Next arrow bottom position.

- **Left** (number with units) - Next arrow left position.

- **Transform** (transform) - Next arrow transformations.

## Dots

- **Show dots** (checkbox) - Display pagination dots.

- **Dynamic dots** (checkbox) - Enable dynamic bullet pagination.

- **Vertical** (checkbox) - Display dots vertically.

- **Height** (number with units) - Dot height.

- **Width** (number with units) - Dot width.

- **Top** (number with units) - Dots container top position.

- **Right** (number with units) - Dots container right position.

- **Bottom** (number with units) - Dots container bottom position.

- **Left** (number with units) - Dots container left position.

- **Border** (border) - Dot border styling.

- **Color** (color) - Inactive dot color.

- **Active color** (color) - Active dot color.

- **Margin** (spacing) - Margin around individual dots.

:::tip[Developer reference]
See the [Slider Schema](/developer/schema/elements/slider/) for the full JSON schema of this element's settings and controls.
:::
