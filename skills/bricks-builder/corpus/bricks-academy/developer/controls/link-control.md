---
title: "Link Control"
description: "Reference for the Bricks Link control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/link-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/link-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-08-04T12:13:33.000Z"
---
The link control give you the choice of different link types:

- Internal post/page
- External URL
- Popup (image, video)

```php
class Prefix_Element_Link extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleLink'] = [
      'tab'         => 'content',
      'label'       => esc_html__( 'Link', 'bricks' ),
      'type'        => 'link',
      'pasteStyles' => false,
      'placeholder' => esc_html__( 'http://yoursite.com', 'bricks' ),
      // 'exclude'     => [
      //  'rel',
      //  'newTab',
      // ],
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleLink'] ) ) {
      // Set link attributes by passing attribute key and link settings
      $this->set_link_attributes( 'a', $this->settings['exampleLink'] );

      echo '<a ' . $this->render_attributes( 'a' ) . '>' . get_bloginfo( 'name' ) . '</a>';
    } else {
      esc_html_e( 'No link provided.', 'bricks' );
    }
  }
}
```
