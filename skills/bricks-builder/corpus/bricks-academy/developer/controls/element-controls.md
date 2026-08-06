---
title: "Element Controls"
description: "Reference for the Bricks Element Controls control, including its options, CSS mapping, and usage in custom elements."
canonical: "https://academy.bricksbuilder.io/developer/controls/element-controls/"
markdownUrl: "https://academy.bricksbuilder.io/developer/controls/element-controls.md"
pageType: "article"
section: "developer"
category: "controls"
lastmod: "2026-08-04T12:13:33.000Z"
---
Element controls allow the user to change the content and appearance of an element. You can define the controls of an element with the set_controls() method in your [element PHP class](/developer/elements/create-your-own-elements/).

Example element class with control parameters for control `testColor`:

```php
class Prefix_Element_Test extends \Bricks\Element {
  public function set_controls() {
    $this->controls['testColor'] = [
      'tab' => 'content',
      'group' => 'settings',
      'label' => esc_html__( 'Text color', 'bricks' ),
      'type' => 'color',
      'inline' => true,
      'small' => true,
      'css' => [
        [
          'property' => 'color',
          'selector' => '.content',
          'important' => true, // Optional
        ],
      ],
      'default' => [
        'rgb' => 'rgba(158, 158, 158, .8)',
        'hex' => '#9e9e9e',
      ],
      'pasteStyles' => false,
      'description' => esc_html__( 'Define the content color.', 'bricks' ),
      'required' => ['showText', '!=', ''],
    ];
  }
}
```

The following control parameters are available for all control types. To dive deeper into the arguments of a specific control type select the control from the list at the bottom.

### Universal control arguments

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| tab | string | content | Tab under which to show the control. Accepts: `content` or `style`. |
| group | string |  | Group under which to show the control. By default a control shows ungrouped under the `content` tab. |
| label | string |  | Localized control label. E.g.: `esc_html__( 'Color', 'bricks' ),` |
| type | string |  | Set the control type (see the list below for a list of all available control types). |
| inline | bool | false | Set to true to show control label and input on the same line. |
| small | bool | false | Set to true to show a control input of 60px width. By default inline label and input have equal widths of 50%. |
| css | array |  | Array with CSS rule definitions. Each CSS rule is a separate array and requires a `property` and `selector` parameter. |
| default | string/array |  | Default control value. Either a string or an array (depending on the control type, see control list below for specific control default) |
| pasteStyles | bool | true | Set to true excludes setting from being pasted via the builders' custom right click "Paste Styles". Recommended for all controls that output HTML content instead of CSS. |
| description | string |  | Optional description for controls that need additional explanation or link to a resource. |
| required | array |  | Show control in relation to the setting of another control.<br /><br />Parameter #1: control ID<br /><br />Parameter #2: comparison operator: `=`, `!=`, `>`, `<`, `>=`, `<=`<br /><br />Example: `'required' => ['layout', '=', ['list', 'grid']],`<br /><br />Required condition: Show this control if setting value of control `layout` equals `=` either `list` or `grid`. |

### Controls Types

| Control Type | Output (Content/CSS) |
| --- | --- |
| [apply](/developer/controls/apply-control/) | None |
| [align-items](/developer/controls/align-items-control/) | CSS |
| [audio](/developer/controls/audio-control/) | Content |
| [background](/developer/controls/background-control/) | CSS |
| [border](/developer/controls/border-control/) | CSS |
| [box-shadow](/developer/controls/box-shadow-control/) | CSS |
| [checkbox](/developer/controls/checkbox-control/) | Conditional |
| [code](/developer/controls/code-control/) | Content |
| [color](/developer/controls/color-control/) | CSS |
| [datepicker](/developer/controls/datepicker-control/) | Content |
| [dimensions](/developer/controls/dimensions-control/) | CSS |
| [direction](/developer/controls/direction-control/) | CSS |
| [editor](/developer/controls/editor-control/) | Content |
| [filters](/developer/controls/filters-control/) | CSS |
| [gradient](/developer/controls/gradient-control/) | CSS |
| [icon](/developer/controls/icon-control/) | Content |
| [image](/developer/controls/image-control/) | Content/CSS |
| [image-gallery](/developer/controls/image-gallery-control/) | Content |
| [info](/developer/controls/info-control/) | Builder panel only |
| [justify-content](/developer/controls/justify-content-control/) | CSS |
| [link](/developer/controls/link-control/) | Content |
| [number](/developer/controls/number-control/) | Content/CSS |
| [posts](/builder/elements/wordpress/posts/) | Content |
| [repeater](/developer/controls/repeater-control/) | Content |
| [select](/developer/controls/select-control/) | Content/CSS |
| [slider](/developer/controls/slider-control/) | Content |
| [svg](/developer/controls/svg-control/) | Content |
| [text](/developer/controls/text-control/) | Content |
| [textarea](/developer/controls/textarea-control/) | Content |
| [text-align](/developer/controls/text-align-control/) | CSS |
| [text-decoration](/developer/controls/text-decoration-control/) | CSS |
| [text-shadow](/developer/controls/text-shadow-control/) | CSS |
| [text-transform](/developer/controls/text-transform-control/) | CSS |
| [typography](/developer/controls/typography-control/) | CSS |
