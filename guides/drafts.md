---
layout: default
title: Draft tournaments
permalink: /guides/drafts/
---
# Draft tournaments

Bracket Control displays a simple [website legal acknowledgement]({{ "/guides/legal-acknowledgement/" | relative_url }}). Global Player Registration and Individual Player Acceptance are no longer required. All Discord setup channels are optional. Tournament organisers communicate and enforce their own rules.

A draft starts with individual players. Selected captains choose players on the website to form teams, then the organiser generates the bracket.


## 1. Prepare the tournament

Create a Draft tournament, choose Standard or Snake draft and set the schedule. Rules are optional information. Configure a waiting room only if you use Discord voice; otherwise import Player tags and use your chosen voice service.

1. Create a tournament and choose **Draft** under **Tournament type**.
2. Set **Draft Call Opens**, **Draft Call Locks** and **Tournament Start Time**. Opening must be before locking, and locking must be at or before the tournament starts.
3. If using Discord voice, use your existing configured **Draft Voice Waiting Room**. Players join between the opening and locking times; there is no need to create another channel.
3. Open **Manage Tournament → Live Draft** and check the player pool. Unpicked players gathered from voice are removed from the pool if they leave the waiting room.


### Automatic call access

**Draft Call Opens:** When players can start joining the Draft Voice Channel.

**Draft Call Locks:** When the channel closes to new participants so drafting can begin.

The bot keeps the configured room locked before the call, opens it at the scheduled time and locks it at the scheduled locking time. People already connected remain connected. Existing private-channel restrictions still apply; opening does not invite unrelated server members. Administrators retain their Discord access.

The room locks again when the tournament finishes or is cancelled, and remains locked until the next valid call. Weekly drafts repeat automatically. Choose different call times for drafts sharing a channel. If an earlier tournament is still running, the room stays locked. After a bot restart, access catches up to the current schedule.

An organiser can update a call in the tournament settings before drafting starts. Missing channels or missing bot permissions need administrator attention; check the configured room and the bot’s permission to manage channel permissions.

Normal tournaments keep **Registration Opens**, **Registration Closes** and their existing team-registration process.

## 2. Confirm captain selection

1. Open **Manage Tournament → Captain Selection**.
2. In **Draft Captain Registry**, use **Add New Captain** to add a server member, then **Save Captain**.
3. Select the captains for this event and select **Confirm Selected Captains**.
4. Check the selected count and team names. Edit names under **Teams & players** if needed.

The registry can be reused for later tournaments, but captains must be explicitly selected for this one. Admin access and voice presence do not assign captain status. Captain selection locks when drafting starts.

## 3. Run the Live Draft

1. Open **Live Draft** and check there are at least two captain teams and four available starting-player picks per captain.
2. Select **START CAPTAIN DRAFT**.
3. Captains sign in, open **Captain Dashboard** and choose their tournament.
4. When **Your turn to pick** appears, the captain selects the button beside an available player.
5. Follow the **Draft Style** and **Selection order** shown in Live Draft and the captain dashboard. Each captain chooses one player per turn. The first four chosen players join the captain in the starting five.
6. Extra picks are optional substitutes. Players needed to complete other starting lineups are reserved. Use **Pass optional picks** when offered.
7. When drafting finishes, check **Teams & players**. Valid completed lineups are approved automatically; captains do not need manual approval.

Organisers can supervise and make a pick for a captain from **Live Draft** when necessary. Captains choose through the website.

### Choose the draft style

Only tournament administrators can choose or change **Draft Style**. Choose it under **Tournament details** when creating a captain draft tournament, or in **Manage Tournament → Live Draft** before selecting **START CAPTAIN DRAFT**. The choice locks as soon as drafting begins.

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

Choose a **Registered Teams** channel in the tournament's channel settings, or select a destination under **Discord & publishing → Team list**. This also works for draft-only communities; no team-registration or staff-approval channel is needed.

With **Image — automatic updates** selected, Bracket Control publishes the Teams List after the draft is complete, its rosters are approved and its team voice rooms are ready. The PNG uses the same layout as other tournaments: team names, captains, five starters and any substitutes. Disconnected players do not prevent publishing once their team rooms are ready.

To publish or refresh it yourself, open **Manage Tournament → Discord → Team list**, check the destination and image format, select **Save this tournament**, then **Publish Teams List**.

Approved roster changes update the same Discord message when automatic updates are enabled. Refreshing manually also updates that message. Changing the destination publishes in the new channel and keeps the old post as history. **Do not publish** and manual-only settings are respected. Unpublished tournaments are not posted, and private drafts require a verified staff-only destination.

## 6. Generate the bracket and play

1. Check the completed lineups under **Teams & players**. Clear remaining warnings in **Overview**.
2. Check the starting order under **Team order**.
3. In **Overview**, expand **Ready to start? Bracket controls** and select **LOCK ROSTERS & GENERATE BRACKET**. Confirm after checking the teams.
4. Use **Discord & publishing → Publish bracket** to post to **#bracket-updates** if wanted.
5. Captains use **Captain Dashboard** to **Report Win** with one screenshot or scoresheet per game. The opponent confirms or disputes it.
6. Confirmed results and scoresheets publish to the configured **Match Results** channel, such as **#claim-rank**. Claim Rank is the community's channel name, not another feature.

See [Match results]({{ '/guides/match-results/' | relative_url }}) for screenshots, confirmation and corrections.

## Draft without Discord voice

Discord voice is optional for general setup and drafting. Organisers can use **Live Draft → Player tags → IMPORT PLAYERS** to add a player pool and use another voice service. Imported gaming tags alone do not verify a player's Discord account. Resolve readiness warnings before starting the bracket.

Without a configured Discord waiting room, automatic Teams List publishing follows draft completion and roster approval. You can still use **Publish Teams List** to refresh it manually.

## Reserve Player Pool and substitute requests

When drafting finishes, undrafted players automatically form that tournament's **Reserve Player Pool**. This works with Standard, Snake and existing Legacy drafts. Players are not automatically assigned to teams. Optional substitutes already drafted onto a team stay on that team.

Open **Manage Tournament → Teams & players → Reserve Player Pool** to see available reserves and requests. Captains choose the player they want through **Request Substitute** in their existing dashboard. A selected reserve is held for that request; one team cannot take a player reserved by another team.

1. Open a substitute request from **Needs Attention**, or find it under **Teams & players**.
2. Review the outgoing player and the captain's chosen reserve. Select **Approve request** or **Reject request**.
3. Ask the reserve player to open **Substitute invitations** using their own Discord account and confirm the invitation. No separate legal or tournament-rules acceptance is required.
4. Approval and confirmation complete the change when all checks pass. If the request is still waiting after a match ends, select **Finish replacement** to check again.
5. Check the updated team roster. The existing Teams List publication refreshes according to its publishing settings, and configured team voice management uses the updated roster. Manual publishing stays manual; no extra Discord channel is needed.

The designated captain cannot be replaced through this process. Finish the team's active match, scoresheet upload, reported result or dispute first. Roster limits, server membership and player eligibility are checked again before the lineup changes. Previous rosters, matches, results and acceptance records are kept.

Rejection, captain cancellation or the reserve player's decline releases the reservation. The team keeps its current lineup. A player who completes a replacement leaves the available reserve pool; the outgoing player is not automatically added to it. Cancelling the tournament cancels unfinished requests.

Requests also appear in the existing private staff approval message when a staff notification channel is configured. No new channel or setup step is required.
