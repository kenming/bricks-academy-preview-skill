---
title: "Filter: bricks/form/save-submission/form_data"
description: "The bricks/form/save-submission/formdata filter allows you to modify submitted Bricks form data before it is saved to the database and shown in the Form."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-save-submission-form_data/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/bricks-form-save-submission-form_data.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-07-29T10:15:35.000Z"
---
The `bricks/form/save-submission/form_data` filter allows you to modify submitted Bricks form data before it is saved to the database and shown in the Form Submissions admin screen. ([Save submission](/builder/features/save-form-submissions/))

This is useful when you want to:

- Remove unwanted fields from stored submissions
- Mask sensitive values (e.g. passwords, tokens, IDs)
- Normalize or reformat values before storage



### Example:

In this example, the form submission should store other registration fields, but the password field is masked before saving.

```php
/**
 * $form_data is an array of Submission data to be saved.
 * $form_id The Bricks Form element ID.
 * $post_id The post/page ID where the form is located
 */
add_filter( 'bricks/form/save-submission/form_data', function( $form_data, $form_id, $post_id ) {
  if ( $form_id !== 'coudkb' ) {
    return $form_data;
  }

  // Array of all data going to be saved for this submission, the array key is the field ID
  // Example, mask the field ID 798ce3 before saving
  if ( isset( $form_data['798ce3']['value'] ) ) {
    $form_data['798ce3']['value'] = '******';
  }
  return $form_data;
}, 10, 3 );
```



**Notes:**

- This filter affects **save submissions only**. It does not change what is sent via email actions or other integrations unless those also use the stored submission data.
- For sensitive fields, consider disabling save submission entirely if you don’t need it, or mask/remove values using this filter.
