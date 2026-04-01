The dimensions control is perfect for adding multi-directional CSS properties such as margin and padding (top/right/bottom/left). You can set the directions to anything you want via the `directions` property.

```php
class Prefix_Element_Dimensions extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleDimensions'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title padding', 'bricks' ),
      'type' => 'dimensions',
      'css' => [
        [
          'property' => 'padding',
          'selector' => '.prefix-element-dimensions-title',
        ]
      ],
      'default' => [
        'top' => '30px',
        'right' => 0,
        'bottom' => '10em',
        'left' => 0,
      ],
      // 'unitless' => false, // false by default
      // Custom directions
      // 'directions' => [
        // 'offsetX' => esc_html__( 'Offset X', 'bricks' ),
        // 'offsetY' => esc_html__( 'Offset Y', 'bricks' ),
        // 'spread'  => esc_html__( 'Spread', 'bricks' ),
        // 'blur'    => esc_html__( 'Offset Y', 'bricks' ),
      // ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h5 class="prefix-element-dimensions-title">' . get_bloginfo( 'name' ) . '</h5>';
  }
}
```
