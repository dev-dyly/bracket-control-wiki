---
layout: default
title: Troubleshooting
permalink: /troubleshooting/
---
# Troubleshooting

Find the problem below and follow the steps. Contact your community organiser for entry, rules and match decisions.

## I cannot find my server or dashboard

1. Check that you signed in with the correct Discord account and still belong to the server.
2. Open **Your Discord servers**.
3. Ask the server owner to check that the bot is connected and your organiser access is correct.
4. If you are a player, use the tournament link supplied by the organiser.

Signing in alone does not grant organiser access. If onboarding says your community needs approval, follow that message.

## Do I need to register again?

**Global Player Registration** covers the current platform documents across participating communities. If the documents change, review them again. Use **Verify Registration** on another server's registration message to confirm your status there.

Tournament entry is separate. Regular weekly teams must confirm attendance for each event. Where required, each player must accept that tournament's rules in **My Participation**.

## Global registration or the registered role is missing

1. Open [Player Registration](https://app.devdylnz.com/app/register) and use your own Discord account.
2. Complete the current documents and select **Accept Registration**.
3. Return to Discord and select **Verify Registration**.
4. If the role is missing, ask the server administrator to check **Bracket Control Registered** has no permissions, sits below the bot's role and the bot has **Manage Roles**.
5. If the page shows an unavailable message, contact the organiser or Bracket Control operator.

## My Participation shows no tournament

1. Check you are using the correct Discord account and the organiser's participation link.
2. Ask the captain or organiser to check the Discord account assigned to your player entry.
3. For a voice-based draft, join the configured waiting room so your entry can be recognised.
4. Check whether this tournament requires individual acceptance.

A gaming name alone does not link a player entry to your account. Another person cannot accept rules for you.

## My approved team is not ready

1. Open the correct event in **My Teams**.
2. Check **CONFIRM PARTICIPATION** and the registration deadline.
3. Ask the organiser to check **Teams → Participation readiness** and **Overview**.
4. Resolve outstanding personal registration, rules acceptance or division warnings.

An approved lineup and confirmed attendance are separate. If attendance has expired, ask the organiser for help. A changed lineup may need approval again.

## Setup stopped

1. Return to **Open Server Setup**.
2. Choose **Resume interrupted setup**.
3. Review the saved plan, check the resume confirmation and select **Resume setup**.
4. Wait for any Discord retry time shown.

For new Manual Setup channels, use **Refresh Discord inventory** after creating them. Only Global Player Registration is mandatory; choose **Not Required** for unused destinations.

## A message went to the wrong channel or did not arrive

1. Check the selected tournament, not just the server name.
2. Check the tournament's **Settings** and **Discord** tab for a different destination.
3. Review server **Channel Preview — Effective Channels** and **Discord delivery status**.
4. Check the bot can view the destination, send messages, show links and attach files.
5. Save changed publishing settings before using **Send now to Discord**. Allow a short time for queued posts.

Global Player Registration and Team Registration use different destinations. **#claim-rank**, if used, maps to **Match Results**.

Final standings and the weekly ladder are unavailable until the tournament is complete, including any scheduled placement games.

## Draft players or voice rooms are missing

1. Check the tournament's **Draft Voice Waiting Room** assignment.
2. Ask players to join that room and remain connected. Unpicked voice entrants who leave are removed from the pool.
3. Check **Captain Selection** and select **Confirm Selected Captains** before starting the draft.
4. Check there are at least two captain teams and four available starting-player picks per captain.
5. Review the voice status shown in **Captain Selection**.
6. Ask the Discord administrator to check **Manage Channels**, **Manage Roles**, **View Audit Log**, **Connect** and **Move Members**, including category restrictions.

The bot moves recognised players only from the configured waiting room or the tournament's captain room. It cannot move disconnected people or pull them from unrelated rooms.

The captain room is private. Team rooms inherit waiting-room permissions and are not automatically private to each team. Have an administrator adjust access if needed. Temporary room cleanup can wait until occupants leave or can move safely.

## A captain link does not work

1. Sign in with the account assigned as captain.
2. Check you still belong to the hosting Discord server.
3. Open **My Teams** or **My Matches** to find your verified assignment.
4. Ask the organiser to check the captain assignment if it is missing.

Keep private captain links within your team and organiser group.

## My scoresheet will not upload

1. For **Report Game Victory**, choose one PNG, JPEG, WebP or PDF file, up to **10 MB**.
2. Check that you are the winning captain for the selected game.
3. Check that the previous game is confirmed and the tournament is live.
4. If the upload still fails, give the organiser the tournament, match and error message.

## A result is disputed or the bracket has not changed

1. Open **My Matches** and check whether the opponent still needs to confirm.
2. The opponent can select **Confirm game result**, or enter a reason and select **Dispute game result**.
3. A dispute pauses the series until an organiser reviews it in **Manage Tournament → Matches**.
4. A match advances only when a team reaches the required confirmed game wins.

See [Match results]({{ '/guides/match-results/' | relative_url }}) for corrections and Discord result delivery.

## I need private support

Use your community's Discord support panel if **Support Tickets** is enabled. Open **Profile → My Support Tickets** for available ticket history. Communities do not have to enable tickets.

For privacy requests, use the contact details in the [Privacy Policy]({{ '/legal/privacy/' | relative_url }}). For a browser security warning, stop and tell the operator which page and warning appeared.

Return to the [Complete user guide]({{ '/guides/user-guide/' | relative_url }}).
