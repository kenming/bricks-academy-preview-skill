---
title: "Editor Control"
description: "Reference for the Bricks Editor control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/editor-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/editor-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-07-29T10:15:35.000Z"
---
The editor control provides the default WordPress editor. To directly edit content in the builder preview set the `inlineEditing` properties. See the code example below:

```php
class Prefix_Element_Editor extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleEditor'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text editor', 'bricks' ),
      'type' => 'editor',
      'inlineEditing' => [
        'selector' => '.text-editor', // Mount inline editor to this CSS selector
        'toolbar' => true, // Enable/disable inline editing toolbar
      ],
      'default' => esc_html__( 'Here goes the content ..', 'bricks' ),
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleEditor'] ) ) {
      echo '<div class="text-editor">' . $this->settings['exampleEditor'] . '</div>';
    }
  }
}
```
