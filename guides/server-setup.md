---
layout: default
title: Discord server setup
permalink: /guides/server-setup/
---
# Discord server setup wizard

**For:** Discord server administrators and authorised organisers · **Guide reviewed:** 29 October 2026.

> **Availability:** The expanded automatic/manual wizard illustrated in the supplied **Bracket Control Discord Server Setup Guide** is part of Bracket-App **PR #75**, which was **open and deployed only to staging** when this guide was updated. Do not assume its ticket options or full first-install flow are live on production. The earlier Stage 2 wizard is merged into the application repository but is separately controlled by a release flag. Check the setup screen actually shown in your server.

## Before you begin

1. Open [Bracket Control](https://app.devdylnz.com/app/) and sign in with the Discord account that can administer the server.
2. Use **Your Discord servers** to select the correct community. Connect the existing Bracket Control bot if necessary, using the app's installation flow.
3. Open **Complete server setup** if displayed, or **Server Management → Open Server Setup** when enabled.
4. Check your Discord permissions. The bot requires suitable channel, message, role and voice permissions; its highest role must be above the zero-permission **Bracket Control Registered** role. Setup never grants a support role tournament-administrator privileges.
5. Keep **Global Player Registration** (`#tournament-registration`) separate from **Team Registration** (`#team-registration`). The former records a player's global choice; the latter starts a captain's tournament-specific team application.

## Automatic setup — expanded workflow illustrated in the PDF (PR #75, staging)

The accompanying eight-page administrator PDF shows these **14 steps** with genuine test-server screenshots:

1. Open the production app and sign in (**PDF p. 1**).
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

## Manual setup — expanded workflow (PR #75, staging)

1. Choose **Manual Setup** on the method screen.
2. Create and permission the desired channels/categories yourself inside Discord first.
3. Select the existing safe resources and the existing registered-player role in the wizard. Manual setup does **not** create, rename, move, permission-edit or delete Discord resources.
4. Choose optional publication of global registration, team registration and support ticket panels deliberately. These choices start **off**.
5. Review the exact mapping and consequences, confirm, apply and verify. If interrupted, resume the saved plan rather than starting over.

If Support Tickets are turned off, they should not require an optional support category/channel or panel publication. Existing support resources are preserved rather than deleted by that choice.

## Earlier Stage 2 wizard (when that version is shown)

The version already merged to main uses **Welcome → Channel Configuration → Registered Role → Review Configuration → Apply Configuration → Setup Complete**, and offers **Automatic Setup** or **Custom Setup**. Its smaller set of destinations is not the full PR #75 configuration; do not follow an expanded-wizard screenshot when those controls are absent. See the existing screen for its exact available options.

## After setup

Review **Server Management → Discord Settings (Global)** and your division/tournament overrides, then test registration with an authorised account. Completing setup does not create tournaments, approve teams or constitute a player's individual rules acceptance. The registered role alone is not proof of tournament eligibility.

### Troubleshooting

- **Bot role warning:** Correct the role order in Discord and then resume the saved setup.
- **Rate limit / retry-after:** Observe the exact displayed waiting period. Never clear receipts or create duplicate channels to bypass a cooldown.
- **No setup button:** The server may be complete already, the feature flag may be disabled or your account may lack current organiser rights.
- **Unexpected public staff channel:** Stop and verify staff/private channel permission overwrites before publishing.
- **Missing registration panel:** Confirm which of the two distinct registration messages was explicitly selected for publication.

**Screenshot source:** *Bracket_Control_Discord_Server_Setup_Guide.pdf* (8 pages, supplied by the documentation owner; staging test-server captures). The PDF itself must be distributed separately until its images are published as approved wiki assets.
