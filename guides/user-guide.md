---
layout: default
title: Complete user guide
permalink: /guides/user-guide/
---
# Bracket Control — Complete user guide
**Edition:** 2.1 / current fixture workflows · **Updated:** 29 October 2026 · **Source baseline:** Bracket-App main `d9839b2`. Production revision was not independently confirmed. Expanded Discord setup/support tickets (PR #75) remain unmerged and staging-only.

> **Product branding:** The official public product name is **Bracket Control**. The source-code repository retains its technical name `dev-dyly/Bracket-App` for continuity. Navigation wording can vary between mobile and desktop. An administrator must be authorised in the relevant Discord server; signing in alone does not grant admin access.

**Quick access to the five illustrated/operational workflows:** [Discord Setup Wizard]({{ '/guides/server-setup/' | relative_url }}) · [Creating Tournaments]({{ '/guides/tournament-creation/' | relative_url }}) · [Captain Team Registration]({{ '/guides/team-registration/' | relative_url }}) · [Approving Teams]({{ '/guides/team-approvals/' | relative_url }}) · [Divisions]({{ '/guides/divisions/' | relative_url }}).

> **PDF status:** The supplied 14-step setup guide shows the expanded **PR #75 staging wizard**, not confirmed production behaviour. The 30-step tournament-creation and eight-step captain PDFs were used to prepare the focused guides. Follow the controls present in the running application.

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
| **My Matches** | Captain assignments across verified hosting servers, prioritising opponent confirmation and open games; each reported game victory uses one scoresheet. |
| **My Teams** | Verified captains' continuing team memberships, invitations and captaincy requests; administrators have a separate **Team management** view |
| **Server Management** | Expand to find **Server Settings**, **Team management**, **Announcements**, **Divisions** and **Discord Settings (Global)** |
| **Top bar: Bracket / Ladder / Match Results** | Public views for the **currently selected tournament**; links are disabled until one is selected |
| **Tournament selector** | Switch between known events for the current server; keep checking the title before editing |
| **Server selector** | Change Discord community; selection refreshes permission-scoped content |
| **Profile** | Displays Discord account and provides Sign out |
| **Mobile navigation** | Open the **Navigation** disclosure for the sidebar links and selectors; content stacks vertically |

The public occurrence address follows `/app/g/{guildId}/o/{occurrenceId}/`; append `/standings` or `/results` for its other public views. Organisers should share the **Copy/Share public link** provided by the UI or Discord post, rather than editing internal IDs manually. Restricted invitations may require a valid invitation and/or sign-in.

## 3. Organiser: connect and configure a server

1. Sign in, open **Your Discord servers**, choose the correct community and check your current Discord administrator/organiser authority.
2. Where enabled, open **Complete server setup** or **Open Server Setup**. The merged **Stage 2** wizard uses **Welcome, Channel Configuration, Registered Role, Review Configuration, Apply Configuration, Setup Complete**. It remains controlled by a release flag.
3. The expanded **Automatic Setup / Manual Setup** flow with complete channel categories, private approvals and optional native support tickets is in **PR #75 (staging only)**. The attached screenshot PDF follows that newer **14-step** flow, not the older six-step version.
4. Review proposed resources and effective private permissions before approval. Keep **Global Player Registration** (`#tournament-registration`) separate from **Team Registration** (`#team-registration`). A registered-player role is not consent or tournament eligibility.
5. Apply only the exact approved changes. If interrupted or rate-limited, follow the displayed retry period and **Resume setup** using saved receipts rather than making duplicate channels.
6. After **Setup Complete**, verify real Discord resources. Open **Server settings**, **Discord Settings (Global)** and division/tournament overrides. Setup itself does not create tournaments or approve players.

**Full screenshot-led procedure:** [Discord setup wizard]({{ '/guides/server-setup/' | relative_url }}).

## 4. Organiser: create and schedule a tournament

1. Select your server → **Dashboard → + Create tournament**.
2. **Basics:** Enter a **Tournament name**, choose a **Bracket format** (double elimination, single elimination or round robin), **Maximum approved teams** (**2–16**), an optional **Division**, whether this is a captain-draft event and whether it repeats weekly.
3. Optionally select **Require Individual Player Acceptance**. It is off by default and separately feature-gated. Where enabled, **every listed captain, starter and substitute personally accepts**; a captain declaration and administrator approval do not replace that action.
4. **Schedule:** Set the **Tournament timezone** before day/time entry, **Every** weekday for recurring events, **Start time**, **Registration opens**, **Close registration (minutes before start)** and **How teams return each week** (**New application every week** / **Prefilled roster; captain must check in**).
5. **Tournament Rules:** Enter and preview rules (mandatory if requiring individual acceptance). **Rules and individual-acceptance policy are permanently locked at creation**; their later change requires an authorised cancellation/replacement, preserving old evidence.
6. **Discord:** Verify destinations inherited from server/division and choose optional series overrides. Creating the tournament is not itself a public bracket/announcement send.
7. **Review:** Confirm the permanent lock, check optional per-round game/placement formats, verify all settings and choose **Create tournament** once.
8. Return to **Dashboard → Manage Tournament**, review registration and readiness, approve teams, set seeds and generate the bracket when eligible. Registration closing alone does not create a bracket.

**Full procedure:** [Creating tournaments]({{ '/guides/tournament-creation/' | relative_url }}) — based on the supplied **30-step, 23-page PDF**.

### Series versus occurrence changes

Schedule changes to the recurring series differ from changes to one occurrence. **Cancel Tournament** preserves the selected event's protected history; **End Recurring Tournament Schedule** stops future scheduling but does not automatically cancel an already-active occurrence. Tournament rules and individual participation policy cannot be edited after creation.

## 5. Organiser: fixed teams, approval, confirmation and rollover

### First-time registration and approval

1. Publish an authorised **team-registration invitation** in Discord or provide the secure registration link. The global player-registration message is separate.
2. The captain submits a team name, five starters (including themselves), up to two substitutes and a required **captain declaration**. It is **not independent acceptance by teammates**.
3. Open **Manage Tournament → Teams → Approval queue**. Filter **pending / approved / rejected / withdrawn / all**, compare the current revision and **Previous completed week**, and inspect verified captain/roster identities.
4. Choose **Approve** or **Reject**, giving the reason where prompted. Check **Approval history**. A revised roster generally needs reapproval; a previous approved snapshot remains protected.
5. Recheck event readiness. Attendance, division, capacity, personal global registration and optional tournament-specific player acceptance remain independent conditions. Valid completed draft rosters are approved by their draft workflow.

Read [Team captain registration]({{ '/guides/team-registration/' | relative_url }}) and [Approving teams]({{ '/guides/team-approvals/' | relative_url }}).

### Returning teams and weekly confirmation

For recurring fixed teams, choose **New application every week** or **Prefilled roster; captain must check in** at creation. An unchanged, safely carried approved roster may retain approval, but the captain must **CONFIRM PARTICIPATION** for each week. Changed rosters/captaincy may need fresh review. Check **Teams → Review & Resolve** for identity/division holds. **WITHDRAW FROM THIS TOURNAMENT** skips only that occurrence; **LEAVE RECURRING COMPETITION** stops future automatic entries. Historical rosters/results remain preserved.

## 6. Captain: registration, participation and rosters

1. Open **#team-registration** in the correct Discord community, then choose **Create a new team** or **Update current team**. Sign in as the actual captain and check server/tournament.
2. Enter **Team name**, your five-person starting lineup and up to two optional substitutes. Search for the correct Discord accounts or use **Enter Discord User ID** where necessary.
3. Expand **Review proposed roster before submission**. Read **Terms**, **Privacy Policy**, **Player Information Notice** and tournament rules. Make the captain declaration only if its conditions are accurate.
4. Select **Register Team**; submission is **pending administrator approval**, not acceptance into the bracket.
5. For a recurring team, open **My Teams**, check the next event and **CONFIRM PARTICIPATION** for that occurrence before its deadline. Roster approval, attendance and enrollment are distinct.
6. Use **Edit team members** where available; changes may require reapproval. Withdrawal from one tournament differs from leaving the recurring competition.
7. Where **Individual Player Acceptance** is required, every listed player must personally satisfy global registration and this event's immutable rules. The captain cannot do it for them.

See the [eight-step screenshot guide]({{ '/guides/team-registration/' | relative_url }}) for each field and declaration.

## 7. Organiser and captains: draft-pool tournaments

1. In Discord, organisers configure a **Draft Waiting Room** voice channel and create a draft tournament. Anyone wishing to enter the free-agent pool joins that waiting room; selected captains are explicitly excluded from the free-agent pool.
2. The organiser opens the event's **Captain Selection** tab, adds or verifies captains in the server-scoped registry, and selects the intended captains using **checkboxes**. The selected team names can be edited in **Teams**. The registry persists across draft events and keeps deactivated-captain history.
3. Selecting captains creates a private **Draft Captains** voice room. Selected captains are moved/allowed there; other players remain in the waiting room.
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

For **game-based fixtures**, a winning captain reports each individual game's victory, attaching one scoresheet. The opposing captain **confirms** the winner or **disputes** with a reason. A dispute stops that game and requires an authorised organiser decision in **Matches → Game reports and disputes**. The opposing captain can supply one optional dispute document.

If a confirmed game was recorded incorrectly, the organiser can use **Confirmed and corrected games** to preview a reasoned correction, attach optional evidence, review downstream impact and approve required consequential changes. Correction history is append-only; previously confirmed games and original scorecards are retained. A corrected BO3 may reopen 2–0 to 1–1, and voided downstream matches require new replay fixtures rather than silent score edits. The Bracket, standings and historical Discord result publications follow the effective confirmed game history. Restricted match evidence must never be posted publicly.

## 9. Captain: report games, confirm results and upload evidence

### Report and confirm individual games

1. Sign in using the correct Discord captain account. Open **My Matches** in the sidebar (or `/app/my-matches`) to see assignments **across your eligible servers**; opponent confirmation requests appear first. Select the right tournament and open match. Registration does **not** need to be open for an authorised captain to report an active match.
2. For each game your team **won**, select **Report Game Victory**, attach **exactly one** PNG/JPEG/WebP/PDF scoresheet (**up to 10 MB**), then submit. A losing captain must not report a game victory.
3. The opposing captain reviews the displayed winner and secure evidence. Select **Confirm game result** (no second upload needed), or enter a reason and select **Dispute game result**. A dispute pauses progression; the opponent can optionally upload **one supporting scoresheet**.
4. The winner/series progress updates only after confirmation or an authorised administrator resolution. Continue through the required BO1/BO3/BO5/BO7 game wins. Confirmed results drive bracket advancement, Discord scorecard publication and Grand Final/reset progression.
5. If a game is wrong after confirmation, ask an organiser to use the protected correction/impact-preview workflow. Do not submit a fabricated victory to compensate for a mistake.

**Evidence privacy:** game documents are available only through authorised captain/organiser controls. The app preserves original/corrected game evidence for audit and uses planned retention rules; evidence is not a public image gallery.

## 10. Organiser: Discord Publisher and announcements

Open the selected event's **Discord** tab or **Edit Discord**. Bracket, Teams and Announcement use event-specific modes such as **Do not publish, Automatic PNG, Manual PNG, Custom Embed** and **Plain Message**, where supported. **PR #42 was merged on 20 October 2026**, restoring default automatic bracket/team PNG publication for eligible new occurrences, ladder PNG and private recap actions, while respecting explicit saved off/manual/custom settings. Confirm the **deployed revision and actual saved publishing mode** rather than presuming defaults.

- **Team roster images:** Publish only approved snapshots; inspect actual PNG text and players before sharing.
- **Registration messages:** Global legal registration/verification is distinct from tournament captain applications.
- **Post-event recap:** Organiser reviews and approves the official public winner announcement. Reminders/actions do not automatically publish champions.
- **Delivery:** Safe receipt reconciliation prevents blind duplicate sends; a Discord 429 or missing image text needs diagnosis, not repetitive sending.

## 11. Organiser: divisions, promotion and team management

In **Server Management → Divisions**, choose **Create a division**, enter its name and optionally set Discord channel overrides. Under **Division rules**, use **Move up/Move down** to rank divisions, select an optional recurring non-draft **Division Championship series**, choose **Automatic promotion/relegation** (**1–3 teams** each) and decide whether to post updates to the effective results channel. **Save rules**; changing an established Championship requires explicit reason and confirmation.

Under **Team memberships**, first enter **Division override reason**, find the team and select its new Division. Transfers apply to **future** registrations; they do not rewrite historical rosters/brackets/results. Review **Recent team transfers** and unresolved holds before readiness. Draft and unrelated events do not automatically affect qualifying ladders.

**Complete procedure:** [Adding and configuring divisions]({{ '/guides/divisions/' | relative_url }}). Separately use **Team management** to handle captain ownership, transfer/retirement and reusable memberships.

## 12. Spectators: viewing tournaments without an organiser account

Use an organiser-shared **public tournament URL**. Open **Bracket** for match progression, **Ladder/Standings** for placements and **Match Results** for confirmed scores. Published completed tournaments may remain accessible; private, unlisted or restricted events may not. **Browse Tournaments** does not enumerate everyone’s Discord communities. Player names and approved lineups may be visible, but scoresheet files, pending rosters, private draft pools and admin data are not meant for public access.

## 13. Troubleshooting and common questions

| Symptom | What to check / next action |
| --- | --- |
| **Server missing** | Signed into correct Discord account? Is Bracket Control bot/server integration active? Do you actually belong to the hosting server? Use the server chooser, then retry. |
| **Administrator access required** | An authorised server administrator/organiser must grant the relevant role. Discord sign-in by itself is insufficient. |
| **Captain link denies access** | Use the account currently verified as captain, remain in the hosting server, and follow the current event link. Expired or replaced links may be invalid. |
| **Cannot confirm this week** | Registration window may be closed, attendance already expired/withdrawn, or a division/rollover hold blocks the team. Ask an organiser; reopening alone does not confirm. |
| **Roster approved but not in bracket** | Also check attendance, division, capacity, deadline, current revision and readiness. |
| **Waiting-room member not moved** | Check that the bot has Discord voice permissions, the member is connected in a managed room, and the draft is at the relevant stage. Moves retry on voice/worker reconciliation. |
| **Scoresheet upload rejected** | For each game victory, upload **one** PNG/JPEG/WebP/PDF scoresheet up to **10 MB**. Check the match state, current captain permission and upload limits. Renaming an invalid file does not make it valid. |
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

## 15. Release notes and verified documentation scope — 29 October 2026

| Feature | Status when this page was updated |
| --- | --- |
| Global Player Registration | **PR #67 merged**; separate release flag/actual production state still matters. Separate from team registration. |
| Base Discord Setup Wizard | **PR #68 merged**, feature-gated; follow the wizard shown in the running app. |
| Expanded Discord wizard and native Support Tickets | **PR #75 open and staging-only**; 14-step screenshot PDF is *not* production confirmation. |
| Individual tournament rules acceptance | **PR #69 merged**, separately gated; rules/policy cannot be changed after creation. |
| Automatic Bracket/Teams PNG and recap actions | **PR #42 merged**; verify deployment and saved per-event overrides. |
| Simplified wording and cleanup | **PR #72 merged**; screenshot labels may differ from later builds. |

This wiki is maintained against reviewed repository source and the three operator-provided PDFs, **not** an independently verified production SHA. No change to a public guide is proof of live Discord acceptance, legal approval, age-eligibility enforcement or a deployed release. Tier-based skill balancing and automatic Valorant/Fortnite statistics remain future proposals, not current creation controls.
