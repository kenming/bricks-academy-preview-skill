Use the **text-align** control to allow users to set the text-align CSS property like so:

```php
public function set_controls() {
  $this->controls['textAlign'] = [ // Setting key
    'tab' => 'content',
    'label' => esc_html__( 'Text align', 'bricks' ),
    'type' => 'text-align',
    'css' => [
      [
        'property' => 'text-align',
        'selector' => '.text-wrapper',
      ],
    ],
  ];
}
```
