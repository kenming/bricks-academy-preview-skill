Bricks 1.11.1 introduces a Bricks-native Password Protection feature, giving you a simple yet powerful way to secure content across your website without needing extra plugins.

Whether you want to lock down individual pages, posts, broader areas like custom post types, or even the entire website, you can create custom templates that control access with ease.

Customize the password entry experience, schedule when protection is active, and manage everything directly within Bricks.

## How to set up password protection

1. Enable this experimental feature under `Bricks > Settings > General > Password Protection`
2. **Create a password protection template**
  - From the WordPress dashboard, navigate to `Bricks > Templates` and create a new template.
  - Under **Template type**, select **Password protection**.
3. **Configure password protection settings**
  - Click **Edit in Bricks** to customize the template.
  - To access the password protection settings, go to `Settings > Template settings > Password protection`.
  - Available settings include:
    - **Password source:** Select how passwords are managed. Options are **Template password**, **Post password**, or **Template & post password**. See details on each method in the [password source options](#password-source-options) section below.
    - **Password:** Set the password for template-wide protection. This field is only available if the **Password source** is set to **Template password** or **Template & post password**.
    - **Disable header**.
    - **Disable footer**.
    - **Disable popups**.
    - **Allow logged-in users to bypass**.
    - **Schedule:** Schedule when the password protection is active.
      - **Start date:** Set the date and time when protection begins.
      - **End date:** Set the date and time when protection ends.

![](imgs/bricks-password-protection-settings-e713b1adb5.png)

![](imgs/bricks-password-protection-settings-group-63ee01c26d.png)

![](imgs/bricks-password-protection-settings-1-13b6e10096.png)

1. **Set template conditions**
  - Set [the template conditions](/builder/features/template-settings/#template-conditions) under `Settings > Template settings > Conditions` to define where this template applies.
  - For more dynamic control, use the [`bricks/password_protection/is_active`](https://academy.bricksbuilder.io/filter-bricks-password_protection-is_active) filter to customize when the template should be active or bypassed.

![](imgs/bricks-password-protection-template-conditions-e31525199e.png)

1. **Add form element for unlocking**
  - Add a **Form Element** to the password protection template.
  - Add an **Unlock password protection** form action. This action will allow users to unlock the protected content by entering the correct password.

![](imgs/bricks-password-protection-form-action-af97a38160.png)

## Password source options {#password-source-options}

The behavior of the password protection feature depends on the selected **password source** option. Below are details on how each option works and instructions for setup:

### Template password

Selecting **Template password** applies the password set in the template settings to all pages or posts that meet the template conditions. No further configuration is needed on individual posts. Simply:

- Set the password in `Settings > Template settings > Password protection > Password`.
- Define the template conditions under `Settings > Template settings > Conditions` to specify where this template will apply.

![](imgs/bricks-password-protection-template-password-2731f3656e.png)

For any content matching these conditions, the password form will be automatically rendered, restricting access to those pages.

### Post password

When **Post password** is selected, this template customizes the default WordPress password protection form but requires individual post-level password settings.

To protect content using the **Post password** method:

1. Enable password protection on each post or page through the WordPress editor.
2. Set a password directly on the individual post or page (or through quick edit).
3. The template conditions will control where the custom password form appearance applies, but protection is managed at the post level.

![](imgs/bricks-password-protection-wp-editor-63e8703975.png)

![](imgs/bricks-password-protection-post-password-79bf1bff93.png)

### Template & post password

The **Template & post password** option uses the template password by default. However, if an individual post password is set, it will take precedence.

Setup process:

1. Enter a password in **Password protection > Password**.
2. Define template conditions as needed to apply the password protection across relevant content.
3. For any posts with an individual password set, that password will override the template password.

![](imgs/bricks-password-protection-template-and-post-password-86673cf3d7.png)

This setup provides flexibility by allowing individual content to have unique passwords while maintaining general protection for all content under the template.

### Password protection filters: {#filters}

- [/developer/hooks/filters/filter-bricks-password_protection-cookie-expires/](/developer/hooks/filters/filter-bricks-password_protection-cookie-expires/)
- [/developer/hooks/filters/filter-bricks-password_protection-is_active/](/developer/hooks/filters/filter-bricks-password_protection-is_active/)
