---
title: "Element Interactions Schema"
description: "Full schema for element interactions: triggers, actions, targets, animation settings, and sub-conditions."
canonical: "https://academy.bricksbuilder.io/developer/schema/elements/common/interactions/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/elements/common/interactions.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-08-04T12:13:33.000Z"
---
import SchemaJson from '../../../../../../components/SchemaJson.astro'

Element interactions define event-driven behavior: when a trigger fires, an action is executed on a target. They are stored in the `_interactions` key inside any element's `settings` object.

## Data structure

Interactions are a flat array of interaction items. Each item specifies a trigger event, the action to perform, and a target element or selector.

<SchemaJson path="elements/common/interactions.json" />

## `interactionItem` core properties

| Property | Type | Description |
|---|---|---|
| `id` | string \| integer | Unique identifier for this interaction |
| `trigger` | string | Event that fires this interaction (see triggers below) |
| `action` | string | Action to perform (see actions below) |
| `target` | string | Target reference (`"self"`, element ID, or selector context) |
| `targetSelector` | string | CSS selector for the target element |
| `delay` | string | Delay before executing the action (ms) |
| `runOnce` | boolean | If true, the interaction fires only once |

## Additional properties

These properties apply depending on the chosen action:

| Property | Type | Used with |
|---|---|---|
| `animationType` | string | `startAnimation` (animation type) |
| `animationId` | string | `startAnimation` (predefined animation ID) |
| `animationDelay` | string | `startAnimation` (animation delay) |
| `animationDuration` | string | `startAnimation` (animation duration) |
| `jsFunction` | string | `javascript` (function name to call) |
| `jsFunctionArgs` | array | `javascript` (arguments array: `[{ jsFunctionArg: "value" }]`) |
| `scrollToDelay` | string | `scrollTo` (delay before scrolling) |
| `scrollToOffset` | string | `scrollTo` (scroll offset in pixels) |
| `scrollOffset` | string | `scroll` trigger (scroll position threshold) |
| `rootMargin` | string | `enterView`/`leaveView` (IntersectionObserver root margin) |
| `templateId` | string | Template ID reference |
| `formId` | string | Form element ID |
| `ajaxQueryId` | string | AJAX query element ID |
| `offCanvasSelector` | string | `toggleOffCanvas` (offcanvas CSS selector) |
| `toggleOffCanvasInfo` | string | `toggleOffCanvas` (info field) |
| `filterElementId` | string | Query filter element ID |
| `infoBoxId` | string | Info box element ID |
| `loadMoreQuery` | string | `loadMore` (query element ID) |
| `targetFormSelector` | string | `clearForm` (form CSS selector) |
| `actionAttributeKey` | string | `setAttribute`/`removeAttribute`/`toggleAttribute` (attribute name) |
| `actionAttributeValue` | string | `setAttribute`/`toggleAttribute` (attribute value) |
| `disablePreventDefault` | boolean | Do not call `preventDefault()` on the trigger event |
| `storageType` | string | `storageAdd`/`storageRemove`/`storageCount` (storage type) |
| `popupContextId` | string | Popup context ID |
| `popupContextType` | string | Popup context type |
| `conditionsSep` | string | Visual separator for conditions UI |

### Example

```json
{
  "_interactions": [
    {
      "id": "abc123",
      "trigger": "click",
      "action": "startAnimation",
      "target": "self",
      "animationType": "fadeIn",
      "animationDuration": "500"
    },
    {
      "id": "def456",
      "trigger": "enterView",
      "action": "show",
      "target": "self",
      "rootMargin": "0px 0px -100px 0px",
      "runOnce": true
    }
  ]
}
```

## Triggers

**Element**
- `click`
- `mouseover`
- `focus`
- `blur`
- `mouseenter`
- `mouseleave`
- `enterView`
- `leaveView`
- `animationEnd`
- `ajaxStart`
- `ajaxEnd`
- `filterSubmitStart`
- `filterSubmitEnd`
- `formSubmit`
- `formSuccess`
- `formError`

**Browser / Window**
- `scroll`
- `contentLoaded`
- `mouseleaveWindow`

**Query filters**
- `filterOptionEmpty`
- `filterOptionNotEmpty`

**WooCommerce**
- `wooAddedToCart`
- `wooAddingToCart`
- `wooRemovedFromCart`
- `wooUpdateCart`
- `wooCouponApplied`
- `wooCouponRemoved`

Popup templates have two additional triggers (`showPopup`, `hidePopup`) available via the `templateInteractionItem` variant in template settings.

## Actions

| Action | Description |
|---|---|
| `show` | Show element |
| `hide` | Hide element |
| `click` | Click element |
| `setAttribute` | Set an HTML attribute |
| `removeAttribute` | Remove an HTML attribute |
| `toggleAttribute` | Toggle an HTML attribute |
| `toggleOffCanvas` | Toggle an offcanvas panel |
| `loadMore` | Load more items (query loop) |
| `startAnimation` | Start a CSS animation |
| `scrollTo` | Scroll to an element |
| `javascript` | Execute a custom JavaScript function |
| `openAddress` | Open a map address |
| `closeAddress` | Close a map address |
| `clearForm` | Clear a form |
| `storageAdd` | Add item to browser storage |
| `storageRemove` | Remove item from browser storage |
| `storageCount` | Count items in browser storage |

## Interaction sub-conditions

Each interaction can optionally include sub-conditions that must be met before the action fires. These are stored in the `interactionConditions` array, with `interactionConditionsRelation` controlling whether conditions are combined with AND or OR logic.

| Property | Type | Description |
|---|---|---|
| `interactionConditions` | array | Array of `interactionConditionItem` objects |
| `interactionConditionsRelation` | string | `"and"` or `"or"` (default: `"and"`) |

### `interactionConditionItem` properties

| Property | Type | Description |
|---|---|---|
| `conditionType` | string | Type of condition check |
| `storageCompare` | string | Comparison operator for storage value |
| `storageCompareValue` | any | Value to compare storage against |
| `storageKey` | any | Browser storage key to check |

### Example with sub-conditions

```json
{
  "id": "abc123",
  "trigger": "click",
  "action": "show",
  "target": "self",
  "interactionConditions": [
    {
      "conditionType": "storage",
      "storageKey": "user_preference",
      "storageCompare": "==",
      "storageCompareValue": "dark"
    }
  ],
  "interactionConditionsRelation": "and"
}
```
