---
title: "Datepicker Control"
description: "Reference for the Bricks Datepicker control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/datepicker-control/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/datepicker-control.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-08-20T13:12:40.000Z"
---
The datepicker control provides a great interface for selecting a specific date and time and outputting it in the [format of your choice](http://hilios.github.io/jQuery.countdown/documentation.html#directives).

The Datepicker control leverages the Flatpickr library to offer a robust date selection interface. Since Bricks 1.9.8 an `options` property has been added which allows for further customization.

## Properties:

### Property: options (since 1.9.8)

- **Type:** array (associative)
- **Description:** Enables customization of the datepicker by passing an associative array of options defined in the Flatpickr library.
- **Default values:**
  - **enableTime:** Defaults to `true` unless explicitly set through a passed property.
  - **altInput:** Defaults to `true` unless specified otherwise through a passed property.

**Example usage:**

```php
$this->controls['date'] = [
  'tab' => 'content',
  'label' => esc_html__('Date', 'bricks'),
  'type' => 'datepicker',
  'options' => [
    'enableTime' => true,  // Enables time selection.
    'time_24hr' => true,   // Displays time picker in 24-hour mode.
    'noCalendar' => true   // Hides the calendar day selection.
  ]
];
```

In this example, the `options` array is configured to create a time picker that operates in 24-hour format without showing a calendar for day selection. The `enableTime` option is set to true to ensure time can be selected, `time_24hr` is enabled for 24-hour time format, and `noCalendar` is set to true to hide the calendar component. Adjust the `options` array as needed to customize the datepicker to meet different requirements.

For a full list of customizable options available in Flatpickr, please refer to the [Flatpickr Options documentation](https://flatpickr.js.org/options/).

### Property: enableTime

- **Type:** boolean
- **Description:** Determines whether time selection is enabled. Overridden if any settings are passed in the `options` property.
- **Default:** true

### Property: altInput

- **Type:** boolean
- **Description:** Enables an alternative, more user-friendly input style. Overridden if any settings are passed in the `options` property.
- **Default:** true

## Example: Countdown element

```php
// Example: Countdown element
class Prefix_Element_Countdown extends \Bricks\Element {
  public $category = 'general';
  public $name     = 'countdown';
  public $icon     = 'ti-timer';
  public $scripts  = ['bricksCountdown'];

  public function get_label() {
    return esc_html__( 'Countdown', 'bricks' );
  }

  public function set_controls() {
    $this->controls['date'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Date', 'bricks' ),
      'type' => 'datepicker',
      'options' => ['enableTime' => true, 'altInput' => true],
      'default' => '2019-01-01 12:00',
    ];

    $this->controls['format'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Format', 'bricks' ),
      'type' => 'text',
      'default' => '%D days %H hours %M minutes %S seconds.',
      'description' => sprintf(
        '%s <a target="_blank" href="http://hilios.github.io/jQuery.countdown/documentation.html#directives">%s</a>.',
        esc_html__( 'For formatting options see', 'bricks' ),
        esc_html__( 'directives', 'bricks' )
      ),
    ];
  }

  public function render() {
    $this->set_attribute( 'wrapper', 'class', 'countdown-wrapper' );

    $countdown_options = [
      'date' => isset( $this->settings['date'] ) ? $this->settings['date'] : '',
      'format' => isset( $this->settings['format'] ) ? $this->settings['format'] : '',
    ];

    $this->set_attribute( 'wrapper', 'data-bricks-countdown-options', wp_json_encode( $countdown_options ) );

    // Render
    if ( ! isset( $this->settings['date'] ) || ! isset( $this->settings['format'] ) ) {
      return $this->render_element_placeholder( [
        'icon-class' => 'ti-timer',
        'text'       => esc_html__( 'No date/format set.', 'bricks' ),
      ] );
    } else {
      echo '<div ' . $this->render_attributes( 'wrapper' ) . '></div>';
    }
  }
}
```
