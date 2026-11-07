---
layout: default
title: Server Audit Log
description: "How Discord Server Owners and Administrators access and filter the read-only Bracket Control Server Audit Log for tournaments, teams, drafts and match changes."
permalink: /guides/audit-log/
---
# Server Audit Log

The Server Audit Log gives your Discord server's Owner and Administrators a clear, read-only history of important changes made in Bracket Control.

## Who can access it

Only:

- the **Discord Server Owner**, and
- Discord members who have the **Administrator** permission in that server.

Tournament organisers, captains, players, support staff, members who only have "Manage Server", and Bracket Control staff do not get access automatically. Each server's log belongs to that server alone. If your permissions cannot be verified with Discord, the log is not shown.

Open **Server Management → Audit Log**. The menu item is hidden from everyone else.

## What is recorded

Important actions taken by anyone participating in or running your tournaments:

- **Tournaments** – created, edited, settings or schedule changed, started, completed, cancelled, archived, deleted or reset; registrations opened or closed.
- **Teams** – registered, withdrawn, approved or rejected, roster changes, captain changes, division changes, promotions and demotions, teams removed.
- **Player participation** – registering for or withdrawing from a tournament or draft, substitute requests, approvals and confirmations.
- **Draft tournaments** – draft started, player picks and passes, draft pool changes, draft order shuffled, draft settings or captains changed.
- **Matches** – results submitted, approved, rejected, corrected or overridden, scores updated by an organiser.
- **Server configuration** – server setup, Discord channels, divisions, announcement and notification settings, and administration roles.
- **Automatic actions** – shown as **Bracket Control (System)**, including automatic division promotions, bracket advancement, tournament completion and weekly rollover.

Only completed changes are added. An action that failed or was cancelled is not recorded as completed.

## Why spectators and browsing are excluded

Spectators and public visitors are never recorded. Bracket Control also does not record viewing brackets, standings or results, opening dashboards, moving between pages, searching, filtering, refreshing pages, Discord chat messages or routine background checks that change nothing.

Being a registered player, captain or administrator does not mean every click is tracked. Recording only real changes keeps the log focused on what happened to your tournament, and avoids tracking people who are simply looking at schedules or scores.

## Reading the log and using filters

Entries appear newest first, using your local date and time:

| Date & Time | User | Action | Details |
|---|---|---|---|
| 07 Nov 2026, 10:30 AM | @Admin | Tournament Created | Weekly Tournament |
| 07 Nov 2026, 10:35 AM | @Captain | Roster Changed | Team Alpha |
| 07 Nov 2026, 10:40 AM | @Player | Draft Registration | Friday Draft |
| 07 Nov 2026, 10:45 AM | Bracket Control (System) | Team Promoted | Division 2 → Division 1 |

You can narrow the list at the top of the page:

1. **From** and **To** – pick a start or end date (both days are included).
2. **User** – enter part of a display name or a Discord ID.
3. **Action** – choose a group (such as all draft actions) or one specific action.
4. Select **Apply filters**, or **Clear** to see everything again. Use **Previous** and **Next** at the bottom to move through pages.

Entries are read-only. Nobody, including the Server Owner, can edit or delete individual entries through Bracket Control.
