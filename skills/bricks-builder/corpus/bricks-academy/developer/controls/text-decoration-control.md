---
title: "Text Decoration Control"
description: "Reference for the Bricks Text Decoration control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/text-decoration-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/text-decoration-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-08-20T13:12:40.000Z"
---
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
