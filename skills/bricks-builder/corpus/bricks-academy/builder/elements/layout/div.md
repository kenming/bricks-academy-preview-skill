---
title: "Div"
description: "The Div element is one of the four layout elements in Bricks (1.5+)."
canonical: "https://academy.bricksbuilder.io/builder/elements/layout/div/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/layout/div.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-04T12:13:33.000Z"
---
The Div element is one of the four [layout elements](/builder/styling/layout/) in Bricks (1.5+).

Introduced together with the Section & Block element, it allows you to create flexible layouts in record time. The Div element in Bricks is a plain, unstyled div. It's the most generic element to group and lay out your content.

While you use the **Container** to "contain" other elements inside a preset width of 1100px, and the **Block** element with a 100% width, the **Div** element has no presets at all.

This makes it perfect to use inside other layout elements as it grows & shrinks according to its content, or to build Div-only class-based layouts. Use the Div element for grouping content, creating custom layouts, or when you need complete control over styling without any predefined properties.

**Tip:** The Div element's HTML tag setting allows you to transform it into any semantic HTML element (article, nav, ul, li, a (link), etc.) while keeping all the powerful layout and styling controls. This flexibility makes it a versatile building block that can adapt to different content structures and semantic requirements.

## Settings

- **Grid column** (text) - CSS grid column span when parent uses grid layout. Controls `grid-column` property.

- **Grid row** (text) - CSS grid row span when parent uses grid layout. Controls `grid-row` property.

- **Query loop** - Enable query loop functionality for dynamic content. Available for Container, Block, Div, and Section elements.

- **Link** (link) - Link settings when using anchor tag. Required when HTML tag is set to 'a'.

- **HTML tag** (select) - HTML tag for the div element. Options: div, section, a [Link], article, nav, ol, ul, li, aside, address, figure, custom. Default: div.

- **Custom tag** (text) - Custom HTML tag when "custom" is selected. Without attributes. Required when HTML tag is 'custom'.

- **Display** (select) - CSS display property. Options: flex, grid, block, inline-block, inline, none. Default: block.

### Grid Layout (when Display is grid)

- **Gap** (number with units) - Gap between grid items. Controls `grid-gap` property.

- **Grid template columns** (text) - CSS grid template columns. Supports dynamic data and variables.

- **Grid template rows** (text) - CSS grid template rows. Supports dynamic data and variables.

- **Grid auto columns** (text) - Grid auto columns size. Supports dynamic data and variables.

- **Grid auto rows** (text) - Grid auto rows size. Supports dynamic data and variables.

- **Grid auto flow** (select) - Grid auto flow direction. Options: row, column, dense.

- **Justify items** (justify-content) - Grid justify items alignment.

- **Align items** (align-items) - Grid align items alignment.

- **Justify content** (justify-content) - Grid justify content alignment.

- **Align content** (align-items) - Grid align content alignment.

### Flex Layout (when Display is flex)

- **Flex wrap** (select) - Flexbox wrapping behavior. Options: No wrap, Wrap, Wrap reverse.

- **Direction** (direction) - Flexbox direction (row/column). Controls `flex-direction` property.

- **Align self** (align-items) - Align self for this flex item. Controls `align-self` property with `!important`.

- **Align main axis** (justify-content) - Justify content alignment. Controls `justify-content` property.

- **Align cross axis** (align-items) - Align items alignment. Controls `align-items` property.

- **Column gap** (number with units) - Gap between flex columns. Controls `column-gap` property.

- **Row gap** (number with units) - Gap between flex rows. Controls `row-gap` property.

- **Flex grow** (number) - Flex grow factor. Minimum: 0. Controls `flex-grow` property. Default placeholder: 0.

- **Flex shrink** (number) - Flex shrink factor. Minimum: 0. Controls `flex-shrink` property. Default placeholder: 1.

- **Flex basis** (text) - Flex basis value. Supports dynamic data and variables. Controls `flex-basis` property. Default placeholder: auto.

### Order

- **Order** (number) - Flexbox order. Minimum: -999. Controls `order` property. Default placeholder: 0. Available when display is not 'none'.

## Style

These controls can be accessed under the **Style** tab in the element settings.

### Masonry

- **Masonry layout** (checkbox) - Enable masonry layout for child elements.
- **Columns** (number) - Number of masonry columns. Default: 3. Controls `--columns` CSS property.
- **Spacing** (number with units) - Spacing between masonry items. Default: 10px. Controls `--gutter` CSS property.
- **Horizontal order** (checkbox) - Enable horizontal ordering in masonry layout.
- **Transition: Duration** (number with units) - Animation duration for masonry transitions. Default: 0.4s. Set to "0" to disable default animations.
- **Reveal animation** (select) - Animation type for masonry items. Options: Scale, Fade, Slide from left, Slide from right, Skew. Default: Scale. Only applies to new items added to the DOM.

## Theme Style: Element – Div

You can change the defaults of the Div element in your theme styles under "Element – Div":

- `display`
- `flex-direction` (if display set to "flex")
- `justify-content` (if display set to "flex")
- `align-items` (if display set to "flex")
- `width`
- `min-width`
- `max-width`
- `margin`
- `padding`

:::tip[Developer reference]
See the [Div Schema](/developer/schema/elements/div/) for the full JSON schema of this element's settings and controls.
:::
