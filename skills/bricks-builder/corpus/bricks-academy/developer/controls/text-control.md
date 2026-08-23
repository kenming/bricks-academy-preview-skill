---
title: "Text Control"
description: "Reference for the Bricks Text control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/text-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/text-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-08-20T13:12:40.000Z"
---
The text control displays a text input field. You can set the following parameters:

- `spellcheck`: true/false. (Default: false)
- `trigger`: 'keyup'/'enter'. (Default: keyup)
- `inlineEditing`: Set to true to enable

```php
class Prefix_Element_Text extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleText'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text', 'bricks' ),
      'type' => 'text',
      'spellcheck' => true, // Default: false
      // 'trigger' => 'enter', // Default: 'enter'
      'inlineEditing' => true,
      'default' => 'Here goes your text ..',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleText'] ) ) {
      echo $this->settings['exampleText'];
    } else {
      esc_html_e( 'No text provided.', 'bricks' );
    }
  }
}
```

### Resources

- [https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg)
- [https://css-tricks.com/using-svg/](https://css-tricks.com/using-svg/)
