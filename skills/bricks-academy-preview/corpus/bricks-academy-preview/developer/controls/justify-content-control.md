Use the justify-content control to allow users to set the `justify-content` CSS property (alignment along the [main-axis](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content)) of your CSS flexbox layout.

There is also a [`align-items`](/developer/controls/align-items-control/) control to allow users to set the alignment along the cross axis of your CSS flexbox layout:

```php
public function set_controls() {
  $this->controls['justifyContent'] = [
    'tab'   => 'content',
    'label' => esc_html__( 'Justify content', 'bricks' ),
    'type'  => 'justify-content',
    'css'   => [
      [
        'property' => 'justify-content',
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
