---
layout: default
title: Discord Server Setup
description: "Connect your Discord server to Bracket Control and use Automatic or Manual Setup to configure optional channels for teams, brackets, drafts and match results."
permalink: /guides/server-setup/
---
# Discord Server Setup

Connect your server, then configure only the features your community uses. **Every Discord channel is optional.** No registration role, player-registration channel or verification message is needed.

## Connect and choose a method

1. Sign in with Discord and open **Your Discord servers**.
2. Connect the server you manage and invite the bot if needed. Server owner or administrator access is required.
3. Open **Complete server setup**, or **Server settings → Open Server Setup**.
4. Choose **Automatic Setup** to create selected resources after review, or **Manual Setup** to select resources you have already created in Discord.

Manual Setup keeps existing channel names, locations and permissions. Use **Refresh Discord inventory** after making changes in Discord.

## Choose optional channels

| Setting | Purpose |
| --- | --- |
| Team Registration and Management | Captains enter ready-made teams and manage their teams. |
| Tournament Announcements | General tournament announcements. |
| Registered Teams | Approved team lists. |
| Bracket Updates | Bracket images and updates. |
| Standings | Rankings and weekly ladders. |
| Match Results | Results and scoresheets. A channel named #claim-rank can be used here. |
| Staff Approvals | Private staff notifications for team applications. |
| Support Ticket Panel | Entry point for private support tickets. |
| Draft Voice Waiting Room | Optional waiting room for draft voice automation. |

Choose **Not Required** for unused features. Website-only organisers can leave every channel unused. Draft-only communities can configure a waiting room without team-registration or staff-approval channels. Standard tournament communities can choose team registration, announcements and results as needed.

Keep Staff Approvals private. If you enable support tickets, select its panel channel, private category and support staff settings. Choose categories only where needed. Existing configured channels and support settings remain available.

## Review and finish

1. Continue to **Optional messages** and choose whether to publish the team-registration message.
2. Review **Support Ticket Configuration**; leave tickets disabled if unused.
3. Select **Review Configuration** and check the proposed actions.
4. Check the confirmation, then select **Apply Configuration**.
5. Select **Go to Dashboard** when setup completes.

If setup was interrupted before simplification, review a new plan. Existing roles, channels and messages are not automatically deleted. For a current interrupted plan, confirm **Resume setup** after any displayed Discord wait.

The bot needs permissions only for features you use: text publishing needs channel access, sending messages, embeds, attachments and message history. Creating channels needs Manage Channels and View Audit Log. Draft voice also needs Connect and Move Members. Support ticket privacy checks remain in place.

## Players and rules

Bracket Control displays a compact [website legal acknowledgement]({{ '/guides/legal-acknowledgement/' | relative_url }}). Discord Global Player Registration roles and channels are no longer required. Individual Player Acceptance is no longer required. Organisers communicate and enforce their own community and tournament rules.

Team registration, approvals, captain dashboards, drafting, substitutes, brackets, reporting, publishing and support continue normally.

## Illustrated references and downloads

These earlier illustrations remain available. Some show retired registration or acceptance screens; follow the current guidance above.

The [original Discord Server Setup PDF]({{ '/assets/guides/server-setup/Bracket_Control_Discord_Server_Setup_Guide.pdf' | relative_url }}) is still available. Its screenshots may show an earlier setup screen. Use this page for current channel requirements and button instructions.
