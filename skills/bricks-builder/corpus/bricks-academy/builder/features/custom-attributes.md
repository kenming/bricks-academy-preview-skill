---
title: "Custom Attributes"
description: "Add custom HTML attributes in Bricks for integrations, JavaScript hooks, accessibility, and advanced frontend behavior."
canonical: "https://academy.bricksbuilder.io/builder/features/custom-attributes/"
markdownUrl: "https://academy.bricksbuilder.io/builder/features/custom-attributes.md"
pageType: "article"
section: "builder"
category: "features"
lastmod: "2026-08-04T12:13:33.000Z"
---
Bricks 1.3 introduces the possibility to add your own custom HTML attributes to any element.

You can add custom attributes under "Style > Attributes". Set a "Name" and a "Value" and your attribute(s) will be added to the elements' most relevant node. By default, your attributes are added to the element root node. Besides manually entered values you can populate custom attribute values with dynamic data, too.

In there you'll be able to insert multiple attributes (name and value). Dynamic Data is rendered for attribute values on the frontend.

![](imgs/feature-custom-attributes-37d8f7736f.png)

<figcaption>

Container: Custom Attributes

</figcaption>

Let's say you want to add an ARIA **role** and **label** to a container that contains multiple images that should be [considered as a single image](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/Role_Img). You'd add the following two attributes when editing your container:

- Attribute #1 name: **role**
- Attribute #1 value: **img**
- Attribute #2 name: **aria-label**
- Attribute #2 value: **Description of the overall image**

This results in the following container HTML:

```html
<div id="brxe-sfglik" class="brxe-sfglik brxe-container" role="img" aria-label="Description of the overall image">
... Container elements ...
</div>
```

Custom attributes take precedence over default attributes. So if you set a custom **alt** attribute when editing your image, this custom attribute will be used instead of the default image **alt** attribute.

Elements where custom attributes are added to the following specific HTML tags:

| **Bricks Element** | **HTML tag** |
| --- | --- |
| Nav Menu | `<nav>` |
| Heading | `<h1>` or any other heading tag |
| Text | `<div>` |
| Button | `<button>` or `<a>` depending if there is a link |
| Image | `<img>` |
| Video | `<div>` |
| Form | `<form>` |

### How To Add Tooltips {#tooltips}

Bricks comes with built-in (CSS-only) tooltips that you can set via custom attributes.

Make sure to set the attribute "Name" to `data-balloon` and the value to whatever you want your tooltip text to be. You also have to set a second HTML attribute named `data-balloon-pos` and then set the value to whatever you want your tooltip to be positioned like:

- top | top-right | top-left
- right
- bottom | bottom-right | bottom-left
- left

For a full list of all available tooltip HTML attributes please visit the official website of the Balloon.css library Bricks uses for its tooltips: [https://kazzkiq.github.io/balloon.css/](https://kazzkiq.github.io/balloon.css/)

:::note
If you are planning to add tooltips on the Icon element, please wrap the Icon element in a Div element and set the attribute on the Div element. Otherwise, balloon library CSS will overwrite the Icon element's CSS and cause it invisible in the frontend.
:::

#### Resources:

- HTML attribute reference: [https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)
