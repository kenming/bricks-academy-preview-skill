The typography control provides the following CSS properties:

- color
- font-size
- text-align
- text-transform
- font-family
- font-weight
- font-style
- line-height
- letter-spacing
- text-shadow
- text-decoration

Use the `exclude` parameter to hide specific typography properties. Set `popup` to false to show control inline.

```php
class Prefix_Element_Typography extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleTypography'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Typography', 'bricks' ),
      'type' => 'typography',
      'css' => [
        [
          'property' => 'typography',
          'selector' => '.prefix-typography',
        ],
      ],
      'inline' => true,
      // 'exclude' => [
      //   'font-family',
      //   'font-weight',
      //   'text-align',
      //   'text-transform',
      //   'font-size',
      //   'line-height',
      //   'letter-spacing',
      //   'color',
      //   'text-shadow',
      // ],
      // 'popup' => false, // Default: true
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h3 class="prefix-typography">' . get_bloginfo( 'name' ) . '</h3>';
  }
}
```
