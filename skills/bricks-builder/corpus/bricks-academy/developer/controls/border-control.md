---
title: "Border Control"
description: "Reference for the Bricks Border control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/border-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/border-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-08-04T12:13:33.000Z"
---
The border control lets you set the following border properties:

- Border width (top/right/bottom/left)
- Background style (top/right/bottom/left)
- Background color (none/solid/double/dotted/dashed)
- Border radius (top/right/bottom/left)

The example below illustrates how to apply a border via the `css` parameter and how to set border defaults.

```php
class Builder_Element_Prefix_Test extends \Bricks\Element {
  public function set_controls() {
    $this->controls['titleBorder'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title border', 'bricks' ),
      'type' => 'border',
      'css' => [
        [
          'property' => 'border',
          'selector' => '.prefix-test-title',
        ],
      ],
      'inline' => true,
      'small' => true,
      'default' => [
        'width' => [
          'top' => 1,
          'right' => 0,
          'bottom' => 0,
          'left' => 0,
        ],
        'style' => 'solid',
        'color' => [
          'hex' => '#ffff00',
        ],
        'radius' => [
          'top' => 1,
          'right' => 1,
          'bottom' => 1,
          'left' => 1,
        ],
      ],


    ];
  }
}
```
