---
title: "Carousel"
description: "The Carousel element displays images or posts in a swipeable carousel with customizable navigation and effects, using the Swiper library."
canonical: "https://academy.bricksbuilder.io/builder/elements/media/carousel/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/media/carousel.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-20T13:12:40.000Z"
---
The Carousel element displays images or posts in a swipeable carousel with customizable navigation and effects, using the Swiper library.

## Settings

- **Type** (select) - Content type. Options: `media`, `posts`. Default: `media`.

- **Images** (image-gallery) - Select images for the carousel. Only shown for media type.

- **Query** (query) - Configure which posts to display. Only shown for posts type.

### Settings

- **Adaptive height** (checkbox) - Adjust height to content.

- **Height** (number with units) - Fixed carousel height. Default: 300px. Not available when adaptive height is enabled.

- **Spacing** (number) - Spacing between slides in pixels. Default: 0.

- **Initial slide** (number) - Starting slide index. Default: 0.

- **Items to show** (number) - Number of slides visible at once. Default: 2. Supports breakpoints.

- **Items to scroll** (number) - Number of slides to advance per swipe. Default: 1. Supports breakpoints.

- **Effect** (select) - Transition effect. Options: `slide`, `fade`, `cube`, `coverflow`, `flip`. Default: `slide`.

- **Align items** (align-items) - Vertical alignment of slides. Only shown when adaptive height is enabled.

- **Loop** (checkbox) - Enable infinite loop. Default: true.

- **Center mode** (checkbox) - Center the active slide.

- **Disable lazy load** (checkbox) - Load all images immediately.

- **Autoplay** (checkbox) - Enable automatic sliding.

- **Pause on hover** (checkbox) - Pause autoplay on hover.

- **Stop on last slide** (checkbox) - Stop autoplay on last slide.

- **Autoplay delay in ms** (number) - Delay between slides in milliseconds. Default: 3000.

- **Animation speed in ms** (number) - Transition speed in milliseconds. Default: 300.

### Image

- **Hide image** (checkbox) - Hide images in post carousels.

- **Image size** (select) - Size of images.

- **Link to lightbox** (checkbox) - Open images in lightbox. Only for media type.

- **Image size** (select) - Size of images in lightbox.

- **Image click action** (select) - Action when clicking images. Options: `zoom`, `zoom-or-close`, `toggle-controls`, `next`, `close`. Default: `zoom`.

- **Animation** (select) - Lightbox animation type. Default: `zoom`.

- **Caption** (checkbox) - Show image captions in lightbox.

- **Thumbnail navigation** (checkbox) - Show thumbnail navigation in lightbox.

- **Thumbnail size** (number with units) - Size of thumbnails. Default: 60px.

- **Padding** (dimensions) - Lightbox padding in pixels.

### Fields

- **Fields** (repeater) - Configure which post fields to display. Each field has:
  - **Dynamic data** (text) - Dynamic data tag (e.g., `{post_title:link}`, `{post_excerpt:20}`).
  - **HTML tag** (select) - HTML tag for the field. Options: `div`, `p`, `h1`-`h6`. Default: `div`.
  - **Width** (number with units) - Field width.
  - **Margin** (spacing) - Field margin.
  - **Padding** (spacing) - Field padding.
  - **Background color** (color) - Field background color.
  - **Border** (border) - Field border styling.
  - **Typography** (typography) - Field text styling.
  - **Overlay** (checkbox) - Show field as overlay.

### Content

- **Alignment** (select) - Content alignment. Options: `top left`, `top center`, `top right`, `middle left`, `middle center`, `middle right`, `bottom left`, `bottom center`, `bottom right`.

- **Min. height** (number with units) - Minimum content height.

- **Margin** (spacing) - Content wrapper margin.

- **Padding** (spacing) - Content wrapper padding.

- **Background color** (color) - Content wrapper background color.

### Overlay

- **Show on hover** (checkbox) - Show overlay only on hover.

- **Fade in animation** (select) - Overlay animation. Options: `fade-in-up`, `fade-in-right`, `fade-in-down`, `fade-in-left`, `zoom-in`, `zoom-out`.

- **Alignment** (select) - Overlay alignment. Options: `top left`, `top center`, `top right`, `middle left`, `middle center`, `middle right`, `bottom left`, `bottom center`, `bottom right`.

- **Margin** (spacing) - Overlay margin.

- **Padding** (spacing) - Overlay padding.

- **Background color** (color) - Overlay background color.

- **Inner background color** (color) - Inner overlay background color.

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

### Next arrow

- **Next arrow** (icon) - Next arrow icon. Default: `ion-ios-arrow-forward`.

- **Top** (number with units) - Next arrow top position.

- **Right** (number with units) - Next arrow right position.

- **Bottom** (number with units) - Next arrow bottom position.

- **Left** (number with units) - Next arrow left position.

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

- **Margin** (spacing) - Margin around individual dots. Default: 0px top, 5px right, 0px bottom, 0px left.

:::tip[Developer reference]
See the [Carousel Schema](/developer/schema/elements/carousel/) for the full JSON schema of this element's settings and controls.
:::
