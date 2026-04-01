The filters control offers the following [CSS filters](https://developer.mozilla.org/en-US/docs/Web/CSS/filter): `blur`, `brightness`, `contrast`, `hue`, `invert`, `opacity`, `saturation`, `sepia`.

```php
class Prefix_Element_Filters extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleFilters'] = [
      'tab' => 'content',
      'label' => esc_html__( 'CSS filters', 'bricks' ),
      'type' => 'filters',
      'inline' => true,
      'css' => [
        [
          'property' => 'filter',
          'selector' => '.css-filter',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<div class="css-filter">' . echo get_bloginfo( 'name' ); . '</div>';
  }
}
```

:::note
All sections, rows, columns, and elements already have a **CSS Filters** control under the Style tab CSS group.
:::
