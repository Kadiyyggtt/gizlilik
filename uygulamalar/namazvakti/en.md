<!-- YAYIN ADRESİ — mağaza formuna bu yazılacak.
     Türkçe:   https://kadiyyggtt.github.io/gizlilik/uygulamalar/namazvakti/tr.html
     English:  https://kadiyyggtt.github.io/gizlilik/uygulamalar/namazvakti/en.html
     Bu dosya aslı; site ~/Desktop/gizlilik deposundan yayımlanıyor.
     Burada değiştirdikten sonra: bash ~/Desktop/gizlilik/yenile.sh -->

# NamazVakti — Privacy Policy

**Last updated:** 12 September 2026

This policy applies to the **NamazVakti** application.

---

## In short

**NamazVakti collects, stores and shares no personal data.**

Your location is used only inside your device, to calculate prayer times, and
**is never sent anywhere**. You do not need to register, no account is asked
for, and no advertising is shown.

---

## Location

Prayer times are calculated from your latitude and longitude, which is why the
app asks for location permission.

**What happens to your location:**

- It stays inside your device. The calculation runs entirely on your phone,
  using the `adhan` library.
- **It is never sent to a server of ours.** There is no server the app sends
  location data to.
- **One exception, the place name:** to show a city name such as "Istanbul" on
  screen, the coordinates are passed to your phone's own address lookup
  service (Google on Android, Apple on iPhone). This is the operating
  system's standard service; we see nothing of that request and the answer
  stays on your device. Offline, no place name is shown and the times are
  still calculated.
- Only the most recently used location is kept on the device, so that you are
  not asked for permission every time you open the app.
- Deleting the app deletes this information with it.

**If you deny permission:** the app keeps working; you select your location
manually to see the times.

## Internet use

The app's **core features work without internet:**

- Prayer times are calculated on the device
- The qibla direction is calculated on the device
- The Quran text, translation, transliteration, Names of Allah, supplications
  and the verse of the day are stored on the device

Internet is used for **one thing only**: listening to surah recitations. The
audio files are served from `mp3quran.net`. Unless you play a recitation, the
app connects to no server at all.

During that request only the identity of the requested surah is sent; no
identity, location or personal information is transmitted.

## What stays on your device

The following is stored only on your phone:

- The most recently used location
- Calculation method and madhab preference
- Time adjustment settings (± minutes)
- Translation preference
- Adhan and notification settings

This information is **never sent anywhere** and is deleted together with the
app.

## Notifications

Prayer time notifications are scheduled **on your device**. They are not sent
from a server; no push notification infrastructure is used. If you do not want
notifications, you can turn them off in your phone settings.

## Data we do not collect

- Name, email address, phone number
- Account or sign-in information
- Contacts, photos, files
- Usage statistics, analytics, or crash reports **sent to us**
  (the technical log described below never leaves your device)
- Advertising identifier

## The technical log that stays on your device

If Namaz Vakti closes unexpectedly, a short technical log of what happened is kept
**on your phone only**. It is never sent anywhere and never reaches any
server.

- You can read it yourself under **Settings → Technical Log**.
- You can delete it there with a single tap.
- E-mail addresses, the user name inside file paths and long digit
  sequences are stripped out as it is written.
- At most 10 entries are kept; the oldest is dropped when a new one arrives.

There is no automatic way to send it to us. If you want to, you can copy
the text and send it yourself — the choice is entirely yours.

This is why the "we never collect" list above stays accurate: the log is
**not collected**, it simply sits on your device.

## Advertising and purchases

- **There is no advertising.** No ad network or tracking tool is used.
- **There are no in-app purchases.** The entire app is free.

## Permissions and why they are requested

| Permission | Why |
|---|---|
| Location | To calculate prayer times for where you are |
| Internet | Only while listening to a surah recitation |
| Notifications | Prayer time reminders |
| Background audio | So recitation continues when the screen is off |
| Motion sensor | So the qibla compass can show which way the phone faces |
| Vibration | A short tap response — can be turned off in Settings |

The app does **not** request **microphone**, **camera**, **contacts**,
**photos** or **storage** permissions.

## Third party services

The app contains no analytics, advertising, remote crash reporting or social media
SDK. The only external connection is to the `mp3quran.net` servers from which
recitation audio is fetched.

## Children's privacy

The app is suitable for users of all ages, and because it collects no personal
data from any user, it collects none from children either.

## Content sources

The sources of the Quran text, translation, transliteration and recitations
are listed openly on the **Sources** screen inside the app.

## Changes

If this policy is updated, the date at the top changes. If the data collection
behaviour changes, that is also stated separately in the app update notes.

## Contact

Questions: **yyggttkadir@gmail.com**
