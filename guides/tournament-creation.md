---
layout: default
title: Tournament creation
permalink: /guides/tournament-creation/
---
# Create a tournament

Bracket Control displays a simple [website legal acknowledgement]({{ "/guides/legal-acknowledgement/" | relative_url }}). Global Player Registration and Individual Player Acceptance are no longer required. All Discord setup channels are optional. Tournament organisers communicate and enforce their own rules.


## Open the tournament form

1. Sign in with Discord and open **Your Discord servers**.
2. Choose your server and open its **Dashboard**.
3. Select **+ Create tournament**.

Everything is on one form. Fields marked with an asterisk (*) are required. **Custom Discord channels (optional)** and **Advanced match settings (optional)** are closed until you need them.

## Choose the tournament type

Choose **Tournament type** first:

- **Standard Team**: captains register an existing team.
- **Draft**: captains choose players from a shared pool. Choose the **Draft Style**. Standard keeps the same captain order each round; Snake reverses it each round. Existing competitions using the older draft order keep that choice.


1. Enter **Tournament name**.
2. Choose **Bracket format**: single elimination (out after one loss), double elimination (out after two losses) or round robin (every team plays every other team).
3. Set **Maximum approved teams**, from 2 to 16.
4. For Standard Team, choose **Division (optional)** if you group teams by skill. Drafts stay independent of divisions.
5. Check **Repeat this tournament weekly** if you want recurring events. Clear it for a one-time event.

For drafts, see [Draft tournaments]({{ '/guides/drafts/' | relative_url }}) and [Draft-only community setup]({{ '/guides/draft-only-setup/' | relative_url }}). Drafts do not require team-registration or staff-approval channels.

## Set the date and registration period

1. Choose **Tournament timezone**.
2. For a one-time event, set the tournament start. For a weekly competition, choose the day and **Start time**.
3. For normal **Standard Team** tournaments, continue using **Registration Opens** and **Registration Closes** (shown as **Registration opens** and **Close registration (minutes before start)**).
4. For **Draft** tournaments, set **Draft Call Opens**, **Draft Call Locks** and **Tournament Start Time**. Draft Call Opens is when players can start joining the Draft Voice Channel. Draft Call Locks is when the channel closes to new participants so drafting can begin. Opening must be before locking, and locking must be at or before the tournament starts.
5. For weekly Standard Team tournaments, choose **How teams return each week**: **New application every week** or **Prefilled roster; captain must check in**.

Prefilling a lineup does not confirm attendance. Captains still confirm each event they intend to play. New or changed lineups need organiser approval; an unchanged approved lineup can keep approval. Valid draft lineups are approved automatically when the draft completes.

Draft calls use the existing configured Draft Voice Channel. The bot locks it before opening, opens it at the scheduled time, and locks it to new arrivals at the locking time. Connected participants remain in the room. It locks again after tournament completion or cancellation. Weekly calls repeat automatically. Overlapping calls for the same channel are rejected; choose different times. If an earlier tournament is still running, the room stays locked. Existing private-channel restrictions continue to apply.

Organisers can edit an individual call under the tournament settings. Editing recurring defaults applies to future tournaments; check already-created weeks separately. Website-only drafts can still use imported player tags without a voice channel.

## Check the rules and optional settings

1. Optionally enter **Tournament rules**. Organisers communicate and enforce these; individual acceptance is not required.
2. Open **Preview tournament rules** to check the text.
3. If needed, open **Custom Discord channels (optional)**. Empty choices use the division's channels, then server defaults. Pending approvals must use a private staff channel.
4. If needed, open **Advanced match settings (optional)** to choose best-of formats or extra placement games. Only settings for your chosen bracket format are shown.

A best-of-three match needs two game wins; best-of-five needs three. In double elimination, the lower-bracket finalist must win the Grand Final and the reset to become champion. Optional placement games must finish before the tournament is complete.


## Create and prepare the tournament

1. Confirm the tournament configuration.
2. Select **Create tournament**.
3. Open **Manage Tournament** on the event's card.
4. For Standard Team, open **Teams & players** to review the **Approval queue**. For Draft, use **Captain Selection**, then **Live Draft**.
5. Check readiness in **Overview**. Use **Team order** to check the starting order.
6. In **Overview**, expand **Ready to start? Bracket controls** and select **LOCK ROSTERS & GENERATE BRACKET**. Read and confirm the prompt.

Use **Matches & results** to record results or review disputes. Use **Discord & publishing** for bracket images, team lists and announcements. Creating a tournament does not publish every tournament's messages. See [Match results]({{ '/guides/match-results/' | relative_url }}).

## Example screens

These earlier illustrations may show removed acceptance fields. Follow the current instructions above.


![Tournament creation on desktop, with type, schedule, rules and optional settings on one form.]({{ '/assets/guides/admin-experience/creation-1280.png' | relative_url }})

[View the mobile form example]({{ '/assets/guides/admin-experience/creation-390.png' | relative_url }}).

## Cancelling or ending a schedule

**Cancel Tournament** cancels the selected event and stops its reporting and future posts while preserving its history. **End Recurring Tournament Schedule** stops future events in that competition; it does not cancel an event already running. Check the name in each confirmation carefully.

## Illustrated reference

The [original Creating Tournaments PDF]({{ '/assets/guides/tournament-creation/Bracket_Control_Tournament_Creation_User_Guide.pdf' | relative_url }}) remains available. Use this page for current instructions where older screenshots differ.
