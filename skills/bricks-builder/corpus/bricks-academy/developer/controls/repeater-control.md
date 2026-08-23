---
title: "Repeater Control"
description: "Reference for the Bricks Repeater control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/repeater-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/repeater-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-08-20T13:12:40.000Z"
---
The repeater control lets you create repeatable fields. Fields can be cloned, deleted, and sorted via Drag & Drop. Use the `fields` argument to set up the field controls.

```php
class Prefix_Element_Posts extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleRepeater'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Repeater', 'bricks' ),
      'type' => 'repeater',
      'titleProperty' => 'title', // Default 'title'
      'default' => [
        [
          'title' => 'Design',
          'description' => 'Here goes the description for repeater item.',
        ],
        [
          'title' => 'Code',
          'description' => 'Here goes the description for repeater item.',
        ],
        [
          'title' => 'Launch',
          'description' => 'Here goes the description for repeater item.',
        ],
      ],
      'placeholder' => esc_html__( 'Title placeholder', 'bricks' ),
      'fields' => [
        'title' => [
          'label' => esc_html__( 'Title', 'bricks' ),
          'type' => 'text',
        ],
        'description' => [
          'label' => esc_html__( 'Description', 'bricks' ),
          'type' => 'textarea',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    $items = $this->settings['exampleRepeater'];

    if ( count( $items ) ) {
      foreach ( $items as $item ) {
        echo '<h4>' . $item['title'] . '</h4>';
        echo '<p>' . $item['description'] . '</p>';
      }
    } else {
      esc_html_e( 'No items defined.', 'bricks' );
    }
  }
}
```
