---
layout: default
title: Organiser guide
permalink: /guides/organisers/
---
# Organiser guide

## 1. Configure the community

In **Your Discord servers**, choose **Server settings**. Review timezone and organiser roles. In **Server Management → Discord Settings (Global)**, choose registration, approval, teams, bracket, results, standings and draft voice channels. Check the bot has channel access and the necessary voice-management permissions. Tournament-specific channels can override global defaults.

## 2. Create an event

Go to **Dashboard** and create a standalone or recurring series/event. For the selected occurrence, open **Manage Tournament**. Its tabs are **Overview, Teams, Matches, Seed, Discord, Settings**, plus **Captain Selection** and **Live Draft** for draft events. In **Settings**, choose registration dates, team cap (2–16), bracket type (single/double/round robin), BO1/BO3/BO5 phase rules, public visibility, optional placement tiebreaks and channel overrides. Open registration when appropriate.

## 3. Manage entries and confirm readiness

In **Teams**, review applications, prior-week roster changes, approved snapshots, captain verification, recurring enrollment, division conflicts, weekly attendance and notifications. Approve new or revised lineups when required. An unchanged approved recurring roster can carry its approval forward, **but its captain must explicitly confirm attendance every week**. If readiness identifies ineligible entrants, resolve those reasons before seeding and generating a bracket. Registration closing alone does not start a bracket.

## 4. Run and complete

Use **Seed** to set eligible team placement, then generate when ready. In **Matches**, review **one-file per-game victory reports**, opposing confirmations, disputes, optional evidence and audited corrections. Older legacy match reports still use two files; use logged correction controls when necessary. Double elimination supports the original grand-final reset, and optional placement games can delay event completion.

## 5. Discord and divisions

Use **Discord** (or **Edit Discord**) for an individual event's Bracket, Teams and Announcement content. Set **Do not publish / Automatic PNG / Manual PNG / Custom Embed / Plain Message** as supported. Preview target channel and content. At the current `main` baseline, automatic team/bracket images can be opt-in per occurrence. Restoration of automatic defaults is **open PR #42 (not deployed)**. Confirm the actual settings, channel and PNG text before public use. In **Server Management → Announcements**, manage server notices and post-event recap templates; in **Divisions**, configure qualifying series, promotion/relegation and administrative overrides.

**Security release note (20 October 2026):** The approved-only public roster and evidence-hardening changes are still in open PRs #27/#28; the automatic image/recap changes are in open PR #42. Verify that your running deployment includes them before public roster publication. See [complete user guide]({{ '/guides/user-guide/' | relative_url }}).

**Recurring Option B:** A valid current approved roster and verified captain can establish series-specific membership. Old bulk activation and the two-completed-week requirement are retired. Carry-over prepares next occurrence, but every captain still explicitly confirms attendance; manual policy requires a fresh application.

**Completion recap:** The official announcement is manually reviewed and posted through Server Management → Announcements. PR #42 plans a private staff reminder and an in-app action, not an automatic public winner announcement.
