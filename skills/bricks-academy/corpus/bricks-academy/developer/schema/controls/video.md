---
title: "Video Control Schema"
description: "Value schema for video control type"
canonical: "https://academy.bricksbuilder.io/developer/schema/controls/video/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/controls/video.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-07-29T10:15:35.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

<SchemaJson path="controls/video.json" />

## Properties

| Property | Type | Description |
|---|---|---|
| `source` | string | One of: `media`, `youtube`, `vimeo`, `url` |
| `id` | string \| integer | — |
| `url` | string | — |
| `youtubeId` | string | — |
| `vimeoId` | string | — |
| `autoplay` | boolean | — |
| `loop` | boolean | — |
| `muted` | boolean | — |
| `controls` | boolean | — |
