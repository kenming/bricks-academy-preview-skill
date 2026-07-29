---
title: "Slider Control"
description: "Reference for the Bricks Slider control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/slider-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/slider-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-07-29T10:15:35.000Z"
---
The slider control shows a draggable range input field. Default units are `px`, `em` and `rem`. You can set the following control parameters:

- units (array with custom units and `min`, `max`, `step` attributes)
- unitless (set to `false` for plain number)

```php
class Prefix_Element_Slider extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleSliderFontSize'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Font size', 'bricks' ),
      'type' => 'slider',
      'css' => [
        [
          'property' => 'font-size',
        ],
      ],
      'units' => [
        'px' => [
          'min' => 1,
          'max' => 50,
          'step' => 1,
        ],
        'em' => [
          'min' => 1,
          'max' => 20,
          'step' => 0.1,
        ],
      ],
      'default' => '30px',
      'description' => esc_html__( 'Slider adjusts font size via CSS.', 'bricks' ),
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h3>' . get_bloginfo( 'name' ) . '</h3>';
  }
}
```

### Resources

- [https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/range](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/range)
