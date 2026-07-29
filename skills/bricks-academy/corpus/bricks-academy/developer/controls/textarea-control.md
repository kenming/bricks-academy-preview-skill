---
title: "Textarea Control"
description: "Reference for the Bricks Textarea control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/textarea-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/textarea-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-07-29T10:15:35.000Z"
---
The textarea control displays a textarea input field. You can set the following parameters:

- `rows` (number. Default: 5)
- `readonly` (true/false. Default: false)
- `spellcheck` (true/false. Default: false)
- `inlineEditing` (true to enable)

```php
class Prefix_Element_Textarea extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleTextarea'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Textarea', 'bricks' ),
      'type' => 'textarea',
      // 'readonly' => true, // Default: false
      'rows' => 10, // Default: 5
      'spellcheck' => true, // Default: false
      'inlineEditing' => true,
      'default' => 'Here goes your content ..',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleTextarea'] ) ) {
      echo $this->settings['exampleTextarea'];
    } else {
      esc_html_e( 'No text provided.', 'bricks' );
    }
  }
}
```
