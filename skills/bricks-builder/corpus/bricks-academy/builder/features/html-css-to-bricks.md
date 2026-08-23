---
title: "HTML & CSS to Bricks"
description: "Convert existing HTML and CSS into Bricks layouts more efficiently by using the builder structure, classes, and styling tools."
canonical: "https://academy.bricksbuilder.io/builder/features/html-css-to-bricks/"
markdownUrl: "https://academy.bricksbuilder.io/builder/features/html-css-to-bricks.md"
pageType: "article"
section: "builder"
category: "features"
lastmod: "2026-08-20T13:12:40.000Z"
---
Building a layout in Bricks based on a web layout library or AI-generated layouts usually means building it from scratch, element by element. This feature changes that workflow. You can now paste HTML or CSS directly into the builder to create native elements and styles instantly.

https://www.youtube.com/watch?v=Jxib7wc_1SU

## Configuration

You can control how Bricks handles pasted code in the settings.

**Path:** `Bricks > Settings > Builder > HTML & CSS to Bricks`

- **Enabled (confirm on paste):** A dialog appears asking for permission to convert the code on paste.
- **Enabled (no confirm on paste):** Bricks converts the code automatically on paste.
- **Disabled**

## How it works

When you paste HTML or CSS, the builder identifies the content type and initiates a conversion process.

### HTML conversion

Bricks parses the HTML and maps standard tags to native elements.

- `<section>` becomes a Section element.
- `<div>` becomes a Div.
- `<h1>` through `<h6>` become Headings.
- `<img>` becomes an Image.

### Global classes & variables

The converter identifies classes in your code and creates corresponding Bricks global classes and global variables.

- **Mapped styles:** Properties like margin, padding, and typography are applied directly to the Bricks UI controls.
- **Custom CSS:** Properties that do not have a dedicated UI control are added to the element's Custom CSS area.
- **Variables:** Any variables defined in `:root` are converted into Bricks Global Variables.

## Example: HTML with a global class

Copy both the HTML and CSS, then paste them into the builder:

```html
<section class="feature">
  <h2>Built for client work</h2>
  <p>Start with a native Bricks structure, then refine it in the builder.</p>
</section>

<style>
  :root {
    --feature-space: 2rem;
  }

  .feature {
    padding: var(--feature-space);
    background-color: #f4f4f4;
  }
</style>
```

Bricks creates native Section, Heading, and text elements. It also creates the `feature` global class and the `--feature-space` global variable. Supported declarations are mapped to builder controls; remaining declarations stay in custom CSS.

## Example: CSS-only paste

Paste CSS by itself when the structure already exists and you only need classes or variables:

```css
:root {
  --card-radius: 12px;
}

.card {
  border-radius: var(--card-radius);
  padding: 1.5rem;
}
```

Bricks creates the variable and global class. Apply the new `card` class to an element from the builder.

## Security

Bricks will not execute JavaScript or load external stylesheets automatically upon pasting until reviewed.

Any detected scripts or external links are placed inside a **Code** element. You must manually review, sign, and save these elements before they are executed.

For example, pasting `<script>console.log('Ready')</script>` creates a Code element. The script remains inactive until a user with permission reviews and signs it.

## Notes

- **Refinement:** The conversion provides a structural foundation. Because your site has existing theme styles and theme or plugin CSS, the output may require further manual adjustments to match the source perfectly.
- **Permissions:** You must have the [user permission](/builder/interface/builder-access/#custom) to "Create global classes" for the converter to generate styles correctly.
- **CSS-only paste:** If you paste only CSS, Bricks will generate the global classes and variables.
- **Missing class styles:** Confirm that your role can create global classes. Without that permission, the converter cannot create the class records used by the imported CSS.
