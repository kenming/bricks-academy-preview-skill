---
title: "Animated typing"
description: "The Animated Typing element creates a typewriter effect that cycles through a list of strings with customizable timing and behavior."
canonical: "https://academy.bricksbuilder.io/builder/elements/general/animated-typing/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/general/animated-typing.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-20T13:12:40.000Z"
---
The Animated Typing element creates a typewriter effect that cycles through a list of strings with customizable timing and behavior.

## Settings

- **Tag** (select) - The HTML tag to use for the element. Options: `div`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`. Default: `div`.

- **Prefix** (text) - Text displayed before the animated strings. Default: "We ".

- **Suffix** (text) - Text displayed after the animated strings. Default: " for you!".

- **Strings** (repeater) - List of strings to cycle through. Each item has a **Text** field. Default: "design", "code", "launch".

### Settings

- **Type speed in ms** (number) - Speed of typing each character. Default: 55.

- **Back speed in ms** (number) - Speed of deleting each character. Default: 30.

- **Start delay in ms** (number) - Delay before starting the animation. Default: 500.

- **Back delay in ms** (number) - Delay before starting to delete. Default: 500.

- **Cursor character** (text) - Character used as the cursor. Default: "|".

- **Loop** (checkbox) - Repeat the animation indefinitely. Default: checked.

- **Shuffle** (checkbox) - Randomize the order of strings each cycle.

:::tip[Developer reference]
See the [Anim. Typing Schema](/developer/schema/elements/animated-typing/) for the full JSON schema of this element's settings and controls.
:::
