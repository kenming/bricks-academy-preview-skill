---
title: "Action: bricks/form/custom_action"
description: "Runs when a form with a \"Custom\" action is submitted. This allows you to execute custom PHP logic to handle the form submission."
canonical: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-form-custom_action/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/actions/bricks-form-custom_action.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
Runs when a form with a "Custom" action is submitted. This allows you to execute custom PHP logic to handle the form submission.

## Parameters

- `$form` (*Bricks\Form*): The form instance.

## Example usage

```php
add_action( 'bricks/form/custom_action', function( $form ) {
    // Get form fields
    $fields = $form->get_fields();
    
    // Get form settings
    $settings = $form->get_settings();
    
    // Get submitted data
    $form_data = $fields['formId'] ?? []; // Or retrieve specific field values
    
    // Perform custom logic, e.g., send to external API
    $name = isset( $fields['form-field-name'] ) ? $fields['form-field-name'] : '';
    
    if ( $name === 'Specific Name' ) {
        // Do something
        $form->set_result( [
            'type' => 'success', // or 'danger', 'info', 'warning'
            'message' => esc_html__( 'Custom action executed successfully.', 'bricks' ),
        ] );
    }
} );
```
