<!-- YAYIN ADRESİ — mağaza formuna bu yazılacak.
     Türkçe:   https://kadiyyggtt.github.io/gizlilik/uygulamalar/cumlekur/tr.html
     English:  https://kadiyyggtt.github.io/gizlilik/uygulamalar/cumlekur/en.html
     Bu dosya aslı; site ~/Desktop/gizlilik deposundan yayımlanıyor.
     Burada değiştirdikten sonra: bash ~/Desktop/gizlilik/yenile.sh -->

# CümleKur — Gizlilik Politikası

**Son güncelleme:** 12 Eylül 2026

CümleKur, Türkçe konuşanlar için yapılmış bir İngilizce öğrenme
uygulamasıdır. Bu metin, uygulamanın hangi bilgilere dokunduğunu ve
dokunmadığını açıkça anlatır.

**Kısa cevap:** Hesap açmıyorsun, kimliğini istemiyoruz, reklam yok,
takip yok. Öğrenme ilerlemenin tamamı **yalnız senin cihazında** duruyor.
Tek istisna çeviri özelliği — aşağıda ayrıntısıyla anlatılıyor.

---

## Toplamadığımız şeyler

Uygulama şunları **istemiyor, toplamıyor ve hiçbir yere göndermiyor:**

- Ad, soyad, e-posta, telefon numarası
- Konum
- Rehber, takvim, fotoğraf, dosya
- Kamera ve mikrofon (izin bile istenmiyor)
- Reklam kimliği (uygulamada reklam yoktur)
- Kullanım istatistiği, çökme raporu, analiz aracı

Hesap sistemi **yoktur.** Giriş yapmıyorsun, çünkü giriş yapılacak bir
yer yok.

---

## Cihazında saklanan bilgiler

Şunlar **yalnız kendi cihazında** saklanıyor:

- Kurduğun cümle sayısı, öğrendiğin kelimeler, XP ve günlük serin
- Hangi hata türlerinde zorlandığın (koç ekranının konuşabilmesi için;
  **cümlenin kendisi değil**, yalnız hatanın türü saklanır)
- Tamamladığın kelime setleri ve okuma/dinleme ilerlemen
- Seçtiğin tema, ses ve seviye tercihlerin
- Satın alma yaptıysan, satın almanın kaydı

Bu bilgiler cihazda **şifreli** tutuluyor; şifreleme anahtarı işletim
sisteminin güvenli deposunda duruyor. Hiçbiri cihazdan dışarı çıkmıyor.
Uygulamayı silersen hepsi silinir.

**Kelime veritabanı** (2.818 kelime) uygulamanın içinde gelir ve
tamamen çevrimdışı çalışır.

---

## Çeviri özelliği — internete giden tek şey

Uygulamada "Türkçe → İngilizce" ekranı var. Oraya bir cümle yazıp
çevirtirsen:

1. **Yalnızca yazdığın metin** kendi sunucumuza (Cloudflare Workers)
   gönderilir. Yanında kimlik, cihaz numarası, konum ya da başka
   hiçbir bilgi gitmez.
2. Sunucumuz metni, çeviriyi üretmesi için **Google'ın Gemini** yapay
   zekâ hizmetine iletir.
3. Çeviri geri döner ve ekranda gösterilir.

**Sunucumuz yazdığın metni saklamaz, günlüğe yazmaz ve başka bir yere
aktarmaz** — yalnızca iletir ve cevabı geri verir.

Metin Google'ın hizmetine gittiği için, o aşamada Google'ın kendi
gizlilik koşulları geçerlidir:
<https://policies.google.com/privacy>

**Bu özellik isteğe bağlıdır.** Çeviri ekranını hiç açmazsan uygulama
hiçbir sunucuya bağlanmaz. Oyunların, derslerin ve ilerlemenin tamamı
internetsiz çalışır.

> **Öneri:** Çeviri kutusuna kişisel bilgi (ad, adres, telefon, parola
> gibi) yazma. Bu kutu bir dil aracıdır, özel bir not defteri değildir.

---

## Hatalı çeviri bildirmek

Çeviriyi bir yapay zekâ üretiyor ve her zaman doğru olmayabilir. Çeviri
sonucunun altında **"Yanlış ya da uygunsuz mu? Bildir"** bağlantısı var.

Bu bağlantıya dokunduğunda:

1. **Kendi e-posta uygulaman** açılır — uygulama arka planda hiçbir şey
   göndermez.
2. Mesajın içinde yazdığın Türkçe cümle ve gelen çeviri **hazır olarak
   durur**; göndermeden önce görürsün ve istersen silersin.
3. Göndermeye karar verirsen mesaj doğrudan bize ulaşır.

Yani bu bir **senin başlattığın** e-postadır. Göndermezsen hiçbir şey
bize ulaşmaz.

Bildirimleri yalnızca çeviriyi düzeltmek için okuruz; başka bir yerde
kullanmayız ve kimseyle paylaşmayız.

---

## Hatırlatma bildirimleri

Uygulama günlük çalışma hatırlatması gönderebilir. Bu bildirimler
**tamamen cihazında** kurulur ve çalışır; bir sunucudan gönderilmez ve
bildirim için hiçbir kayıt tutulmaz. Ayarlar'dan kapatabilirsin.

---

## Satın alma

Uygulama içinde tek seferlik bir satın alma bulunur (abonelik yoktur).
Ödeme tamamen **Google Play** ya da **App Store** üzerinden yapılır;
kart bilgin uygulamaya hiçbir zaman girilmez ve bizim erişimimiz olmaz.
Bize yalnızca mağazadan "bu cihazda satın alma yapılmış" bilgisi gelir.

---

## Çocuklar

CümleKur çocuklara yönelik değildir; hedef kitlesi ergen ve
yetişkinlerdir. Çocuklardan bilerek bilgi toplamıyoruz — zaten
hiç kimseden kişisel bilgi toplamıyoruz.

---

## Haklarını kullanmak

Tuttuğumuz hiçbir kişisel verin olmadığı için silinecek, düzeltilecek
ya da dışa aktarılacak bir kaydın da yok. Cihazındaki ilerlemeyi
uygulamayı silerek her zaman tamamen kaldırabilirsin.

---

## Değişiklikler

Bu politika değişirse yukarıdaki tarih güncellenir. Veri kullanımını
genişleten bir değişiklik olursa uygulama içinde bildirilir.

## İletişim

Soruların için: **yyggttkadir@gmail.com**
