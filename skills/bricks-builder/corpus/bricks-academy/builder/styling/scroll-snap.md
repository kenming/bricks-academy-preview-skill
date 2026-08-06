---
title: "Scroll Snap"
description: "Use CSS Scroll Snap in Bricks to create scroll-controlled sections, sliders, and other snapping layouts."
canonical: "https://academy.bricksbuilder.io/builder/styling/scroll-snap/"
markdownUrl: "https://academy.bricksbuilder.io/builder/styling/scroll-snap.md"
pageType: "article"
section: "builder"
category: "styling"
lastmod: "2026-08-04T12:13:33.000Z"
---
With the introduction of scroll snapping in Bricks 1.9.3, enhancing your web pages with sophisticated scrolling effects has never been easier.

In our latest video, we provide a step-by-step guide on using scroll snap in Bricks, including how to set it up on a page and fine-tune it for individual elements.

https://www.youtube.com/watch?v=LoKCda8uDNw

## Page-level scroll snap

Open the page settings and use the **Scroll snap** controls to set the page scroll snap **Type**. Bricks applies `scroll-snap-type` to `html` and, by default, applies snap alignment to `.brxe-section`.

You can change the **Snapping elements selector** if your snap items are not sections. The **Align**, **Margin**, **Padding**, and **Stop** controls let you fine-tune the snapping behavior.

## Element-level scroll snap

Layout elements also expose scroll snap controls under their layout settings. Use these when a specific element should become its own scroll snap container or when you need element-level snap alignment, margin, or stop behavior.

:::note
Scroll snap is disabled inside the builder preview. Check the page on the frontend to verify the actual snapping behavior.
:::

For an in-depth look at the CSS properties behind this feature, such as `scroll-snap-align`, `scroll-snap-type`, and more, please visit [https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll_snap](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll_snap)
