The Nav Menu element displays WordPress navigation menus with customizable styling and behavior. It supports mega menus, multilevel navigation, mobile responsiveness, and various animation effects.

## Settings

### Menu Selection

- **Menu (WordPress)** (select) - Select a WordPress navigation menu to display. Options are populated from available WordPress menus. Includes a link to manage menus in WordPress admin.

- **Alignment** (direction) - Layout direction of the menu. Controls `flex-direction` property for `.bricks-nav-menu` selector.

### Top level

- **Justify content** (justify-content) - Horizontal alignment of menu items. Excludes space options. Controls `justify-content` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle` selectors.

- **Gap** (number with units) - Gap between menu items. Controls `gap` property for `.bricks-nav-menu` selector.

- **Margin** (spacing) - Margin around menu items. Controls `margin` property for `.bricks-nav-menu > li` selector.

- **Padding** (spacing) - Padding inside menu items. Controls `padding` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle > *` selectors.

- **Background** (background) - Background styling for menu items. Excludes video. Controls `background` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle` selectors.

- **Border** (border) - Border styling for menu items. Controls `border` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle` selectors.

- **Typography** (typography) - Font settings for top-level menu items. Controls `font` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle > *` selectors.

#### Active State

- **Active** (separator) - Visual separator for active state controls.

- **Active background** (background) - Background styling for active/current page items. Controls `background` property for current menu item selectors including `.bricks-nav-menu > .current-menu-item > a`, `.bricks-nav-menu > .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active border** (border) - Border styling for active items. Controls `border` property for current menu item selectors including `.bricks-nav-menu .current-menu-item > a`, `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active typography** (typography) - Typography settings for active items. Controls `font` property for current menu item selectors including `.bricks-nav-menu .current-menu-item > a`, `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle > *`, and ancestor selectors.

#### Icon

- **Icon** (separator) - Separator for icon controls.

- **Icon (Sub menu)** (icon) - Icon for submenu toggles. Triggers re-render. Controls SVG rendering for `.bricks-nav-menu > li.menu-item > .brx-submenu-toggle svg` selector.

- **Icon transform** (transform) - Transform settings for submenu icons when closed. Controls `transform` property for `.bricks-nav-menu button[aria-expanded="false"] > *` selector.

- **Icon transform (Open)** (transform) - Transform settings for submenu icons when open. Controls `transform` property for `.bricks-nav-menu button[aria-expanded="true"] > *` selector.

- **Icon typography** (typography) - Typography settings for submenu toggle buttons. Excludes font-family, font-weight, font-style, text-align, text-decoration, text-transform, and letter-spacing. Controls `font` property for `.bricks-nav-menu > li.menu-item-has-children > .brx-submenu-toggle button[aria-expanded]` selector.

- **Icon position** (select) - Position of submenu icons. Options from icon position control options. Default placeholder: "Right".

- **Icon margin** (spacing) - Margin around submenu toggle buttons. Controls `margin` property for `.bricks-nav-menu .brx-submenu-toggle button` selector.

- **Icon padding** (spacing) - Padding inside submenu toggle buttons. Controls `padding` property for `.bricks-nav-menu .brx-submenu-toggle button` selector.

### Sub menu

- **Position: Static** (checkbox) - Enable to position submenus in document flow (e.g. inside offcanvas). Description: "Enable to position in document flow (e.g. inside offcanvas)."

- **Background** (background) - Background styling for sub-menus. Excludes video. Controls `background` property for `.bricks-nav-menu .sub-menu` selector.

- **Border** (border) - Border styling for sub-menus. Controls `border` property for `.bricks-nav-menu .sub-menu` selector.

- **Box shadow** (box-shadow) - Shadow effect for sub-menus. Controls `box-shadow` property for `.bricks-nav-menu .sub-menu` selector.

- **Transform** (transform) - Transform settings for sub-menus. Controls `transform` property for `.bricks-nav-menu > li > .sub-menu` and `.bricks-nav-menu > li > .brx-megamenu` selectors.

- **Transform (Open)** (transform) - Transform settings for sub-menus when open. Controls `transform` property for `.bricks-nav-menu > li.open > .sub-menu` and `.bricks-nav-menu > li.open > .brx-megamenu` selectors.

#### Caret

- **Caret** (separator) - Separator for caret controls.

- **Size** (number with units) - Size of the caret (triangle pointer). Triggers re-render. Controls `border-width` property for `.bricks-nav-menu > li > .sub-menu.caret::before` selector.

- **Color** (color) - Color of the caret. Controls `border-bottom-color` property for `.bricks-nav-menu > li > .sub-menu.caret::before` selector. Only available when caret size is set.

- **Transform** (transform) - Transform settings for the caret. Controls `transform` property for `.bricks-nav-menu > li > .sub-menu.caret::before` selector. Only available when caret size is set.

- **Position** (dimensions) - Position settings for the caret. Controls positioning properties for `.bricks-nav-menu > li > .sub-menu.caret::before` selector. Only available when caret size is set.

#### Item

- **Item** (separator) - Separator for submenu item controls.

- **Justify content** (justify-content) - Horizontal alignment of submenu items. Excludes space options. Controls `justify-content` property for `.bricks-nav-menu .sub-menu a` and `.bricks-nav-menu .sub-menu button` selectors.

- **Padding** (spacing) - Padding inside submenu items. Controls `padding` property for `.bricks-nav-menu .sub-menu a` and `.bricks-nav-menu .sub-menu button` selectors.

- **Background** (background) - Background styling for submenu items. Controls `background` property for `.bricks-nav-menu .sub-menu .menu-item` selector.

- **Border** (border) - Border styling for submenu items. Controls `border` property for `.bricks-nav-menu .sub-menu > li` selector.

- **Typography** (typography) - Font settings for submenu items. Controls `font` property for `.bricks-nav-menu .sub-menu > li > a` and `.bricks-nav-menu .sub-menu > li > .brx-submenu-toggle > *` selectors.

#### Active State

- **Active** (separator) - Separator for submenu active state controls.

- **Active background** (background) - Background styling for active submenu items. Controls `background` property for current submenu item selectors including `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active border** (border) - Border styling for active submenu items. Controls `border` property for current submenu item selectors including `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active typography** (typography) - Typography settings for active submenu items. Controls `font` property for current submenu item selectors including `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle > *`, and ancestor selectors.

#### Icon

- **Icon** (separator) - Separator for submenu icon controls.

- **Icon** (icon) - Icon for submenu toggles. Triggers re-render. Controls SVG rendering for `.bricks-nav-menu .sub-menu .brx-submenu-toggle svg` selector.

- **Icon size** (number with units) - Size of submenu icons. Controls `height` and `width` properties for `.bricks-nav-menu .sub-menu .brx-submenu-toggle svg` selector, and `font-size` for `.bricks-nav-menu .sub-menu .brx-submenu-toggle i` selector.

- **Icon transform** (transform) - Transform settings for submenu icons. Controls `transform` property for `.bricks-nav-menu .sub-menu button > *` selector.

- **Icon transform (Open)** (transform) - Transform settings for submenu icons when open. Controls `transform` property for `.bricks-nav-menu .sub-menu button[aria-expanded="true"] > *` selector.

- **Icon typography** (typography) - Typography settings for submenu toggle buttons. Excludes font-family, font-weight, font-style, text-align, text-decoration, text-transform, and letter-spacing. Controls `font` property for `.bricks-nav-menu .sub-menu .brx-submenu-toggle > a + button` selector.

- **Icon position** (select) - Position of submenu icons. Options from icon position control options. Default placeholder: "Right".

- **Icon margin** (spacing) - Margin around submenu toggle buttons. Controls `margin` property for `.bricks-nav-menu .sub-menu .brx-submenu-toggle button` selector.

- **Icon padding** (spacing) - Padding inside submenu toggle buttons. Controls `padding` property for `.bricks-nav-menu .sub-menu .brx-submenu-toggle button` selector.

### Mobile menu

- **Mobile menu** (separator) - Separator for mobile menu controls.

- **Hide at breakpoint** / **Show at breakpoint** (select) - Breakpoint at which to show/hide mobile menu. Options include all breakpoints plus "Always" and "Never". Default placeholder: "Mobile landscape". Triggers re-render.

- **Position** (select) - Position of mobile menu. Options: Right, Left. Default placeholder: "Left".

- **Top** (number with units) - Top position of mobile menu. Controls `top` property for `.bricks-mobile-menu-wrapper` selector.

- **Width** (number with units) - Width of mobile menu. Controls `width` property for `.bricks-mobile-menu-wrapper` selector. Default placeholder: "300px".

- **Height** (number with units) - Height of mobile menu. Controls `height` property for `.bricks-mobile-menu-wrapper` selector.

- **Fade in** (checkbox) - Enable fade-in animation for mobile menu.

- **Vertical** (justify-content) - Vertical alignment of mobile menu content. Controls `justify-content` property for `.bricks-mobile-menu-wrapper` selector. Default placeholder: "Top".

- **Horizontal** (align-items) - Horizontal alignment of mobile menu content. Excludes stretch option. Controls `align-items` and `justify-content` properties for `.bricks-mobile-menu-wrapper` selector, and sets `width` to `auto` for `.bricks-mobile-menu-wrapper a`. Default placeholder: "Top".

- **Text align** (text-align) - Text alignment in mobile menu. Controls `text-align` property for `.bricks-mobile-menu-wrapper` selector.

- **Background** (background) - Background styling for mobile menu wrapper. Controls `background` property for `.bricks-mobile-menu-wrapper:before` selector.

- **Background filters** (filters) - Background filters for mobile menu. Controls `filter` property for `.bricks-mobile-menu-wrapper:before` selector.

- **Box shadow** (box-shadow) - Shadow effect for mobile menu. Controls `box-shadow` property for `.bricks-mobile-menu-wrapper:before` selector.

- **Overlay** (background) - Background styling for mobile menu overlay. Excludes video. Controls `background` property for `.bricks-mobile-menu-overlay` selector.

#### Top level

- **Top level** (separator) - Separator for mobile menu top-level controls.

- **Padding** (spacing) - Padding for top-level mobile menu items. Controls `padding` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle > *` selectors. Default placeholder: top 0, right 30, bottom 0, left 30.

