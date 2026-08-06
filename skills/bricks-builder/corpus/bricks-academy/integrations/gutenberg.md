---
title: "Gutenberg"
description: "Understand how Bricks integrates with Gutenberg, including what each editor is responsible for and where the workflows can overlap."
canonical: "https://academy.bricksbuilder.io/integrations/gutenberg/"
markdownUrl: "https://academy.bricksbuilder.io/integrations/gutenberg.md"
pageType: "article"
section: "integrations"
category: "gutenberg"
lastmod: "2026-08-04T12:13:33.000Z"
---
If you've created your pages with Gutenberg you can continue editing them with Bricks without having to start all over again. Bricks will convert your Gutenberg blocks into Bricks elements.

You can also save and convert your Bricks generated data to Gutenberg data to continue editing a page with Gutenberg.

This way you'll not suffer any lock-in effect when start using Bricks or if you should ever decide to move away from Bricks.

:::note
The block conversion works only with standard WordPress Gutenberg blocks, NOT custom-third party blocks
:::

## How to load Gutenberg data into Bricks

Bricks allows you to convert your existing Gutenberg data into Bricks data. So you can continue editing any page created with Gutenberg in Bricks.

This only works for pages without any existing Bricks data. To delete the Bricks data of any page, first enable **Enable "Delete Bricks data" button** under **Bricks > Settings > General > Miscellaneous**. Then click the "Delete Bricks data" button in the WordPress top menu when editing a page in WordPress.

To enable this functionality go to **Bricks > Settings > General > Block editor** and make sure **Load Block editor data into Bricks** is selected.

## How to save Bricks data for Gutenberg

By default, your WordPress-generated data won’t change when editing with Bricks. If you want to save your Bricks generated data as Block editor data as well go to **Bricks > Settings > General > Block editor** and select **Save Bricks data as Block editor data**.

From now on whenever you edit and save in Bricks, your content will be saved as WordPress content, too. So your WordPress and Bricks data are in sync.

## Render content with Bricks or WordPress {#render-with-wordpress}

You decide which pages you want to create with Gutenberg, the Classic Editor, or Bricks. The post status next to the page title tells you which content is used for rendering on the frontend:

![](imgs/wp-admin-pages-post-status-1024x576-2ad3aab461.png)

To change the data being used to render a page edit the page in WordPress and hover over the **Render with WordPress/Bricks** button in the top menu, and select the source you want to use:



![](imgs/wp-admin-edit-page-render-with-wordpress-bricks-1024x576-63459736af.png)

<figcaption>

Render with Bricks / Render with WordPress

</figcaption>
