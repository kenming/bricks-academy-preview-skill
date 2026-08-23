---
title: "Dropdown"
description: "The Dropdown element is a nestable menu item: a toggle (link/text + optional icon button) with a dropdown panel (default inner structure is a Div with tag ul."
canonical: "https://academy.bricksbuilder.io/builder/elements/general/dropdown/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/general/dropdown.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-20T13:12:40.000Z"
---
The **Dropdown** element is a **nestable** menu item: a toggle (link/text + optional icon button) with a **dropdown panel** (default inner structure is a **Div** with tag `ul` and class `brx-dropdown-content` containing links). Use it inside [Nav (Nestable)](/builder/elements/general/nav-nested/) or similar structures.

Default HTML tag for the root is **`li`**. The script `bricksSubmenuPosition` handles positioning.

## Top-level

- **HTML tag** (text) — Root tag; validated in the builder. Placeholder: `li`.

- **Text** (text) — Label for the trigger. Default: “Dropdown”.

- **Link to** (link) — Optional link around the text (lightbox fields excluded).

- **Attribute: aria-label** (text) — Applied to the **toggle button** when an icon is present. Placeholder: “Toggle dropdown”.

## Icon

- **Icon** (icon) — If set, shown in the toggle **button** next to the text.

- **Icon padding** (spacing) — On `.brx-submenu-toggle button`.

- **Gap** (number with units) — Flex gap on `.brx-submenu-toggle`.

- **Icon position** (select) — Uses flex direction (`row-reverse` when set to place icon on the **left**).

- **Icon size** (number with units) — `font-size` on the button.

- **Icon color** (color).

- **Icon transform**, **Icon transform (Open)** (transform) — Default vs `aria-expanded="true"`.

- **Icon transition** (text) — CSS `transition` on the button.

## Caret

Optional triangle on the dropdown root (adds class `caret` when **Size** is set):

- **Size** (number with units) — `border-width` on `> .brx-dropdown-content::before`.

- **Color** (color) — `border-bottom-color` (when size ≠ 0).

- **Transform** (transform).

- **Position** (dimensions).

## Content

- **Position: Static** (checkbox) — Keeps the panel in document flow (e.g. inside [Offcanvas](/builder/elements/general/offcanvas/)). Static dropdowns **always toggle on click**, not hover.

- **Toggle on** (select) — `click`, `hover`, or `click or hover`. Hidden when **Static** is enabled (click only).

- **Min. width** (number with units) — On `.brx-dropdown-content`.

- **Transition** (text), **Transform**, **Transform (Open)** — Panel motion (`&.open > .brx-dropdown-content` for open state).

- **Background** (background), **Border**, **Box shadow**, **Typography** — Panel chrome on `.brx-dropdown-content`.

### Item

Row styling for direct links and submenu toggles inside the panel:

- **Justify content** (justify-content).

- **Padding** (spacing).

- **Background** (color), **Border** (border), **Typography**, **Transition** (text).

### Active

States matching `aria-current="page"` / `.aria-current`:

- **Background**, **Border**, **Typography**.

## Mega menu

- **Enable** (checkbox) — Full-width style mega panel (`brx-has-megamenu`); “covers entire available width” by default.

- **CSS selector (Horizontal)** (text) — Optional: align width/horizontal position to another node.

- **CSS selector (Vertical)** (text) — Optional: vertical alignment reference.

## Multilevel

- **Enable** (checkbox) — Shows one submenu level at a time; toggles on click; inner dropdowns inherit multilevel behavior.

- **Back: Text** (text) — Back control label (default “Back”).

- **Back: Typography**, **Back: Background** — `.brx-multilevel-back` styling.

:::tip[Developer reference]
See the [Dropdown Schema](/developer/schema/elements/dropdown/) for the full JSON schema of this element's settings and controls.
:::
