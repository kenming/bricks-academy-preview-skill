---
title: "Installation and setup"
description: "Install Bricks, activate the theme, configure the basic WordPress setup, and prepare your site for the rest of the Academy walkthrough."
canonical: "https://academy.bricksbuilder.io/getting-started/installation-setup/"
markdownUrl: "https://academy.bricksbuilder.io/getting-started/installation-setup.md"
pageType: "article"
section: "getting-started"
category: "installation-setup"
lastmod: "2026-08-04T12:13:33.000Z"
---
https://youtu.be/sUgx3lg6Jko

Let's get Bricks installed on your WordPress site.

Before you install, confirm your host meets [Bricks requirements](/builder/setup/requirements/) (PHP, database, memory, upload size, and a modern browser). Most hosting does; use that article if you need to raise limits or troubleshoot.

## Install the Bricks theme

Installing Bricks works exactly like any other WordPress theme. Use one place for everything account-related: [my.bricksbuilder.io](https://my.bricksbuilder.io/) (download the theme ZIP and find your license key there).

### Download Bricks

Log into [my.bricksbuilder.io](https://my.bricksbuilder.io/) and download the latest version as a ZIP file.

![](imgs/download-bricks-8df7d5725c.png)

### Upload to WordPress

:::note[Theme, not plugin]
Install Bricks as a **theme** (**Appearance > Themes > Upload**), not under **Plugins**. Uploading the ZIP as a plugin will not work.
:::

1. In your WordPress dashboard, go to **Appearance > Themes**
2. Click **Add New**
![](imgs/wordpress-add-theme-369bc1536f.png)
3. Click **Upload Theme**
![](imgs/wordpress-upload-theme-bc999f97cb.png)
4. Select the `bricks.zip` file from your computer
5. Click **Install Now**
6. After the upload completes, click **Activate** (or go to **Appearance > Themes** and activate **Bricks**)

**If the upload fails**, it is usually because your WordPress site does not allow large enough uploads. See [Requirements](/builder/setup/requirements/) (max file upload size) or, as a last resort, unzip the file on your computer and upload the `bricks` folder via FTP to `/wp-content/themes/`.

## Activate your license

Once Bricks is installed, you'll see a new **Bricks** menu item in your WordPress dashboard, along with a notification prompting you to activate your license.

Click **Bricks > License** (or the notification link). This opens the license activation screen.
![](imgs/bricks-license-tab-8235ad185f.png)

### Steps to activate

1. Copy your license key from [my.bricksbuilder.io](https://my.bricksbuilder.io/)
2. Paste it into the license field
3. Click **Activate License**

You should see a confirmation that your license is **active**.

For blueprint sites, cloned sites, or code-managed setups, you can also define the license key in `wp-config.php` with the `BRICKS_LICENSE_KEY` constant. See [Define the license key in wp-config.php](/builder/license/license-and-updates/#constant) for the full workflow and database-key behavior.

That's it, Bricks is ready to use!

For license limits, staging URLs, managing activations, automatic updates, and updating safely, see [License, updates, and your account](/builder/license/license-and-updates/).

## What you've accomplished

You now have Bricks installed and licensed.
