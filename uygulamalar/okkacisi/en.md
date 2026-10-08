<!-- PUBLISHED AT — use this URL in store forms.
     English:  https://kadiyyggtt.github.io/gizlilik/uygulamalar/okkacisi/en.html
     Turkish:  https://kadiyyggtt.github.io/gizlilik/uygulamalar/okkacisi/tr.html
     This file is the source; the site is published from ~/Desktop/gizlilik.
     After editing here: bash ~/Desktop/gizlilik/yenile.sh -->

# Arrow Escape (Ok Kaçışı) — Privacy Policy

**Last updated:** 8 October 2026

Arrow Escape is a puzzle game. This page explains plainly which
information the game touches and which it does not.

**Short answer:** No account, no sign-up, no server of ours. This version
has **no ads and no in-app purchases.** We collect no information and the
game plays offline. The one exception is the optional **Google Play
leaderboard**: if you sign in with Play Games, your progress numbers and
gamer identity go to Google (see below).

---

## What we do not collect

The game does **not ask for or collect:**

- Name, email, phone number, date of birth
- Location
- Contacts, calendar, photos, files
- Camera or microphone
- Advertising ID or any other device identifier
- Usage statistics, crash reports, analytics

There is **no** account system and **no** server of ours. No third-party
advertising, measurement or analytics library is included. (The optional
Google Play leaderboard's own diagnostics data is described below.)

## Permissions

**You are not asked for any permission.** Location, camera, microphone,
contacts, photos and storage are never requested. On iOS there is no
"allow tracking" prompt — no tracking takes place.

Technical permissions that may appear on the store page are granted
automatically by Android at install time without a prompt:

| Permission | Why |
|---|---|
| Vibration | A short buzz when an arrow collides and when a level ends — can be turned off in Settings |
| Audio settings | So game sounds do not interrupt your own music |
| Internet | Only for the optional Google Play leaderboard (in versions where it is switched on) — the game itself works offline and connects nowhere else. The permission ships with Expo's standard components |
| View network connections | Comes from the audio playback library (AndroidX Media3); the game does not read this information or send it anywhere |
| Prevent phone from sleeping | Comes from the same audio library; the game does not use it and plays no sound in the background |

The package also contains an internal permission defined by Android's own
library for in-app security (`…DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION`);
you are never asked for it and it opens nothing to other apps.

Android's advertising-ID permission (AD_ID) is **explicitly blocked** in
the app.

---

## Internet

The game works offline: levels are generated on your phone and your
progress is stored on your phone. Only the Google Play leaderboard (if you
signed in with Play Games) goes online; while offline a score is silently
skipped and the game never waits.

---

## Google Play leaderboard (optional)

On Android, Arrow Escape can use the Google Play Games Services **leaderboard**
(daily, weekly and all-time; top 10 and your own rank). This feature is
**optional**: if you do not sign in with your Google Play Games account,
nothing is sent and the game stays entirely on your device, as before.

If you do sign in, according to Google's own disclosure
(developer.android.com/games/pgs/data-collection):

- Your **gamer identity** (Play Games gamertag and avatar) is shared with
  this game and shown on the leaderboard.
- Your **scores** (the highest level you have completed and your total stars) are sent to Google's servers and shown on the
  leaderboard.
- Play Games Services collects **analytics and diagnostics** data to keep
  its own SDK stable.
- Data is **encrypted in transit using HTTPS**.
- **You choose** who can see your profile (everyone / friends only / only
  you) in your Play Games settings.
- You can **delete** this data from your Play Games profile
  (play.google.com/games/profile) or your Google Account
  (myaccount.google.com).

This data **goes to Google, not to us**: we never see your e-mail address,
real name or location. Google's processing is governed by the Google
Privacy Policy (policies.google.com/privacy).

The iOS version has no leaderboard; nothing is sent there.

---

## What is stored on your device

Only **on your own device**:

- Which level you reached and your stars per level
- The moves, lives and hints used in a level you left unfinished
  (so you can continue where you stopped after closing the app)
- Your settings (sound, vibration, language)

None of this is sent anywhere (only the leaderboard numbers above go to
Google, if you signed in). **Settings → Reset game** deletes all of
it; uninstalling the game removes it entirely.

---

## Future versions

If a later update adds advertising or any other feature, this policy will
be changed **before** that update is published, and the change will be
described here.

---

## Children

Arrow Escape is not presented as an app made for children; we collect no
personal data and there are no ads; the leaderboard is optional and sends
nothing unless the player signs in to Google Play Games.

---

## Your rights

We hold no personal data about you, so there is nothing to delete,
correct or export on our side. You can reset your progress in the game or
uninstall it to remove everything, and delete leaderboard data from your
Play Games profile or your Google Account.

## Contact

Questions: **yyggttkadir@gmail.com**
