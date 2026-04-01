Use the **text-transform** control to allow users to set the text-transform CSS property like so:

```php
public function set_controls() {
  $this->controls['textTransform'] = [ // Setting key
    'tab' => 'content',
    'label' => esc_html__( 'Text transform', 'bricks' ),
    'type' => 'text-transform',
    'css' => [
      [
        'property' => 'text-transform',
        'selector' => '.text-wrapper',
      ],
    ],
  ];
}
```
