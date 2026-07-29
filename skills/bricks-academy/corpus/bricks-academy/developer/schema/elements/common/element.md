---
title: "Element Schema"
description: "Canonical reference for a Bricks element: the envelope structure, settings layers, meta-settings, and selectors."
canonical: "https://academy.bricksbuilder.io/developer/schema/elements/common/element/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/elements/common/element.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-07-29T10:15:35.000Z"
---
import SchemaJson from '../../../../../../components/SchemaJson.astro'

Every element in Bricks uses the same envelope structure, regardless of type. Element-specific controls are documented on each element's schema page; content areas (the flat arrays that hold elements) are documented in the [content area schema](/developer/schema/general/content-area/).

<SchemaJson path="elements/common/element.json" />

## Element envelope

Every element object has these top-level fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Unique 6-character alphanumeric identifier (e.g. `"dlceeu"`) |
| `name` | string | Yes | Element type, matches the element schema filename (e.g. `"button"`, `"heading"`) |
| `parent` | string \| 0 | Yes | Parent element ID, or `0` for root-level elements |
| `children` | string[] | Yes | Ordered array of child element IDs |
| `settings` | object | Yes | All control values for this element (element-specific + inherited + meta) |
| `selectors` | array | No | Custom CSS selectors with scoped settings (since Bricks 2.0) |
| `label` | string | No | Custom label assigned by the user in the builder |
| `themeStyles` | array | No | Theme style overrides applied to this element |

## Settings: three layers

The `settings` object combines three layers of keys:

1. **Element-specific controls:** unique to each element type (e.g. `text`, `tag`, `link` on a button). Documented in each element's schema.
2. **Inherited CSS controls:** shared by all elements, prefixed with `_` (e.g. `_typography`, `_margin`, `_padding`, `_background`). These support responsive and pseudo-class variants via colon suffixes (e.g. `_typography:tablet_portrait:hover`). Documented in each element's schema under the `_`-prefixed keys.
3. **Meta-settings:** shared by all elements but not listed in individual element schemas. These control visibility, behavior, and class assignment. Documented below.

## Meta-settings

These keys can appear in any element's `settings` object. They are not included in per-element schemas to avoid duplication across 130+ elements.

### `_cssGlobalClasses`

Array of global class IDs applied to this element. Each ID references a global class defined in the [global classes](/developer/schema/global/global-classes/) data.

```json
"_cssGlobalClasses": ["mmdqed", "xkatss"]
```

### `_conditions`

Element display conditions that control whether this element renders. Structured as an array of arrays: outer array is OR groups, inner arrays are AND items.

```json
"_conditions": [
  [
    { "id": "abc123", "key": "user_logged_in", "compare": "==", "value": true }
  ]
]
```

See the [Element Conditions](./conditions/) page for the full `conditionItem` schema, all 32 condition keys, and available comparison operators.

### `_interactions`

Array of interaction rules that trigger actions in response to events (click, scroll, hover, etc.). Each interaction specifies a trigger, action, and target.

```json
"_interactions": [
  {
    "id": "abc123",
    "trigger": "click",
    "action": "startAnimation",
    "target": "self"
  }
]
```

See the [Element Interactions](./interactions/) page for the full `interactionItem` schema, all triggers, actions, and sub-conditions.

### `_hideElementBuilder`

Boolean (default `false`). When `true`, the element is hidden on the builder canvas but still renders on the frontend.

### `_hideElementFrontend`

Boolean (default `false`). When `true`, the element is hidden on the frontend but remains visible in the builder.

### `_attributes`

Array of custom HTML attributes added to the element's root DOM node.

```json
"_attributes": [
  { "id": "abc123", "name": "data-aos", "value": "fade-up" }
]
```

## Selectors

The `selectors` array allows scoping control settings to arbitrary CSS selectors on an element (since Bricks 2.0). Each selector entry has its own `settings` object that follows the same structure as the element's main settings.

```json
"selectors": [
  {
    "id": "nopzhs",
    "selector": "#brxe-opxcoa h3",
    "settings": {
      "_typography": { "color": { "raw": "blue" } }
    },
    "label": "Heading within container"
  }
]
```

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Unique identifier for this selector entry |
| `selector` | string | Yes | CSS selector string (e.g. `".my-class"`, `"&::before"`, `"& > span"`) |
| `settings` | object | Yes | Control settings scoped to this selector |
| `label` | string | No | Display label in the builder UI |

### Selector item schema

```json
{
  "type": "object",
  "description": "Custom CSS selector on an element or global class (since Bricks 2.0). Allows scoping control settings to arbitrary CSS selectors.",
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier for this selector entry"
    },
    "selector": {
      "type": "string",
      "description": "CSS selector string (e.g. \".my-class\", \"&::before\", \"& > span\")"
    },
    "settings": {
      "description": "Control settings scoped to this selector (same shape as element settings)",
      "_note": "Dynamic map of all settings for this element or class. Keys are element-specific control names (e.g. `text`, `style`) or inherited CSS setting keys, optionally suffixed with a breakpoint and/or pseudo-class using colon syntax (e.g. `_typography:tablet_portrait:hover`). See the individual element schemas for available control keys."
    },
    "label": {
      "type": "string",
      "description": "Optional display label for this selector in the builder UI"
    }
  },
  "required": [
    "id",
    "selector",
    "settings"
  ],
  "additionalProperties": false
}
```

## How this relates to individual element schemas

Each element schema (e.g. [button](/developer/schema/elements/button/), [heading](/developer/schema/elements/heading/)) documents the element-specific and inherited CSS controls that go into the `settings` object. The envelope fields (`id`, `name`, `parent`, `children`, `selectors`, `label`, `themeStyles`) and meta-settings (`_cssGlobalClasses`, `_conditions`, `_interactions`, etc.) documented on this page apply identically to every element type.

To construct a complete element, combine:
1. The envelope fields from this page
2. Element-specific controls from the individual element schema
3. Inherited CSS controls (the `_`-prefixed keys in the element schema)
4. Any applicable meta-settings from this page
