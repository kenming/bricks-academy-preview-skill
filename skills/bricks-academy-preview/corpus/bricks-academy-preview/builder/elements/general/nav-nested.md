The Nav (Nestable) element creates hierarchical navigation menus with dropdown functionality, multilevel support, and mobile-responsive behavior. It supports nested menu structures and can be used to build complex navigation systems.

## Settings

### HTML Tag & Accessibility

- **HTML tag** (text) - HTML tag for the navigation element. Supports dynamic data. Default placeholder: `nav`. Validates HTML tag format.

- **aria-label** (text) - Accessibility label for the navigation. Supports dynamic data. Default placeholder: "Menu".

### Top Level (Item)

- **Gap** (number with units) - Gap between top-level navigation items. Controls `gap` property for `.brx-nav-nested-items` selector.

- **Justify content** (justify-content) - Horizontal alignment of top-level items. Deprecated since version 1.10. Description suggests using "Align items" under "Mobile menu" instead. Direction: row. Excludes space options.

- **Padding** (spacing) - Padding for top-level navigation items. Controls `padding` property for multiple selectors including `.brx-nav-nested-items > li > a`, text links, icons, SVG elements, and submenu toggles.

- **Background color** (color) - Background color for top-level items. Controls `background-color` property for links, text links, icons, SVG elements, and submenu toggles.

- **Border** (border) - Border styling for top-level items. Controls `border` property for links, text links, icons, SVG elements, and submenu toggles.

- **Typography** (typography) - Typography settings for top-level items. Controls `font` property for links, text links, icons, SVG elements, and submenu toggles.

- **Transform** (transform) - Transform settings for top-level items. Controls `transform` property for links, text links, icons, SVG elements, and submenu toggles.

- **Transition** (text) - Transition settings for top-level items. Supports dynamic data. Controls `transition` property for list items, links, text links, icons, SVG elements, submenu toggles, and submenu toggle children.

#### Active State

- **Active** (separator) - Visual separator for active state controls.

- **Background color** (color) - Background color for active/current page items. Controls `background-color` property for `[aria-current="page"]` and `.brx-submenu-toggle.aria-current` selectors.

- **Border** (border) - Border styling for active items. Controls `border` property for `[aria-current="page"]` and `.brx-submenu-toggle.aria-current` selectors.

- **Typography** (typography) - Typography settings for active items. Controls `font` property for `[aria-current="page"]` and `.brx-submenu-toggle.aria-current > *` selectors.

#### Dropdown (Top Level Only)

- **Dropdown** (separator) - Separator for top-level dropdown controls. Description: "Only applies to top level dropdown elements."

- **Text padding** (spacing) - Padding for dropdown text. Controls `padding` property for `.brx-nav-nested-items > li > .brx-submenu-toggle > span` selector.

- **Icon padding** (spacing) - Padding for dropdown icons. Controls `padding` property for `.brx-nav-nested-items > li > .brx-submenu-toggle button` selector.

- **Gap** (number with units) - Gap between text and icon in dropdown toggles. Controls `gap` property for `.brx-nav-nested-items > li > .brx-submenu-toggle` selector.

### Dropdown

#### Text

- **Text** (separator) - Separator for dropdown text controls. Description: "Control dropdown element text."

- **Text padding** (spacing) - Padding for dropdown text. Controls `padding` property for `.brx-submenu-toggle span` selector (applies to all dropdowns).

#### Icon

- **Icon** (separator) - Separator for dropdown icon controls. Description: "Edit dropdown to set icon individually."

- **Icon padding** (spacing) - Padding for dropdown icons. Controls `padding` property for `.brx-submenu-toggle button` selector.

- **Gap** (number with units) - Gap between text and icon in dropdown toggles. Controls `gap` property for `.brx-submenu-toggle` selector.

- **Icon position** (select) - Position of the dropdown icon. Options from icon position control options. Default placeholder: "Right". Controls `flex-direction` property for `.brx-submenu-toggle` selector (sets to `row-reverse` when left).

- **Icon size** (number with units) - Size of the dropdown icon. Controls `font-size` property for `.brx-submenu-toggle button` selector.

- **Icon color** (color) - Color of the dropdown icon. Controls `color` property for `.brx-submenu-toggle button` selector.

- **Icon transform** (transform) - Transform settings for dropdown icons. Controls `transform` property for `.brx-submenu-toggle button > *` selector (targets icon only).

- **Icon transform (Open)** (transform) - Transform settings for dropdown icons when open. Controls `transform` property for `.brx-submenu-toggle button[aria-expanded="true"] > *` selector (targets icon only).

- **Icon transition** (text) - Transition settings for dropdown icons. Supports dynamic data. Controls `transition` property for `.brx-submenu-toggle button[aria-expanded] > *` selector (targets icon only). Uses `!important` to override other transitions.

#### Content

- **Content** (separator) - Separator for dropdown content controls. Description: "Sub menu, mega menu, or multilevel area."

