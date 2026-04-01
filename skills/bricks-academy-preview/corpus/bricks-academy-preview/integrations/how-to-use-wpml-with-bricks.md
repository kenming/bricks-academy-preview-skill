WPML is a WordPress plugin known for its role in facilitating the creation of multilingual websites.

Coupling it with Bricks (`@since 1.9.1`) allows not only for the manual translation of posts, pages, and various content types into numerous languages but also offers automatic translation features, significantly broadening your website's reach and accessibility.

Once you've established a page in your primary language with Bricks, WPML enables you to easily translate the content into any language you wish to add to your website, be it manually or automatically.

This documentation will guide you through the process of translating your Bricks website using WPML.

## Setting up the environment

Before translating, set up your environment with the necessary plugins:

1. **Bricks setup**:
  - This guide will illustrate the translation process using a simple Bricks website. This website has main pages like Home and Blog, and templates including a header and an "All Archives" template, which has a [template condition](/builder/features/template-settings/#template-conditions) to apply to all archives and the blog page.

1. **WPML plugin installation**:
  - You can use the [OTGS installer](https://wpml.org/version/otgs-installer-3-0-0/) to install the required **WPML Multilingual CMS **and** WPML String Translation** plugins.

![](imgs/bricks-wpml-3-1024x520-0d06281547.png)

1. **Language Configuration**:
  - You can configure your website's languages and other settings through [the WPML setup wizard](https://wpml.org/documentation/getting-started-guide/). During this process, WPML will also ask you for context about your website, such as what it’s about and whose it for.

![](imgs/Bricks-Translation-Context-1024x748-2967d7a334.png)

Using the context that you provide, WPML’s AI translator – [PTC (Private Translation Cloud)](https://ptc.wpml.org/about/) will create translations that fit your target audience and industry.

## Translation options with WPML & Bricks

WPML offers different ways to translate your Bricks content:

1. **[Advanced Translation Editor](https://wpml.org/documentation/translating-your-contents/advanced-translation-editor/)**:
  - Automatic (AI) Translation: Instantly translate your content using WPML’s AI-based engine, then optionally review it before publishing.
  - Manual Translation: A method where each page & string is translated individually.
2. **[String Translation](https://wpml.org/documentation/getting-started-guide/string-translation/)**:
  - Translate theme/plugin strings, widget texts, and other interface strings found under WPML → String Translation.
3. **Edit with Bricks**:
  - If needed, post-translation modifications to design or layout can be done in the Bricks builder for each language.

For more in-depth information on each method, refer to the official [WPML documentation](https://wpml.org/documentation/).

## Translating website content

Translate your website content using WPML and Bricks through the following steps:

### Bulk translation via translation dashboard {#translation-dashboard}

WPML can translate any content you build with Bricks, including pages, posts, templates, and components.

To translate any Bricks content, start by going to **WPML **→ **Translation Dashboard**. From here, expand the section with the content you want to translate and select your items.

For example, to translate a page, expand the **Pages** section and select the page. This will include all Bricks element data and any component instance property values used on that page. To translate Bricks components themselves, expand the **Bricks components** section and select the components you want to translate.

![](imgs/Bricks-TD-efcca4e3e9.png)

Next, select **Translate automatically** for the languages you want to translate into, and click the **Translate **button to begin. If you look under the table, WPML also shows you how much translating your content costs.

![](imgs/Bricks-TD-Step-2-03bfc3b70f.png)

In most cases, your translations will be good to go, but you can always review and make changes using WPML’s **Advanced Translation Editor**.

![](imgs/Editing-translations-in-the-Advanced-Translation-Editor-fccf36bc01.png)

Just visit the translated page you want to edit on the front-end, and click **Edit translation **in the top admin bar. This will open the editor, where you can make any changes necessary.

Once you’re done reviewing, you can instantly publish your translations and display them on your website. Remember that you need to switch languages to view your translations.

### Translating individual pages and posts

While **Translation Management** is perfect for translating multiple pages and templates in one go, you may sometimes want to focus on a single page or post—either for fine-tuning the translation or making additional adjustments. In those cases, you can use the **WPML Advanced Translation Editor** directly from the page/post edit screen.
For comprehensive guidance on the various methods to translate pages and posts created by page builders like Bricks, refer to [WPML's official documentation](https://wpml.org/documentation/translating-your-contents/page-builders/) about this topic.

![](imgs/bricks-wpml-4-1024x518-361fa0bfa5.png)

![](imgs/bricks-wpml-8-1024x516-6f584b0b8f.png)

### Template translation: {#template-translation}

Translating templates follows the same process as translating WordPress pages & posts. Your template settings & type will be automatically duplicated to the translated post.

:::note
If the translation of templates is not automatically enabled when you activate WPML, please [refer to the WPML documentation](https://wpml.org/documentation/support/language-configuration-files/#custom-types) on how to enable translation for custom post types, and ensure that it is enabled for “bricks_template”.
:::

![](imgs/bricks-wpml-15-1024x296-57a6e9acc0.png)

![](imgs/bricks-wpml-14-02733440de.png)

### Example: Translating an archive template:

We have set up a simple archive template, which is applied to both the "Blog" page and its translated version, "Blogue".

![](imgs/bricks-wpml-17-1024x428-3af0457f1a.png)

![](imgs/bricks-wpml-19-564x1024-ef8b4a1a74.png)

Each blog page will only display blog posts of that particular language (using only one template):

![](imgs/bricks-wpml-18-1024x545-b6867df6c7.png)

![](imgs/bricks-wpml-25-1024x563-ba4714525d.png)

## Language switcher & menu translation

### Language switcher

Bricks provides a “Language switcher” element for WPML, which you can add anywhere on your site.

By default, the language switcher comes with a basic preset design. However, you can always customize the switcher to match your website style:

1. Go to **WPML **→ **Languages**.
2. Scroll down to **Custom language switchers** and check the **Enable **box. This will reveal a **Customize **button.
3. Click the button to set your custom preferences and save.

Your changes will immediately take effect on your website.

![](imgs/bricks-wpml-7-1024x515-05d35589f3.png)

![](imgs/Adding-language-swicther-in-Bricks-2ff09b9009.png)

![](imgs/Viewing-language-switcher-on-front-end-b708121596.png)

### WPML menu translation:

Consult WPML documentation for guidance on [translating WordPress menus](https://wpml.org/documentation/getting-started-guide/translating-menus/).

## Sync Bricks data across translated pages {#sync-bricks-data}

After translating a page, you might want to modify the original page. Those changes you perform with Bricks in your original page are not applied to the secondary language pages.

But Bricks and WPML make it seamless to sync your design changes across translated pages without affecting the translated text. Here’s how you can do it:

### Step 1: Edit your original page with Bricks

Open the page in the primary language in the builder. Make the necessary design changes (edit layout, change styles, etc.)

### Step 2: Save your changes

Once done, save your changes.

### Step 3: Edit with WordPress

Close the builder by clicking "Edit with WordPress" to edit the page in WordPress.

![](imgs/bricks-wpml-26-1024x568-d4e89d4c1e.png)

### Step 4: Update translation in the "Languages" panel

In the WordPress editor, navigate to the "Languages" panel. Typically found in the right sidebar or the document settings panel.

Here, you will find an option to edit or update the translation. Click the icon to open the "Advanced Translations Editor" as shown in this screenshot:

![](imgs/bricks-wpml-27-532x1024-1f11064b01.png)

Translate any untranslated strings inside the Advanced Translation Editor, then click the "Complete" button at the bottom of the screen. Your new design changes are now synced with this translated page without affecting the translated text.

## Creating different designs per language {#different-designs}

You can also access and edit the translated content directly with Bricks for specific language design or content modifications. For instance, instead of simply translating the text of your homepage, you can create a completely different layout that appeals to a specific target audience.

To create a different design per language:

1. Use the admin language switcher to change to the language you want to edit.
2. Find the page or template you want to make changes to and open it in Bricks.

![](imgs/Switching-to-translations-in-WordPress-admin-1024x692-918234febe.png)

1. Make your design changes and save. Your pages will now have different designs when switching languages.

![](imgs/Translations-with-design-A-1024x661-2d2c514c64.png)

![](imgs/Translations-with-design-B-1024x661-344f18f5b6.png)

## Additional resources

Consult the following official WPML documentation for further guidance:

1. [**Getting Started with WPML**.](https://wpml.org/documentation/getting-started-guide/)
2. [**WPML FAQ**.](https://wpml.org/faq/)
3. [**Translating Content Created with Page Builders**.](https://wpml.org/documentation/translating-your-contents/page-builders/)
4. [**Translating External Links**.](https://wpml.org/announcements/2020/02/translating-links-with-advanced-translation-editor/)

## Fancy trying out WPML?

If you found this post insightful and you're considering giving WPML a try, we encourage you to use [our affiliate link](https://wpml.org/?aid=482001&affiliate_key=S35UDkP4zjiP).

*Note: The link we've provided is an affiliate link. This means we may earn a small commission if you decide to make a purchase through it. This comes at no extra cost to you, and it assists us in further innovating and refining our offerings.*
