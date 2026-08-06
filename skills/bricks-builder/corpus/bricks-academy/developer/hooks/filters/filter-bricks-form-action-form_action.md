---
title: "Filter: bricks/form/action/{form_action}"
description: "The bricks/form/action/{formaction} filter is triggered when a custom action (one that is not reserved by Bricks) is selected in a form. It allows developers to."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-form-action-form_action/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-form-action-form_action.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-04T12:13:33.000Z"
---
The `bricks/form/action/{form_action}` filter is triggered when a custom action (one that is not reserved by Bricks) is selected in a form. It allows developers to define custom logic for handling such actions dynamically.

Bricks provides several reserved actions out of the box, including:

- **email**
- **redirect**
- **mailchimp**
- **sendgrid**
- **login**
- **registration**
- **lost-password**
- **reset-password**
- **custom**

If the user's selected action is not in this list, the `bricks/form/action/{form_action}` filter is triggered.

## Example usage

Here’s how you can handle a custom action called `slack-notification`:

```php
// Handle the Slack notification action
add_action(
    'bricks/form/action/slack-notification',
    function ( $form ) {
        $settings = $form->get_settings();
        $fields   = $form->get_fields();

        // Implement Slack notification logic
    }
);
```

## Parameters:

- **`$form` (\Bricks\Integrations\Form\Init)**: The current form instance, providing access to settings and submitted fields.
