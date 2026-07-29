---
title: "Form Schema"
description: "Schema for Bricks Form element"
canonical: "https://academy.bricksbuilder.io/developer/schema/elements/form/"
markdownUrl: "https://academy.bricksbuilder.io/developer/schema/elements/form.md"
pageType: "article"
section: "developer"
category: "schema"
lastmod: "2026-07-29T10:15:35.000Z"
---
import SchemaJson from '../../../../../components/SchemaJson.astro'

| Property | Value |
|---|---|
| `name` | form |
| `category` | general |
| `tag` | form |
| `nestable` | false |

<SchemaJson path="elements/form.json" />

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `fields` | repeater | Type | `font` on `.password-toggle .show-password i` |
| `requiredAsterisk` | checkbox | Show required asterisk | — |
| `disableRequiredAsteriskInPlaceholder` | checkbox | Disable required asterisk in placeholder | — |
| `showLabels` | checkbox | Show labels | — |
| `labelTypography` | typography | Label typography | `font` on `label`, `font` on `.label` |
| `placeholderTypography` | typography | Placeholder typography | `font` on `::placeholder`, `font` on `select` |
| `disableFormValidationOn` | select | Disable form validation | — |
| `disableBrowserValidation` | checkbox | Don\ | — |
| `validateAllFieldsOnSubmit` | checkbox | Validate all fields on submit | — |
| `fieldMargin` | spacing | Spacing | `padding` on `.form-group:not(.submit-button-wrapper):not(.message):not(.captcha)` |
| `fieldPadding` | spacing | Padding | `padding` on `.form-group input`, `padding` on `.flatpickr`, `padding` on `select`, `padding` on `textarea` |
| `horizontalAlignFields` | justify-content | Alignment | `justify-content` |
| `fieldBackgroundColor` | color | Background color | `background-color` on `.form-group input`, `background-color` on `.flatpickr`, `background-color` on `select`, `background-color` on `textarea` |
| `fieldBorder` | border | Border | `border` on `.form-group input`, `border` on `.flatpickr`, `border` on `select`, `border` on `textarea`, `border` on `.bricks-button:not([type=submit])`, `border` on `.choose-files` |
| `fieldTypography` | typography | Typography | `font` on `.form-group input`, `font` on `select`, `font` on `textarea` |
| `submitButtonText` | text | Text | — |
| `submitButtonSize` | select | Size | — |
| `submitButtonStyle` | select | Style | — |
| `submitButtonWidth` | number | Width | `width` on `.submit-button-wrapper` |
| `submitButtonMargin` | spacing | Margin | `margin` on `.submit-button-wrapper` |
| `submitButtonTypography` | typography | Typography | `font` on `.bricks-button` |
| `submitButtonBackgroundColor` | color | Background | `background-color` on `.bricks-button` |
| `submitButtonBorder` | border | Border | `border` on `button[type=submit].bricks-button` |
| `submitButtonIcon` | icon | Icon | — |
| `submitButtonIconPosition` | select | Icon position | — |
| `actions` | select | Actions after successful form submit | — |
| `successMessage` | text | Success message | — |
| `noticeCloseAfter` | number | Close after | — |
| `noticeCloseButton` | checkbox | Close button | — |
| `emailSubject` | text | Subject | — |
| `emailTo` | select | Send to email address | — |
| `emailToCustom` | text | Send to custom email address | — |
| `emailBcc` | text | BCC email address | — |
| `fromEmail` | text | From email address | — |
| `fromName` | text | From name | — |
| `replyToEmail` | text | Reply to email address | — |
| `emailContent` | textarea | Email content | — |
| `emailErrorMessage` | text | Error message | — |
| `htmlEmail` | checkbox | HTML email | — |
| `webhooks` | repeater | Endpoints | — |
| `webhookMaxSize` | number | Max payload size | — |
| `webhookRateLimit` | checkbox | Rate limiting | — |
| `webhookRateLimitRequests` | number | Max requests per hour | — |
| `webhookErrorIgnore` | checkbox | Continue on error | — |
| `webhookErrorMessage` | text | Error message | — |
| `confirmationEmailSubject` | text | Subject | — |
| `confirmationEmailTo` | text | Send to email address | — |
| `confirmationFromEmail` | text | From email address | — |
| `confirmationFromName` | text | From name | — |
| `confirmationReplyToEmail` | text | Reply to email address | — |
| `confirmationEmailContent` | textarea | Email content | — |
| `confirmationEmailHTML` | checkbox | HTML email | — |
| `redirectAdminUrl` | checkbox | Redirect to admin area | — |
| `redirect` | text | Custom redirect URL | — |
| `redirectTimeout` | number | Redirect after (ms) | — |
| `mailchimpDoubleOptIn` | checkbox | Double opt-in | — |
| `mailchimpList` | select | List | — |
| `mailchimpGroups` | select | Groups | — |
| `mailchimpEmail` | select | Field | — |
| `mailchimpFirstName` | select | First name | — |
| `mailchimpLastName` | select | Last name | — |
| `mailchimpPendingMessage` | text | Pending message | — |
| `mailchimpErrorMessage` | text | Error message | — |
| `sendgridList` | select | List | — |
| `sendgridEmail` | select | Field | — |
| `sendgridFirstName` | select | Field | — |
| `sendgridLastName` | select | Field | — |
| `sendgridPendingMessage` | text | Pending message | — |
| `sendgridErrorMessage` | text | Error message | — |
| `loginName` | select | Field | — |
| `loginPassword` | select | Field | — |
| `loginRemember` | select | Field | — |
| `loginErrorMessage` | text | Error message | — |
| `registrationEmail` | select | Field | — |
| `registrationPassword` | select | Field | — |
| `registrationPasswordMinLength` | number | Password min. length | — |
| `registrationUserName` | select | Field | — |
| `registrationFirstName` | select | Field | — |
| `registrationLastName` | select | Field | — |
| `registrationRole` | select | Role | — |
| `registrationAutoLogin` | checkbox | Auto log in user | — |
| `registrationWPNotification` | checkbox | Send WordPress notification | — |
| `lostPasswordEmailUsername` | select | Field | — |
| `resetPasswordNew` | select | Field | — |
| `createPostType` | select | Post type | — |
| `createPostErrorMessage` | text | Error message | — |
| `createPostDisableCapabilityCheck` | checkbox | Disable capability checks | — |
| `createPostTitle` | select | Post title | — |
| `createPostContent` | select | Post content | — |
| `createPostExcerpt` | select | Post excerpt | — |
| `createPostFeaturedImage` | select | Featured image | — |
| `createPostStatus` | select | Post status | — |
| `createPostMeta` | repeater | Post meta | — |
| `createPostTaxonomies` | repeater | Taxonomies | — |
| `updatePostId` | select | Post to update | — |
| `updatePostErrorMessage` | text | Error message | — |
| `updatePostDisableCapabilityCheck` | checkbox | Disable capability checks | — |
| `updatePostTitle` | select | Post title | — |
| `updatePostContent` | select | Post content | — |
| `updatePostExcerpt` | select | Post excerpt | — |
| `updatePostFeaturedImage` | select | Featured image | — |
| `updatePostStatus` | select | Post status | — |
| `updatePostMeta` | repeater | Post meta | — |
| `updatePostTaxonomies` | repeater | Taxonomies | — |
| `enableRecaptcha` | checkbox | reCAPTCHA (Google) | — |
| `enableTurnstile` | checkbox | Turnstile (Cloudflare) | — |
| `turnstileSize` | select | Turnstile:  | — |
| `turnstileTheme` | select | Turnstile:  | — |
| `turnstileLabel` | text | Turnstile:  | — |
| `enableHCaptcha` | select | hCaptcha | — |
| `hCaptchaSize` | select | hCaptcha:  | — |
| `hCaptchaTheme` | select | hCaptcha:  | — |
| `submissionFormName` | text | Form name | — |
| `submissionSaveIp` | checkbox | Save IP address | — |
| `submissionMaxEntries` | number | Max. entries | — |
| `submissionMaxEntriesErrorMessage` | text | Error message | — |
| `submissionDupEntries` | repeater | Compare with | — |
| `submissionDupEntriesErrorMessage` | text | Error message | — |
| `passwordProtectionPassword` | select | Field | — |
| `passwordProtectionErrorMessage` | text | Error message | — |

