---
title: "Testimonials"
description: "The Testimonials element displays testimonials in a swipeable carousel with images, names, titles, and content."
canonical: "https://academy.bricksbuilder.io/builder/elements/general/testimonials/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/general/testimonials.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-04T12:13:33.000Z"
---
The Testimonials element displays testimonials in a swipeable carousel with images, names, titles, and content.

## Settings

### Testimonials

- **Testimonials** (repeater) - Add testimonial entries. Each testimonial has:
  - **Content** (textarea) - The testimonial text.
  - **Name** (text) - Name of the person giving the testimonial.
  - **Title** (text) - Job title or role of the person.
  - **Image** (image) - Profile image of the person.

### Settings

- **Initial slide** (number) - Starting slide index. From swiper controls.

- **Slides to show** (number) - Number of testimonials visible at once. From swiper controls.

- **Slides to scroll** (number) - Number of slides to advance per swipe. From swiper controls.

- **Gutter** (number with units) - Spacing between slides. From swiper controls.

- **Align items** (justify-content) - Vertical alignment of testimonial items. Applied to `.repeater-item` selector. Excludes space options.

- **Text align** (text-align) - Text alignment for testimonials.

- **Effect** (select) - Transition effect. From swiper controls.

- **Infinite** (checkbox) - Enable infinite loop. From swiper controls.

- **Random order** (checkbox) - Display testimonials in random order.

- **Center mode** (checkbox) - Center the active slide. From swiper controls.

- **Disable lazy load** (checkbox) - Disable lazy loading of images. From swiper controls.

- **Autoplay** (checkbox) - Enable autoplay. From swiper controls.

- **Pause on hover** (checkbox) - Pause autoplay on hover. From swiper controls.

- **Autoplay speed** (number) - Autoplay delay in milliseconds. From swiper controls.

- **Speed** (number) - Transition speed in milliseconds. From swiper controls.

### Image

- **Image align** (align-items) - Vertical alignment of images. Applied to `.repeater-item` selector. Excludes stretch option.

- **Image position** (select) - Position of the image relative to content. Options: `top`, `right`, `bottom`, `left`. Default: `left`.

- **Image size** (number with units) - Size of the images. Controls both `width` and `height` of `.image` selector. Default placeholder: `60`.

- **Image border** (border) - Border styling for images. Applied to `.image` selector.

- **Image box shadow** (box-shadow) - Shadow effect for images. Applied to `.image` selector.

### Arrows

- **Arrows** (checkbox) - Show navigation arrows. From swiper controls.

- **Arrow height** (number with units) - Height of navigation arrows. From swiper controls.

- **Arrow width** (number with units) - Width of navigation arrows. From swiper controls.

- **Arrow background** (color) - Background color of navigation arrows. From swiper controls.

- **Arrow border** (border) - Border styling for navigation arrows. From swiper controls.

- **Arrow typography** (typography) - Font styling for navigation arrows. From swiper controls. Default color: body color.

- **Previous arrow** (text) - Custom previous arrow icon. From swiper controls.

- **Previous arrow position** - Top, right, bottom, left positioning for previous arrow. From swiper controls.

- **Next arrow** (text) - Custom next arrow icon. From swiper controls.

- **Next arrow position** - Top, right, bottom, left positioning for next arrow. From swiper controls.

### Dots

- **Dots** (checkbox) - Show pagination dots. From swiper controls.

- **Dynamic dots** (checkbox) - Enable dynamic pagination bullets. From swiper controls.

- **Vertical dots** (checkbox) - Display dots vertically. From swiper controls.

- **Dots height** (number with units) - Height of pagination dots. From swiper controls.

- **Dots width** (number with units) - Width of pagination dots. From swiper controls.

- **Dots position** - Top, right, bottom, left positioning for dots. From swiper controls.

- **Dots border** (border) - Border styling for pagination dots. From swiper controls.

- **Dots color** (color) - Color of inactive pagination dots. From swiper controls.

- **Active dots color** (color) - Color of active pagination dot. From swiper controls.

- **Dots spacing** (number with units) - Spacing between pagination dots. From swiper controls.

## Style

- **Testimonial** (typography) - Font styling for testimonial content. Applied to `.testimonial-content-wrapper` selector.

- **Name** (typography) - Font styling for testimonial names. Applied to `.testimonial-name` selector.

- **Title** (typography) - Font styling for testimonial titles. Applied to `.testimonial-title` selector.

:::tip[Developer reference]
See the [Testimonials Schema](/developer/schema/elements/testimonials/) for the full JSON schema of this element's settings and controls.
:::
