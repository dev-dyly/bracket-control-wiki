# Production documentation review — 2 November 2026 (Pacific/Auckland)

This file is excluded from the public website. It records evidence, rather than adding implementation details to user instructions.

## Production identity

- Application repository: https://github.com/dev-dyly/Bracket-App
- Reviewed commit: `6647a77d12f75f40201e012eedf604ad457aa2e8` (latest successful production deployment when reviewed).
- Repository package version: `2.0.0`. The commit is the more precise release identifier; do not describe it as an unverified newer numbered release.
- GitHub deployment `7466427969`, environment `Bracket App / production`, reports success at `2026-11-01T00:31:26Z`. The Cloudflare Pages check on the same commit also reports success.
- Production health at `https://app.devdylnz.com/api/health`: `ok: true`.
- Production presentation metadata at `https://app.devdylnz.com/api/auth/me` confirms `tournamentRulesRequired`, `individualParticipation`, `globalPlayerRegistration` and `serverSetupWizard` are all enabled. No session was used.
- Served entry asset: `/app/assets/index-svh6KXK7.js`. Read-only inspection of 45 linked production JavaScript assets confirmed the 19 UI labels checked by `probe_production.py`, including optional-channel setup, draft captain selection, reporting, corrections, transfers and retirement.
- Source review used a separate detached checkout at the deployed commit. The user's application workspace contains unrelated uncommitted work and was not edited, committed or deployed.

## Evidence supporting guide changes

All paths below refer to the reviewed application commit.

| Area | Source evidence | Documentation decision |
| --- | --- | --- |
| Setup and channel requirements | `shared/serverSetup.js`, `frontend/src/pages/ServerSetup.jsx`, `backend/src/services/serverSetup.js` | Only Global Player Registration is mandatory; optional destinations use Not Required. Manual Setup uses existing resources, safe existing role and explicitly selected messages. |
| Connection and navigation | `frontend/src/pages/ServerManagement.jsx`, `components/ServerManagementMenu.jsx`, `components/Shell.jsx` | Use current Connect server, Invite bot, Connect installed bot, Open Server Setup, server menu and Profile labels. |
| Registration and acceptance | `pages/GlobalPlayerRegistration.jsx`, `pages/PlayerRegistration.jsx`, `pages/MyParticipation.jsx`, `components/IndividualParticipation.jsx` | Global registration is distinct from tournament association, attendance, approval and personal rules acceptance. |
| Tournament creation | `pages/Dashboard.jsx`, `components/TournamentRules.jsx` | Five creation steps, 2–16 teams, optional divisions, independent drafts, rules and individual-acceptance policy fixed at creation. |
| Captain registry and draft | `components/DraftCaptainSelection.jsx`, `pages/AdminPanel.jsx`, `pages/LeaderDashboard.jsx`, `components/DraftTeamStatus.jsx` | Explicit captain selection, website picks, 2/1/2/1 stages, reserved starter picks and automatic approval of valid completed rosters. |
| Voice behaviour | `backend/src/services/draftVoice.js`, `draftCaptainsVoice.js`, `draftVoiceGateway.js`, `voicePool.js` | Private captain room; team rooms copy waiting-room permission overwrites. Do not promise private per-team access. Moves require connected recognised members in appropriate source rooms. Cleanup can defer. Manage Channels, Manage Roles, View Audit Log, Connect and Move Members are relevant. |
| Results and evidence | `components/GameMatch.jsx`, `GameResolutions.jsx`, `GameCorrections.jsx`, `backend/src/services/gameDiscord.js` | Winning captain supplies one game scoresheet, opponent confirms without another file, disputes pause progression, confirmed evidence is published to configured results channel. Correct false blanket claims that scoresheets cannot be seen by spectators. |
| Discord publication | `components/TournamentDiscordMenu.jsx`, `TournamentDiscordPublisher.jsx`, `DiscordDelivery.jsx`, `backend/src/services/manualDiscord.js` | Separate per-tournament actions, saved format/destination, automatic versus manual bracket posts, completion requirements for final standings and non-draft weekly ladder. |
| Divisions | `pages/ServerDivisions.jsx`, `backend/src/services/divisions.js` | Eligible division tournament winner moves one division upward on completion; remove nonexistent championship selector, relegation/promotion counts and manual override-reason field. |
| Team lifecycle | `pages/MyTeams.jsx`, `components/CaptainEnrollment.jsx` | Weekly attendance is separate from approval and recurring participation; transfer requires recipient acceptance and organiser approval; retirement preserves history and ends future participation. |

Claim Rank is the user's requested community channel naming convention. It maps to the existing Match Results destination; no separate feature was inferred.

## Preserved material and boundaries

- All three original illustrated PDFs and image assets are preserved, as are their direct URLs. Current web guides take precedence for interface instructions; illustrated references explicitly warn that screenshots may show earlier screens.
- The three former PDF-redirect pages are now normal guides with the common layout. Navigation never opens a PDF automatically.
- Legal agreements, privacy notices and immutable historical policy versions are retained without changing the application's acceptance documents. These are policies, not step-by-step user guides. In particular, the existing Terms of Service describes rule revision capabilities more broadly than the current locked creation workflow; current guides describe only the available controls. A legal-policy revision and coordinated document-version rollout were not performed as part of this documentation-only change.
- No real production tournament, registration receipt, report, Discord message, role, channel, database record or infrastructure setting was created or changed to test these instructions.
- Read-only source and served-asset verification establishes deployed implementation and labels, not successful execution for every Discord server. End-to-end Discord role assignment, private captain room creation, player moves/cleanup, actual result delivery and authenticated organiser/captain interactions were not exercised. Existing server permissions and connectivity must be checked by each organiser.
- Browser visual/interaction checks were unavailable: local browser control is disabled, and native Firefox access was stopped because Windows browser URL policy enforcement is unsupported. Do not claim completed desktop/mobile screenshot or click testing. Responsive CSS and generated structure were checked; the existing design is retained, with a scrollable desktop contents panel and existing mobile stacking.

## Validation and publication

- Jekyll 3.10.0 strict-front-matter build.
- `python _internal/check_docs.py`: all rendered pages, internal links and anchors, reciprocal ordered navigation, explicit PDF references and unchanged PDF SHA-256 values.
- `python _internal/probe_production.py`: healthy production, four enabled features, 45 served assets and 19 UI labels.
- `git diff --check`.
- Publishing target: existing wiki repository `main`, root, custom domain `docs.devdylnz.com`.
- After push, verify the Pages build references the new commit and returns `built`, then run `python _internal/check_docs.py --live` against the custom domain. Do not claim publication based on a successful push alone.
