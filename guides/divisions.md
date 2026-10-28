---
layout: default
title: Adding and configuring divisions
permalink: /guides/divisions/
---
# Add and configure divisions

**For:** Authorised server organisers · **Reviewed:** 29 October 2026.

These steps follow the application's **ServerDivisions** interface. The supplied three PDFs do not contain a separate Divisions screenshot walkthrough.

## Create a division

1. Sign in and select the correct Discord community.
2. Open **Server Management → Divisions**.
3. In **Create a division**, type a unique **Name** (for example, `Division 1 — Premier`).
4. Optionally expand **Discord Channel Settings (Optional)** and select division-specific destinations. Leave values on **Use server default** to inherit the community's settings.
5. Select **Add division**. The new division appears in **Division rules**.

A community may have multiple divisions; **each tournament** still supports **2–16 teams**.

## Configure rank and Championship rules

6. In **Division rules → Choose division**, select the division you wish to edit.
7. Update **Division name** if required. Use **Move up ↑** or **Move down ↓** to set the ladder order. The top division ranks first.
8. Optionally select a **Division Championship series**. The list contains eligible **recurring, non-draft series already assigned to this division**. If none appears, create/assign an appropriate tournament first.
9. Choose **Automatic promotion** and **Teams promoted** (**1–3**) if you want top eligible teams to move up after the designated completed Championship.
10. Choose **Automatic relegation** and **Teams relegated** (**1–3**) if you want bottom eligible teams to move down.
11. Decide whether to **Post promotion/relegation updates to the effective results channel**.
12. Expand **Discord Channel Settings** if this division needs channel overrides; otherwise retain the inherited defaults.
13. Select **Save rules**. If you change or remove an established Championship series, confirm the prompted reason. **Previously completed tournament results remain unchanged.**

**Important:** A Division Championship is optional. Enrolment into an existing recurring division competition does not require every division to have a Championship. Draft and unrelated events do not become qualifying Championship series.

## Assign or move an existing team

14. Scroll to **Team memberships**, enter a meaningful **Division override reason** first (required before a membership change).
15. Use **Find a team** to locate a reusable team profile.
16. Use the **Division for [team]** selector to choose the target division or **Unassigned**. The app records who changed it, when and the old/new division.
17. Check **Recent team transfers** for the recorded action.

Transfers apply to **future registrations**. They do **not** rewrite historical tournament rosters, locked brackets or results. Unassigned recurring teams are flagged for organiser review.

## Connect a tournament to a division

When creating the tournament, select **Division (optional)** in **Basics**, as shown on **page 7** of the supplied *Bracket Control Tournament Creation User Guide*. For a Division Championship, create/assign the recurring series first, then return to **Division rules** and select it.

## Safety and troubleshooting

- **No Championship available:** It must already be a recurring, non-draft series assigned to this division.
- **Promotion/relegation did not run:** Verify that the designated Championship has a qualifying completed result and no protected placement/identity hold remains.
- **Cannot move a team:** Provide an override reason of at least two characters and verify current organiser permission.
- **Delete empty division:** Only unused, empty divisions can be deleted. Preserve associated membership/history rather than deleting to force a transfer.
- **Channel delivery appears wrong:** Check tournament/series overrides before changing global or division defaults.

See [Creating tournaments]({{ '/guides/tournament-creation/' | relative_url }}) and [Approving teams]({{ '/guides/team-approvals/' | relative_url }}).
