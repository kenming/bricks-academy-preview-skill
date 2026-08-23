---
title: "Map (Leaflet)"
description: "Map (Leaflet) (map-leaflet) embeds an interactive map using Leaflet and tile layers (default: OpenStreetMap). Unlike the Google Map element, it does not use the."
canonical: "https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/general/map-leaflet.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-20T13:12:40.000Z"
---
**Map (Leaflet)** (`map-leaflet`) embeds an interactive map using **Leaflet** and **tile layers** (default: **OpenStreetMap**). Unlike the Google [Map](/builder/elements/general/map/) element, it does **not** use the Google Maps JavaScript API—use this when you want OSM-style tiles or custom tile URLs without Google.

The element is **not draggable** in the builder (`draggable = false`) to avoid conflicts with map interaction. It enqueues `bricks-leaflet` scripts and styles.

## Layers

**Layers** (repeater) — Each layer:

- **Name** (text) — e.g. `OpenStreetMap`.
- **URL** (text) — Tile URL template with `{z}`, `{x}`, `{y}` placeholders.
- **Min Zoom**, **Max Zoom** (number).
- **Error Tile URL** (text).
- **Attribution** (text).

Default repeater row uses OpenStreetMap’s standard tile URL.

## Markers

**Markers** (repeater):

- **Coordinates** (text) — `latitude, longitude` (comma-separated). Supports dynamic data.
- **Label** (text) — Builder-only helper to tell markers apart.
- **Icon** (image) — Per-marker image; **Height** / **Width** (px) when set.
- **Popup (Text)** (editor) — Popup content for that marker.

### Marker (Default)

Global defaults when a marker has no custom icon:

- **Icon** (image), **Icon: Height (px)**, **Icon: Width (px)**.

## Map

- **Height** (number with units) — Map container height. Default placeholder: `300px`. Triggers reload when changed.

- **Map center** (text) — `latitude, longitude`.

- **Zoom level (Initial)** (number).

- **Zoom level (Min)**, **Zoom level (Max)** (number).

- **Zoom: Snap**, **Zoom: Delta** (number).

- **Zoom: Double-click** (select) — Enabled, Enabled (Center), or Disabled.

- **Zoom: Scroll wheel** (select) — Same options.

- **Box Zoom** (checkbox).

- **Zoom Control** (checkbox).

- **Attribution Control** (checkbox).

- **Close popup on click** (checkbox).

- **Dragging** (checkbox).

- **Track resize** (checkbox) — See [Leaflet map options](https://leafletjs.com/reference.html#map).

:::tip[Developer reference]
See the [Map (Leaflet) Schema](/developer/schema/elements/map-leaflet/) for the full JSON schema of this element's settings and controls.
:::
