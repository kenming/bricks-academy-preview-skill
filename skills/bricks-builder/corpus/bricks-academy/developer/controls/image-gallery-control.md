---
title: "Image Gallery Control"
description: "Reference for the Bricks Image Gallery control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/image-gallery-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/image-gallery-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-08-20T13:12:40.000Z"
---
The image gallery control lets you select multiple images from your media library. Once images have been selected you can choose the image size.

Your selected images are stored in an array, which you have to loop through (see code example below). Use the `id` and `size`  of each image to render it on your page.

:::note
**Tip #1:** Hold down the *SHIFT* key in order to select multiple image in your media library.
:::

:::note
**Tip #2:** Select the smallest possible image size in which the image still looks crisp. This helps to reduce the loading time of your website and is great for SEO, as loading times are an important ranking factor for search engines.
:::

```php
class Prefix_Element_Image extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleImageGallery'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Image gallery', 'bricks' ),
      'type' => 'image-gallery',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleImageGallery'] ) ) {
      foreach( $this->settings['exampleImageGallery'] as $index => $image ) {
        echo wp_get_attachment_image(
          $image['id'],
          $image['size'],
          false,
          ['class' => 'css-filter']
        );
      }
    } else {
      esc_html_e( 'No image(s) selected.', 'bricks' );
    }
  }
}
```
