---
layout: default
title: Complete user guide
permalink: /guides/user-guide/
---
# Bracket Control — Complete user guide

Use Bracket Control to organise tournaments for your Discord community, captain a team, take part in a draft and follow results. Options depend on your role and the tournament you select.

## 1. Sign in and find your community

1. Open [Bracket Control](https://app.devdylnz.com/app/) and select **Sign in with Discord**.
2. Use the Discord account you use in your community.
3. Open **Your Discord servers**, choose your community and open its dashboard or tournament link.
4. Captains use **My Teams** and **Captain Dashboard**. Organisers open **Manage Tournament** on the correct event.
5. On a phone, open **Navigation** to find the menu. Personal options such as **My Participation**, **Player Registration**, **My Support Tickets** and **Privacy Settings** are in **Profile**.

**Browse Tournaments** opens public links shared by organisers. It does not provide a directory of every community or private tournament.

| Page | What you do there |
| --- | --- |
| **Dashboard** | Choose, create and manage your server's tournaments. |
| **My Teams** | Review captain-owned teams, lineups and upcoming participation. |
| **Captain Dashboard** | Report victories and confirm or dispute opponents' game reports. |
| **My Participation** | Personally accept required tournament rules. |
| **Server Management** | Manage server settings, optional divisions and Discord destinations. |
| **Bracket** | Follow matches and advancement. |
| **Ladder / Standings** | View tournament rankings. |
| **Match Results** | View confirmed match scores and game history. |

## 2. Complete Global Player Registration

1. Open your server's registration message, commonly in **#tournament-registration**, or [Global Player Registration](https://app.devdylnz.com/app/register).
2. Sign in with your own Discord account.
3. Read the **Terms of Service**, **Privacy Policy** and **Player Information Notice**.
4. Complete the three acceptance and acknowledgement choices and select **Accept Registration** if you agree.
5. Use **Verify Registration** on the server's Discord registration message to confirm your current registration and receive its registered-player role.

Registration covers the current platform documents across participating Bracket Control communities. Updated documents can require renewed review.

**Registration does not enter a tournament, register a team, confirm attendance or accept a tournament's rules.** A captain cannot make another player's personal decisions. If **Require Individual Player Acceptance** is enabled for a tournament, every captain, starter and substitute opens **My Participation**, reviews the displayed rules, checks the statement and selects **ACCEPT TOURNAMENT RULES**.

## 3. Organisers: set up Discord

1. Connect your server through **Your Discord servers → Connect server → Invite bot**, then complete the connection.
2. Open **Complete server setup**, or **Server settings → Open Server Setup**.
3. Choose **Automatic Setup** or **Manual Setup**.
4. Assign **Global Player Registration**. This is the **only mandatory Discord channel for general setup**.
5. Choose channels for the features you want. Set all unnecessary destinations to **Not Required**. Team registration, standings, staff approvals and draft voice are optional.
6. For Manual Setup, create **Bracket Control Registered** yourself, with no permissions, below the bot's highest role.
7. Select the role and **Publish or update the Global Player Registration message**.
8. Leave **Enable Support Tickets** off unless wanted.
9. Select **Review Configuration**, check the choices, complete the approval checkbox and select **Apply Configuration**.

Manual Setup uses existing Discord resources and does not change their permissions or locations. Check bot and member access in Discord.

For a draft community using Discord voice, create and assign:

| Channel | Setting |
| --- | --- |
| **#tournament-registration** | **Global Player Registration** |
| **#bracket-updates** | **Bracket Updates** |
| **#claim-rank** | **Match Results** |
| **Draft Waiting Room** — voice | **Draft Voice Waiting Room** |

**Claim Rank is the community's channel name for Match Results, not a separate feature.** This four-channel plan is a chosen draft workflow, not a requirement for every community.

Follow [Discord Server Setup]({{ '/guides/server-setup/' | relative_url }}) or the full [Draft-only community setup]({{ '/guides/draft-only-setup/' | relative_url }}) guide.

## 4. Organisers: create a tournament

1. Open **Dashboard → + Create tournament**.
2. Choose **Tournament type**: **Standard Team** or **Draft**. Enter the name, bracket format and maximum teams, from 2 to 16. Choose an optional division or the draft style shown for drafts.
3. Decide whether to **Require Individual Player Acceptance** and **Repeat this tournament weekly**.
4. Set **Date and registration**, then enter **Tournament rules**.
5. Open **Custom Discord channels (optional)** or **Advanced match settings (optional)** only when needed.
6. Check the form, complete the displayed confirmation and select **Create tournament**. There are no separate creation steps.

Rules and individual acceptance are fixed at creation. To change them, cancel and create a replacement tournament or recurring competition.

For details, see [Tournament creation]({{ '/guides/tournament-creation/' | relative_url }}).

## 5. Captains: enter a ready-made team

1. Open the team-registration invitation from your organiser. A team-registration Discord channel is needed only if the community chooses to use it.
2. Sign in as the captain and choose **Create a new team** or **Update current team**.
3. Enter the team name and five starters, including yourself, plus up to two optional substitutes.
4. Select the correct Discord account for each teammate and check their gaming name.
5. Review the published rules and captain declaration. Share the required documents with teammates.
6. Complete the declaration truthfully and select **Register Team**.
7. Check the entry status. New or changed lineups need organiser approval.

The captain's declaration does not register teammates globally or personally accept their tournament rules. Draft teams use the draft process instead.

For regular weekly competitions, **Prefilled roster; captain must check in** can carry a lineup forward. Captains must still select **Confirm participation** for each event they intend to play. An unchanged approved lineup can retain approval; changing players requires a review. **Withdraw from this tournament** skips one event. **LEAVE RECURRING COMPETITION** stops future entries.

See [Team registration]({{ '/guides/team-registration/' | relative_url }}) and [Captain guide]({{ '/guides/captains/' | relative_url }}).

### Hand over or retire a team

1. In **My Teams**, select **Transfer Captaincy**, choose an existing teammate and select **Invite replacement captain**.
2. The replacement selects **Accept captaincy** with their own account. An organiser reviews it under **Server Management → Team Management** and selects **Approve transfer** before ownership changes.
3. Review affected lineups again after a transfer; attendance stays separate.
4. If the team is ending, use **Retire Team**, read the effects, type the team name and select **Confirm retirement**. Retirement preserves history and stops future participation; running events or staff restrictions may block it.

See [Captain guide]({{ '/guides/captains/' | relative_url }}) for details.

## 6. Organisers: review ready-made teams

1. Select **Review registration** in the dashboard's **Needs Attention** section, or open **Manage Tournament → Teams & players → Approval queue**.
2. Check the captain, starters, substitutes and any lineup changes.
3. Select **Approve** or **Reject**, giving a reason where needed.
4. Check attendance, division issues and **Participation readiness** separately.
5. Return to **Overview** and resolve the remaining warnings.

Roster approval alone does not confirm attendance or complete personal rules acceptance. Draft captains require no manual approval; valid draft lineups are approved automatically at draft completion.

See [Approving team registrations]({{ '/guides/team-approvals/' | relative_url }}).

## 7. Run a draft

1. Create a tournament with **Draft** selected under **Tournament type**.
2. Ask players to complete Global Player Registration. Gather them in the configured **Draft Waiting Room** if using Discord voice.
3. Open **Captain Selection → Draft Captain Registry**, add captains as needed and select **Confirm Selected Captains**.
4. With Discord voice configured, Bracket Control creates a private **Draft Captains** room and moves selected captains who are in the waiting room.
5. Check the player pool under **Live Draft**, then select **START CAPTAIN DRAFT** when enough players are ready.
6. Captains use their **Captain Dashboard**. At **Your turn to pick**, they select a player on the website.
7. Follow the displayed Standard or Snake turns. Older tournaments keep their original 2/1/2/1 stages. The first four picks complete each captain's starting five. Optional picks can supply up to two substitutes; captains can pass when offered.
8. At completion, valid lineups are automatically approved. Check any remaining individual-acceptance requirements before generating the bracket.

Temporary team rooms are created at completion. Connected, recognised players can move from the waiting room and captains from the captain room. **Team rooms copy the waiting room's permissions; they are not automatically private to each team.** Ask a Discord administrator to review team-room access if privacy is required.

The bot needs **Manage Channels**, **Manage Roles**, **View Audit Log**, **Connect** and **Move Members**, plus access to the channels and category. Temporary rooms are cleaned up when safe.

Discord voice is optional: organisers can import **Player tags** under **Live Draft** and use another voice service. Imported tags do not by themselves verify Discord accounts or complete individual acceptance.

See [Draft tournaments]({{ '/guides/drafts/' | relative_url }}) and [Draft-only community setup]({{ '/guides/draft-only-setup/' | relative_url }}).

## 8. Generate the bracket

1. Check **Teams & players**, **Participation readiness** and **Overview**.
2. Use **Team order** to check the starting order.
3. In **Overview**, expand **Ready to start? Bracket controls**.
4. Select **LOCK ROSTERS & GENERATE BRACKET** and confirm after checking the lineups.

This locks the lineups and starts the competition. Follow matches under **Matches & results**.

## 9. Report games and follow results

1. The winning captain opens **Captain Dashboard** and selects one screenshot or scoresheet for the correct game.
2. Use PNG, JPEG, WebP or PDF, up to **10 MB**, then select **Report Win**.
3. The opposing captain reviews the evidence and selects **Confirm Result** or gives a reason and selects **Dispute Result**.
4. Confirmation needs no second screenshot. Disputes pause the series for organiser review in **Manage Tournament → Matches**.
5. Confirmed games update the series score. Reaching the required wins completes the match and advances the bracket.

Best-of-three needs two wins; best-of-five needs three. Double elimination can require a Grand Final reset. Optional placement games must also finish before the tournament is complete.

With a **Match Results** channel assigned, confirmed scoresheets and results are posted there, including **#claim-rank** if that is your chosen destination. **People with access to that Discord channel can see the published scoresheets.** Website evidence access is restricted to authorised accounts.

See [Match results]({{ '/guides/match-results/' | relative_url }}) for disputes, corrections and delivery help.

## 10. Publish to Discord

1. Open the selected tournament's **Discord & publishing** tab.
2. Choose **Publish bracket**, **Team list** or **Custom announcement**.
3. Select the destination and delivery format.
4. Select **Save this tournament**.
5. For manual delivery, select **Send now to Discord**. For a bracket image, **Image — automatic updates** keeps that tournament's post current.

**Registration notice**, **Match results** and **Final standings** have their own actions. Final standings and the weekly ladder publish only after completion. A tournament's publishing choices do not publish every other tournament.

Channel defaults can be replaced by division, recurring-competition or individual-tournament choices, and by a selected publishing destination. Check **Channel Preview — Effective Channels** and the tournament's current destination if a message goes to the wrong place.

## 11. Optional divisions and announcements

Organisers can use **Server Management → Divisions** to create skill groups, order them and assign teams. When a linked division tournament completes, its eligible winner moves up one division if a higher division exists. Draft tournaments are independent of divisions. Existing results are preserved when a team moves.

See [Divisions]({{ '/guides/divisions/' | relative_url }}). Server **Announcements** lets authorised organisers prepare community messages separately from a tournament's own posts.

## 12. History and support

**Cancel Tournament** affects the selected event and preserves its records. **End Recurring Tournament Schedule** stops future events; it does not cancel an event already running. Finished and cancelled events can be found in **History**.

Contact your community organiser for tournament decisions. **Support Tickets** is available only in communities that enable it; use their Discord panel to open a private ticket and **Profile → My Support Tickets** for available ticket history.

Read [Troubleshooting]({{ '/troubleshooting/' | relative_url }}) for common problems and the [Privacy Policy]({{ '/legal/privacy/' | relative_url }}) for privacy contacts.

The [original illustrated PDF guides]({{ '/guides/visual-guides/' | relative_url }}) remain available. Their screenshots may differ from the current app; use these web guides for current requirements.
