---
layout: default
title: Organiser guide
permalink: /guides/organisers/
---
# Organiser guide

## 1. Configure the community

Select **Your Discord servers** and open the applicable [Setup Wizard]({{ '/guides/server-setup/' | relative_url }}) or **Server settings**. The merged Stage 2 wizard is feature-gated; the expanded **14-step automatic/manual wizard and native support tickets are only in open, staging PR #75** at this review. Global Player Registration and Team Registration are separate. Check effective staff-only approval permissions, registered-role hierarchy, timezone and channel overrides before applying. An interrupted setup uses the saved-plan recovery rather than duplicate resource creation.

## 2. Create an event

Follow [Creating tournaments]({{ '/guides/tournament-creation/' | relative_url }}): **Dashboard → + Create tournament → Basics → Schedule → Tournament Rules → Discord → Review**. Set format and approved-team cap (2–16), optional division and recurrence, registration dates/timezone, and applicable personal-acceptance policy. **Tournament rules and individual acceptance are permanently locked once created**, so review before confirming. After creation, use **Manage Tournament** for registration, teams, seeds and readiness.

## 3. Manage entries and confirm readiness

In **Teams → Approval queue**, filter pending/approved/rejected/withdrawn, verify captain identity and the current roster against the previous completed week, then **Approve** or **Reject**. Inspect the immutable approval history. The captain's submission is not itself approval. A safely unchanged recurring roster can carry approval, **but attendance must be confirmed every week**. Where personal acceptance is required, each listed player must act individually. Resolve Division holds and readiness blockers before seeding and bracket generation. See [Approving teams]({{ '/guides/team-approvals/' | relative_url }}) and [Divisions]({{ '/guides/divisions/' | relative_url }}).

## 4. Run and complete

Use **Seed** to set eligible team placement, then generate when ready. In **Matches**, review **one-file per-game victory reports**, opposing confirmations, disputes, optional evidence and audited corrections. Older legacy match reports still use two files; use logged correction controls when necessary. Double elimination supports the original grand-final reset, and optional placement games can delay event completion.

## 5. Discord and divisions

For each event, choose its **Discord** publishing mode and effective channel; explicit saved off/manual/custom settings override automatic defaults. **Automatic bracket/team PNG and private recap actions are in merged PR #42**, not open review, but confirm deployed behaviour and image content before posting. The official winner announcement remains an organiser-approved public action.

Use [Divisions]({{ '/guides/divisions/' | relative_url }}) to create/rank divisions, select optional eligible recurring Championships, set 1–3 promotions/relegations and record reasoned team moves. Transfers affect future registrations, not past results.

**Release check (29 October 2026):** The 14-step expanded setup/support-ticket screenshot guide is for **staging PR #75**. Stage 1 Global Player Registration and Stage 3 personal tournament rules acceptance are separately controlled; merged source does not by itself prove those switches are active on the production deployment.
