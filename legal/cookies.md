---
layout: default
title: Cookie Notice
permalink: /legal/cookies/
---
# Cookie Notice

**Effective: 22 October 2026**

Bracket Control / Dev Dyl NZ (NZBN **9429054041851**) uses browser cookies and session storage for Discord sign-in, account security and tournament navigation.

## Essential application cookies

| Cookie | Purpose | Typical expiry |
| --- | --- | --- |
| `bc_session` | Keeps an authenticated session active after Discord sign-in. | Up to **24 hours** |
| `bc_oauth_state` | Protects and links an OAuth sign-in attempt to the correct browser. | Up to **10 minutes** |

In the reviewed application source both cookies are `HttpOnly` and `SameSite=Lax`, with the `Secure` attribute when running in production mode. The session cookie has path `/`; the OAuth state cookie has path `/api/auth` and is cleared on callback. Signing out ends the application session.

These cookies are for **authentication and security**, not advertising. Preventing them from working can stop Discord login or protected tournament features.

## Other browser storage

The app uses an in-memory CSRF token for signed-in requests, not a separate CSRF cookie. Browser `sessionStorage` can remember a chosen server, tournament or certain older interface preferences; it is not an ordinary cookie.

The reviewed application source does not intentionally install advertising or analytics tracking tags. If optional tracking is introduced, this notice and any legally required choice mechanisms must be updated first.

## Discord and hosting providers

Opening the Discord login page means Discord's own cookie and privacy practices apply. Cloudflare and other providers can use security or delivery technologies according to their settings. Their cookie names and lifetimes can vary.

This inventory reflects the reviewed application source; **a full independent inspection of every live browser and third-party cookie has not been completed**.

## Your choices and contact

Your browser can show, block or delete cookies and site storage. Blocking essential storage may prevent login. Use **Sign out** to end your session.

For more information contact **privacy@devdylnz.com** or read the [Privacy Policy]({{ '/legal/privacy/' | relative_url }}) and [Terms of Service]({{ '/legal/terms/' | relative_url }}).