- **Min. width** (number with units) - Minimum width for dropdown content. Controls `min-width` property for `.brx-dropdown-content` selector. Triggers re-render.

- **Background color** (color) - Background color for dropdown content. Controls `background-color` property for `.brx-dropdown-content` selector.

- **Border** (border) - Border styling for dropdown content. Controls `border` property for `.brx-dropdown-content` selector.

- **Box shadow** (box-shadow) - Box shadow for dropdown content. Controls `box-shadow` property for `.brx-dropdown-content` selector.

- **Typography** (typography) - Typography settings for dropdown content. Controls `font` property for `.brx-dropdown-content` selector.

- **Transform** (transform) - Transform settings for dropdown content. Controls `transform` property for `.brx-nav-nested-items > .brxe-dropdown > .brx-dropdown-content` selector.

- **Transform (Open)** (transform) - Transform settings for dropdown content when open. Controls `transform` property for `.brx-nav-nested-items > .brxe-dropdown.open > .brx-dropdown-content` selector.

- **Transition** (text) - Transition settings for dropdown content. Supports dynamic data. Controls `transition` property for `.brx-dropdown-content` selector.

- **Z-index** (number) - Z-index for dropdown elements. Controls `z-index` property for `.brxe-dropdown` selector. Default placeholder: 1001.

#### Item

- **Item** (separator) - Separator for dropdown item controls.

- **Padding** (spacing) - Padding for dropdown items. Controls `padding` property for `.brx-dropdown-content > li > a` and `.brx-dropdown-content :where(.brx-submenu-toggle > *)` selectors.

- **Background** (color) - Background color for dropdown items. Controls `background-color` property for `.brx-dropdown-content > li` and `.brx-dropdown-content .brx-submenu-toggle` selectors.

- **Border** (border) - Border styling for dropdown items. Controls `border` property for `.brx-dropdown-content > li:not(.brxe-dropdown)` and `.brx-dropdown-content .brx-submenu-toggle` selectors.

- **Typography** (typography) - Typography settings for dropdown items. Controls `font` property for `.brx-dropdown-content > li > a` and `.brx-dropdown-content .brx-submenu-toggle > *` selectors.

- **Transition** (text) - Transition settings for dropdown items. Supports dynamic data. Controls `transition` property for dropdown content items, links, submenu toggles, and megamenu elements.

#### Multilevel

- **Multilevel** (separator) - Separator for multilevel controls. Description: "Show only active dropdown. Toggle on click. Inner dropdowns inherit multilevel."

- **Enable** (checkbox) - Enable multilevel dropdown functionality.

- **Back: Text** (text) - Text for the back button in multilevel navigation. Only available when multilevel is enabled.

- **Back: Typography** (typography) - Typography settings for the back button. Only available when multilevel is enabled. Controls `font` property for `.brx-multilevel-back` selector.

- **Back: Background** (color) - Background color for the back button. Only available when multilevel is enabled. Controls `background-color` property for `.brx-multilevel-back` selector.

### Mobile Menu

- **Mobile menu** (separator) - Separator for mobile menu controls. Description: "Insert "Toggle" element after "Nav items" to show/hide your mobile menu."

- **Keep open while styling** (checkbox) - Keep mobile menu open during styling in the builder. Adds `brx-open` class. Not saved as setting.

- **Hide at breakpoint** / **Show at breakpoint** (select) - Breakpoint at which to show/hide mobile menu. Options include all breakpoints plus "Always" and "Never". Default placeholder: "Mobile landscape". Triggers re-render.

- **Width** (number with units) - Width of the mobile menu. Controls `width` property for `&.brx-open .brx-nav-nested-items` selector.

- **Height** (number with units) - Height of the mobile menu. Controls `height` property for `&.brx-open .brx-nav-nested-items` selector.

- **Padding (Dropdown)** (spacing) - Padding for dropdown content in mobile view. Controls padding for `&.brx-open .brx-dropdown-content > *` selector. Description: "Used to create visual hierarchy between nested dropdowns."

- **Align items** (align-items) - Vertical alignment of mobile menu items. Controls `align-items` property for `&.brx-open .brx-nav-nested-items` selector.

- **Justify content** (justify-content) - Horizontal alignment of mobile menu items. Controls `justify-content` property for `&.brx-open .brx-nav-nested-items` selector.

- **Position** (dimensions) - Position settings for the mobile menu. Controls multiple position properties.

- **Background color** (color) - Background color for the mobile menu. Controls `background-color` property for mobile menu selectors.

#### Item

- **Item** (separator) - Separator for mobile menu item controls.

- **Align items** (align-items) - Vertical alignment of mobile menu items. Excludes `stretch` option. Controls `align-items` property for various mobile menu item selectors.

:::tip[Developer reference]
See the [Nav (Nestable) Schema](/developer/schema/elements/nav-nested/) for the full JSON schema of this element's settings and controls.
:::
