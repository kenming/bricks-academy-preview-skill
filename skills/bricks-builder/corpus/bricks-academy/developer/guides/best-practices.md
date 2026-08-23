---
title: "Best Practices"
description: "Follow Bricks development best practices for permalinks, image handling, child-theme usage, and safer long-term customization."
canonical: "https://academy.bricksbuilder.io/developer/guides/best-practices/"
markdownUrl: "https://academy.bricksbuilder.io/developer/guides/best-practices.md"
pageType: "article"
section: "developer"
category: "guides"
lastmod: "2026-08-20T13:12:40.000Z"
---
Please keep the points below in mind when working with Bricks:

| **Permalink Settings** | We recommend **Post name** permalinks for cleaner URLs. Go to **Settings > Permalinks**, select **Post name**, and click **Save Changes**. Bricks builds builder URLs from the page permalink, so other WordPress permalink structures can work as long as WordPress resolves them correctly. |
| --- | --- |
| **Min. Image Dimensions** | Upload images with a minimum width of 600 pixels. Ideally 1600 pixels in width or more.<br /><br />If you already have images in your media library and start working with Bricks make sure to [Regenerate Thumbnails](https://wordpress.org/plugins/regenerate-thumbnails/) so all Bricks-specific image sizes are generated properly. |
| **Never Edit Theme Code Directly** | **Do not edit any of the Bricks theme core files directly!**<br /><br />As all your changes will be lost/overwritten when updating the theme. Use the [Bricks child theme](/developer/guides/child-theme/) or a code snippet plugin to extend Bricks with your custom code. |
