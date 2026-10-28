---
layout: default
title: Draft tournaments
permalink: /guides/drafts/
---
# Draft tournaments: live picks and Discord voice

1. **Organiser:** Create a draft tournament and configure the **Draft Waiting Room** in Discord. Players join that waiting room to form the free-agent pool.
2. **Organiser:** Open **Manage Tournament → Captain Selection**. Verify or register captains within this Discord server; use **checkboxes** to confirm who captains. Captains aren't counted as free agents. Team names can be edited in the **Teams** tab.
3. **Bot:** Create a private **Draft Captains** voice room for selected captains. They are permitted into this room; ordinary free agents stay in the waiting room.
4. **Organiser:** Open **Live Draft**, check ready players and start the draft.
5. **Captains:** Sign in to the captain web portal. When the UI says **YOUR TURN TO PICK**, click an available player's button. The system follows **2 / 1 / 2 / 1** picks; once the starting lineup is complete, an optional **PASS REMAINING OPTIONAL PICKS** action may appear.
6. **Bot:** Once finished and valid, auto-approve draft rosters, create one team voice channel per captain, then move currently connected assigned members from managed waiting/captains rooms to the correct team room. Disconnected players are not force-moved from other rooms.
7. **Organiser:** Check roster readiness, generate the bracket and run matches. Temporary channels are removed conservatively after completion/cancellation when safe; occupied rooms may remain until cleanup can succeed.

**Permissions:** The bot needs View Channel, Connect, Move Members, Manage Channels and View Audit Log; the private captains room also needs Manage Roles to adjust channel permissions. This uses Discord voice-state presence, **not an audio recording or voice draft call**.
