---
layout: default
title: Complete user guide
permalink: /guides/user-guide/
---
# Bracket Control — Complete user guide
**Edition:** 1.1 / release review · **Updated:** 20 October 2026 · **Baseline:** GitHub main `4406ee7` (PR #40 merged); deployed production SHA must be checked independently. PRs #27, #28 and #42 are not documented as live.

> **Product branding:** The official public product name is **Bracket Control**. The source-code repository retains its technical name `dev-dyly/Bracket-App` for continuity. Navigation wording can vary between mobile and desktop. An administrator must be authorised in the relevant Discord server; signing in alone does not grant admin access.

## 1. What Bracket Control does

Bracket Control helps Discord communities run single and recurring esports competitions. Organisers configure independent servers, seasons/series, dates, team divisions, registrations, seeding, match formats, scoresheets, brackets and standings. Players register or rejoin a team, and captains manage lineups, confirm participation or take turns drafting free agents. A Discord bot handles tournament invitations, selected announcements, standings/results, and temporary voice-room coordination. Some outputs can be displayed publicly via secure tournament links. **Brackets and results are hosted on the app; organisers control whether their tournament is public.** The platform itself is free at launch and does not collect fees or pay prizes.

## 2. Before you begin

You need a Discord account meeting Discord's applicable age rules, membership in the hosting Discord server for protected captain/registration features, and a browser able to use secure authentication cookies. Organisers also need administrator or an authorised organiser role in that server, a connected Discord bot and appropriate channel permissions. A captain should be signed in with the Discord account assigned to their team. Never post private captain links in public channels.

### Access and sign in

1. Open **https://app.devdylnz.com/app/**. The home page is public.
2. **Browse Tournaments** opens a **public-link navigator**, not a public directory of all communities. Use a tournament link supplied by an organiser to open the right event.
3. **Manage Your Tournaments** opens the server chooser at **Your Discord servers** (`/app/servers`); if prompted, choose **Sign in with Discord**.
4. Authorise Discord's requested identity/server scope. After login, **captains are directed toward My Matches** when the account has verified match assignments; **organisers** can open the server chooser and dashboard; users with both roles can use either route. You can also select **My Matches**, **My Teams** or **Your Discord servers** in the navigation. A member without organiser permission can select **View tournaments** where available.
5. Select your profile menu → **Sign out** when finished. A Discord logout and a Bracket Control logout are different actions.

### Understand navigation

| Where | What you see / do |
| --- | --- |
| **Home** | Introduction, Browse Tournaments and Manage Your Tournaments |
| **Dashboard** | Selected server's tournament cards, create/edit series, active events, schedules and history; organiser-only controls |
| **Notifications** | Organiser queue of pending roster applications, disputed games and other deployed administrator actions; badge indicates outstanding items |
| **My Matches** | Captain assignments across verified hosting servers, prioritising opponent confirmation and open games; each new game uses a one-file victory report. |
| **My Teams** | Verified captains' continuing team memberships, invitations and captaincy requests; administrators have a separate **Team management** view |
| **Server Management** | Expand to find **Server Settings**, **Team management**, **Announcements**, **Divisions** and **Discord Settings (Global)** |
| **Top bar: Bracket / Ladder / Match Results** | Public views for the **currently selected tournament**; links are disabled until one is selected |
| **Tournament selector** | Switch between known events for the current server; keep checking the title before editing |
| **Server selector** | Change Discord community; selection refreshes permission-scoped content |
| **Profile** | Displays Discord account and provides Sign out |
| **Mobile navigation** | Open the **Navigation** disclosure for the sidebar links and selectors; content stacks vertically |

The public occurrence address follows `/app/g/{guildId}/o/{occurrenceId}/`; append `/standings` or `/results` for its other public views. Organisers should share the **Copy/Share public link** provided by the UI or Discord post, rather than editing internal IDs manually. Restricted invitations may require a valid invitation and/or sign-in.

## 3. Organiser: connect and configure a server

1. Sign in with a server account that can manage tournaments. At **Your Discord servers**, select your server and open **Server settings**.
2. Check the hosting server, organisers/roles and IANA timezone. Correct timezone and registration deadlines are vital for recurring events and daylight-saving transitions.
3. In **Server Management → Discord Settings (Global)**, select bot channels for **Registration, Teams, Pending/Approval, Bracket, Standings, Results** and, if relevant, **Voice**. The bot must see and post to those channels; check Discord permissions and hierarchy in Discord itself.
4. Understand precedence: an individual tournament may override its series/division settings, which can override a server default. Inspect the channel preview before saving. Publishing mode and its saved destination may also override a channel default.
5. Go to **Announcements** to prepare general community announcements or result recaps. General announcements are server-wide; a tournament recap can use event placeholders. Preview content and channel before posting.
6. Go to **Divisions** to establish ladder order and qualifying series. Set automatic promotions (top 1–3, if enabled), optional relegations (bottom 1–3, if enabled), and any explicit overrides. Only qualifying completed series count for movement.

**Discord permissions:** Core bot abilities include viewing and sending messages, reading channels, attaching images, managing its created voice channels and moving members when used. The newer private Draft Captains room also needs **Manage Roles** for permission overwrites; ensure View Channel, Connect, Move Members, Manage Channels and View Audit Log as documented for the server. The bot is not given privileged member Gateway intents simply to power the workflow.

## 4. Organiser: create and schedule a tournament

1. In **Dashboard**, choose the correct **Server**, then use the create tournament/series action.
2. Decide whether this is a **standalone** occurrence, a **weekly recurring series**, a **division/ladder competition**, or a **draft tournament**. Standalone and recurring series have independent history and scheduling; draft results do not automatically change normal division standings.
3. Choose the series and event name, starts-at date/time, server timezone, registration open/close window and approved-team capacity (the event settings UI supports **2–16** teams).
4. Choose a bracket type in the event editor: **Double elimination**, **Single elimination** or **Round robin**. New game-based matches can use BO1, BO3, BO5 or BO7 where the configuration supports that choice; review the exact format available in the event UI by bracket phase (winners, losers, grand final and round robin). If desired, enable additional placement-tiebreak matches (through 4th/8th/16th) for elimination events.
5. Open the specific tournament card → **Manage Tournament**. Its tab bar is **Overview · Teams · Matches · Seed · Discord · Settings**; draft events also add **Captain Selection** and **Live Draft**.
6. In **Settings**, inspect public visibility, schedule, registration status, capacity, formats and optional channel overrides. Save event-specific settings while editing is allowed. **Open registration** or **Close registration** explicitly; do not assume a planned schedule has executed if the background worker is paused.
7. Check the **Overview** for readiness and next steps. A bracket is generated only after actual eligibility checks pass—creating an event does not generate a bracket automatically.

### Event-specific and series-wide changes

A series schedule creates or coordinates future occurrences; event **Settings** change only the selected occurrence. Changes to an already completed series, historical rosters or locked event may be intentionally restricted. Use **Cancel occurrence** instead of deleting an event when you need to preserve its registration and result history; destructive actions may be blocked if dependent records exist. Use **Cancel Tournament** to cancel the selected occurrence (including permitted active/locked events); use **End Recurring Tournament Schedule** to stop future scheduling. Ending a schedule does not automatically cancel an already active occurrence. Protected **Delete / Archive** actions retain history and can be blocked by dependent records. A one-time cancellation is different from stopping all future weekly creation.

## 5. Organiser: fixed teams, approval, confirmation and rollover

### First-time registration

1. Open the event **Teams** tab. Registrations can originate from a **Discord registration invitation** (captain signs in and applies) or from an administrator's manual team entry tools.
2. Teams ordinarily have **five starters**, one of whom is captain, plus **up to two optional substitutes**. Names, Discord identity and relevant hosting-server membership are checked; unverified membership may prevent a submission.
3. Use the **approval queue** with filters **Pending / Approved / Rejected / Withdrawn / All**. Compare this week with the previous roster. Approve or reject each required revision. View the roster's approval history for audit context.
4. If a roster changes, a new revision can require approval. An unapproved replacement should **not** overwrite a previously approved roster in public posts. Do not publish roster PNGs until SEC-003 release checks are complete.

### Returning recurring teams — canonical Option B (merged PR #40)

1. For a recurring fixed-team series, choose either **carry-over** or **manual** registration policy. A team with a **current, valid approved roster and verified captain** can establish membership in that specific recurring series; **two completed past weeks are no longer a requirement**. Team identity and membership are scoped to the series rather than automatically merged across every division ladder.
2. Under **carry-over**, eligible approved roster evidence prepares future occurrences without requiring a previously completed source match. The next week's entry begins **pending captain attendance confirmation**; no automatic confirmation is carried forward. Under **manual**, the captain must make a fresh weekly application, although an unchanged prior approval may be reused where valid.
3. A captain must still choose **CONFIRM PARTICIPATION** for each relevant occurrence before its deadline. An unchanged approved roster can inherit approval; a changed roster or changed captain may need new review. Confirming attendance never overrides a separate roster or Division hold.
4. In **Teams → Review & Resolve**, investigate current requirements, restrictions, captain identity, ambiguous historical enrollment intent and destination Division/series placement. The former bulk **Review recurring enrollment** activation and cross-series merge workflow have been retired. They must **not** be used as current setup instructions.
5. Promotions/relegations still use qualifying completed Championship results when configured. Genuine unsettled Championship placement can hold future Division placement; an ordinary unfinished tournament does not block membership solely for being unfinished. If a Division transfer leaves multiple possible recurring destination series, an organiser must explicitly choose one using the versioned authorised control.
6. Captains can **WITHDRAW FROM THIS TOURNAMENT** without ending their permanent membership, or separately **LEAVE RECURRING COMPETITION** to stop future automatic entry. Administrator restrictions and explicit opt-outs are not cancelled by a later approval or background retry.

**Do not infer a failed enrollment from an old error message.** The current review screen uses actionable reason codes and current restrictions. Check your selected series, captain identity, roster approval, weekly attendance and Division placement before bracket generation.

## 6. Captain: registration, participation and rosters

1. Follow the registration invitation or open your private team page. Sign in with **your own Discord account** and remain a member of the hosting server. A private link locates a team, but does **not** bypass captain identity or guild membership.
2. For a new team, complete the registration form with your team name, Discord identity, five starters (captain first) and optionally two substitutes; submit before registration closes. The organiser may need to approve it.
3. For a recurring team, open **My Teams** or the tournament's captain page. Review your upcoming **division, date, deadline**, **Attendance** and **Roster Approval** indicators. Select **CONFIRM PARTICIPATION** when you will compete. Merely opening the page **does not confirm you**.
4. If you cannot attend a particular week, use **WITHDRAW FROM THIS TOURNAMENT** and confirm it. This preserves your recurring membership and historical records, but may require an organiser to reinstate you for that week.
5. To stop automatic entry permanently, use **LEAVE RECURRING COMPETITION** (a distinct confirmation). Ask an organiser about joining again; never assume an expired confirmation is reactivated by reopening registration.
6. Under **Your Registered Lineup**, choose **Edit team members** while roster editing is open. Keep five starters including yourself and up to two substitutes. Save; ordinary changed rosters become pending administrator review. You can view an existing approved roster separately.
7. When changing captaincy, use the supported **My Teams** transfer workflow. The proposed captain must accept from their own Discord account; organisers review/approve as required. Only verified identity transfers are valid. Retirement is separate from losing a single match or declining one week.

**Important:** Confirmation, roster approval and enrollment are **three separate statuses**. Always check all three before the cutoff. Your team can stay in the database and still be excluded from this week's bracket.

## 7. Organiser and captains: draft-pool tournaments

1. In Discord, organisers configure a **Draft Waiting Room** voice channel and create a draft tournament. Anyone wishing to enter the free-agent pool joins that waiting room; selected captains are explicitly excluded from the free-agent pool.
2. The organiser opens the event's **Captain Selection** tab, adds or verifies captains in the server-scoped registry, and selects the intended captains using **checkboxes**. The selected team names can be edited in **Teams**. The registry persists across draft events and keeps deactivated-captain history.
3. For a **new-workflow** draft, selecting captains creates a private **Draft Captains** voice room. Selected captains are moved/allowed there; other players remain in the waiting room. Existing/legacy draft occurrences retain their original workflow rather than being silently converted.
4. The organiser opens **Live Draft** and starts the draft when registration, captains and free-agent pool are ready. Captains use their own authenticated **captain web portal** to choose an available player by clicking the button beside their name—**not** drag-and-drop and **no voice draft call is required**.
5. Picks proceed in the existing **2 / 1 / 2 / 1** sequence. The system reserves enough free agents for other captains' required starters. Once the initial five are complete, captains can **PASS REMAINING OPTIONAL PICKS** if applicable. The UI shows whose turn it is.
6. After all valid picks/passes, the app records/approves the finished rosters and creates private **Team {captain}** voice channels, moving *connected* assigned participants from managed rooms to their team's room. Disconnected players retain assignment and can be moved when they return to the waiting room. The organiser may supervise and use logged administrative overrides.
7. Temporary team/captain voice rooms are cleaned up conservatively when the event completes/cancels and rooms are safe to delete. They may remain if occupied by unrelated people or Discord permission/errors prevent safe cleanup. Avoid manually deleting bot-owned rooms during active drafting.

Voice presence is used for pool management; it is not an audio recording service. Discord's own voice functionality is subject to Discord rules.

## 8. Organiser: start, seed and run the bracket

1. In **Overview**, resolve readiness warnings and get enough eligible teams. In **Teams**, finish approvals or draft completion. Check capacity and intended division.
2. Use **Seed** to review the seed editor and arrange the approved entrants as allowed. The editor may be disabled after a bracket starts or if approvals are invalid.
3. Generate the bracket through the organiser controls once ready. It does not happen automatically merely because registration closes.
4. Switch to **Matches** for current fixtures, statuses, disputes and authorised corrections. Winning captains advance only after an accepted/confirmed result. Bracket formats can include original grand-final reset semantics for double elimination: the lower-bracket finalist must win the first final **and** reset to become champion.
5. Where enabled, additional elimination placement tiebreaks finish after the champion is decided; the event is not complete until required placement matches are resolved.
6. Review **Bracket / Ladder / Match Results** through the top navigation to confirm what spectators see. Finalise the occurrence only after scores/disputes and any placement matches are resolved.

### Correcting, disputing or replaying a game

For newly generated **game-based** fixtures, a winning captain reports each individual game's victory, attaching one scoresheet. The opposing captain **confirms** the winner or **disputes** with a reason. A dispute stops that game and requires an authorised organiser decision in **Matches → Game reports and disputes**. The opposing captain can supply one optional dispute document.

If a confirmed game was recorded incorrectly, the organiser can use **Confirmed and corrected games** to preview a reasoned correction, attach optional evidence, review downstream impact and approve required consequential changes. Correction history is append-only; previously confirmed games and original scorecards are retained. A corrected BO3 may reopen 2–0 to 1–1, and voided downstream matches require new replay fixtures rather than silent score edits. The Bracket, standings and historical Discord result publications follow the effective confirmed game history. Restricted match evidence must never be posted publicly.

**Legacy matches** retain the older match-level reporting form and correction contract. Follow the form displayed for the specific fixture; do not attempt to use old score-entry fields on a new game-based fixture.

## 9. Captain: report games, confirm results and upload evidence

### Newer matches — individual game reporting (Phase 12)

1. Sign in using the correct Discord captain account. Open **My Matches** in the sidebar (or `/app/my-matches`) to see assignments **across your eligible servers**; opponent confirmation requests appear first. Select the right tournament and open match. Registration does **not** need to be open for an authorised captain to report an active match.
2. For each game your team **won**, select **Report Game Victory**, attach **exactly one** PNG/JPEG/WebP/PDF scoresheet (**up to 10 MB**), then submit. A losing captain must not report a game victory.
3. The opposing captain reviews the displayed winner and secure evidence. Select **Confirm game result** (no second upload needed), or enter a reason and select **Dispute game result**. A dispute pauses progression; the opponent can optionally upload **one supporting scoresheet**.
4. The winner/series progress updates only after confirmation or an authorised administrator resolution. Continue through the required BO1/BO3/BO5/BO7 game wins. Confirmed results drive bracket advancement, Discord scorecard publication and Grand Final/reset progression.
5. If a game is wrong after confirmation, ask an organiser to use the protected correction/impact-preview workflow. Do not submit a fabricated victory to compensate for a mistake.

### Existing legacy matches — two-file match reports

Some older fixtures retain **SUBMIT MATCH REPORT** with series score fields. On those older fixtures **each reporting captain attaches two scoresheets**, each PNG/JPEG/WebP/PDF up to **10 MB**. Matching captain reports can confirm the series; disagreements require organiser review. This is a compatibility workflow **only**; it is not the upload procedure for newly generated game-based matches.

**Evidence privacy:** game documents are available only through authorised captain/organiser controls. The app preserves original/corrected game evidence for audit and uses planned retention rules; evidence is not a public image gallery.

## 10. Organiser: Discord Publisher and announcements

Open a specific event → **Discord** or use the event's **Edit Discord** action. The publisher separates **Bracket**, **Teams** and **Announcement** content for that occurrence. For each, set a mode such as **Do not publish**, **Automatic PNG**, **Manual PNG**, **Custom Embed** or **Plain Message**, as offered by that content type. Confirm the target channel and preview and then publish/re-sync as appropriate. **Current production/main baseline:** Bracket/Teams automatic PNG publishing is configured per occurrence, and absent publishing settings can mean **off**. The restoration of **automatic-by-default publication for new eligible fixed-team/bracket occurrences**, along with series ladder PNGs and completion-to-recap admin reminders, is in **open PR #42** and is **not live until separately merged and deployed**. Explicit manual/off/custom settings continue to take priority. Do not tell organisers the PR #42 defaults are already running.

- **Registration invitations:** Discord posts may link directly to the registration form. Staff and captains need correct membership permissions; a public invitation does not provide organiser access.
- **Team images:** Include approved roster content only. The October 2026 production release still requires confirmation that image fonts render and SEC-003 snapshots are deployed.
- **Bracket images and links:** Tournament posts provide the associated live public bracket link where publishing is permitted. If the preview is blank or Discord image text is missing, stop publication and ask staff to verify server fonts and the current deployment; a successful send acknowledgement does not prove visible text.
- **Announcements and recaps:** The **post-tournament official winner recap remains an organiser-approved manual action**. Open **Server Management → Announcements → Post-tournament recap**, select the completed occurrence, check winners/rosters and send explicitly. PR #42 adds a persistent in-app **Create announcement** action and a **private staff-channel reminder**, not an automatic public champion post; treat that new action as pending release. Draft custom embed or plain text, select destination and preview mention behavior. Post-completion recap templates may use `{tournament}`, `{winner}`, `{runner_up}`, `{winner_roster}`, `{runner_up_roster}`, `{final_scores}`, `{placements}`, `{server}`, `{bracket_url}`, `{standings_url}`, `{results_url}`. Current queued legacy recaps may need review/requeue after approved-roster security changes.
- **Delivery monitoring:** Game scorecards and corrections use durable, immutable-aware publication receipts. Ambiguous Discord sends require safe receipt reconciliation, not blind duplicate resends. Discord message IDs are retained for update rather than duplicate posts, with retries and **Force Re-sync** where provided. Discord outages and changed permissions can defer delivery.

## 11. Organiser: promotion, standings, history and team management

In **Server Management → Divisions**, review each qualifying series and its promotion/relegation rules. After eligible completed weeks, standings calculate ladder movement and can notify affected captains privately. Teams missing recent competitions may be placed at the bottom or marked inactive according to the configured history rules. Use audited overrides only when you understand their effect on future rollover. Draft/side events do not automatically change the qualifying ladder.

In **Team management / My Teams (admin)**, verify captain ownership, accept or manage transfer/retirement requests, investigate ambiguous historical identities and handle per-server team memberships. In **Dashboard**, inspect completed tournament history, results and past schedules. Historic results may persist even when a team skips the next occurrence. Do not confuse tournament deletion with team retirement or permanent enrollment withdrawal.

## 12. Spectators: viewing tournaments without an organiser account

Use an organiser-shared **public tournament URL**. Open **Bracket** for match progression, **Ladder/Standings** for placements and **Match Results** for confirmed scores. Published completed tournaments may remain accessible; private, unlisted or restricted events may not. **Browse Tournaments** does not enumerate everyone’s Discord communities. Player names and approved lineups may be visible, but scoresheet files, pending rosters, private draft pools and admin data are not meant for public access.

## 13. Troubleshooting and common questions

| Symptom | What to check / next action |
| --- | --- |
| **Server missing** | Signed into correct Discord account? Is Bracket Control bot/server integration active? Do you actually belong to the hosting server? Use the server chooser, then retry. |
| **Administrator access required** | An authorised server administrator/organiser must grant the relevant role. Discord sign-in by itself is insufficient. |
| **Captain link denies access** | Use the account currently verified as captain, remain in the hosting server, and follow the latest event link. Rotated legacy links may be invalid. |
| **Cannot confirm this week** | Registration window may be closed, attendance already expired/withdrawn, or a division/rollover hold blocks the team. Ask an organiser; reopening alone does not confirm. |
| **Roster approved but not in bracket** | Also check attendance, division, capacity, deadline, current revision and readiness. |
| **Waiting-room member not moved** | Check that the bot has Discord voice permissions, the member is connected in a managed room, and the draft is at the relevant stage. Moves retry on voice/worker reconciliation. |
| **Scoresheet upload rejected** | For a new game victory: **one** file; for a legacy match report: **two**. Check PNG/JPEG/WebP/PDF format, each up to 10 MB, match state, current captain permission and upload admission limits. Renaming an invalid file does not make it valid. |
| **Game waiting for confirmation** | The reporting captain waits until the opposing captain uses **Confirm game result** or **Dispute game result** in **My Matches**. |
| **Scores conflict / disputed game** | A game dispute pauses progression. An organiser reviews protected evidence and chooses a reasoned resolution. |
| **Chrome warning after OAuth** | Do not bypass a browser security warning. Keep the exact host and warning category, omit tokens/codes from screenshots, and report it to the operator for Search Console/redirect/registered callback investigation. |
| **Discord PNG appears blank** | Pause publishing; verify PNG preview text, deployed fonts, asset/image URLs, bot permissions and pending security PR rollout. Report the exact occurrence/channel to an organiser. |
| **Discord notices delayed** | Check channel permissions, direct-message privacy, background worker and delivery status. A Discord notification is not the authoritative state. |
| **Public link returns restricted/empty** | Verify occurrence visibility and organiser-issued link. Public browsing intentionally does not list all communities. |
| **Need personal-data access/deletion** | Use the verified privacy contact once the operator publishes it. Identity verification is required before protected disclosure. |

## 14. Privacy, safe use and support

- Minimum-age and applicable consent requirements must be approved and implemented before unrestricted launch; follow Discord rules and applicable local law.
- Team names, public display names, approved rosters, match results and standings can be visible publicly, including on Discord. Never put private data into usernames or public announcement fields.
- Uploaded scoresheets are organiser-only evidence rather than general public content. Automatic 90-day live evidence removal is planned but not yet enabled; lawful holds and backups affect availability/deletion.
- For help with tournament settings or score disputes, contact your Discord community organiser. The operator must confirm the published privacy/contact address and legal minimum-age rules before an unrestricted launch. The operator must publish a verified privacy, security and legal contact before unrestricted launch.
- This guide describes the repository's current feature set. Features in security PRs still under release review should be treated as **not confirmed on production** until the team validates the deployed SHA and live behavior.

## 15. What's not live yet / October release notes

- **Discord PNG and recap release status:** Teams image behaviour changed after the documented baseline; other automatic publishing and administrative recap features may be staged. Check the current deployed release and per-occurrence settings rather than assuming review-only features are live.
- **PR #27 / PR #28:** coordinated evidence validation/orphan recovery/operator-hold authority and approved-only public roster projection remain **under release review**. The user guide describes the intended security behavior, not a sign-off that every guard is deployed.
- **Chrome OAuth unsafe-site warning:** separate unresolved investigation; application callback checks passed within tested scope but the Chrome warning was not explained or cleared. Users should not bypass a live interstitial.
- **Security issues #16–18:** supported Node runtime, PostgreSQL backup remote checksum verification and browser CSP/frame protections require tracked verification.
- **Production evidence:** prior live tests passed Discord captain sign-in, match access, scoresheet submissions, BO3 confirmation, Discord results, advancement and champion declaration; remaining live administrator cancellation, publication rendering and the above issues must still be checked.
- **Future proposal only:** the tier balancing idea (maximum two A-tier players or one A-tier plus one S-tier) has not been built or activated.
