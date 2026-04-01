:::note
**Global elements are officially deprecated since Bricks 2.0! Please convert all existing global elements into components using the new converter under Bricks > Settings > General > Global elements as soon as possible as we will remove global elements render completely in a future 2.x release.**
:::

To reuse an existing element somewhere else on your site we can convert this element into a **Global Element**.

## How To Create A Global Element

Once you've finished editing your element (content & styles), right-click onto your element to reveal the custom context menu. Then click **Save as global element**.

Your element is now available as a global element at the bottom of your elements panel under the **Global Elements** group.

You can now add this global element anywhere else on your site. Whenever you make changes to a global element (content & styles) those changes are automatically applied in real-time to any other instance of this global element throughout your entire site.

:::note
When you save an element as a global element you save the selected element only. Its children are not saved as those are different elements. If a container contains other elements, and you'd like to save all of them, you have to [save it as a template](#multiple-elements).
:::

https://youtu.be/Ny7qucg8pvM

## Saving multiple elements as a template {#multiple-elements}

When you want to add multiple elements as a "global" reusable component, the way in Bricks is to add them into a "section" template type. Just right-click in the container and select "Save as template" or edit the container and you'll find a save icon on the edit element panel, to save the container (and its children elements) as a Bricks template.

You may add this section to your templates or pages using the Template element or the Shortcode element (using the template shortcode). Whenever you change the original section template content, it will automatically change inside the pages where you add it using the Template element or the Template shortcode.

If you opt to insert the template directly (Templates popup > Insert) the template won't change whenever you update the original section template.
