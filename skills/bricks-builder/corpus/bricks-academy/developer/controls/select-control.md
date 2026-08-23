---
title: "Select Control"
description: "Reference for the Bricks Select control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/select-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/select-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-08-20T13:12:40.000Z"
---
The select control lets you select an option from a dropdown. It can be used to render content or CSS styling. Use the options array to populate the dropdown with your own options. The option key should be all lowercase, with no spaces.

```php
class Prefix_Element_Posts extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    // Example content
    $this->controls['exampleSelectTitleTag'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title tag', 'bricks' ),
      'type' => 'select',
      'options' => [
        'h1' => 'H1',
        'h2' => 'H2',
        'h3' => 'H3',
        'h4' => 'H4',
        'h5' => 'H5',
        'h6' => 'H6',
      ],
      'inline' => true,
      'placeholder' => esc_html__( 'Select tag', 'bricks' ),
      'multiple' => true,
      'searchable' => true,
      'clearable' => true,
      'default' => 'h3',
    ];

    // Example CSS
    $this->controls['exampleSelectTextAlign'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text align', 'bricks' ),
      'type' => 'select',
      'options' => [
        'right' => esc_html__( 'Right', 'bricks' ),
        'center' => esc_html__( 'Center', 'bricks' ),
        'left' => esc_html__( 'Left', 'bricks' ),
      ],
      'inline' => true,
      'css' => [
        [
          'property' => 'text-align',
          'selector' => '.prefix-title',
        ],
      ],
      'placeholder' => esc_html__( 'Select', 'bricks' ),
      'default' => 'center', // Option key
    ];
  }

  // Render element HTML
  public function render() {
    $title_tag = isset( $this->settings['exampleSelectTitleTag'] ) ? $this->settings['exampleSelectTitleTag'] : 'h5';
    echo '<' . $title_tag . ' class="prefix-title">' . get_bloginfo( 'name' ) . '</' . $title_tag . '>';
  }
}
```
