---
layout: default
title: Discord Server Setup
permalink: /guides/server-setup/
---
# Discord Server Setup

Connect Bracket Control to your Discord community, then choose only the channels your community will use.

**Global Player Registration is the only mandatory Discord channel for general server setup.** Team registration, team lists, standings, staff approvals, announcements, support tickets and draft voice are optional. You can manage tournaments on the website and use another voice service.

For a community running only drafts with Discord voice, follow [Draft-only community setup]({{ '/guides/draft-only-setup/' | relative_url }}).

## 1. Connect the server

1. Open [Bracket Control](https://app.devdylnz.com/app/) and **Sign in with Discord**.
2. Open **Your Discord servers**. Find the server you manage.
3. If it is not connected, select **Connect server → Invite bot** and add the bot through Discord. If it is already installed, select **Connect installed bot**.
4. Return to Bracket Control. Open **Complete server setup**, or **Server settings → Open Server Setup** for an existing server.

If you cannot connect the bot or manage the server, ask the server owner to check your access. Being a player does not grant organiser permissions.

## 2. Choose your setup method

1. Choose **Automatic Setup** to let Bracket Control prepare missing resources that you select. You review the changes before applying them.
2. Choose **Manual Setup** if you want to create the channels and role yourself in Discord and assign them in the app.

Manual Setup does not create, rename, move or delete channels or categories, create roles, or change existing channel permissions. Use **Refresh Discord inventory** after making changes in Discord.

## 3. Choose channels

| Setting | Use it for |
| --- | --- |
| **Global Player Registration** — required | A one-time registration message, **Verify Registration** and the registered-player role. A common name is **#tournament-registration**. |
| **Team Registration and Management** — optional | Invitations for captains entering ready-made teams. Use a separate channel from Global Player Registration. |
| **Tournament Announcements** — optional | General community tournament announcements. |
| **Registered Teams** — optional | Approved team lists. |
| **Bracket Updates** — optional | Tournament brackets and updates. |
| **Standings** — optional | Tournament standings and the weekly ladder. |
| **Match Results** — optional | Confirmed match results and game scoresheets. Your community may call this **#claim-rank**. |
| **Staff Approvals** — optional | Private staff notifications for team registrations. |
| **Support Ticket Panel** — optional | A message members use to ask for private support, when tickets are enabled. |
| **Draft Voice Waiting Room** — optional | A voice room used to gather draft players and support temporary tournament rooms. |

1. Select an existing channel for **Global Player Registration**, or choose to create one in Automatic Setup.
2. Select any other channels you want to use. Choose **Not Required** for the rest.
3. Keep **Staff Approvals** private if you use it. Existing channels keep their permissions, so check access in Discord yourself.
4. Leave **Enable Support Tickets** unchecked unless wanted. Enabling it requires the panel channel, a private ticket category and support staff settings.
5. Choose categories only where needed. Manual Setup can leave them on **No category assignment**.
6. Select **Continue**.

**Claim Rank is a channel name, not a separate feature.** Assign **#claim-rank** to **Match Results** if that is the name your community prefers.

## 4. Choose the role and registration message

1. For Manual Setup, create **Bracket Control Registered** in Discord with no permissions and put it below the bot's highest role.
2. Select it under **Registered-player role**. Automatic Setup can reuse a safe role or create one if missing.
3. Enable **Publish or update the Global Player Registration message** so members can register and verify in your server.
4. Publish the team-registration message only if you chose to use team registration.
5. Continue through **Support Ticket Configuration**. Leave tickets disabled if you do not want them.

Setup does not assign the registered role to every member. A player uses **Verify Registration** after completing the current Global Player Registration.

## 5. Review and apply

1. Select **Review Configuration**.
2. Under **Review & Confirm**, check the channels, role and selected messages.
3. Check **I approve these exact assignments, resource actions and selected message publications**.
4. Select **Apply Configuration**.
5. Check the selected messages in Discord, then select **Go to Dashboard**.

If setup is interrupted, open **Resume interrupted setup**, confirm the saved plan and select **Resume setup**. Wait for any Discord retry time shown before trying again.

## 6. Check permissions and later changes

The bot needs **View Channels**, **Send Messages**, **Embed Links**, **Attach Files** and **Read Message History** in the selected text channels. It needs **Manage Roles** to assign the registered-player role. For draft voice, also check **Manage Channels**, **View Audit Log**, **Connect** and **Move Members**; see [draft-only setup]({{ '/guides/draft-only-setup/' | relative_url }}).

Use **Open Server Setup** to review global registration settings. Use **Manage Discord Settings** after setup to change tournament channel defaults and check **Channel Preview — Effective Channels**. A tournament can choose different channels, so check its own **Settings** and **Discord** tab if posts go somewhere unexpected.

## Player registration and tournament entry are separate

Each person registers with their own account through [Global Player Registration](https://app.devdylnz.com/app/register). That registration covers the current platform documents across participating communities; updated documents may require another review. It does not enter a tournament or accept that tournament's rules.

Ready-made teams still need a captain's entry. Drafts still need player selection. If **Require Individual Player Acceptance** is selected when creating a tournament, every captain, starter and substitute completes their own tournament-rules decision through **My Participation**.

## Illustrated reference

The [original Discord Server Setup PDF]({{ '/assets/guides/server-setup/Bracket_Control_Discord_Server_Setup_Guide.pdf' | relative_url }}) is still available. Its screenshots may show an earlier setup screen. Use this page for current channel requirements and button instructions.
