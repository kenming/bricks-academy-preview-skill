---
title: "Text Transform Control"
description: "Reference for the Bricks Text Transform control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/text-transform-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/text-transform-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-07-29T10:15:35.000Z"
---
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
