Use the direction control to allow users to set the `flex-direction` CSS property of your CSS flexbox layout.

```php
public function set_controls() {
  $this->controls['direction'] = [ // Setting key
    'tab'   => 'content',
    'label' => esc_html__( 'Direction', 'bricks' ),
    'type'  => 'direction',
    'css'   => [
      [
        'property' => 'flex-direction',
        'selector' => '.flexbox-wrapper',
        // 'id'       => '', // Leave 'id' empty to apply to .flexbox-wrapper directly (@since 1.5.6)
      ],
    ],
  ];
}
```
