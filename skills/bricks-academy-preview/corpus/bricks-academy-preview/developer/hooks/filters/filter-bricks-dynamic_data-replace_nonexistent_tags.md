Dynamic data tags are strings with a special syntax wrapped by curly brackets. Sometimes this syntax has conflicts with other plugins (e.g. Fluent Forms) or with the content itself (e.g. mathematical equations).

From Bricks 1.4 onwards, the default Bricks logic is to keep the nonexistent tags (they won't be replaced by an empty string anymore). It is possible to switch off the default Bricks behavior and tell Bricks to replace the nonexistent dynamic data tags with an empty string.

To replace nonexistent tags add the following PHP snippet to your `functions.php` file:

```php
add_filter( 'bricks/dynamic_data/replace_nonexistent_tags', '__return_true', 10, 1 );
```

:::note
Note: Bricks 1.3.5 introduced the possibility to toggle this behavior, but by default Bricks was replacing the tags. Bricks 1.4 changed the default action.
:::
