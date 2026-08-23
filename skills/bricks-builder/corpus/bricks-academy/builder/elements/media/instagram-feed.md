---
title: "Instagram feed"
description: "The Instagram feed element loads media from the Instagram Graph API using an access token saved in Bricks → Settings → API keys (instagramAccessToken). Without."
canonical: "https://academy.bricksbuilder.io/builder/elements/media/instagram-feed/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/media/instagram-feed.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-20T13:12:40.000Z"
---
The **Instagram feed** element loads media from the **Instagram Graph API** using an **access token** saved in **Bricks → Settings → API keys** (`instagramAccessToken`). Without a token, the element shows a placeholder asking you to connect the account.

Responses are **cached** in a transient to limit API calls; cache length is configurable.

## Requirements

Add a valid **Instagram access token** under **Bricks → Settings → API keys**. The element’s info message links there when the global token is missing.

## Layout

- **Columns** (number) — CSS grid columns for the list (`ul`). Placeholder: `3`. Valid range on the front end: `1–6`.

- **Posts** (number) — How many posts to request (min `1`, max `100`). Placeholder: `9`.

## Image

- **Object fit** (select) — Applied to `img`.

- **Aspect ratio** (text).

- **Height**, **Width** (number with units).

- **Gap** (number with units) — Gap on the `ul` grid.

- **Border** (border) — Image border.

- **Link** (checkbox) — Wrap each image in a link to the Instagram permalink.

## Carousel

Optional styling for the **carousel** badge on **CAROUSEL_ALBUM** items:

- **Icon** (icon), **Icon color** (color), **Icon size** (number with units), **Icon position** (dimensions).

## Video

Optional styling for the **video** play overlay on **VIDEO** items:

- **Icon** (icon), **Icon color** (color), **Icon size** (number with units), **Icon position** (dimensions).

## Caption

- **Enable** (checkbox) — Show the post caption below the image.

When enabled: **Background color**, **Border**, **Typography** on `.caption`.

## Follow

Optional “Follow us” row linking to `instagram.com/{username}`:

- **Text** (text) — Default mentions `@yourhandle`; replace with your copy or dynamic data.

- **Position** (select) — `top` or `bottom`.

- **Icon** (icon) — Default Instagram logo.

- **Typography** — `.follow` text.

## Cache

- **Duration** (select) — `30 minutes`, `1 hour`, `1 day`, or `1 week` (stored as seconds: `1800`, `3600`, `86400`, `604800`). Default placeholder: 1 hour.

:::tip[Developer reference]
See the [Instagram feed Schema](/developer/schema/elements/instagram-feed/) for the full JSON schema of this element's settings and controls.
:::
