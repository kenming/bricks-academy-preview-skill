---
title: "Justify Content Control (Flexbox)"
description: "Reference for the Bricks Justify Content Control (Flexbox) control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/justify-content-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/justify-content-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-07-29T10:15:35.000Z"
---
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
