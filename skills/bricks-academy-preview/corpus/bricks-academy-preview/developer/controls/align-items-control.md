Use the align-items control to allow users to set the `align-items` CSS property (alignment along the [cross-axis](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items)) of your CSS flexbox layout.

There is also a [`justify-content`](/developer/controls/justify-content-control/) control to allow users to set the alignment along the main axis of your CSS flexbox layout:

```php
public function set_controls() {
  $this->controls['alignItems'] = [ // Setting key
    'tab'   => 'content',
    'label' => esc_html__( 'Align items', 'bricks' ),
    'type'  => 'align-items',
    'css'   => [
      [
        'property' => 'align-items',
        'selector' => '.flexbox-wrapper',
      ],
    ],
    // 'isHorizontal' => false,
    // 'exclude' => [
      // 'flex-start',
      // 'center',
      // 'flex-end',
      // 'space-between',
      // 'space-around',
      // 'space-evenly',
    // ],
  ];
}
```
