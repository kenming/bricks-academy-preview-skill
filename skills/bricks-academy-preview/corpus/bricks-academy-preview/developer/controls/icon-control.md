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
