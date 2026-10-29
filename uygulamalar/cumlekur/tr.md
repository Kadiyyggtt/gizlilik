<!-- YAYIN ADRESİ — mağaza formuna bu yazılacak.
     Türkçe:   https://kadiyyggtt.github.io/gizlilik/uygulamalar/cumlekur/tr.html
     English:  https://kadiyyggtt.github.io/gizlilik/uygulamalar/cumlekur/en.html
     Bu dosya aslı; site ~/Desktop/gizlilik deposundan yayımlanıyor.
     Burada değiştirdikten sonra: bash ~/Desktop/gizlilik/yenile.sh -->

# CümleKur — Gizlilik Politikası

**Son güncelleme:** 29 Ekim 2026

CümleKur, Türkçe konuşanlar için yapılmış bir İngilizce öğrenme
uygulamasıdır. Bu metin, uygulamanın hangi bilgilere dokunduğunu ve
dokunmadığını açıkça anlatır.

**Kısa cevap:** Hesap açmıyorsun, kimliğini istemiyoruz, reklam yok,
takip yok. Öğrenme ilerlemenin tamamı **yalnız senin cihazında** duruyor.
Uygulama kendi başına internete veri göndermez. Tek dikkat edilecek nokta
isteğe bağlı "Sesli söyle" özelliği: cihazın çevrim dışı ses tanıması yoksa
uygulama önce sana sorar; **izin verirsen** telefonun sistem servisi sesi
işler (aşağıdaki "Mikrofon" bölümü).

---

## Toplamadığımız şeyler

Uygulama şunları **istemiyor, toplamıyor ve hiçbir yere göndermiyor:**

- Ad, soyad, e-posta, telefon numarası
- Konum
- Rehber, takvim, fotoğraf, dosya
- Kamera. Mikrofon yalnız **sen "Sesli söyle" düğmesine bastığında** kullanılır;
  ses **kaydedilmez, saklanmaz, bize gönderilmez** (aşağıda ayrı bölüm)
- Reklam kimliği (uygulamada reklam yoktur)
- Kullanım istatistiği, **bize gönderilen** çökme raporu, analiz aracı
  (aşağıdaki teknik kayıt cihazından hiç çıkmıyor)

Bizim bir hesap sistemimiz **yoktur.** Uygulamaya giriş yapmıyorsun.

---

## Cihazında kalan teknik kayıt

CümleKur beklenmedik şekilde kapanırsa, ne olduğuna dair kısa bir teknik kayıt
**yalnızca telefonunda** tutulur. Bu kayıt hiçbir yere gönderilmez ve
hiçbir sunucuya ulaşmaz.

- **Ayarlar → Teknik Kayıt** bölümünden kendin okuyabilirsin.
- Aynı yerden tek dokunuşla silebilirsin.
- Yazılırken e-posta adresi, dosya yolundaki kullanıcı adı ve uzun sayı
  dizileri temizlenir.
- En fazla 10 kayıt tutulur; yenisi geldiğinde en eski düşer.

Bunu bize göndermenin otomatik bir yolu yoktur. İstersen metni
kopyalayıp kendin gönderebilirsin — karar tamamen senindir.

Yukarıdaki "toplanmıyor" listesi bu yüzden doğru kalıyor: kayıt
**toplanmıyor**, yalnızca senin cihazında duruyor.

## Cihazında saklanan bilgiler

Şunlar **yalnız kendi cihazında** saklanıyor:

- Kurduğun cümle sayısı, öğrendiğin kelimeler, XP ve günlük serin
- Hangi hata türlerinde zorlandığın (koç ekranının konuşabilmesi için;
  **cümlenin kendisi değil**, yalnız hatanın türü saklanır)
- Tamamladığın kelime setleri ve okuma/dinleme ilerlemen
- Seçtiğin tema, ses ve seviye tercihlerin

Bu bilgiler **yalnız cihazında** saklanır; uygulama onları hiçbir yere
göndermez. Telefon değiştirince ilerlemen kaybolmasın diye bu ilerleme
kaydı telefonunun **kendi yedeğine** dahildir: Android'de Google
hesabındaki Android yedeğine ve yeni telefona aktarıma, iPhone'da iCloud
yedeğine. Bu yedeği telefonunun sistemi senin hesabında tutar; biz onu
göremeyiz ve almayız. Yedeklemeyi telefonunun ayarlarından kapatabilirsin.
Uygulamayı silersen cihazdaki kayıt silinir.

**Kelime veritabanı** (2.818 kelime) uygulamanın içinde gelir ve
tamamen çevrim dışı çalışır.

---

