---
title: "Create Your Own Elements"
description: "Create custom Bricks elements by extending the element API, registering controls, and rendering frontend output."
canonical: "https://academy.bricksbuilder.io/developer/elements/create-your-own-elements/"
markdownUrl: "https://academy.bricksbuilder.io/developer/elements/create-your-own-elements.md"
pageType: "article"
section: "developer"
category: "elements"
lastmod: "2026-07-29T10:15:35.000Z"
---
The Bricks [child theme](/developer/guides/child-theme/), which you can download from your [Bricks account](https://my.bricksbuilder.io/) includes a simple custom element for demonstration purposes. The article below explains in more detail how to create your own elements programmatically.

Creating your own elements with Bricks follows a pattern similar to how you create WordPress widgets. You start by extending the `Bricks\Element` class and populate the required properties and methods for your element.

First, create a new file `element-test.php` in the root folder of your Bricks child theme.

## Blank element class {#builder}

```php
<?php
// element-test.php
if ( ! defined( 'ABSPATH' ) ) exit; // Exit if accessed directly

class Prefix_Element_Test extends \Bricks\Element {
  // Element properties
  public $category     = '';
  public $name         = '';
  public $icon         = '';
  public $css_selector = '';
  public $scripts      = [];
  public $nestable     = false; // true || @since 1.5

  // Methods: Builder-specific
  public function get_label() {}
  public function get_keywords() {}
  public function set_control_groups() {}
  public function set_controls() {}

  // Methods: Frontend-specific
  public function enqueue_scripts() {}
  public function render() {}
}
```

Let's walk through the element builder properties and methods:

| **$category** required | Category name (all lowercase, no spaces). Use any of the predefined element categories (e.g. `general`, `media`, etc.) or assign your own category name.<br /><br />When setting your own category make sure to provide a translatable category string for the builder using the filter: [bricks/builder/i18n](/developer/hooks/filters/filter-bricks-i18n/) |
| --- | --- |
| **$name** required | Unique element identifier (all lowercase, no spaces). To avoid any conflicts with other elements please prefix your element name, e.g.: `prefix-element-test`. |
| **$icon** | Icon font CSS class. Bricks includes the following icon fonts. Use any icon font CSS class to represent your element in the builder panel:  [Fontawesome 6](https://fontawesome.com/icons?d=gallery&m=free) (i.e. "fas fa-anchor") [Ionicons 4](https://ionicons.com/v4/cheatsheet.html) (i.e. "ion-md-alarm") [Themify Icons](https://themify.me/themify-icons) (i.e. "ti-bolt-alt") |
| **$css_selector** | By default all CSS control settings are applied to the element wrapper:  `.bricks-element-wrapper`. If you want the default CSS selector to target a child HTML element, set this selector here. |
| **$nestable** | Omit for plain elements. Set to `true` to create a [nestable element](/developer/elements/nestable-elements/). |
| **$scripts** | An array of JavaScript scripts that run when an element is rendered on the frontend or updated in the builder. The Counter element, for example, uses a script named "bricksCounter" (defined in *frontend.min.js*).<br /><br />To load this script we use: `public $scripts = ['bricksCounter'];`<br /><br />Please prefix all your scripts. E.g.: `prefixElementTest` |
| **get_label()** required | Return localised element label. |
| **get_keywords()** | Array of strings that when matched during the element search display the element in the search results. |
| **set_control_groups()** | By default, all element controls show ungrouped in the builder panel under the "Content" tab. Define custom control groups for your element controls by setting the following properties for each control group: **title** — Localized control group title. **tab** — Set to either "content" or "style". |
| **set_controls()** required | Define element controls. For an overview of all available controls and their settings visit: [Element Controls](/developer/controls/element-controls/) |
| **enqueue_scripts()** | Load element-specific scripts and styles. Those are loaded only on pages where this element is used. Results in better performance. Example: `wp_enqueue_script( 'prefix-element-test', get_template_directory_uri() . '/js/custom.js', ['jquery'], '1.0', true );` |
| **render()** required | Renders element HTML. Define HTML attributes via `$this->set_attribute()` and output them via `$this->render_attribute()` |
| **`set_attribute( $key, $attribute, $value )`** | Helper function to set HTML attributes for any HTML tag. `$key` serves as the unique identifier for this HTML tag. `$attribute` is the HTML attribute name. `$value` is a string or array which holds the attribute value(s). |
| **`render_attributes( $key )`** | Helper function to render HTML attributes defined via `$this->set_attribute()`. `$key` serves as the unique identifier for this HTML tag. |
| **`render_dynamic_data_tag( $tag, $context, $args )`** | Helper function to render dynamic data tags inside the render function using `$this->render_dynamic_data_tag(...)`. An example of a `$tag` is the `{post_title}`. Using this helper function sets the correct post Id depending on the environment where the element is being rendered. |
| **`render_dynamic_data( $content )`** | Helper function to render content (string) that could contain dynamic data tags. Use this helper function inside the render function calling `$this->render_dynamic_data(...)`. Using this helper function sets the correct post Id depending on the environment where the element is being rendered. |

Let's populate our element properties and methods with some data:

```php
<?php
// element-test.php

if ( ! defined( 'ABSPATH' ) ) exit; // Exit if accessed directly

class Prefix_Element_Test extends \Bricks\Element {
  // Element properties
  public $category     = 'general'; // Use predefined element category 'general'
  public $name         = 'prefix-test'; // Make sure to prefix your elements
  public $icon         = 'ti-bolt-alt'; // Themify icon font class
  public $css_selector = '.prefix-test-wrapper'; // Default CSS selector
  public $scripts      = ['prefixElementTest']; // Script(s) run when element is rendered on frontend or updated in builder

  // Return localised element label
  public function get_label() {
    return esc_html__( 'Test element', 'bricks' );
  }

  // Set builder control groups
  public function set_control_groups() {
    $this->control_groups['text'] = [ // Unique group identifier (lowercase, no spaces)
      'title' => esc_html__( 'Text', 'bricks' ), // Localized control group title
      'tab' => 'content', // Set to either "content" or "style"
    ];

    $this->control_groups['settings'] = [
      'title' => esc_html__( 'Settings', 'bricks' ),
      'tab' => 'content',
    ];
  }

  // Set builder controls
  public function set_controls() {
    $this->controls['content'] = [ // Unique control identifier (lowercase, no spaces)
      'tab' => 'content', // Control tab: content/style
      'group' => 'text', // Show under control group
      'label' => esc_html__( 'Content', 'bricks' ), // Control label
      'type' => 'text', // Control type
      'default' => esc_html__( 'Content goes here ..', 'bricks' ), // Default setting
    ];

    $this->controls['type'] = [
      'tab' => 'content',
      'group' => 'settings',
      'label' => esc_html__( 'Type', 'bricks' ),
      'type' => 'select',
      'options' => [
        'info' => esc_html__( 'Info', 'bricks' ),
        'success' => esc_html__( 'Success', 'bricks' ),
        'warning' => esc_html__( 'Warning', 'bricks' ),
        'danger' => esc_html__( 'Danger', 'bricks' ),
        'muted' => esc_html__( 'Muted', 'bricks' ),
      ],
      'inline' => true,
      'clearable' => false,
      'pasteStyles' => false,
      'default' => 'info',
    ];
  }

  // Enqueue element styles and scripts
  public function enqueue_scripts() {
    wp_enqueue_script( 'prefix-test-script' );
  }

  // Render element HTML
  public function render() {
    // Set element attributes
    $root_classes[] = 'prefix-test-wrapper';

    if ( ! empty( $this->settings['type'] ) ) {
      $root_classes[] = "color-{$this->settings['type']}";
    }

    // Add 'class' attribute to element root tag
    $this->set_attribute( '_root', 'class', $root_classes );

    // Render element HTML
    // '_root' attribute is required (contains element ID, class, etc.)
    echo "<div {$this->render_attributes( '_root' )}>"; // Element root attributes
      if ( ! empty( $this->settings['content'] ) ) {
        echo "<div>{$this->settings['content']}</div>";
      }
    echo '</div>';
  }
}
```

You can browse the documented Bricks controls at: [/developer/controls/](/developer/controls/)

:::note
All element settings are stored in `$this->settings`. To view of element settings you can print them on the screen like so: `var_dump( $this->settings );` in the `render()` function.
:::

## Load and register your element {#register}

After creating your custom element you need to load and register your element. Open up `functions.php` of your Bricks child theme and copy & paste the following code:

```php
/**
 * Register custom elements
 */
add_action( 'init', function() {
  $element_files = [
    __DIR__ . '/element-test.php',
  ];

  foreach ( $element_files as $file ) {
    \Bricks\Elements::register_element( $file );
  }
}, 11 );
```

The `register_element` method accepts 3 arguments:

- `$file` (required): The full path to the custom element PHP file in the server
- `$name` (optional): A string containing the name of the custom element (e.g.: `prefix-element-test`)
- `$element_class` (optional): A string containing the class name of the element (e.g.: `Prefix_Element_Test`) which should derive from the Bricks element class (`\Bricks\Element`)

:::note
**Note:** Using the `$name` and `$element_class` arguments will improve the loading performance.
:::
