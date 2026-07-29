---
title: "Global Classes Schema"
description: "Reference for the Bricks Global Classes schema, including the exported structure and top-level properties used in global settings."
canonical: "https://academy.bricksbuilder.io/developer/schema/global/global-classes/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/global/global-classes.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-07-29T10:15:35.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

<SchemaJson path="global/global-classes.json" />

## Item properties

| Property | Type | Description |
|---|---|---|
| `id` | string | — |
| `name` | string | — |
| `category` | string | — |
| `settings` | dynamic | Dynamic map of all settings for this element or class. Keys are element-specific control names (e.g. `text`, `style`) or inherited CSS setting keys, optionally suffixed with a breakpoint and/or pseudo-class using colon syntax (e.g. `_typography:tablet_portrait:hover`). See the individual element schemas for available control keys. |
| `selectors` | array | Custom CSS selectors with scoped settings (since Bricks 2.0) |
| `modified` | integer \| string | — |
| `user_id` | integer \| string | — |
| `deletedAt` | integer \| string | — |
