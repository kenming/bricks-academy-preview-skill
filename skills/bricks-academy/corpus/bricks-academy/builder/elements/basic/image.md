---
title: "Image"
description: "The Image element displays images with support for responsive sources, captions, lightbox functionality, masks, and various other styling options."
canonical: "https://academy.bricksbuilder.io/builder/elements/basic/image/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/basic/image.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-07-29T10:15:35.000Z"
---
The Image element displays images with support for responsive sources, captions, lightbox functionality, masks, and various other styling options.

## Settings

### Basic

- **Image** (image) - Select an image from the media library or use dynamic data.

- **HTML tag** (select) - The HTML tag to wrap the image. Options: `figure`, `picture`, `div`, `custom`. Default: `figure`. When sources are used, Bricks outputs a `<picture>` element around the image sources. If the image has a caption, Bricks keeps the `figure` wrapper and places the `<picture>` element inside it.

- **Custom tag** (text) - Specify a custom HTML tag name without attributes. Only available when HTML tag is set to "custom" and sources are not used.

- **Sources** (repeater) - Configure different images for different breakpoints using the `<picture>` element. Each source has:
  - **Breakpoint** (select) - Target breakpoint or custom media query
  - **Media query** (text) - Custom media query string (only when breakpoint is "Custom")
  - **Image** (image) - Image to display for this breakpoint

  Order matters because the browser uses the first matching `<source>` inside the generated `<picture>` element. Add sources for breakpoints below the base breakpoint first, from smallest to largest. Then add sources for breakpoints above the base breakpoint, from largest to smallest. Add the base breakpoint source last so it can act as the fallback image.

  Bricks generates `max-width` media queries for breakpoints below the base breakpoint and `min-width` media queries for breakpoints above the base breakpoint. For example, if Desktop is the base breakpoint and you add a Desktop XL breakpoint at `1890px`, the Desktop XL source uses `(min-width: 1890px)`. A Tablet portrait source below the base breakpoint uses its `max-width` condition.

  Choose **Custom** when you need to write the media query manually. Bricks uses the custom media query as entered, so keep it in the correct source order.

- **Aspect ratio** (text) - Set the image aspect ratio (e.g., `16/9`, `4/3`, `1/1`).

- **Object fit** (select) - How the image should fit its container. Options: `fill`, `contain`, `cover`, `none`, `scale-down`.

- **Object position** (text) - Position of the image within its container (e.g., `center center`, `top left`).

### Alt & Caption

- **Custom alt text** (text) - Override the default alt text from the media library.

- **Caption type** (select) - Display a caption below the image. Options: `none`, `attachment` (from media library), `custom`. Default: `attachment`.

- **Custom caption** (text) - Custom caption text. Only available when caption type is set to "custom".

### Display Options

- **Loading** (select) - Image loading behavior. Options: `eager`, `lazy`. Default: `lazy`.

- **Show title** (checkbox) - Display the image title attribute from the media library.

- **Stretch** (checkbox) - Make the image width 100% of its container.

- **Image Overlay** (color) - Add a color overlay on top of the image.

### Link To

- **Link** (select) - Make the image clickable. Options: `lightbox`, `attachment` (attachment page), `media` (media file), `url` (custom URL). Default: None.

#### Lightbox Settings

Available when link is set to "lightbox":

- **Image size** (select) - The image size to display in lightbox. Options based on registered image sizes. Default: Full.

- **Width** (number) - Custom lightbox image width in pixels.

- **Height** (number) - Custom lightbox image height in pixels.

- **Animation** (select) - Lightbox animation type. Options: `zoom`, `fade`, `none`. Default: `zoom`.

- **Caption** (checkbox) - Show image caption in lightbox.

- **ID** (text) - Group multiple images with the same lightbox ID to create a gallery.

- **Cropped** (checkbox) - Enable for smoother transitions if the image is cropped.

- **Padding** (dimensions) - Padding around the lightbox image in pixels.

#### Attachment/Media Settings

Available when link is set to "attachment" or "media":

- **Open in new tab** (checkbox) - Open the link in a new browser tab.

#### URL Settings

Available when link is set to "url":

- **URL** (link) - Configure the custom link URL and attributes.

### Icon

Optional icon overlay displayed when the image has a link:

- **Disable icon** (checkbox) - Hide the icon even if configured in theme styles.

- **Icon** (icon) - Select an icon to display on the image.

- **Icon background color** (color) - Background color for the icon.

- **Icon border** (border) - Border styling for the icon.

- **Icon box shadow** (box-shadow) - Box shadow for the icon.

- **Icon typography** (typography) - Typography settings for the icon (size, color).

- **Icon height** (number) - Height of the icon container.

- **Icon width** (number) - Width of the icon container.

- **Icon transition** (text) - CSS transition for the icon.

### Mask

Apply a mask to the image for creative shapes and effects:

- **Mask** (select) - Choose from predefined mask shapes or use a custom mask image. Options include:
  - **Custom** - Use a custom mask image
  - **Boom** - Boom shape mask
  - **Box** - Box shape mask
  - **Bubbles** - Bubbles pattern mask
  - **Circle dots** - Circle dots pattern mask
  - **Circle line** - Circle line pattern mask
  - **Circle waves** - Circle waves pattern mask
  - **Circle** - Circle shape mask
  - **Drop 2** - Drop 2 shape mask
  - **Drop** - Drop shape mask
  - **Fire** - Fire shape mask
  - **Grid circles** - Grid circles pattern mask
  - **Grid dots** - Grid dots pattern mask
  - **Grid filled diagonal** - Grid filled diagonal pattern mask
  - **Grid lines diagonal** - Grid lines diagonal pattern mask
  - **Grid** - Grid pattern mask
  - **Heart** - Heart shape mask
  - **Hexagon dent** - Hexagon dent shape mask
  - **Hexagon** - Hexagon shape mask
  - **Hourglass** - Hourglass shape mask
  - **Masonry** - Masonry pattern mask
  - **Ninja star** - Ninja star shape mask
  - **Octagon dent** - Octagon dent shape mask
  - **Play** - Play shape mask
  - **Plus** - Plus shape mask
  - **Round zig zag** - Round zig zag pattern mask
  - **Splash** - Splash shape mask
  - **Square rounded** - Square rounded shape mask
  - **Squares 3x3** - Squares 3x3 pattern mask
  - **Squares 4x4** - Squares 4x4 pattern mask
  - **Squares 4 diagonal rounded** - Squares 4 diagonal rounded pattern mask
  - **Squares 4 diagonal** - Squares 4 diagonal pattern mask
  - **Squares diagonal** - Squares diagonal pattern mask
  - **Squares merged** - Squares merged pattern mask
  - **Tiles 2** - Tiles 2 pattern mask
  - **Tiles** - Tiles pattern mask
  - **Waves** - Waves pattern mask

- **Custom mask** (image) - Upload or select a custom mask image. Only available when mask is set to "Custom".

- **Size** (select) - How the mask should fit. Options: `auto`, `cover`, `contain`, `custom`. Default: `contain`.

- **Custom size** (number) - Custom mask size with units. Only available when size is set to "custom".

- **Position** (select) - Position of the mask. Options: `center center`, `center left`, `center right`, `top center`, `top left`, `top right`, `bottom center`, `bottom left`, `bottom right`. Default: `center center`.

- **Repeat** (select) - How the mask should repeat. Options: `no-repeat`, `repeat`, `repeat-x`, `repeat-y`, `round`, `space`. Default: `no-repeat`.

:::tip[Developer reference]
See the [Image Schema](/developer/schema/elements/image/) for the full JSON schema of this element's settings and controls.
:::
