---
title: "Maintenance Mode"
description: "Set up maintenance mode in Bricks, choose what visitors see, and control access while you work on the site."
canonical: "https://academy.bricksbuilder.io/builder/features/maintenance-mode/"
markdownUrl: "https://academy.bricksbuilder.io/builder/features/maintenance-mode.md"
pageType: "article"
section: "builder"
category: "features"
lastmod: "2026-08-20T13:12:40.000Z"
---
Bricks 1.9.4 introduces the **Maintenance Mode** feature. A straightforward way to manage your site's availability during updates or construction.

![](imgs/bricks-settings-maintenance-mode-2-0-96527fa78e.png)

Maintenance Mode runs on the frontend only. It does not replace the WordPress admin, and it does not block the Bricks builder.

## How to enable Maintenance Mode

1. Log in to the WordPress dashboard.
2. Navigate to Bricks > Settings > Maintenance.

Here, you'll find several settings to configure:

- **Mode selection**: Choose `Disabled`, `Maintenance`, or `Coming Soon`. "Maintenance" mode (HTTP status code 503) indicates that your site is temporarily unavailable, signaling search engines to come back later. "Coming soon" mode (HTTP status code 200) indicates that your site is available for search engine indexing.
- **Template** *(optional)*: Assign a custom single template for your maintenance or coming soon mode.
  - **Render header** *(optional)*: Enable this setting if you want the active Bricks header to render with the maintenance or coming soon template. This is **disabled by default**.
  - **Render footer** *(optional)*: Enable this setting if you want the active Bricks footer to render with the maintenance or coming soon template. This is **disabled by default**.
  - **Render popups** *(optional)*: Enable this setting if you want Bricks popups to be rendered on the maintenance or coming soon template. This is **disabled by default**.
- **Bypass maintenance**: Customize access settings for different user roles.
- **Exclude posts/pages** *(since 2.0)*: Select specific pages or posts where Maintenance Mode should **not** be applied.

If no template is selected, or the selected template is not published or has no Bricks data, Bricks renders a simple default page with a `Maintenance` or `Coming soon` heading.

## When maintenance mode applies

Maintenance mode is skipped for:

- WordPress admin requests.
- Bricks builder requests.
- The Bricks custom login page, if one is configured.
- Logged-in users who can bypass maintenance.
- Posts or pages selected under **Exclude posts/pages**.

If none of those bypasses apply, Bricks serves the maintenance response. In **Maintenance** mode, Bricks sends HTTP status `503`. In **Coming soon** mode, Bricks sends HTTP status `200`.

When maintenance mode is active, Bricks also removes the canonical tag and does not output Bricks Open Graph meta tags for the maintenance response.

## Custom maintenance templates

The selected maintenance template replaces the requested page content while maintenance mode is applied. The normal search, archive, and error templates are disabled for that response.

Header and footer rendering are off by default and must be enabled with **Render header** and **Render footer**. Popups are also off by default and only load when **Render popups** is enabled, or when the current user can bypass maintenance.

For multilingual sites, Bricks resolves the selected maintenance template through WPML or Polylang when those integrations are active.

## Configuring role-based access

In the "Bypass maintenance" setting:

1. Select from the dropdown menu: `Logged-in users` allows all logged-in users to bypass maintenance mode; `Logged-in users with role` provides a more granular control.
2. If `Logged-in users with role` is selected, checkboxes will appear to enable or disable maintenance mode bypass for specific roles such as Editor, Author, Contributor, etc.

Administrators can bypass maintenance by default. If no custom role selection is enabled, logged-in users can bypass maintenance mode.

## Individual user access settings

To configure access on an individual user level:

1. From the WordPress dashboard, go to "Users".
2. Click to edit a specific user's profile.
3. In the user profile, find and adjust the "Bypass Maintenance" setting.

The individual user setting can explicitly enable or disable maintenance bypass for that user. This takes precedence over the role-based setting and over the default administrator/logged-in behavior.

<span id="filters"></span>

**Filters:**

- [/developer/hooks/filters/filter-bricks-maintenance-should_apply/](/developer/hooks/filters/filter-bricks-maintenance-should_apply/)
