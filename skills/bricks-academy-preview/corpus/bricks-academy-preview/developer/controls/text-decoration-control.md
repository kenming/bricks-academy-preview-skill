Use the **text-decoration** control to allow users to set the text-decoration CSS property like so:

```php
public function set_controls() {
  $this->controls['textDecoration'] = [ // Setting key
    'tab' => 'content',
    'label' => esc_html__( 'Text decoration', 'bricks' ),
    'type' => 'text-decoration',
    'css' => [
      [
        'property' => 'text-decoration',
        'selector' => '.text-wrapper',
      ],
    ],
  ];
}
```
