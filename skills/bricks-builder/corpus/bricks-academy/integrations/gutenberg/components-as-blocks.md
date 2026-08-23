---
title: "Bricks components as blocks"
description: "Expose Bricks components as Gutenberg blocks so editors can insert styled, property-driven Bricks content directly inside the block editor."
canonical: "https://academy.bricksbuilder.io/integrations/gutenberg/components-as-blocks/"
markdownUrl: "https://academy.bricksbuilder.io/integrations/gutenberg/components-as-blocks.md"
pageType: "article"
section: "integrations"
category: "gutenberg"
lastmod: "2026-08-20T13:12:40.000Z"
---
https://youtu.be/tgpjMcZaLNc

Most sites built with Bricks follow a simple pattern: you create your pages and templates in Bricks, and write your posts or other content in the block editor (Gutenberg).

That works well for standard content, but as soon as you need something more custom inside the block editor, like a styled testimonial or a reusable promo block, you quickly run out of options.

We are introducing a new experimental feature called **components as blocks** to bridge this gap. It lets you design blocks in Bricks and make them available directly inside the block editor.

You get the same builder features you already use for pages and templates, while deciding exactly what editors can override through component properties.

This makes it possible to:

- Build custom, styled blocks entirely in Bricks
- Keep design consistent across your site by updating the component once in Bricks
- Give editors freedom to customize content inside the block editor while staying within your design system

## Enable components as blocks

This new feature is currently experimental and disabled by default. You can enable it from the WordPress dashboard under `Bricks → Settings → General → Block editor → Bricks components in the block editor`.

Three options are available:

- **Disabled** (default)
- **Enable individual components manually**
  - Components must be enabled individually to appear in the block editor.
  - In the builder:
    - Open the **Components panel**, hover over a component, click **Use in block editor**, then confirm.
    - Or edit a component and toggle **Use in block editor → Enabled** from the component settings header.
  - A filter in the Components panel lets you view only components enabled for the block editor.
- **Enable all components automatically**
  - All Bricks components are instantly available in the block editor.

When a component is enabled for block editor use, additional block-specific settings appear in the component settings header under "Use in block editor":

- **Block category**: Choose which block category the component should appear under inside the block editor.
- **Block icon**: Select the icon shown in the block picker.
- **Block preview image**: Set an optional preview image that appears in the block inserter.

## Insert a component in the block editor

1. Open or create a post/page in the block editor.
2. Click **Add block (+)** and search for your component by name.
3. Select the component. It renders directly inside the editor.

The component behaves like any other block. You can add text above or below, reorder it, or combine it with other block editor blocks.

### Wide and full-width blocks

The block editor's **Wide width** and **Full width** options apply to the outer WordPress block wrapper. The elements inside the component still use their Bricks layout settings.

A Bricks Container has a default maximum width of 1100px. A component with a Container at its root, or a Container nested inside a full-width root element, can therefore remain constrained even when the Gutenberg block is set to **Full width**.

For a full-width component block, use a Section, Block, or Div with 100% width as the outer element. Set the width or maximum width of any inner Container intentionally, then select the required alignment for the block in Gutenberg.

If the editor preview still differs from the frontend, check both the selected Gutenberg alignment and every Bricks layout element that can set a width or maximum width.

## Customize component properties

When you select a Bricks component block in the block editor, its editable properties appear in the **Block settings sidebar** in the same way as editing an instance in Bricks.

All property types are supported:

- Text
- Rich text
- Icon
- Select
- Toggle
- Global classes
- Image
- Image gallery
- Link
- Query loop *(Query editor (PHP), External APIs, and Query manager are not supported at this time)*

Each block instance can have unique property values, while the component design remains consistent.

## Centralized design updates

All block instances remain linked to the main component in Bricks. Any design change you make in Bricks (such as adjusting layout, typography, or spacing) applies site-wide to every instance, including those inside the block editor.

## Use cases

- **Reusable design elements**: Insert testimonials, event cards, promo blocks, or signup forms into posts.
- **Design consistency**: Global updates in Bricks apply throughout your entire site.
- **Content flexibility**: Editors can update text, images, and toggles per instance without leaving the block editor.
- **Workflow separation**: Designers build components in Bricks, editors use them in the block editor.

As this feature is experimental, we would love your feedback on components as blocks specifically, as well as ideas for how Bricks could integrate even smoother with the block editor to support your workflow. Share your thoughts in the [Bricks forum](https://forum.bricksbuilder.io/) or get in touch with us directly via email.
