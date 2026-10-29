# HisseRadar Privacy Policy

Last updated: October 29, 2026

HisseRadar is an educational app that teaches stock chart patterns in short lessons and lists, every trading day, the BIST and US stocks that match those patterns. The app is developed by Kadir Yiğit.

## In short
- There are no accounts. The app never asks for your name, email, phone number, location, contacts or photos.
- There are no ads and no analytics or tracking tools.
- Everything you enter in the app is stored only on your device. The one exception: If you turn on stock notifications, the ticker symbols of the stocks you follow are sent to Google Firebase so that notifications can be delivered.
- For notifications, Firebase Cloud Messaging (Google) uses a device token; details below.

This text is also the privacy notice required by the Turkish Personal Data Protection Law (KVKK, Law No. 6698) and the Communiqué on the Procedures and Principles for Fulfilling the Obligation to Inform.

## Data controller
Under the Turkish Personal Data Protection Law (KVKK, Law No. 6698), the data controller is **Kadir Yiğit**, the individual who develops the app on his own. Contact: yyggttkadir@gmail.com

## Personal data processed, purpose and legal basis
The only data in the app that may count as personal data relates to notifications and is processed only when you turn a notification on:

| Data | Purpose | Legal basis | How it is collected | When it ends |
|---|---|---|---|---|
| Firebase notification token | Delivering the notifications you turned on to your device | Explicit consent (KVKK Art. 5(1)) | Automatically, by the Firebase library on your device when you turn a notification on | When you turn notifications off or delete the app |
| Firebase installation ID | Keeping the token tied to the right device | Explicit consent (KVKK Art. 5(1)) | The same way, automatically | When you turn notifications off or delete the app |
| Ticker symbols of the stocks you follow (only if you turn on stock notifications) | Notifying you when a stock you follow reaches its first target | Explicit consent (KVKK Art. 5(1)) | When you turn on "Stock notifications" in Settings, through one notification topic subscription per stock | When you turn stock notifications off, unfollow the stock, revoke notification permission or delete the app |

These identifiers are used only for notifications; they are not processed for advertising, profiling or any other purpose. Turning a notification on is your explicit consent to this processing; you can use the rest of the app without turning any notification on.

If you turn on stock notifications, the ticker symbols of the stocks you follow are sent to Google Firebase so that notifications can be delivered. Stock notifications are off by default. Apart from that, the data kept on your device (watchlist, lesson progress, virtual and real portfolios, settings) never reaches the developer or any other server. For that reason it is not personal data processing on the developer's side; only you can see it and only you can delete it.

## Stored on your device
The following are kept on your phone, in the app's own storage. Unless you turn on stock notifications, none of it is sent to any server:

- Lesson progress and quiz scores
- Your watchlist and the named lists you create (if you turn on stock notifications, only the ticker symbols are sent to Google Firebase as notification topics; list names are not sent)
- Your virtual portfolio (virtual cash, virtual trades and their history)
- Your real portfolio: The share count and average cost you enter
- Badges and day streak
- Settings (theme, time horizon preference, the notifications you turned on)

Deleting the app deletes this data. We do not hold a copy, so it cannot be restored.

## Internet use
The app downloads scan results, chart data and history records as public JSON files from GitHub Pages (GitHub, Inc., USA): kadiyyggtt.github.io/hisseradar-veri. No account or device identifier is sent with these requests; the result is the same for everyone. As with any internet request, GitHub, which hosts the files, sees your IP address and basic device information (user agent) when serving them and handles that under its own privacy statement. The app has no connection to any brokerage, bank or payment system.

## Notifications (Firebase Cloud Messaging)
Notifications are delivered through Google's Firebase Cloud Messaging. For this, Firebase creates a device-specific **notification token** and a **Firebase installation ID** and keeps them on Google's servers. These identifiers are not linked to your name, email or any account, and they are not used for advertising or tracking. We run no server that stores tokens: your device only subscribes to the "topics" you turn on, and messages are sent to those topics.

Topics and where to turn them off:

