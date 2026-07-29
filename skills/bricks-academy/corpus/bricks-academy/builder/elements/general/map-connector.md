---
title: "Map Connector"
description: "The Map Connector works with the Google Map element when Sync with query is enabled. Place one Map Connector inside each item of the query loop that should."
canonical: "https://academy.bricksbuilder.io/builder/elements/general/map-connector/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/general/map-connector.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-07-29T10:15:35.000Z"
---
The **Map Connector** works with the Google [Map](/builder/elements/general/map/) element when **Sync with query** is enabled. Place **one Map Connector inside each item** of the query loop that should produce a marker.

It renders an invisible **`<template>`** node that stores latitude, longitude, and/or address plus optional **Info Box** popup template data and **per-item marker overrides**. The Map reads these nodes to build markers when the query updates (pagination, filters, load more, etc.).

See [Map → Sync with query](/builder/elements/general/map/#sync-with-query) for the full workflow.

## Settings

- **Latitude** (text) — Use dynamic data from the looped post (placeholder shows Berlin-area example).

- **Longitude** (text).

- **Address** (text) — Alternative to coordinates; may geocode via Google when coordinates are not set.

An **error** info appears when all three are empty—Bricks expects at least one source of location via dynamic tags.

### Info Box (Popup)

- **Info Box: Template (Popup)** (select) — Popup template with **Template Settings → Popup → Info Box (Map)** enabled.

- **Info** — Reminds you to enable the Info Box option on the popup template.

### Markers

An **info** control notes that **Marker: Type** (text vs image) is configured on the **Map** element, while fields here **override** that map’s defaults for **this** loop item.

On the connector, Bricks only exposes marker fields that are **not** flagged `mainOnly` in the shared map-marker control set—so you set **per-loop values**, not the global marker typography or image dimensions (those stay on the **Map** element):

- **Label** (text) — Screen reader label (`aria-label`) for the marker.

- **Marker: Text** — **Text** field for the default text marker.

- **Marker: Text (Active)** — **Text** field for the active text marker.

- **Marker: Image** — **Icon** (image) for the default image marker.

- **Marker: Image (Active)** — **Icon** (image) for the active image marker.

:::tip[Developer reference]
See the [Map Connector Schema](/developer/schema/elements/map-connector/) for the full JSON schema of this element's settings and controls.
:::
