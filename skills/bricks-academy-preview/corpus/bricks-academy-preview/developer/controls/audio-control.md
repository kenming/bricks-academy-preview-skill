The audio control lets you select an audio file from the media library. It also gives you various options to show/hide artist and title, choose between a light/dark theme, autoplay the audio file, etc. It has no custom control parameters.

```php
class Prefix_Element_Audio extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['file'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Audio file', 'bricks' ),
      'type' => 'audio',
    ];
  }

  // Render element HTML
  public function render() {
    $settings = $this->settings;

    if ( isset( $settings['file']['url'] ) ) {
      echo wp_audio_shortcode( [
        'src'      => $settings['file']['url'],
        'loop'     => isset( $settings['loop'] ) ? $settings['loop'] : false,
        'autoplay' => isset( $settings['autoplay'] ) ? $settings['autoplay'] : false,
        'preload'  => isset( $settings['preload'] ) ? $settings['preload'] : 'none',
      ] );
    }
  }
}
```

### Resources

[https://codex.wordpress.org/Function_Reference/wp_audio_shortcode](https://codex.wordpress.org/Function_Reference/wp_audio_shortcode)
