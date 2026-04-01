The Accordion element creates collapsible content sections with titles and expandable content.

## Settings

- **Accordion** (repeater) - Add accordion items. Each item has:
  - **Title** (text) - The clickable title of the accordion item.
  - **ID** (text) - Anchor ID for linking to the item (no spaces, no pound sign).
  - **Subtitle** (text) - Optional subtitle below the title.
  - **Content** (rich text) - The expandable content of the item.

- **Expand item indexes** (text) - Comma-separated indexes of items to expand on page load (starting at 0).

- **Independent toggle** (checkbox) - Allow multiple items to be open simultaneously. Enable to open & close an item without toggling other items.

- **Transition (ms)** (number) - Animation duration for expanding/collapsing in milliseconds. Default: 200.

- **FAQ schema** (checkbox) - Generate FAQPage structured data (JSON-LD) for search engines.

### Title

- **HTML tag** (select) - HTML tag for titles. Options: `div`, `h1`-`h6`. Default: `h3`.

- **Icon** (icon) - Icon for collapsed state. Default: right arrow (ion-ios-arrow-forward).

- **Icon typography** (typography) - Font settings for the collapsed icon.

- **Icon expanded** (icon) - Icon for expanded state. Default: down arrow (ion-ios-arrow-down).

- **Icon expanded typography** (typography) - Font settings for the expanded icon.

- **Icon position** (select) - Position of the icon relative to text. Default: Right.

- **Icon rotate in °** (number) - Rotation angle for the icon in degrees. Icon rotation for expanded accordion.

- **Margin** (spacing) - Margin around title wrappers.

- **Padding** (spacing) - Padding inside title wrappers.

- **Title typography** (typography) - Typography settings for title text.

- **Subtitle typography** (typography) - Typography settings for subtitle text.

- **Background color** (color) - Background color for title wrappers.

- **Border** (border) - Border styling for title wrappers.

- **Box shadow** (box-shadow) - Box shadow for title wrappers.

- **Active typography** (typography) - Typography settings for active/expanded title text.

- **Active background** (color) - Background color for active/expanded title wrappers.

- **Active border** (border) - Border styling for active/expanded title wrappers.

### Content

- **Margin** (spacing) - Margin around content wrappers.

- **Padding** (spacing) - Padding inside content wrappers.

- **Content typography** (typography) - Typography settings for content text.

- **Background color** (color) - Background color for content wrappers.

- **Border** (border) - Border styling for content wrappers.

:::tip[Developer reference]
See the [Accordion Schema](/developer/schema/elements/accordion/) for the full JSON schema of this element's settings and controls.
:::
