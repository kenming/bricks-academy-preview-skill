For first-time installation and activation, follow [Installation and setup](/getting-started/installation-setup/).

This article covers **automatic updates**, **staging and safe updates**, **which URLs count toward your license**, and **managing activations** in your Bricks account.

Your Bricks account and downloads live at [my.bricksbuilder.io](https://my.bricksbuilder.io/) (same destination the theme uses for remote services).

## How to update Bricks {#how-to-update}

If you have activated your Bricks license key on your site, you'll automatically receive update notifications in your WordPress dashboard. You can then perform the update to the latest version of Bricks with one click from your WordPress dashboard.

![](imgs/bricks-wp-dashboard-how-to-update-41e0c3b43e.png)

You can also always manually download the latest version from your Bricks account at [https://my.bricksbuilder.io/](https://my.bricksbuilder.io/) as a ZIP file.

### Test on staging & read the changelog

We recommend to perform updating a mission-critical software like Bricks first on a staging server. Especially if your website is live, receives a lot of traffic, you are running marketing campaigns, offers, etc. Once you confirmed that everything is working as expected you can update your live site.

Every noticeable host offers, mostly free of charge, an easy one-click staging solution. Please reach out to your host if you are not sure how this works.

Every update is accompanied by an in-depth release changelog. Please take the time to go over it at [https://bricksbuilder.io/changelog/](https://bricksbuilder.io/changelog/) before you perform the update.

This way you know exactly what changed, if any adjustments or steps need to be performed on your end, which new features are available, and so on.

### Local, staging & intranet installations don't count against your license limit {#local}

The following URL structures are qualified as local, staging, or intranet sites and do not count against your license limit.

**Local URLs:**

- `192.168.x.x`
- `127.0.0.1`
- `localhost` (includes)
- `.local` (top-level domain)
- `.test` (top-level domain)
- `.wip` (top-level domain)

<span id="staging"></span>

**Staging URLs:**

- Staging subdomains (dev, staging, test)
  - `dev.yoursite.com`
  - `staging.yoursite.com`
  - `test.yoursite.com`
- Cloudways: `.cloudwaysapps.com`
- Dreamhost: `.stage.site`
- Flywheel: `.mysites.io`
- GoDaddy: `.myftpupload.com`
- Hostinger: `.hostingersite.com`
- InstaWP: `.instawp.site` & `.instawp.xyz` & `instawp.com`
- Kinsta: `.kinsta.cloud`
- Lando Pantheon: `.lndo.site`
- Plesk: `.plesk.page`
- Raidboxes: `.myrdbx.io`
- Runcloud: `.temp-site.link`
- TasteWP: `.tastewp.com`
- WP Engine:`.wpenginepowered.com`
- xCloud: `.wp1.site`
- ZipWP: `.zipwp.link`

<span id="intranet"></span>

**Intranet (top-level domains):**

- `.intranet`
- `.internal`
- `.private`
- `.corp`
- `.home`
- `.lan`

**With a Bricks Starter license (1 active site limit), you can build your site locally with Bricks & use your Starter license on your live site simultaneously.**

You can deactivate the license key from your site from your WP dashboard under `Bricks > License`, and activate it on another site or remove the site from your Bricks account under the "Sites" tab. We monitor any potential misusage (attempts to avoid purchasing a sufficient plan) and reserve the right to limit further license activations.
