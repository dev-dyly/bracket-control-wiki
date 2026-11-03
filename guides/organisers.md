---
layout: default
title: Organiser guide
permalink: /guides/organisers/
---
# Organiser guide

Use this checklist to prepare and run tournaments for your Discord community.

## 1. Set up the server

1. Sign in with Discord and open **Your Discord servers**.
2. Connect the server if needed, then open **Complete server setup** or **Server settings → Open Server Setup**.
3. Choose **Automatic Setup** or **Manual Setup**.
4. Assign **Global Player Registration**, the only mandatory Discord channel for general setup.
5. Select other destinations only for the features you want; use **Not Required** for the rest. Keep **Enable Support Tickets** off unless wanted.
6. Select the **Bracket Control Registered** role, with no permissions and below the bot's role. Manual Setup requires you to create it in Discord.
7. Enable **Publish or update the Global Player Registration message**.
8. Select **Review Configuration**, check the plan, complete the approval checkbox and select **Apply Configuration**.

Follow [Discord Server Setup]({{ '/guides/server-setup/' | relative_url }}). Communities running only drafts can follow [Draft-only community setup]({{ '/guides/draft-only-setup/' | relative_url }}): **#tournament-registration** for Global Player Registration, **#bracket-updates** for Bracket Updates, **#claim-rank** for Match Results and **Draft Waiting Room** for Draft Voice Waiting Room.

Claim Rank is a preferred Discord channel name, not another feature. A draft community does not need team-registration, standings or staff-approval channels unless it chooses those features.

## 2. Explain registration to players

1. Direct all players to the Global Player Registration message, commonly in **#tournament-registration**.
2. Ask them to sign in individually, read the three platform documents and select **Accept Registration** after completing the choices.
3. Ask them to use **Verify Registration** in your server.
4. Explain how to enter your actual tournament: a captain's team entry or the draft player pool.
5. If you require individual acceptance, share **Teams & players → Participation readiness → Copy Participation Link** and ask each captain, starter and substitute to complete **My Participation**.

Global registration covers the current platform documents across participating communities. It does not enter a tournament, confirm attendance, approve a lineup or accept tournament rules. Captains cannot personally accept rules for teammates.

## Find what needs attention

The dashboard shows **Active tournaments** and **Upcoming tournaments** for the selected Discord server. **Needs Attention** lists pending team registrations, substitute requests, match disputes and other outstanding actions. Select **Review registration**, **Review match** or **Review action** to open the existing screen for that item. If more than five actions are waiting, select the link to view all actions. A loading error does not mean the queue is empty; select **Try again**.

![Example community dashboard with a pending registration and a direct review button.]({{ '/assets/guides/admin-experience/dashboard-1280.png' | relative_url }})

[View the mobile dashboard example]({{ '/assets/guides/admin-experience/dashboard-390.png' | relative_url }}). The examples use fictional teams.

## 3. Create the tournament

1. Open **Dashboard → + Create tournament**.
2. Choose **Tournament type**: **Standard Team** or **Draft**. Enter the name, bracket format, capacity and optional division or draft style.
3. Set **Date and registration**, and decide whether the event repeats weekly.
4. Enter **Tournament rules** and decide whether to **Require Individual Player Acceptance**, when available.
5. Open optional Discord or match settings only if you need them.
6. Check the form, complete the confirmation and select **Create tournament**.

Rules and individual acceptance are fixed at creation. Cancel and create a replacement if they need to change. See [Tournament creation]({{ '/guides/tournament-creation/' | relative_url }}).

## 4. Prepare teams or run a draft

For ready-made teams:

1. Open **Manage Tournament → Teams & players → Approval queue**.
2. Review captains, players and lineup changes, then **Approve** or **Reject**.
3. Check attendance and **Participation readiness** separately. Regular weekly entries still need **Confirm participation** even when an unchanged lineup retains approval.

For drafts:

1. Gather registered players in the configured waiting room, or import a player pool under **Live Draft**.
2. Use **Captain Selection → Draft Captain Registry** to add and select captains, then **Confirm Selected Captains**.
3. Open **Live Draft** and select **START CAPTAIN DRAFT** when the captains and player pool are ready.
4. Captains pick through their own signed-in team dashboards. Completed valid lineups are approved automatically.
5. Check remaining participation requirements before generating the bracket.

With Discord voice configured, the bot creates a private captain room and, after the draft, temporary team rooms. Team rooms inherit the waiting room's permissions; check their access if private team conversations are required. See [Draft tournaments]({{ '/guides/drafts/' | relative_url }}) for bot permissions, player moves and cleanup.

After a draft, **Teams & players → Reserve Player Pool** shows undrafted players and captain-selected substitute requests. Review requests from **Needs Attention** or this panel. Approve or reject the selected player; the reserve must personally confirm and complete any applicable registration and rules. Changes complete only after safety checks pass between matches. See [Reserve Player Pool and substitute requests]({{ '/guides/drafts/#reserve-player-pool-and-substitute-requests' | relative_url }}) for the full steps.

## 5. Manage ongoing teams

1. Open **Server Management → Team Management** to review ongoing teams and captain transfer requests.
2. A replacement captain must first sign in and accept their invitation. Review the accepted request, give the required reason and select **Approve transfer** or **Reject transfer**.
3. Review affected lineups again after an approved handover. Captain ownership and attendance are separate.
4. For division membership, use **Server Management → Divisions**. Review any resulting warnings on upcoming entries.

Captains can use **Transfer Captaincy** or **Retire Team** in **My Teams**. Retirement preserves earlier results but stops future participation. See the [Captain guide]({{ '/guides/captains/' | relative_url }}).

## 6. Start matches and review results

1. Check **Overview**, **Teams & players** and **Participation readiness**.
2. Use **Team order** to check the starting order.
3. In **Overview**, expand **Ready to start? Bracket controls** and select **LOCK ROSTERS & GENERATE BRACKET**.
4. Follow games under **Matches & results**. Winning captains submit one scoresheet per game; opponents confirm or dispute.
5. Review disputes and use the organiser's correction controls if a confirmed result is wrong. Check the effect on later matches before confirming a correction.

See [Match results]({{ '/guides/match-results/' | relative_url }}). Confirmed scoresheets published to a results channel are visible to everyone who can access that channel.

## 7. Publish updates

1. Open the tournament's **Discord & publishing** tab.
2. Choose **Publish bracket**, **Team list** or **Custom announcement**.
3. Choose the destination and format, then **Save this tournament**.
4. Use **Publish Teams List** for a manual team-list post or refresh; other messages use **Send now to Discord**. Choose **Image — automatic updates** for automatic bracket or approved-roster updates.
5. Use **Match results** for result-delivery actions. **Final standings** and **Weekly ladder** are available after completion.

Publishing applies to the selected tournament. Check its destination rather than assuming server defaults always apply.

Draft tournaments use the same Teams List PNG, showing team names, captains, five starters and substitutes. With automatic images enabled, the first post follows draft completion, roster approval and its team voice rooms being ready. Later approved roster changes update the existing message. See [Draft tournaments]({{ '/guides/drafts/' | relative_url }}) for setup and refresh steps.

For optional skill groups, see [Divisions]({{ '/guides/divisions/' | relative_url }}). For cancellation, history and other tasks, see the [Complete user guide]({{ '/guides/user-guide/' | relative_url }}) or [Troubleshooting]({{ '/troubleshooting/' | relative_url }}).
