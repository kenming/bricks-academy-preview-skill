The Icon element displays an icon from various icon libraries or custom SVG icons.

## Settings

- **Icon** (icon) - Select an icon from the available icon libraries (Themify, Font Awesome, Ionicons, etc.). Default: `ti-star` from Themify library.

- **Color** (color) - The icon color. Applies to both icon font and SVG fill.

- **Size** (number with units) - The icon size using font-size property.

- **Link** (link) - Make the icon clickable by adding a link.

### Accordion integration

The following settings are only available when the icon is placed inside an Accordion (Nestable) element title wrapper:

- **Is Accordion (Nestable) Icon** (checkbox) - Enable accordion-specific behavior for the icon.

- **Show** (select) - Control icon visibility based on accordion state. Options: `collapsed`, `expanded`. Default: Always visible. When set to a specific state, duplicate the icon element and set different states to show different icons.

- **Transform (Expanded)** (transform) - CSS transform properties to apply when the accordion item is expanded. By default, icons rotate 90° when expanded.

:::tip[Developer reference]
See the [Icon Schema](/developer/schema/elements/icon/) for the full JSON schema of this element's settings and controls.
:::
