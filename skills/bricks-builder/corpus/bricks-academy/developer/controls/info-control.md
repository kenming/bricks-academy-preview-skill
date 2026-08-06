---
title: "Info Control"
description: "Reference for the Bricks Info control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/info-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/info-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-08-04T12:13:33.000Z"
---
The info control does not affect the HTML or CSS on the frontend. It serves as a builder-only helper controls to provide additional information.

Example below: the **Alert** element displays an info control when the *Type* is set to *Custom*.

```php
class Prefix_Element_Info extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['type'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Type', 'bricks' ),
      'type' => 'select',
      'options' => [
        'info' => esc_html__( 'Info', 'bricks' ),
        'success' => esc_html__( 'Success', 'bricks' ),
        'warning' => esc_html__( 'Warning', 'bricks' ),
        'danger' => esc_html__( 'Danger', 'bricks' ),
        'muted' => esc_html__( 'Muted', 'bricks' ),
        'custom' => esc_html__( 'Custom', 'bricks' ),
      ],
      'inline' => true,
      'clearable' => false,
      'pasteStyles' => false,
      'default' => 'info',
    ];

    $this->controls['typeInfo'] = [
      'tab' => 'content',
      'content' => esc_html__( 'Customize alert in STYLE tab.', 'bricks' ),
      'type' => 'info',
      'required' => ['type', '=', 'custom'], // Show info control if 'type' = 'custom'
    ];
  }
}
```
