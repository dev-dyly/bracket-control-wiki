---
layout: default
title: Draft-only community setup
permalink: /guides/draft-only-setup/
---
# Set up a community for draft tournaments

Use this guide when your community wants captains to draft individual players, rather than accept ready-made teams. It uses **Manual Setup** and four Discord channels.

For general server setup, **Global Player Registration is the only mandatory Discord channel**. The other three channels below support this community's chosen draft workflow.

## 1. Connect your Discord server

1. Open [Bracket Control](https://app.devdylnz.com/app/) and **Sign in with Discord**.
2. Open **Your Discord servers** and find the server you manage.
3. Use **Connect server** if the server is not connected, then **Invite bot**. Add the Bracket Control bot through Discord and return to the app. If the bot is already installed, use **Connect installed bot**.
4. Open **Complete server setup**, or **Server settings → Open Server Setup** for a connected server.
5. Choose **Manual Setup**.

You need server-owner, administrator or authorised organiser access. If Discord will not let you add the bot, ask the server owner to connect it.

## 2. Create four channels in Discord

Create these channels yourself, then return to Bracket Control and select **Refresh Discord inventory**.

| Discord channel | Channel type | Bracket Control setting |
| --- | --- | --- |
| **#tournament-registration** | Text | **Global Player Registration** |
| **#bracket-updates** | Text | **Bracket Updates** |
| **#claim-rank** | Text | **Match Results** |
| **Draft Waiting Room** | Voice | **Draft Voice Waiting Room** |

**Claim Rank is this community's preferred channel name for Match Results.** It is not a separate Bracket Control feature or a rank-claiming tool. Captains report games on the website; confirmed results and scoresheets can be published to **#claim-rank**.

## 3. Create the registered-player role

1. In Discord, open **Server Settings → Roles**.
2. Create a role named exactly **Bracket Control Registered**.
3. Leave all permissions off for this role.
4. Place it below the Bracket Control bot's highest role.

This is a registration marker, not a staff role. Do not give it administrator or channel-management permissions. Manual Setup requires this existing role and does not create it for you.

## 4. Assign channels and messages

1. On **Manual Setup — Discord Channels**, assign each channel using the matching setting in the table above.
2. Set **Team Registration and Management**, **Tournament Announcements**, **Registered Teams**, **Standings** and **Staff Approvals** to **Not Required**.
3. Leave **Enable Support Tickets** unchecked unless your community wants private support tickets. Enabling it requires its own support channel, private category and staff settings.
4. Categories can use **No category assignment**. If you already put your channels in a category in Discord, Manual Setup keeps them there.
5. Select **Continue**. Under **Registered-player role and messages**, select **Bracket Control Registered**.
6. Check **Publish or update the Global Player Registration message**. Leave the team-registration message off.
7. Continue through **Support Ticket Configuration**, keeping tickets disabled unless wanted.
8. Select **Review Configuration**. Check all four channel assignments, the role and the registration message.
9. Check **I approve these exact assignments, resource actions and selected message publications**, then select **Apply Configuration**.
10. When setup is complete, check the registration message in **#tournament-registration** and select **Go to Dashboard**.

Manual Setup saves your choices and publishes only the messages you selected. It does not create channels, change channel permissions or move channels in Discord.

If you want a Teams List PNG, also assign **Registered Teams** to a suitable text channel, or choose its destination later under the tournament's **Discord & publishing → Team list**. You can use an existing channel such as **#bracket-updates**. This is optional and does not require ready-made team registration or a staff-approval channel.

## 5. Check the bot's Discord permissions

Ask a server administrator to check the bot's role and the waiting room's category permissions.

| Permission | Why it is needed |
| --- | --- |
| **View Channels**, **Send Messages**, **Embed Links**, **Attach Files**, **Read Message History** | Registration messages, bracket images and result delivery in the selected text channels. |
| **Manage Roles** | Assign the registered-player role and maintain access to the private captain room. Keep the bot's role above the registered-player role. |
| **Manage Channels** | Create and remove temporary voice rooms in the waiting room's category. |
| **View Audit Log** | Recover safely if Discord does not confirm that a temporary room was created. |
| **Connect**, **Move Members** | Move connected captains and players between the waiting room and tournament rooms. |

Channel and category restrictions can override a role's permissions. Check the affected channels as well as the server role. Players need permission to see and join the waiting room; ordinary players should not be given **Move Members** or **Manage Channels**.

## 6. Create the draft tournament

1. On **Dashboard**, select **+ Create tournament**.
2. Under **Tournament details**, enter the name, bracket format and maximum teams. Choose **Draft** under **Tournament type**. Draft tournaments are independent of divisions.
3. Choose whether to **Repeat this tournament weekly**. Set the date, time zone and registration period under **Date and registration**.
4. Decide whether to **Require Individual Player Acceptance**. If enabled, every captain, starter and substitute must personally complete the required registration and tournament-rules acceptance.
5. Add your **Tournament Rules**. Rules and the individual-acceptance choice are fixed at creation, so check them carefully.
6. Open **Custom Discord channels (optional)** only if this tournament needs different channels. Check that **Match Results** uses **#claim-rank** and the draft waiting room is correct.
7. Review the settings, complete the confirmation shown and select **Create tournament**.

See [Tournament creation]({{ '/guides/tournament-creation/' | relative_url }}) for the full creation steps.

## 7. Register players and gather in voice

1. Ask all players, including captains, to open the message in **#tournament-registration** and complete **Global Player Registration** with their own Discord account.
2. Players review the Terms of Service, Privacy Policy and Player Information Notice, complete the three choices and select **Accept Registration**.
3. Players use **Verify Registration** on the server's registration message to receive the registered-player role when their registration is current.
4. Ask players to join **Draft Waiting Room** and remain connected. Bracket Control uses the configured room to gather available draft players.
5. Open **Manage Tournament → Live Draft** and check the player pool. If necessary, use **More Discord actions → Draft voice players** in the tournament's **Discord & publishing** tab to refresh waiting players.
6. If individual acceptance is required, share the tournament's participation link from **Teams & players → Participation readiness → Copy Participation Link**. Players open **My Participation** and select **ACCEPT TOURNAMENT RULES** after reading and checking the displayed statement.

**Global Player Registration is separate from entering a tournament.** It records the current Bracket Control registration across participating communities. It does not put a player in a draft, assign a team, confirm attendance or accept a community's tournament rules. Joining voice supplies a draft player; it does not accept rules. Each player must make their own required decisions.

## 8. Select captains and run the Live Draft

1. Open **Manage Tournament → Captain Selection**.
2. In **Draft Captain Registry**, use **Add New Captain** for anyone not already listed. Search for their Discord account, select the right member and select **Save Captain**. If search cannot find them, ask the member or server administrator for their Discord user ID.
3. Select the captains for this tournament and select **Confirm Selected Captains**. Being a server administrator or joining a voice room does not make someone a captain.
4. Bracket Control creates a private **Draft Captains** voice room for selected captains and authorised staff, and moves selected captains who are connected to the waiting room. Check the voice status shown on **Captain Selection**.
5. Open **Live Draft**. Check that there are at least two captain teams and enough players for four starting-player picks per captain.
6. Select **START CAPTAIN DRAFT**. Captain selections lock when drafting starts.
7. Captains open **My Teams** or **My Matches → Team and draft dashboard**, using their own Discord account. When the portal shows **YOUR TURN TO PICK**, they select the button beside an available player.
8. Follow the on-screen turns. The draft uses stages of two, one, two and one picks, reversing the captain order between stages. Each captain's first four picks complete the starting five; extra picks are optional substitutes. Players needed to finish other teams' starting lineups are reserved.
9. Captains can use **PASS REMAINING OPTIONAL PICKS** when offered. At completion, valid teams are approved automatically; no staff approval channel or manual team approval is needed.

### What happens to voice rooms?

When the draft finishes, Bracket Control creates temporary team voice rooms and moves connected, recognised players from the waiting room and captains from **Draft Captains** into their team rooms where possible. It cannot move someone who is disconnected or bring them out of an unrelated voice room.

The **captain room is private**. **Team rooms copy the waiting room's channel permissions; they are not automatically restricted to each team's members.** If your community needs private team conversations, have a Discord administrator review and adjust each team room's access before play. Do not make the waiting room inaccessible to the players who need to join it.

Temporary rooms are cleaned up after they are no longer needed. Cleanup may wait for occupants to leave or move safely. Do not create the captain or team rooms yourself as permanent setup channels.

### Publish the completed draft's Teams List

With a Teams List destination and **Image — automatic updates**, Bracket Control posts the PNG after the draft is complete, its rosters are approved and its team voice rooms are ready. It shows each team's name, captain, five starters and substitutes using the usual tournament layout.

To publish or refresh it manually, open **Manage Tournament → Discord → Team list**, check the destination and image format, select **Save this tournament**, then **Publish Teams List**. Approved roster changes update the same post automatically; manual refresh also updates it. Turning publishing off or choosing manual-only delivery stops automatic updates. Changing destinations keeps the old channel's post as history.

## 9. Generate and publish the bracket

1. Open **Manage Tournament → Teams** and check every completed team and **Participation readiness**.
2. Clear any remaining readiness warnings. Automatic roster approval does not replace required player acceptance.
3. Use **Team order** to check the teams' starting order.
4. In **Overview**, expand **Ready to start? Bracket controls** and select **LOCK ROSTERS & GENERATE BRACKET**. Confirm the prompt. This locks the lineups and starts the competition.
5. Open **Discord & publishing → Publish bracket**, select **#bracket-updates** as the destination and choose **Image — automatic updates** or **Image — send manually**.
6. Select **Save this tournament**. For a manual post, select **Send now to Discord**. Check the message in Discord.

Creating the tournament alone does not publish every bracket. Publishing settings apply to the tournament you are managing.

## 10. Report games and publish results to #claim-rank

1. The winning captain opens **My Matches**, checks the tournament, opponent and game, and uploads **One scoresheet (required)**.
2. Use one clear screenshot or scoresheet per game: PNG, JPEG, WebP or PDF, up to **10 MB**. Select **Report Game Victory**.
3. The opposing captain reviews the evidence, then selects **Confirm game result** or enters a reason and selects **Dispute game result**. Confirming does not require a second screenshot.
4. An organiser resolves disputes in **Manage Tournament → Matches**. A disputed game pauses the series.
5. Confirmed games update the series score. When a team reaches the required wins, the match completes and the bracket advances.
6. With **Match Results** assigned to **#claim-rank**, Bracket Control publishes confirmed game scoresheets and the match's results there. Posting can take a short time. Check the selected tournament's channel settings if a post is missing.

Screenshots sent to the results channel can be seen by people with access to that channel. Upload only the match evidence needed. For corrections and delivery problems, see [Match results]({{ '/guides/match-results/' | relative_url }}) and [Troubleshooting]({{ '/troubleshooting/' | relative_url }}).
