---
layout: default
title: Draft tournaments
permalink: /guides/drafts/
---
# Draft tournaments

A draft starts with individual players. Selected captains choose players on the website to form teams, then the organiser generates the bracket.

For a complete Discord walkthrough, use [Draft-only community setup]({{ '/guides/draft-only-setup/' | relative_url }}). It covers **#tournament-registration**, **#bracket-updates**, **#claim-rank** and **Draft Waiting Room**, Manual Setup, the registered-player role and bot permissions.

## 1. Prepare the tournament

1. Create a tournament and check **Captain draft tournament** under **Basics**.
2. Choose **Draft Style**: **Standard (1-for-1)** keeps the same captain order each round; **Snake Draft** reverses it each round. Set the schedule and rules. Decide whether to **Require Individual Player Acceptance** before creating it; this choice and the rules are fixed at creation.
3. Ask every player to complete [Global Player Registration](https://app.devdylnz.com/app/register) using their own Discord account.
4. If using Discord voice, assign **Draft Voice Waiting Room** to the correct voice channel and ask players to join it.
5. Open **Manage Tournament → Live Draft** and check the player pool. Unpicked players gathered from voice are removed from the pool if they leave the waiting room.

Global Player Registration does not enter a draft or accept tournament rules. If individual acceptance is required, share the participation link from **Teams → Participation readiness** and have each player complete **My Participation**. Joining a voice room does not accept rules.

## 2. Confirm captain selection

1. Open **Manage Tournament → Captain Selection**.
2. In **Draft Captain Registry**, use **Add New Captain** to add a server member, then **Save Captain**.
3. Select the captains for this event and select **Confirm Selected Captains**.
4. Check the selected count and team names. Edit names under **Teams** if needed.

The registry can be reused for later tournaments, but captains must be explicitly selected for this one. Admin access and voice presence do not assign captain status. Captain selection locks when drafting starts.

## 3. Run the Live Draft

1. Open **Live Draft** and check there are at least two captain teams and four available starting-player picks per captain.
2. Select **START CAPTAIN DRAFT**.
3. Captains sign in and open their **Team and draft dashboard** from **My Matches**, or their team in **My Teams**.
4. When **YOUR TURN TO PICK** appears, the captain selects the button beside an available player.
5. Follow the **Draft Style** and **Selection order** shown in Live Draft and the captain dashboard. Each captain chooses one player per turn. The first four chosen players join the captain in the starting five.
6. Extra picks are optional substitutes. Players needed to complete other starting lineups are reserved. Use **PASS REMAINING OPTIONAL PICKS** when offered.
7. When drafting finishes, check **Teams**. Valid completed lineups are approved automatically; captains do not need manual approval.

Organisers can supervise and make a pick for a captain from **Live Draft** when necessary. Captains choose through the website.

### Choose the draft style

Only tournament administrators can choose or change **Draft Style**. Choose it under **Basics** when creating a captain draft tournament, or in **Manage Tournament → Live Draft** before selecting **START CAPTAIN DRAFT**. The choice locks as soon as drafting begins.

- **Standard (1-for-1):** each captain picks one player, then the same order repeats. With captains A, B and C: **A → B → C → A → B → C**.
- **Snake Draft:** each captain picks one player, then the order reverses for the next round. With captains A, B and C: **A → B → C → C → B → A**.

Both options work with two or more captains. After everyone has four additional starters, there are up to two optional substitute rounds. The live selection order starts with the current captain and shows the rest of this round and the next. Optional turns may be skipped when no players are available.

Existing tournaments keep their original order and display **Legacy (2 / 1 / 2 / 1)**. An administrator can switch an existing tournament before its draft starts. Ongoing drafts continue in their established order. Editing a recurring series changes future tournaments only.

### Remove an unavailable player

1. Open **Manage Tournament → Live Draft**.
2. In **Live draft player pool**, find the available player and select **Remove**.
3. Confirm the removal. The player disappears from the pool and captains can no longer pick them.

Administrators can remove available players before or during drafting. Captains and players already assigned to teams cannot be removed this way. Removing someone does not change the current captain's turn. If a team still needs starters, add more available players before continuing.

A removed player stays out of the pool even if they remain in the voice waiting room. They can return by leaving and rejoining the configured **Draft Waiting VC**, or an administrator can enter their player tag and select **IMPORT PLAYERS**. Normal voice management continues for everyone else: available voice entrants join automatically and unpicked voice entrants leave the pool when they leave the room.

## 4. Understand automatic voice rooms

With a configured Discord waiting room, Bracket Control creates a private **Draft Captains** room after captain selection and moves selected captains who are connected to the waiting room. Authorised staff can also access that captain room.

At draft completion, it creates temporary team rooms and moves recognised, connected players from the waiting room, and captains from the captain room, where possible. It cannot move disconnected players or pull people from unrelated rooms.

**Team rooms copy the waiting room's permissions. They are not automatically private to each team.** Have a Discord administrator check and adjust access if private team conversations are required. The bot needs **Manage Channels**, **Manage Roles**, **View Audit Log**, **Connect** and **Move Members**, plus access to the waiting room and category.

Rooms are cleaned up when no longer needed, with cleanup deferred where occupants cannot be moved safely. Voice errors do not undo draft picks; check the captain-selection status and bot permissions.

## 5. Publish the Teams List

Choose a **Registered Teams** channel in the tournament's channel settings, or select a destination under **Discord → Team list**. This also works for draft-only communities; no team-registration or staff-approval channel is needed.

With **Image — automatic updates** selected, Bracket Control publishes the Teams List after the draft is complete, its rosters are approved and its team voice rooms are ready. The PNG uses the same layout as other tournaments: team names, captains, five starters and any substitutes. Disconnected players do not prevent publishing once their team rooms are ready.

To publish or refresh it yourself, open **Manage Tournament → Discord → Team list**, check the destination and image format, select **Save this tournament**, then **Publish Teams List**.

Approved roster changes update the same Discord message when automatic updates are enabled. Refreshing manually also updates that message. Changing the destination publishes in the new channel and keeps the old post as history. **Do not publish** and manual-only settings are respected. Unpublished tournaments are not posted, and private drafts require a verified staff-only destination.

## 6. Generate the bracket and play

1. Check the completed lineups and **Participation readiness** under **Teams**. Clear remaining warnings in **Overview**.
2. Check the starting order under **Seed**.
3. In **Overview**, expand **Ready to start? Bracket controls** and select **LOCK ROSTERS & GENERATE BRACKET**. Confirm after checking the teams.
4. Use **Discord → Publish bracket** to post to **#bracket-updates** if wanted.
5. Captains use **My Matches** to **Report Game Victory** with one screenshot or scoresheet per game. The opponent confirms or disputes it.
6. Confirmed results and scoresheets publish to the configured **Match Results** channel, such as **#claim-rank**. Claim Rank is the community's channel name, not another feature.

See [Match results]({{ '/guides/match-results/' | relative_url }}) for screenshots, confirmation and corrections.

## Draft without Discord voice

Discord voice is optional for general setup and drafting. Organisers can use **Live Draft → Player tags → IMPORT PLAYERS** to add a player pool and use another voice service. Imported gaming tags alone do not verify a player's Discord account or complete required individual acceptance. Resolve readiness warnings before starting the bracket.

Without a configured Discord waiting room, automatic Teams List publishing follows draft completion and roster approval. You can still use **Publish Teams List** to refresh it manually.
