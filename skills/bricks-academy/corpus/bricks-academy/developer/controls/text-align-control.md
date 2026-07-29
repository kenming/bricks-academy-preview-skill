---
title: "Text Align Control"
description: "Reference for the Bricks Text Align control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/text-align-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/text-align-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-07-29T10:15:35.000Z"
---
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
