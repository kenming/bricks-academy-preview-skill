This article is the **reference** for what your server and browser need to run Bricks, and how to fix common limits. The [Installation and setup](/getting-started/installation-setup/) guide links here when you need the full checklist or troubleshooting.

To provide you with a cutting-edge site builder for WordPress Bricks uses the most modern technology stack (VueJS 3, etc.) while keeping sufficient backward compatibility.

Below are the minimum requirements your server should meet so Bricks runs smoothly:

- PHP 7.4+ (recommended: 8.0+)
- MySQL 5.6+
- WordPress memory limit: min. 64 MB (recommended: 512 MB)
- Max file upload size: min. 64 MB
- Modern browser: **Please use the latest version of Chrome, Firefox, Safari, or Microsoft Edge when editing your website with Bricks**. Older browsers (e.g. Internet Explorer) lack support for some of the more advanced builder features.

:::note
*Bricks is a self-hosted solution that you download & install on your own WordPress website!*
:::

## How To Increase WP Memory Limit {#wp-memory-limit}

You can define **WP_MEMORY_LIMIT** by adding the following code to your **wp-config.php** file, above the line that says "That's all, stop editing!":

```php
define( 'WP_MEMORY_LIMIT', '512M' );
/* That's all, stop editing! Happy publishing. */
```

Some web hosts set the PHP memory limit to as low as 8 MB. In that case, you might consider upgrading to a more powerful hosting plan. If your host does not allow you to config this setting by yourself, please get in touch with them.

## How To Increase Max File Upload Size {#max-file-upload-size}

If you encounter problems uploading larger files to your site (or when downloading high-resolution images from Bricks' Unsplash integration) there are a few ways to increase the maximum upload file size.

A maximum upload size should be 64 MB or more. Log into your hosting account and change the following two **PHP server settings** to:

- post_max_size: 64M
- upload_max_filesize: 64M

If you have access to your **php.ini** file, located in the root directory of your WordPress installation, open it, and modify the following settings:

```php
upload_max_filesize = 64M
post_max_size = 64M
```

You can also add the following code to your **.htaccess** file, but make sure to backup your existing .htaccess file beforehand:

```php
php_value upload_max_filesize 64M
php_value post_max_size 64M
```

If all above fails, you can try adding the following code to your wp-config.php:

```php
@ini_set( 'upload_max_size' , '64M' );
@ini_set( 'post_max_size', '64M');
```

To confirm that your maximum upload file size has been updated successfully, go to **Media > Add New**. On the bottom of this page, you should see your maximum upload file size.

## How To Increase Maximum Execution Time {#max-execution-time}

When you start seeing a message like "Maximum execution time of 30 seconds exceeded" you have to increase the execution time of your website by using one of the following three solutions:

**#1: Add the following code to your wp-config.php file (above the "That's all, stop editing!" line):**

```php
set_time_limit(180);
/* That's all, stop editing! Happy publishing. */
```

**#2: Backup your .htaccess file and add the following code to it:**

```php
php_value max_execution_time 180
```

**#3: Add the following code to your php.ini file:**

```php
max_execution_time = 180
```
