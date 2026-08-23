---
title: "Filter: bricks/form/update_post/meta_value"
description: "This filter is part of the Update post form action in Bricks."
canonical: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-form-update_post-meta_value/"
markdownUrl: "https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-form-update_post-meta_value.md"
pageType: "article"
section: "developer"
category: "hooks"
lastmod: "2026-08-20T13:12:40.000Z"
---
This filter is part of the [**Update post**](/builder/features/create-update-posts-on-the-frontend/) form action in Bricks.

It enables developers to customize the meta values of existing posts being updated through form submissions.

**Functionality:**

The `bricks/form/update_post/meta_value` filter is triggered within the 'Update post' action when a post is being updated from a form submission. It allows for altering the meta values based on custom logic or project-specific needs. This includes formatting data, validating content, handling file uploads, or applying conditional transformations to the meta values.

**Example Usage:**

```php
add_filter(
	'bricks/form/update_post/meta_value',
	function( $meta_value, $meta_key, $post_id, $form_fields ) {
		if ( $meta_key === 'specific_meta_key' ) {
			// Custom logic for 'specific_meta_key'
			$meta_value = modify_meta_value( $meta_value );
		}
		// Implement additional custom logic here
		return $meta_value;
	},
	10,
	4
);
```

In this example, the filter modifies the value of a specific meta key ('specific_meta_key') using a custom function `modify_meta_value`.

**Parameters:**

- `$meta_value` (mixed): The original value of the meta field.
- `$meta_key` (string): The key of the meta field being modified.
- `$post_id` (int): The ID of the post being updated.
- `$form_fields` (array): The form fields data.

**Return:**

- (mixed): The modified value of the meta field, which will be updated in the post's meta data.
