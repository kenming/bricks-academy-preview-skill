The text-shadow control displays a popup that lets you set the CSS text-shadow of a specified HTML text element.

```php
class Prefix_Element_Textarea extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleTextShadow'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text Shadow', 'bricks' ),
      'type' => 'text-shadow',
      'css' => [
        [
          'property' => 'text-shadow',
          'selector' => '.prefix-text',
        ],
      ],
      'inline' => true,
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h3 class="prefix-text">' . get_bloginfo( 'name' ) . '</h3>';
  }
}
```

### Resources

[https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow)
