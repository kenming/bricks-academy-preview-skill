The background control lets you set the following background properties:

- Background color
- Background image
- Background video (requires `bricksBackgroundVideoInit` script. See code example below)

There are various settings for the background image and video. You can exclude color/image/video settings via the `exclude` parameter.

As the background control serves most likely as a CSS setting the following example shows you how to set the `css` parameter to apply it to the elements' `.prefix-test-wrapper` HTML.

Adding a background video requires you to load the `bricksBackgroundVideoInit` script and use the `BricksFrontend::get_element_background_video_wrapper()` method to render it.

:::note
When you just want to set a background color better use the [color control](/developer/controls/color-control/). The background control is handier when using a background image or video on top of the color.
:::

```php
class Prefix_Element_Background extends \Bricks\Element {
  // Required for background video
  public $scripts = ['bricksBackgroundVideoInit'];

  // Set builder controls
  public function set_controls() {
    $this->controls['exampleBackground'] = [ // Setting key
      'tab' => 'content',
      'label' => esc_html__( 'Background', 'bricks' ),
      'type' => 'background',
      'css' => [
        [
          'property' => 'background',
          'selector' => '.prefix-background-wrapper',
        ],
      ],
      'exclude' => [
        // 'color',
        // 'image',
        // 'parallax',
        // 'attachment',
        // 'position',
        // 'positionX',
        // 'positionY',
        // 'repeat',
        // 'size',
        // 'custom',
        // 'videoUrl',
        // 'videoScale',
      ],
      'inline' => true,
      'small' => true,
      'default' => [
        'color' => [
          'rgb' => 'rgba(255, 255, 255, .5)',
          'hex' => '#ffffff',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<div class="prefix-background-wrapper">';

    // Background video
    echo BricksFrontend::get_element_background_video_wrapper(
      ['settings' => $settings],
      'exampleBackground' // Setting key
    );

    echo get_bloginfo( 'name' );

    echo '</div>';
  }
}
```
