---
layout: default
title: Draft-only community setup
permalink: /guides/draft-only-setup/
---
# Draft-only community setup

Every Discord channel is optional. You can run drafts on the website, use another voice service, or configure Discord voice automation.

## Configure only what you use

1. Open **Your Discord servers**, connect your server and open **Complete server setup**.
2. Choose **Manual Setup** to select existing channels, or **Automatic Setup** to create selected resources after review.
3. If using Discord voice automation, select **Draft Voice Waiting Room**. Otherwise choose **Not Required**.
4. Optionally select **Bracket Updates** and **Match Results**. A channel named **#claim-rank** is simply a Match Results destination.
5. Leave team registration, staff approvals and other unused channels on **Not Required**. Leave support tickets disabled unless wanted.
6. Choose categories only if needed. Continue through **Optional messages** and **Support Ticket Configuration**.
7. Review the configuration, confirm the actions and select **Apply Configuration**.

No registered-player role, registration channel, verification button or role rearrangement is needed. Existing resources remain untouched.

## Voice permissions

For draft voice automation, the bot needs access to the waiting room, Connect, Move Members, Manage Channels and View Audit Log. The private captain room can use its existing access-management permissions. These permissions are for voice features, not player registration. Players need access to join the waiting room. Check category restrictions as well as server permissions.

## Run a draft

Create a Draft tournament, choose Standard or Snake draft, select captains and open Live Draft. Gather players in the configured waiting room, or import Player tags and use another voice service. Finish drafting, check the lineups and generate the bracket. Valid completed draft rosters are automatically approved.

Individual Player Acceptance and Global Player Registration are no longer required. Optional tournament rules remain visible; organisers communicate and enforce them. The website legal acknowledgement covers platform documents separately.

Use the existing Teams List publishing settings if you want a roster image. Reserve pools, captain-selected substitute requests, voice rooms, match reporting and results continue normally. See [Draft tournaments]({{ '/guides/drafts/' | relative_url }}).
