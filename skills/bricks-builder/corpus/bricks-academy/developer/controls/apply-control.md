---
title: "Apply Control"
description: "Reference for the Bricks Apply control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/apply-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/apply-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-08-20T13:12:40.000Z"
---
The `apply` control saves your settings. You can set the `reload` control property to **true** in order to trigger a builder reload after the "Apply" button has been clicked. We use it in the builder for settings like the template "Populate Content" or the "SEO" page settings.

```php
$this->controls['apply'] = [
  'group' => 'template-preview',
  'type' => 'apply',
  'reload' => true,
  'label' => esc_html__( 'Apply preview', 'bricks' ),
];
```
