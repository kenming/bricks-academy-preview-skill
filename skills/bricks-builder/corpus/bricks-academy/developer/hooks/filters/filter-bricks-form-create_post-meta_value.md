---
title: "Filter: bricks/form/create_post/meta_value"
description: "This filter is used within the Create post form action in Bricks."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-form-create_post-meta_value/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-form-create_post-meta_value.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
This filter is used within the [Create post](/builder/features/create-update-posts-on-the-frontend/) form action in Bricks.

It allows developers to alter the meta values of new posts created from form submissions before they are saved to the database.

**Functionality:**

This filter activates during the execution of the 'Create Post' action. It provides an opportunity to modify the meta values based on custom logic or specific project requirements. This can include data formatting, validation, files handling, or applying conditional transformations to the meta values.

**Example Usage:**

```php
add_filter(
	'bricks/form/create_post/meta_value',
	function( $meta_value, $meta_key, $form_settings, $form_fields ) {
		if ( $meta_key === 'my_meta_key' ) {
			// Custom logic for 'my_meta_key'
			$meta_value = transform_meta_value( $meta_value );
		}
		// Additional custom logic can be implemented here
		return $meta_value;
	},
	10,
	4
);
```

In this example, the filter modifies the value of the meta key 'my_meta_key' using a custom function `transform_meta_value`.

**Parameters:**

- `$meta_value` (mixed): The original value of the meta field.
- `$meta_key` (string): The key of the meta field being modified.
- `$form_settings` (array): The settings of the form from which the post is created.
- `$form_fields` (array): The form fields data.

**Return:**

- (mixed): The modified value of the meta field, which will be saved with the post.
