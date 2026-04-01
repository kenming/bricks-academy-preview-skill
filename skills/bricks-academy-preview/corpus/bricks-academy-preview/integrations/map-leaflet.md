Starting with **Bricks 2.1**, you can use the new **Map (Leaflet)** element to display fully interactive maps powered by [Leaflet.js](https://leafletjs.com/).

This element allows you to combine multiple map layers, add custom markers, and fine-tune map behaviour directly inside Bricks.

## Overview {#overview}

The Map (Leaflet) element is divided into three main groups of settings:

1. **Layers** – define map sources (OpenStreetMap, OpenTopoMap, etc.)
2. **Markers** – add custom points with icons and popups
3. **Map** – configure global map settings (center, zoom, etc.)

Let’s explore each group in detail.

## Layers {#layers}

Layers control which map tiles are displayed.

Each layer is defined through a **Repeater**. Meaning you can add multiple layers (map styles) and let visitors switch between them.

For each layer, you'll configure:

- **Name** – label shown in the layer switcher (e.g. “Street Map”, “Topographic”).
- **URL** – the provider URL (e.g. `https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png`). You can view list of *some* providers [here](https://leaflet-extras.github.io/leaflet-providers/preview/index.html).
  - The placeholders `{s}`, `{z}`, `{x}`, `{y}` must be present because Leaflet replaces them dynamically:
    - `{s}` → subdomain (a, b, c, …)
    - `{z}` → zoom level
    - `{x}` / `{y}` → tile coordinates
- **Min/Max Zoom** – zoom levels the layer supports.
- **Error Tile URL** – fallback image if tiles fail to load.
- **Attribution** – copyright or usage text (required by most providers).

👉 Example:

- **Street Map** → OpenStreetMap tiles
- **Topo Map** → OpenTopoMap tiles
- **Satellite** → Esri or other provider

Your users can then toggle between these layers on the frontend.

## Markers {#markers}

Markers let you highlight specific points of interest on your map.

You can set:

- **Default Marker Icon** – used if no custom icon is defined.
- **Marker Repeater** – add multiple markers, each with:
  - **Coordinates (Lat, Lng)**
  - **Label** (for identification)
  - **Custom Icon** (optional, overrides default icon)
  - **Popup Text** (text that shows when the marker is clicked)

## Map

The **Map** group controls the basic setup of your map. The most important settings are the **map height**, which is set to 300 px by default but can be adjusted to match your layout, along with the **map center** (latitude and longitude) and the **initial zoom level**. These define how the map looks and where it is focused when first loaded.

Beyond that, you’ll also find controls grouped around **zoom behaviour**, **map interactions** (like dragging and clicking), and **display options** (such as attribution and resizing). All of these settings are based on Leaflet.js, and you can find full descriptions in the [Leaflet documentation](https://leafletjs.com/reference.html#map).
