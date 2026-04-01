The box-shadow control is a CSS control and you can set the following properties:

- Offset X
- Offset Y
- Spread
- Blur
- Color
- Inset

```php
class Prefix_Element_Box_Shadow extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleBoxShadow'] = [
      'tab' => 'content',
      'label' => esc_html__( 'BoxShadow', 'bricks' ),
      'type' => 'box-shadow',
      'css' => [
        [
          'property' => 'box-shadow',
          'selector' => '.prefix-box-shadow-wrapper',
        ],
      ],
      'inline' => true,
      'small' => true,
      'default' => [
        'values' => [
          'offsetX' => 0,
          'offsetY' => 0,
          'blur' => 2,
          'spread' => 0,
        ],
        'color' => [
          'rgb' => 'rgba(0, 0, 0, .1)',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<div class="prefix-box-shadow-wrapper">';
    echo get_bloginfo( 'name' );
    echo '</div>';
  }
}
```

### Resources

[https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow)