## Mikrofon ve ses tanıma (isteğe bağlı)

Cümle Kur'da doğru kurduğun cümleyi sesli söyleyip kontrol edebilirsin.
Bu özellik **tamamen isteğe bağlıdır**; kullanmazsan mikrofon izni hiç
istenmez.

- Mikrofon **yalnız "Söyle" düğmesine bastığın an** açılır, konuşman
  bitince kapanır.
- Ses **kaydedilmez ve saklanmaz.** Uygulama sesin kendisini hiçbir
  dosyaya yazmaz; yalnızca telefonun ses tanıma özelliğinin ürettiği
  **yazıyı** hedef cümleyle karşılaştırır, sonra o yazıyı atar.
- Ses tanımayı **telefonunun kendi sistemi** yapar. Cihazın çevrim dışı
  tanımayı destekliyorsa uygulama onu kullanır ve ses telefondan çıkmaz.
- Cihaz çevrim dışı tanımayı desteklemiyorsa (ya da İngilizce tanıma
  paketi yüklü değilse) uygulama **önce sorar:** "Telefonun konuşmayı
  cihaz üzerinde tanıyamıyor. Bu özellik için sesin Google'ın servisine
  gönderilecek; uygulama sesi saklamaz. Devam edilsin mi?" (iPhone'da
  "Apple'ın servisine").
  - **"Devam et" dersen** ses, telefonunun sistem servisi (Android'de
    genellikle Google'ın ses tanıma servisi, iOS'ta Apple'ın ses tanıma
    servisi) tarafından **kendi gizlilik politikasına göre** işlenir. Bu
    işleme bize ulaşmaz; biz sesi görmeyiz ve almayız.
  - **"Hayır" dersen** ses telefondan çıkmaz ve bu özellik kapalı kalır.
  - Cevabın saklanır, bir daha sorulmaz. Ayarlar ekranındaki **"Bulut
    ses tanımaya izin ver"** anahtarıyla dilediğin zaman değiştirebilirsin.
- İzni dilediğin zaman telefonunun Ayarlar bölümünden geri alabilirsin;
  uygulamanın geri kalanı aynen çalışır.

---

## İnternet bağlantısı

Bizim bir sunucumuz yoktur. Oyunların, derslerin ve ilerlemenin tamamı
internetsiz çalışır; uygulama kendi başına ağa veri göndermez. İnternet
yalnız şu iki durumda devreye girer:

- Ayarlar'daki gizlilik politikası bağlantısına ya da Kaynaklar
  ekranındaki sitelere **sen dokunursan** telefonunun tarayıcısı açılır.
  O siteye giriş tarayıcının ve o sitenin kuralına tabidir.
- "Sesli söyle" özelliğinde, cihazda çevrim dışı tanıma yoksa ve **sen
  izin verdiysen** sistemin ses tanıma servisi (yukarıdaki bölüm).

Bu sürümde Google Play skor tablosu ya da başka bir çevrim içi sıralama
yoktur. İleride böyle bir özellik eklenirse bu politika, sürüm yayımlanmadan
önce güncellenir.

---

## Hatırlatma bildirimleri

Uygulama günlük çalışma hatırlatması gönderebilir. Bu bildirimler
**tamamen cihazında** kurulur ve çalışır; bir sunucudan gönderilmez ve
bildirim için hiçbir kayıt tutulmaz. Ayarlar'dan kapatabilirsin.

---

## Satın alma ve reklam

Bu sürümde uygulama içi satın alma da reklam da **yoktur**. Uygulama
mağazanın ödeme sistemine bağlanmaz, ödeme ya da kart bilgisi istemez,
hiçbir içerik kilitli değildir.

---

## Çocuklar

CümleKur **13 yaş ve üzeri** kullanıcılar için hazırlanmıştır; 13 yaşın
altındaki çocuklara yönelik değildir. Çocuklardan bilerek bilgi
toplamıyoruz — zaten hiç kimseden kişisel bilgi toplamıyoruz.

---

## Haklarını kullanmak

Tuttuğumuz hiçbir kişisel verin olmadığı için silinecek, düzeltilecek
ya da dışa aktarılacak bir kaydın da yok. Cihazındaki ilerlemeyi
uygulamayı silerek her zaman tamamen kaldırabilirsin.

---

## Değişiklikler

Bu politika değişirse yukarıdaki tarih güncellenir. Veri kullanımını
genişleten bir değişiklik olursa (örneğin çevrim içi bir özellik eklenirse)
yeni sürümden önce politika güncellenir.

## İletişim

Soruların için: **yyggttkadir@gmail.com**
