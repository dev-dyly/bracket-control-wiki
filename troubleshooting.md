---
layout: default
title: Troubleshooting
permalink: /troubleshooting/
---
# Troubleshooting

## Login or permissions

- **Server is missing:** Make sure you are using the expected Discord account, belong to the hosting server and the bot is connected. Return to **Your Discord servers** and reselect it.
- **Admin access denied:** Discord login is not sufficient. Ask the server owner to check your role and configured organiser permissions.
- **Captain link denied:** Use the account that owns that team, maintain server membership and use the current event link. Use the latest link supplied by the organiser.

## Discord setup wizard

- **No setup option or different screen from the guide:** The available wizard can vary between servers. Follow the options shown and ask the server administrator if you lack access.
- **Discord role-hierarchy warning:** Move the bot role *above* the zero-permission **Bracket Control Registered** role when prompted; do not move unrelated roles blindly. Review/resume the saved plan.
- **Discord 429 / rate-limit waiting:** Observe the displayed wait and resume the saved plan afterwards. Avoid retry storms or creating replacement channels while receipts are pending.
- **Registration sent to wrong channel:** **Global Player Registration** and **Team Registration** are separate destinations and procedures. Verify global/server/division/tournament channel overrides.

## Registration and bracket

- **Cannot confirm:** Registration may be closed; your entry may have expired, been withdrawn or placed under a roster/division hold. Ask the organiser. Reopening doesn't automatically confirm an expired entry.
- **Not in the bracket:** Approved roster, confirmed weekly attendance, division/rollover eligibility, capacity and readiness must all pass.
- **Cannot edit seeds:** The tournament might already be locked or entries may be ineligible. Review **Overview → readiness**.

## Match evidence

- **Upload fails:** For each game victory report, upload **one** PNG/JPEG/WebP/PDF file (up to 10 MB). Check the game state and permissions. An extension change cannot make an invalid file safe.
- **Result is disputed:** The opponent challenged a reported game winner. An authorised organiser must review evidence and resolve the game. The opponent can optionally upload supporting evidence.

## Discord

- **PNG in Discord has blank text:** Pause publishing, check the image preview and report the event/channel. The release operator must verify the deployed font assets, runtime font availability, PNG cache and public approved-roster safeguards.
- **Notices or voice moves delayed:** Check server and bot permissions, message delivery worker, voice-room occupancy and member connectivity. Discord API outages may defer actions; the web UI remains the place to verify status.

## Still need help?

For tournament decisions and prize/fee disputes, contact your **Discord community organiser**. For privacy or legal requests, use the operator contact published in the approved policy once available. Do not send passwords or unnecessary private scoresheets.

- **Chrome blocks the OAuth page as unsafe:** Do not bypass the Chrome warning. Record the host/category without sending tokens, state or callback codes; report to the operator. The browser reputation investigation is still unresolved.
- **Automatic Discord PNG missing:** At the current live baseline, check each occurrence’s saved Teams/Bracket automatic publishing mode. The behaviour depends on the active production release and event configuration; verify saved settings and the deployed version before assuming defaults.
