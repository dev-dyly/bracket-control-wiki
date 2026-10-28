---
layout: default
title: Discord server setup
permalink: /guides/server-setup/
---
# Discord server setup wizard

**For:** Discord server administrators and authorised organisers · **Guide reviewed:** 29 October 2026.

> **Important:** Available setup options depend on the selected server. Follow the screens shown in your app. The companion screenshots illustrate the complete setup process; optional support-ticket and publishing controls are only relevant when displayed.

## Before you begin

1. Open [Bracket Control](https://app.devdylnz.com/app/) and sign in with the Discord account that can administer the server.
2. Use **Your Discord servers** to select the correct community. Connect the existing Bracket Control bot if necessary, using the app's installation flow.
3. Open **Complete server setup** if displayed, or **Server Management → Open Server Setup** when enabled.
4. Check your Discord permissions. The bot requires suitable channel, message, role and voice permissions; its highest role must be above the zero-permission **Bracket Control Registered** role. Setup never grants a support role tournament-administrator privileges.
5. Keep **Global Player Registration** (`#tournament-registration`) separate from **Team Registration** (`#team-registration`). The former records a player's global choice; the latter starts a captain's tournament-specific team application.

## Automatic setup — illustrated walkthrough

The illustrated setup PDF shows these **14 steps**, with screenshots:

1. Open the Bracket Control app and sign in (**PDF p. 1**).
2. Select **Your Discord servers** (**p. 2**).
3. Open **Complete server setup** for the connected server (**p. 2**).
4. Select **Automatic Setup** (**p. 3**). Preparing choices does not change Discord.
5. Review proposed **channels/categories**, including separate global and team-registration destinations; select **Continue** (**p. 3**).
6. Confirm the registered-player role and choose which **registration messages** should be published; select **Continue** (**p. 4**).
7. If **Support Tickets** are enabled, select a **Support staff role** and check the ticket panel. That role provides ticket access only (**p. 4**).
8. Check optional ticket-panel publication and **transcript retention**; choose **Review Configuration** (**p. 5**).
9. Read the exact resources, roles, private staff access and publication changes; tick the explicit approval checkbox only if correct (**p. 5**).
10. Choose **Apply Configuration** once and do not repeatedly submit during processing (**p. 6**).
11. **Only if prompted**, fix Discord's role hierarchy by moving the bot's role above **Bracket Control Registered** in **Server Settings → Roles** (**p. 6**).
12. If setup was interrupted, return to the existing wizard and tick **I confirm resuming the saved setup plan** (**p. 7**).
13. After correcting the displayed problem or waiting out a Discord rate limit, select **Resume setup**. The saved receipts are used to avoid creating duplicate resources (**p. 7**).
14. **Verify the actual “Discord Server Setup Complete” state** before selecting **Go to Dashboard**; then inspect the resources in Discord (**p. 8**). The PDF's final screenshot depicts progress, *not* confirmed completion.

**Important:** Automatic setup creates or reuses resources **only after** the final reviewed confirmation. Existing compatible channels keep their original locations and permissions. Private approvals must remain inaccessible to ordinary players, regardless of the chosen support role.

## Manual setup

1. Choose **Manual Setup** on the method screen.
2. Create and permission the desired channels/categories yourself inside Discord first.
3. Select the existing safe resources and the existing registered-player role in the wizard. Manual setup does **not** create, rename, move, permission-edit or delete Discord resources.
4. Choose optional publication of global registration, team registration and support ticket panels deliberately. These choices start **off**.
5. Review the exact mapping and consequences, confirm, apply and verify. If interrupted, resume the saved plan rather than starting over.

If Support Tickets are turned off, they should not require an optional support category/channel or panel publication. Existing support resources are preserved rather than deleted by that choice.


## After setup

Review **Server Management → Discord Settings (Global)** and your division/tournament overrides, then test registration with an authorised account. Completing setup does not create tournaments, approve teams or constitute a player's individual rules acceptance. The registered role alone is not proof of tournament eligibility.

### Troubleshooting

- **Bot role warning:** Correct the role order in Discord and then resume the saved setup.
- **Rate limit / retry-after:** Observe the exact displayed waiting period. Never clear receipts or create duplicate channels to bypass a cooldown.
- **No setup button:** Confirm the server is connected and you are signed in with an authorised administrator account.
- **Unexpected public staff channel:** Stop and verify staff/private channel permission overwrites before publishing.
- **Missing registration panel:** Confirm which of the two distinct registration messages was explicitly selected for publication.



## Illustrated walkthrough — 8 pages

**[Download Discord Server Setup PDF]({{ '/assets/guides/server-setup/Bracket_Control_Discord_Server_Setup_Guide.pdf' | relative_url }})** · [All illustrated guides]({{ '/guides/visual-guides/' | relative_url }})

The original guide pages are displayed below so you can follow the screenshots without opening a separate file.

<figure class="illustrated-page" id="illustration-01">
  <img src="{{ '/assets/guides/server-setup/page-01.jpg' | relative_url }}" alt="Discord Server Setup: illustrated page 1 of 8, showing application screenshots and instructions" fetchpriority="high" decoding="async" width="1440">
  <figcaption>Discord Server Setup — illustrated guide page 1 of 8</figcaption>
</figure>

<figure class="illustrated-page" id="illustration-02">
  <img src="{{ '/assets/guides/server-setup/page-02.jpg' | relative_url }}" alt="Discord Server Setup: illustrated page 2 of 8, showing application screenshots and instructions" loading="lazy" decoding="async" width="1440">
  <figcaption>Discord Server Setup — illustrated guide page 2 of 8</figcaption>
</figure>

<figure class="illustrated-page" id="illustration-03">
  <img src="{{ '/assets/guides/server-setup/page-03.jpg' | relative_url }}" alt="Discord Server Setup: illustrated page 3 of 8, showing application screenshots and instructions" loading="lazy" decoding="async" width="1440">
  <figcaption>Discord Server Setup — illustrated guide page 3 of 8</figcaption>
</figure>

<figure class="illustrated-page" id="illustration-04">
  <img src="{{ '/assets/guides/server-setup/page-04.jpg' | relative_url }}" alt="Discord Server Setup: illustrated page 4 of 8, showing application screenshots and instructions" loading="lazy" decoding="async" width="1440">
  <figcaption>Discord Server Setup — illustrated guide page 4 of 8</figcaption>
</figure>

<figure class="illustrated-page" id="illustration-05">
  <img src="{{ '/assets/guides/server-setup/page-05.jpg' | relative_url }}" alt="Discord Server Setup: illustrated page 5 of 8, showing application screenshots and instructions" loading="lazy" decoding="async" width="1440">
  <figcaption>Discord Server Setup — illustrated guide page 5 of 8</figcaption>
</figure>

<figure class="illustrated-page" id="illustration-06">
  <img src="{{ '/assets/guides/server-setup/page-06.jpg' | relative_url }}" alt="Discord Server Setup: illustrated page 6 of 8, showing application screenshots and instructions" loading="lazy" decoding="async" width="1440">
  <figcaption>Discord Server Setup — illustrated guide page 6 of 8</figcaption>
</figure>

<figure class="illustrated-page" id="illustration-07">
  <img src="{{ '/assets/guides/server-setup/page-07.jpg' | relative_url }}" alt="Discord Server Setup: illustrated page 7 of 8, showing application screenshots and instructions" loading="lazy" decoding="async" width="1440">
  <figcaption>Discord Server Setup — illustrated guide page 7 of 8</figcaption>
</figure>

<figure class="illustrated-page" id="illustration-08">
  <img src="{{ '/assets/guides/server-setup/page-08.jpg' | relative_url }}" alt="Discord Server Setup: illustrated page 8 of 8, showing application screenshots and instructions" loading="lazy" decoding="async" width="1440">
  <figcaption>Discord Server Setup — illustrated guide page 8 of 8</figcaption>
</figure>
