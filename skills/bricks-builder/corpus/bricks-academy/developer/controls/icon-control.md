---
title: "Icon Control"
description: "Reference for the Bricks Icon control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/icon-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/icon-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-08-20T13:12:40.000Z"
---
The icon control lets you select and output icons from the following icon font libraries:

- [Fontawesome 6](https://fontawesome.com/icons?d=gallery&m=free)
- [Ionicons 4](https://ionic.io/ionicons/v4/cheatsheet.html)
- [Themify](https://themify.me/themify-icons)

The user can also select individually uploaded SVG files if you've enabled "**SVG Uploads**" under `Bricks > Settings` in your WordPress dashboard, and custom icon sets since Bricks 2.0.

```php
class Prefix_Element_Icon extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleIcon'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Icon', 'bricks' ),
      'type' => 'icon',
      'default' => [
        'library' => 'themify', // fontawesome/ionicons/themify
        'icon' => 'ti-star',    // Example: Themify icon class
      ],
      'css' => [
        [
          'selector' => '.icon-svg', // Use to target SVG file
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    // Set icon 'class' attribute
    if ( isset( $this->settings['exampleIcon'] ) ) {
      Helpers::render_control_icon( $settings['exampleIcon'], ['test-class', 'test-class-2'] );
    }
  }
}
```
