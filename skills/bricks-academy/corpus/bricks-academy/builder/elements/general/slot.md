---
title: "Slot"
description: "The Slot element is used inside Bricks components as a placeholder: when you place a component instance on the canvas, the content you add into that instance is."
canonical: "https://academy.bricksbuilder.io/builder/elements/general/slot/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/general/slot.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-07-29T10:15:35.000Z"
---
The **Slot** element is used **inside Bricks components** as a **placeholder**: when you place a component instance on the canvas, the content you add into that instance is rendered in place of each Slot.

On the front end, the Slot outputs **nothing by itself**—it only renders the child elements assigned to that slot on the **component instance** (`slotChildren` for that Slot id). If there is no matching instance or no children, the Slot outputs nothing.

The element shows a single **info** control explaining that it acts as a placeholder for instance content.

:::tip[Nestable]
Slot uses the nestable builder UI (`bricks-nestable`) but does not ship with default nested children; structure is defined in your **component** template.
:::

:::tip[Developer reference]
See the [Slot Schema](/developer/schema/elements/slot/) for the full JSON schema of this element's settings and controls.
:::
