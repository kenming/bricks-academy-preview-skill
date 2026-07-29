---
title: "Contextual Spacing"
description: "Apply contextual spacing in Bricks to create more consistent rhythm between elements without manually tweaking every margin."
canonical: "https://academy.bricksbuilder.io/builder/styling/contextual-spacing/"
markdownUrl: "https://academy.bricksbuilder.io/builder/styling/contextual-spacing.md"
pageType: "article"
section: "builder"
category: "styling"
lastmod: "2026-07-29T10:15:35.000Z"
---
Bricks 2.0 introduces **Contextual spacing** to give you full control over vertical spacing (margin) between elements like headings, paragraphs, and lists within embedded content.

Contextual spacing automatically applies to elements within:

- Rich text element
- Post content element (source: WordPress)
- WooCommerce embedded content (excluding Checkout)

Out-of-the-box, Bricks tries to apply various top margins (`margin-block-start`) to elements like headings and paragraphs depending on their context.

If you want to override these defaults, you had to manually remove browser spacing, undo Bricks' built-in styles, and then define your own margins.

Contextual spacing simplifies this process. You can now reset those margins and visually define custom spacing rules under **[Theme Styles](/builder/styling/theme-styles/) →** Contextual Spacing.

Whether you are styling embedded content, working with dynamic layouts, or creating utility-based wrappers, this feature gives you consistent and flexible control over spacing.

## How to use contextual spacing

![](imgs/bricks-2.0-contextual-spacing-1-51c9882828.png)

You can enable Contextual spacing inside the builder under **Style Manager → Theme Styles → Contextual Spacing**.

**Remove default margins**: Lets you select the HTML tags from which you want to remove the default margins (i.e. Heading, Paragraph, Lists, etc.). This creates a clean starting point for spacing that fits your layout needs, without interference from inherited or default styles.

**Remove default padding**: Lets you remove default padding from selected tags such as `ul`, `ol`, `blockquote`, and `button`.

:::note
The remove-default selectors are output exactly as selected. Broad tag selections such as `p`, `ul`, or `h1,h2,h3,h4,h5,h6` reset every matching element in the generated Theme Style CSS, not only the embedded-content selectors used by the spacing rules. Use more specific custom selectors if the reset should be narrower.
:::

:::note
**Contextual spacing:** Only applies margins when an element is preceded by another. This prevents extra spacing at the very top while maintaining consistent spacing between elements.
:::

## Settings overview

| Setting | Description |
| --- | --- |
| **Remove default margins** | Resets margins on the selected or manually entered HTML tags. |
| **Remove default padding** | Resets padding on the selected or manually entered HTML tags. |
| **Heading** | Applies top margin to `h1` through `h6` elements when they are preceded by another element. |
| **Paragraph** | Applies top margin to `p` elements when they are preceded by another element. |
| **Fallback spacing** | Applied to any element that does not match a heading, paragraph, or target elements, or when those targets have no spacing value defined. |
| **Additional target elements** | Define spacing rules for elements like `ul`, `blockquote`, or any custom selector. Lets you block margin (top, bottom) and inline padding (left, right). |
| **Apply spacing inside** | Extend contextual spacing to other parts of your layout by targeting wrapper selectors such as `.contextual-spacing`. |

## Additional target elements

Use the **Additional target elements** repeater to extend Contextual spacing to more than headings and paragraphs.

You can choose from predefined elements:

- Unordered list (ul)
- Ordered list (ol)
- List item (li)
- Figure (figure)
- Blockquote (blockquote)

Or enter your own custom selectors like `.my-class`, `code`, or `div`.

For each, you can set:

- Top and bottom margin (`margin-block`)
- Start and end padding (`padding-inline`)

This gives you spacing consistency across all types of content.

## Apply to more content areas

:::note
By default, Contextual spacing only targets Rich Text, Post Content, and WooCommerce content. But you can easily extend it by defining **Apply spacing inside** selectors to apply Contextual spacing to any wrapper of your choice, such as `.contextual-spacing, .brxe-shortcode`.
:::

Add these utility classes to wrappers (i.e. Container, Div, Block elements) that hold a mix of content elements, and Bricks will apply your Contextual spacing settings to them.

### Why not apply spacing to all headings and paragraphs by default?

In most Bricks layouts, especially when using **Heading** and **Basic text** elements in combination with other elements, spacing is typically handled using the **gap** property between containers.

Because of that, applying a single spacing rule to all headings and paragraphs wouldn't make sense in every context.

Contextual spacing gives you the flexibility to apply spacing only where it's needed, using selectors and utility classes.

## Example use case 1: Embedded post content

You’re building a single post template using a **Post Content** element (source: WordPress).
Before enabling Contextual spacing, the post displays the default spacing added by Bricks.

When **Remove default margins** is enabled, Bricks removes both its own default spacing and the browser's default margins. You can then define your own spacing values using the Contextual spacing controls.

When you enable **Remove default margins**, then set spacing values. For example:

- **Heading**: `2rem`
- **Paragraph**: `1.25rem`
- **Fallback**: `1rem`

Bricks then applies spacing only between elements where needed. The first element inside the post has no margin above it, but elements that follow each other are spaced consistently.

![](imgs/bricks-contextual-spacing-enable-scaled-6437fe4f17.png)

![](imgs/bricks-contextual-spacing-example-values-scaled-ed24ae0995.png)

**Result:** Clean layout, no spacing at the top, full control over vertical rhythm.

![](imgs/bricks-contextual-spacing-use-case-1-1-1024x791-da431aac33.png)

![](imgs/bricks-contextual-spacing-use-case-1-2-1024x1017-4db15207d5.png)

![](imgs/bricks-contextual-spacing-use-case-1-3-1024x1012-bb1cb747d5.png)

![](imgs/bricks-contextual-spacing-use-case-1-4-926x1024-5ffc904c42.png)

## Example use case 2: Mixed content layout

You've created a custom template that includes a container with the following elements:

- A **Heading** element
- A **Basic text** element (with a `p` tag)
- An **Image** element (with a `figure` tag)
- A **Post Content** element (source: WordPress)

Because these use different systems for spacing, the result may feel inconsistent.

To unify the layout:

1. Under Theme Styles > Contextual Spacing > Enable **Remove default margins**
2. Set spacing values. For example:
  - Heading: `2rem`
  - Paragraph: `1.25rem`
  - Fallback: `1rem`
3. Add a global class like `.contextual-spacing` to the container
4. Enter `.contextual-spacing` under **Apply spacing inside**

![](imgs/bricks-contextual-spacing-utility-class-scaled-1932d6a7a1.png)

![](imgs/bricks-contextual-spacing-apply-to-utility-class-scaled-7f76e3c026.png)

**Result**: All elements within that wrapper now follow your contextual spacing rules.
