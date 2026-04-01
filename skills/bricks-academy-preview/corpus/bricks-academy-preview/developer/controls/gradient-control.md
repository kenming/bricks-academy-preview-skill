The gradient control lets you define an unlimited number of gradients that you can apply to text, background, and as an overlay.

You can set the CSS selector in the control, adjust the angle between 0 and 360°, and set a color stop for each color.

```php
class Prefix_Element_Gradient extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleGradient'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Gradient', 'bricks' ),
      'type' => 'gradient',
      'css' => [
        [
          'property' => 'background-image',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo get_bloginfo( 'name' );
  }
}
```

:::note
All sections, rows, columns, and elements already have a **CSS Gradient** control under the Style tab Gradient / Overlay group.
:::
