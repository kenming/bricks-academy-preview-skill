---
title: "Image gallery"
description: "The Image Gallery element displays a collection of images in various layouts with optional lightbox functionality."
canonical: "https://academy.bricksbuilder.io/builder/elements/media/image-gallery/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/media/image-gallery.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-20T13:12:40.000Z"
---
The Image Gallery element displays a collection of images in various layouts with optional lightbox functionality.

## Settings

- **Images** (image-gallery) - Select and upload images for the gallery.

- **Layout** (select) - Gallery layout type. Options: `grid`, `masonry`, `metro`. Default: `grid`.

- **Columns** (number) - Number of columns in the grid. Minimum: 2. Default: 3. Not available for metro layout.

- **Spacing** (number with units) - Gap between images. Default: 0.

- **Image height** (number with units) - Fixed height for images. Not available for masonry or metro layouts.

- **Image ratio** (text) - Aspect ratio for images (e.g., 4/3, 16/9, 1/1). Not available for masonry or metro layouts.

- **Image caption** (checkbox) - Display image captions.

- **Link to** (select) - Link behavior for images. Options: `lightbox`, `attachment page`, `media file`, `custom URL`.

- **Custom links** (repeater) - Define custom URLs for each image. Only shown when "Link to" is set to "custom URL".

### Lightbox

- **Image size** (select) - Size of images in lightbox. Default: Full.

- **Image click action** (select) - Action when clicking images. Options: `zoom`, `zoom or close`, `toggle controls`, `next`, `close`. Default: `zoom`.

- **Animation** (select) - Lightbox transition animation.

- **Caption** (checkbox) - Show image captions in lightbox.

- **Thumbnail navigation** (checkbox) - Enable thumbnail navigation.

- **Thumbnail size** (number with units) - Size of thumbnails. Default: 60px.

- **Padding (px)** (dimensions) - Padding around the lightbox.

- **Lightbox: ID** (text) - Group images with the same ID together in the same lightbox.

- **Fetch priority** (select) - Image loading priority. Options: `high`, `low`, `auto`.

:::tip[Developer reference]
See the [Image Gallery Schema](/developer/schema/elements/image-gallery/) for the full JSON schema of this element's settings and controls.
:::
