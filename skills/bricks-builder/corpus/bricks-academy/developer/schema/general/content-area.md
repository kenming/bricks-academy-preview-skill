---
title: "Content Area Schema"
description: "A Bricks content area is a flat array of elements stored in post meta. This page documents the array structure and storage."
canonical: "https://academy.bricksbuilder.io/developer/schema/general/content-area/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/general/content-area.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-08-04T12:13:33.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

A content area is a flat array of element objects. Bricks uses three independent content areas per page (header, content, and footer), each stored in its own post meta key. The array is flat (not nested): parent-child relationships are expressed via the `parent` and `children` fields on each element.

For the structure of each element in the array, see the [Element schema](../elements/common/element/).

<SchemaJson path="general/content-area.json" />

## Content areas

A Bricks page (or any post type using Bricks) stores its elements across three independent content areas:

| Content area | WordPress post meta key | Description |
|---|---|---|
| Header | `_bricks_page_header_2` | Header template elements |
| Content | `_bricks_page_content_2` | Main page/post content |
| Footer | `_bricks_page_footer_2` | Footer template elements |

All three use the exact same data structure: an array of elements as described in the [Element schema](../elements/common/element/).

## Storage

These are stored as serialized arrays in the `wp_postmeta` table.

| Data | Meta key | PHP constant |
|---|---|---|
| Header elements | `_bricks_page_header_2` | `BRICKS_DB_PAGE_HEADER` |
| Content elements | `_bricks_page_content_2` | `BRICKS_DB_PAGE_CONTENT` |
| Footer elements | `_bricks_page_footer_2` | `BRICKS_DB_PAGE_FOOTER` |

## Flat array structure

Elements reference each other by ID rather than nesting physically. A root-level element has `"parent": 0`; all others reference their parent's `id`. The `children` array on each element lists its direct children in order. This makes it easy to reorder, move, or flatten elements without restructuring a tree.

```json
[
  { "id": "aaa111", "name": "section", "parent": 0, "children": ["bbb222"], "settings": {} },
  { "id": "bbb222", "name": "heading", "parent": "aaa111", "children": [], "settings": { "text": "Hello" } }
]
```

The array may also contain component instances (identifiable by the presence of a `cid` field). See [Components](../global/components/) for details.
