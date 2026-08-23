---
title: "Filter: bricks/placeholder_image"
description: "The bricks/placeholderimage filter allows you to override the default placeholder image used in Bricks. This can be useful when you want to display a custom."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-placeholder_image/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-placeholder_image.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
The `bricks/placeholder_image` filter allows you to override the default placeholder image used in Bricks. This can be useful when you want to display a custom placeholder for elements when performing template import or pasting elements from another website. `(@since 2.0)`

## Parameters

- `$image` *(string)* – The default placeholder image path or URL.
- `$is_svg` *(bool)* – Whether the placeholder should be an SVG. Leave as is.
- `$format` *(string)* – Can be `'url'` or `'path'` depending on the context Bricks needs it for. Leave as is.

```php
add_filter( 'bricks/placeholder_image', function( $image, $is_svg, $format ) {
  // Custom placeholder images (SVG and non-SVG file required)
  // SVG file: /uploads/2025/04/my-placeholder.svg
  // Non-SVG file: /uploads/2025/04/my-placeholder-img.png
  $relative_path = $is_svg ? '2025/04/my-placeholder.svg' : '2025/04/my-placeholder-img.png';
  $upload_dir    = wp_get_upload_dir();

  if ( $format === 'path' ) {
    // Return absolute path to the image
    $image = $upload_dir['basedir'] . '/' . $relative_path;
  } else {
    // Return full URL to the image
    $image = $upload_dir['baseurl'] . '/' . $relative_path;
  }

  return $image;
}, 10, 3 );
```
