---
title: "Element Conditions Schema"
description: "Full schema for element display conditions: condition keys, comparison operators, and the OR-of-AND data structure."
canonical: "https://academy.bricksbuilder.io/developer/schema/elements/common/conditions/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/elements/common/conditions.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-08-04T12:13:33.000Z"
---
import SchemaJson from '../../../../../../components/SchemaJson.astro'

Element display conditions control whether an element renders on the frontend. They are stored in the `_conditions` key inside any element's `settings` object.

## Data structure

Conditions use an OR-of-AND structure: the outer array contains OR groups, and each inner array contains AND items. The element renders if **any** OR group evaluates to true, and an OR group is true when **all** its AND items are true.

<SchemaJson path="elements/common/conditions.json" />

## `conditionItem` properties

Each condition item has the following properties:

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string \| integer | Yes | Unique identifier for this condition |
| `key` | string | Yes | Condition type (see enum below) |
| `compare` | string | Yes | Comparison operator (see table below) |
| `value` | any | Conditional | The value to compare against. Not needed when compare is `empty` or `empty_not`. |
| `dynamic_data` | string | No | Dynamic data tag to use as the value source |

### Example

```json
{
  "_conditions": [
    [
      { "id": "abc123", "key": "user_logged_in", "compare": "==", "value": true },
      { "id": "def456", "key": "user_role", "compare": "==", "value": "administrator" }
    ],
    [
      { "id": "ghi789", "key": "dynamic_data", "compare": "contains", "value": "sale", "dynamic_data": "{post_title}" }
    ]
  ]
}
```

This reads as: show the element if (user is logged in AND is an administrator) OR (the post title contains "sale").

## Condition keys

**General**
- `browser`
- `current_url`
- `date`
- `datetime`
- `dynamic_data`
- `featured_image`
- `operating_system`
- `referer`
- `time`
- `weekday`

**Post**
- `post_author`
- `post_date`
- `post_id`
- `post_parent`
- `post_status`
- `post_title`

**User**
- `user_id`
- `user_logged_in`
- `user_registered`
- `user_role`

**WooCommerce**
- `woo_product_category`
- `woo_product_featured`
- `woo_product_new`
- `woo_product_purchased_by_user`
- `woo_product_rating`
- `woo_product_sale`
- `woo_product_sold_individually`
- `woo_product_stock_management`
- `woo_product_stock_quantity`
- `woo_product_stock_status`
- `woo_product_tag`
- `woo_product_type`

Available compare operators vary by condition key. For example, `post_id` supports math operators (`==`, `!=`, `>=`, `<=`, `>`, `<`), while `user_logged_in` only supports `==` and `!=`.

## Comparison operators

| Operator | Description |
|---|---|
| `==` | Equal (loose comparison, supports arrays via intersection) |
| `!=` | Not equal (loose comparison) |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |
| `>` | Greater than |
| `<` | Less than |
| `contains` | String contains substring |
| `contains_not` | String does not contain substring |
| `empty` | Value is empty (no value field needed) |
| `empty_not` | Value is not empty (no value field needed) |

## Extensibility

Condition keys and comparison operators are filterable via PHP hooks:

- `bricks/conditions/groups`: add custom condition groups
- `bricks/conditions/options`: add custom condition keys with their own compare operators
- `bricks/conditions/result`: modify the boolean result of any individual condition evaluation

Third-party plugins can introduce additional condition keys beyond those listed above.
