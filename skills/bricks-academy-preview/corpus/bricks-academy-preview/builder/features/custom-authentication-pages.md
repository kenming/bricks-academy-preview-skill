Since Bricks 1.9.2, you can create custom pages for the various authentication processes, effectively substituting the standard WordPress authentication pages.

![Bricks custom authentication settings screen showing options to assign custom pages for login, registration, lost password, and reset password. The ‘WordPress authentication page access’ dropdown is set to 'Error page,' and the ‘Disable custom authentication page bypass’ toggle is enabled.](imgs/bricks-custom-authentication-settings-0e4ab11487.png)

## How to set custom authentication pages

1. Navigate to the WordPress dashboard
2. Navigate to **Bricks** > **Settings** > **General**
3. Scroll down to **Custom authentication pages**

Here, you can choose a custom page for the following processes:

- Login
- Registration
- Lost Password
- Reset Password

## Setting up your custom pages

When creating these custom pages, it's essential to use the "Form" element on those pages with the appropriate authentication actions set under the "Actions" control group of your form.

:::note
For detailed information on setting up form actions and other features of the Form Element, please refer to the [Form element](/builder/elements/general/form/#actions) article.
:::

For instance, for a login page, you should have a form that includes fields for username/email and password, with the "User Login" action set.

## WordPress authentication page access {#wp-auth}

As of Bricks 1.11, you have control over what happens when someone visits a default WordPress authentication URL (such as `wp-login.php`), provided custom authentication pages are set.

To manage this:

1. Navigate to **Bricks** > **Settings** > **General** > **Custom authentication pages**.
2. Under **WordPress authentication page access**, select one of the following options:
  - **Redirect to custom authentication page (default)**: The user will be redirected to the corresponding custom authentication page you’ve set.
  - **Error page**: Visitors will be redirected to the 404 error page, effectively blocking access to the default WordPress login page.
  - **Home URL**: Redirects visitors to your homepage.
  - **Redirect to specific page**: Allows you to choose a specific page on your site to redirect visitors to.

This feature is particularly useful if you want to prevent access to the default WordPress login page (`wp-login.php`) entirely. For example, combining this with the bypass disabling feature (below) will fully restrict access to the default authentication URLs.

## Bypassing custom login (since 1.9.4):

By default, when visiting any authentication page on your site, you can access the default WordPress login page by adding `brx_use_wp_login` as a URL parameter (e.g., https://example.com**/wp-login.php?brx_use_wp_login=1**). This feature allows users to bypass the custom login page if needed.

In Bricks settings, you have the option **to disable this feature**:

- Navigate to Bricks > Settings > General > Custom authentication pages.
- Check the **Disable custom authentication page bypass** setting to force the use of your custom authentication pages, preventing access to the default WordPress login page through the URL parameter.
