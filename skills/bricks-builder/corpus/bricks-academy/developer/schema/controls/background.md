---
title: "Background Control Schema"
description: "Value schema for background control type"
canonical: "https://academy.bricksbuilder.io/developer/schema/controls/background/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/controls/background.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-08-20T13:12:40.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

<SchemaJson path="controls/background.json" />

## Properties

| Property | Type | Description |
|---|---|---|
| `color` | any | Color value in various formats |
| `image` | object | Image settings |
| `video` | object | Video settings |
| `size` | string | — |
| `position` | string | — |
| `repeat` | string | One of: `repeat`, `repeat-x`, `repeat-y`, `no-repeat` |
| `attachment` | string | One of: `scroll`, `fixed`, `local` |