- **Scan notification:** When a pattern has a new match. Turned on and off with the switch on that scan's screen.
- **Stock target notification:** When a stock you follow reaches its first target. Off by default; turned on and off with the "Stock notifications" switch in Settings. If you turn it on, the ticker symbols of the stocks you follow are sent to Google Firebase so that notifications can be delivered: your device subscribes to one topic per stock, such as "hedef-BIST-THYAO", and Google knows which device is subscribed to which topic. Unfollowing a stock leaves that stock's topic; turning the switch off leaves all stock topics.
- **Morning briefing:** Weekday mornings. Turned off in Settings.
- **Weekly summary:** Sundays. Turned off in Settings.

On Android 13 and later, the app asks for notification permission when you first turn a notification on; you can revoke it at any time in your phone's settings. The app checks the permission every time it opens or comes to the foreground; without permission it leaves all topics. Deleting the app invalidates the subscriptions and the token.

## Transfer abroad
The notification token, the installation ID and, if you turned on stock notifications, the topic subscriptions for the ticker symbols you follow are processed on the servers of Google LLC (USA) for Firebase Cloud Messaging. Under Article 9 of the Turkish Personal Data Protection Law (KVKK, Law No. 6698), this transfer abroad is based on your explicit consent (Art. 9(6)(a)). The risk you should know about: the Turkish Personal Data Protection Board has issued no adequacy decision for the USA, and the data may be subject to US law there. Turning a notification on is your consent to this transfer; when you turn all notifications off or delete the app, the transfer stops.

Scan data is downloaded from GitHub Pages (GitHub, Inc., USA); no account or device identifier is sent with that request. The developer does not receive or keep the IP address GitHub sees when serving it.

## Retention
The notification token, the installation ID and the topic subscriptions stay on Google's servers for as long as notifications are on. They become invalid when you turn notifications off or delete the app. The developer keeps no records at all: there is no server that stores tokens, IP addresses or usage information.

## Your rights under the Turkish Personal Data Protection Law (KVKK, Law No. 6698)
Under Article 11, you may apply to the data controller to:

- Learn whether your personal data is processed
- Request information about it if it is
- Learn the purpose of processing and whether it is used for that purpose
- Know the third parties in Turkey or abroad to whom it is transferred
- Request correction if it is incomplete or inaccurate
- Request erasure or destruction under the conditions of Article 7
- Request that correction and erasure be notified to the third parties it was transferred to
- Object to a result against you that arises solely from analysis by automated systems
- Claim compensation if you suffer damage because of unlawful processing

**How to apply:** Send your request by email to yyggttkadir@gmail.com; the other channels listed in the Communiqué on the Procedures and Principles of Application to the Data Controller (written application, registered electronic mail) are also valid. You will receive an answer free of charge within 30 days at the latest. Because the developer does not hold your token, he cannot identify you; the fastest way to delete notification data is to turn notifications off or delete the app.

If your request is rejected, you find the answer insufficient, or you get no answer within 30 days, you may file a complaint with the Turkish Personal Data Protection Board (KVKK Art. 14).

## Backup file
When you choose "Back up" in Settings, your watchlist, lesson progress, virtual and real portfolios and settings are written to a single file. You choose where to save it or whom to send it to; the app never uploads it to any server. If you share the file, you share its contents.

## Share card
When you tap "Share card" on a stock screen, the pattern card is turned into an image on your device and your phone's share sheet opens. You choose where the image goes. If you save the image to your photos on an iPhone, only permission to add photos is requested; your photo library is not read.

## Listening to lessons
The "Listen" option reads the lesson text with your device's own speech engine. The app sends neither the text nor any audio to a server, and the microphone is not used.

## Ads and purchases
This version contains no ads, no analytics and no purchases. If any are added, this policy will be updated beforehand and announced inside the app.

## Children
The app is intended for adults; it is not directed at anyone under 18 and no data is knowingly collected from anyone under 18.

## Not investment advice
Lessons and scan results are for education only and are not investment advice. Trading decisions and their outcomes belong to the user.

## Changes
If this policy changes, this page and the date at the top are updated.

## Contact
yyggttkadir@gmail.com