- **Background** (color) - Background color for mobile menu items. Controls `background-color` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle` selectors.

- **Background (Active)** (color) - Background color for active mobile menu items. Controls `background-color` property for `[aria-current="page"]` and `.bricks-mobile-menu > .current-menu-item > .brx-submenu-toggle` selectors.

- **Border** (border) - Border styling for mobile menu items. Controls `border` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle` selectors.

- **Border (Active)** (border) - Border styling for active mobile menu items. Controls `border` property for current menu item selectors.

- **Typography** (typography) - Font settings for mobile menu items. Excludes text-align. Controls `font` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle > *` selectors.

- **Typography (Active)** (typography) - Typography settings for active mobile menu items. Excludes text-align. Controls `font` property for various current menu item selectors.

#### Icon

- **Icon (Sub menu)** (icon) - Icon for mobile submenu toggles. Triggers re-render. Controls SVG rendering for `.bricks-mobile-menu-wrapper .brx-submenu-toggle svg` selector.

- **Close icon (Sub menu)** (icon) - Close icon for mobile submenu toggles. Triggers re-render. Only available when main icon is set. Controls SVG rendering for `.bricks-mobile-menu-wrapper .brx-submenu-toggle svg.close` selector.

- **Icon typography** (typography) - Typography settings for mobile submenu toggle buttons. Excludes font-family, font-weight, font-style, text-align, text-decoration, text-transform, and letter-spacing. Controls `font` property for `.bricks-mobile-menu > .menu-item-has-children .brx-submenu-toggle button` selector. Only available when icon is set.

- **Icon position** (select) - Position of mobile submenu icons. Options from icon position control options. Default placeholder: "Right".

- **Icon margin** (spacing) - Margin around mobile submenu toggle buttons. Controls `margin` property for `.bricks-mobile-menu .menu-item-has-children .brx-submenu-toggle button` selector.

#### Sub menu

- **Sub menu** (separator) - Separator for mobile submenu controls. Description: "Keep open while styling".

- **Padding** (spacing) - Padding for mobile submenu items. Controls `padding` property for `.bricks-mobile-menu .sub-menu > .menu-item > a` and `.bricks-mobile-menu .sub-menu > .menu-item > .brx-submenu-toggle > *` selectors.

- **Background** (color) - Background color for mobile submenu items. Controls `background-color` property for `.bricks-mobile-menu .sub-menu > .menu-item > a` and `.bricks-mobile-menu .sub-menu > .menu-item > .brx-submenu-toggle` selectors.

- **Background (Active)** (color) - Background color for active mobile submenu items. Controls `background-color` property for current submenu item selectors.

- **Border** (border) - Border styling for mobile submenu items. Controls `border` property for `.bricks-mobile-menu .sub-menu > .menu-item` selector.

- **Border (Active)** (border) - Border styling for active mobile submenu items. Controls `border` property for current submenu item selectors.

- **Typography** (typography) - Font settings for mobile submenu items. Controls `font` property for `.bricks-mobile-menu .sub-menu > li > a` and `.bricks-mobile-menu .sub-menu > li > .brx-submenu-toggle > *` selectors.

- **Active typography** (typography) - Typography settings for active mobile submenu items. Controls `font` property for current submenu item selectors.

#### Hamburger toggle

- **Hamburger toggle** (separator) - Separator for hamburger toggle controls.

- **aria-label** (text) - Accessibility label for hamburger toggle button. Default placeholder: "Open mobile menu".

- **Toggle width** (number with units) - Width of hamburger toggle bars. Controls `width` property for `.bricks-mobile-menu-toggle`, `.bricks-mobile-menu-toggle .bar-top`, `.bricks-mobile-menu-toggle .bar-center`, and `.bricks-mobile-menu-toggle .bar-bottom` selectors with `!important`.

- **Color** (color) - Color of hamburger toggle bars. Controls `color` property for `.bricks-mobile-menu-toggle` selector.

- **Hide close** (checkbox) - Hide hamburger toggle when mobile menu is open. Controls `display` property for `&.show-mobile-menu .bricks-mobile-menu-toggle` selector (sets to `none` with `!important`).

- **Color close** (color) - Color of hamburger toggle when mobile menu is open. Controls `color` property for `&.show-mobile-menu .bricks-mobile-menu-toggle` selector with `!important`.

- **Close position** (dimensions) - Position of hamburger toggle when mobile menu is open. Controls positioning properties for `&.show-mobile-menu .bricks-mobile-menu-toggle` selector.

### Mega menu

- **Enable** (checkbox) - Enable mega menu functionality.

- **CSS selector** (text) - CSS selector for mega menu positioning. Uses width & horizontal position of target node. Only available when mega menu is enabled.

- **Toggle on** (select) - How mega menus are triggered. Options: Click, Hover, Click or hover. Default placeholder: "Hover". Only available when mega menu is enabled.

- **Transition** (text) - Transition settings for mega menus. Supports dynamic data. Controls `transition` property for `.brx-megamenu` selector. Only available when mega menu is enabled.

- **Transform** (transform) - Transform settings for mega menus. Controls `transform` property for `.bricks-nav-menu > .brx-has-megamenu > .brx-megamenu` selector. Only available when mega menu is enabled.

- **Transform (Open)** (transform) - Transform settings for mega menus when open. Controls `transform` property for `.bricks-nav-menu > .brx-has-megamenu.open > .brx-megamenu` selector. Only available when mega menu is enabled.

### Multilevel

- **Enable** (checkbox) - Enable multilevel navigation functionality.

- **Back: Text** (text) - Text for back button in multilevel navigation. Only available when multilevel is enabled.

- **Back: Typography** (typography) - Typography settings for back button. Controls `font` property for `.brx-multilevel-back` selector. Only available when multilevel is enabled.

- **Back: Background** (color) - Background color for back button. Controls `background-color` property for `.brx-multilevel-back` selector. Only available when multilevel is enabled.

:::tip[Developer reference]
See the [Nav Menu Schema](/developer/schema/elements/nav-menu/) for the full JSON schema of this element's settings and controls.
:::