## Inherited CSS controls

Shared CSS controls available on all elements. Keys are prefixed with `_` and support responsive/pseudo-class variants via colon syntax (e.g. `_typography:tablet_portrait:hover`).

| Key | Type | Label | CSS |
|---|---|---|---|
| `_content` | text | Content | `content` |
| `_margin` | spacing | Margin | `margin` |
| `_padding` | spacing | Padding | `padding` |
| `_width` | number | Width | `width` |
| `_widthMin` | number | Min. width | `min-width` |
| `_widthMax` | number | Max. width | `max-width` |
| `_height` | number | Height | `height` |
| `_heightMin` | number | Min. height | `min-height` |
| `_heightMax` | number | Max. height | `max-height` |
| `_aspectRatio` | text | Aspect ratio | `aspect-ratio` |
| `_position` | select | Position | `position` |
| `_top` | number | Top | `top` |
| `_right` | number | Right | `right` |
| `_bottom` | number | Bottom | `bottom` |
| `_left` | number | Left | `left` |
| `_zIndex` | number | Z-index | `z-index` |
| `_order` | number | Order | `order` |
| `_display` | select | Display | `display`, `align-items` |
| `_visibility` | select | Visibility | `visibility` |
| `_overflow` | text | Overflow | `overflow` |
| `_opacity` | number | Opacity | `opacity` |
| `_cursor` | select | Cursor | `cursor` |
| `_isolation` | select | Isolation | `isolation` |
| `_mixBlendMode` | select | Mix blend mode | `mix-blend-mode` |
| `_pointerEvents` | text | Pointer events | `pointer-events` |
| `_perspective` | number | Perspective | `perspective` |
| `_perspectiveOrigin` | text | Perspective origin | `perspective-origin` |
| `_gridItemJustifySelf` | align-items | Justify self | `justify-self` |
| `_flexDirection` | direction | Direction | `flex-direction` |
| `_alignSelf` | align-items | Align self | `align-self` |
| `_justifyContent` | justify-content | Align main axis | `justify-content` |
| `_alignItems` | align-items | Align cross axis | `align-items` |
| `_gap` | number | Gap | `gap` |
| `_flexGrow` | number | Flex grow | `flex-grow` |
| `_flexShrink` | number | Flex shrink | `flex-shrink` |
| `_flexBasis` | text | Flex basis | `flex-basis` |
| `_useMasonry` | checkbox | %s layout | — |
| `_masonryColumn` | number | Columns | `--columns` |
| `_masonryGutter` | number | Spacing | `--gutter` |
| `_masonryHorizontalOrder` | checkbox | Horizontal order | — |
| `_masonryTransitionDuration` | number | Transition | — |
| `_masonryTransitionMode` | select | Reveal animation | — |
| `_typography` | typography | _typography | `font` |
| `_background` | background | _background | `background` |
| `_shapeDividers` | repeater | Custom shape | — |
| `_gradient` | gradient | _gradient | `background-image` |
| `_border` | border | Border | `border` |
| `_boxShadow` | box-shadow | Box shadow | `box-shadow` |
| `_transform` | transform | Transform | `transform` |
| `_transformOrigin` | text | Transform origin | `transform-origin` |
| `_motionElementParallax` | checkbox | Element parallax | — |
| `_motionElementParallaxSpeedX` | number | Horizontal speed | `--brx-motion-parallax-speed-x` |
| `_motionElementParallaxSpeedY` | number | Vertical speed | `--brx-motion-parallax-speed-y` |
| `_motionBackgroundParallax` | checkbox | Background parallax | — |
| `_motionBackgroundParallaxSpeed` | number | Background speed | `--brx-motion-background-speed` |
| `_motionStartVisiblePercent` | number | Parallax start point | — |
| `_cssCustom` | code | Custom CSS | — |
| `_cssClasses` | text | CSS classes | — |
| `_cssId` | text | CSS ID | — |
| `_cssFilters` | filters | CSS Filters | `filter` |
| `_cssTransition` | text | Transition | `transition` |
| `_attributes` | repeater | Name | — |
| `_scrollSnapType` | select | Type | `scroll-snap-type` on `html`, `scroll-snap-align` on `.brxe-section` |
| `_scrollSnapAlign` | select | Align | `scroll-snap-align` on `.brxe-section` |
| `_scrollSnapStop` | select | Stop | `scroll-snap-stop` on `.brxe-section` |
