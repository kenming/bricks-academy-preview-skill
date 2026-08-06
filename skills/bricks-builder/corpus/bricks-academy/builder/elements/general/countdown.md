---
title: "Countdown"
description: "The Countdown element displays a countdown timer to a specified date with customizable fields and actions."
canonical: "https://academy.bricksbuilder.io/builder/elements/general/countdown/"
markdownUrl: "https://academy.bricksbuilder.io/builder/elements/general/countdown.md"
pageType: "article"
section: "builder"
category: "elements"
lastmod: "2026-08-04T12:13:33.000Z"
---
The Countdown element displays a countdown timer to a specified date with customizable fields and actions.

## Settings

- **Date** (datepicker) - The target date and time for the countdown.

- **Time zone** (select) - The time zone for the countdown calculation. Options include various UTC offsets. Default: UTC+00:00.

- **Date Reached** (select) - Action when the countdown reaches zero. Options: `countdown` (show countdown), `hide` (hide element), `text` (show custom text). Default: `countdown`.

- **Date Reached: Custom text** (text) - Custom text to display when the date is reached. Only shown when "Date Reached" is set to "text".

### Fields

- **Fields** (repeater) - Configure the countdown display fields. Each field has:
  - **Prefix** (text) - Text before the field value.
  - **Format** (text) - Format string using %D (days), %H (hours), %M (minutes), %S (seconds). Lowercase removes leading zeros. Default: "%D days", "%H hours", "%M minutes", "%S seconds".
  - **Suffix** (text) - Text after the field value.

- **Direction** (direction) - Flex direction for the fields container.

- **Align main axis** (justify-content) - Justify content alignment for fields.

- **Align cross axis** (align-items) - Align items for fields.

### Field

- **Direction** (direction) - Flex direction for individual fields.

- **Margin** (spacing) - Margin around individual fields. Default: 0 5px 0 0.

:::tip[Developer reference]
See the [Countdown Schema](/developer/schema/elements/countdown/) for the full JSON schema of this element's settings and controls.
:::
