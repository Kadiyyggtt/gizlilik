<!-- YAYIN ADRESİ — mağaza formuna bu yazılacak.
     Türkçe:   https://kadiyyggtt.github.io/gizlilik/uygulamalar/cumlekur/tr.html
     English:  https://kadiyyggtt.github.io/gizlilik/uygulamalar/cumlekur/en.html
     Bu dosya aslı; site ~/Desktop/gizlilik deposundan yayımlanıyor.
     Burada değiştirdikten sonra: bash ~/Desktop/gizlilik/yenile.sh -->

# CümleKur — Gizlilik Politikası

**Son güncelleme:** 12 Kasım 2026

CümleKur, Türkçe konuşanlar için yapılmış bir İngilizce öğrenme
uygulamasıdır. Bu metin, uygulamanın hangi bilgilere dokunduğunu ve
dokunmadığını açıkça anlatır.

**Kısa cevap:** Hesap açmıyorsun, kimliğini istemiyoruz, seni
takip etmiyoruz. Öğrenme ilerlemenin tamamı **yalnız senin cihazında** duruyor.
Uygulama kendi başına internete veri göndermez. Tek dikkat edilecek nokta
isteğe bağlı “Sesli söyle” özelliği: sesin telefondan çıkmayacağı
doğrulanamıyorsa uygulama önce sana sorar; **izin verirsen** telefonun
sistem servisi sesi işler (aşağıdaki “Mikrofon” bölümü).

---

## Toplamadığımız şeyler

Uygulama şunları **istemiyor, toplamıyor ve hiçbir yere göndermiyor:**

- Gerçek ad, soyad, e-posta, telefon numarası (Profil ekranına isteğe
  bağlı bir ad yazabilirsin; o ad yalnız cihazında ve telefonunun kendi
  yedeğinde durur, aşağıya bak)
- Konum
- Rehber, takvim, fotoğraf, dosya
- Kamera. Mikrofon yalnız **sen “Söyle” düğmesine bastığında** kullanılır;
  ses **kaydedilmez, saklanmaz, bize gönderilmez** (aşağıda ayrı bölüm)
- Reklam kimliği (uygulamanın bunu okuma izni yoktur)
- Kullanım istatistiği, **bize gönderilen** çökme raporu, analiz aracı
  (aşağıdaki teknik kayıt bize hiç ulaşmaz)

Bizim bir hesap sistemimiz **yoktur.** Uygulamaya giriş yapmıyorsun.

---

## Cihazında kalan teknik kayıt

CümleKur beklenmedik şekilde kapanırsa ya da bir hata yakalanıp uygulama
çalışmaya devam ederse, ne olduğuna dair kısa bir teknik kayıt
**yalnızca telefonunda** tutulur. Uygulama bu kaydı hiçbir yere göndermez;
ilerleme kaydıyla aynı klasörde durduğu için yalnız telefonunun **kendi
yedeğine** (aşağıda) girer. Biz onu göremeyiz ve almayız.

- **Ayarlar → Teknik kayıt** bölümünden kendin okuyabilirsin.
- Aynı yerden tek dokunuşla silebilirsin.
- Yazılırken e-posta adresi, dosya yolundaki kullanıcı adı ve uzun sayı
  dizileri temizlenir.
- En fazla 10 kayıt tutulur; yenisi geldiğinde en eski düşer.

Bunu bize göndermenin otomatik bir yolu yoktur. İstersen metni
kopyalayıp kendin gönderebilirsin — karar tamamen senindir.

Yukarıdaki “toplanmıyor” listesi bu yüzden doğru kalıyor: kayıt
**toplanmıyor**, yalnızca senin cihazında duruyor.

## Cihazında saklanan bilgiler

Şunlar **yalnız kendi cihazında** saklanıyor:

- Profil ekranına yazdığın ad (isteğe bağlı; gerçek adın olması
  gerekmez, yazmazsan “Öğrenci” görünür). İlerlemeni paylaşmayı seçersen
  bu ad, paylaştığın metnin içinde yer alır.
- Kurduğun cümle sayısı, öğrendiğin kelimeler, XP ve günlük serin
- Hangi hata türlerinde zorlandığın (koç ekranının konuşabilmesi için;
  **cümlenin kendisi değil**, yalnız hatanın türü saklanır)
- Tamamladığın kelime setleri ve okuma/dinleme ilerlemen
- Seçtiğin tema ve seviye tercihlerin, hatırlatma saatin ve bulut ses
  tanıma cevabın

Bu bilgiler **yalnız cihazında** saklanır; uygulama onları hiçbir yere
göndermez. Telefon değiştirince ilerlemen kaybolmasın diye bu ilerleme
kaydı telefonunun **kendi yedeğine** dâhildir: Android’de Google
hesabındaki Android yedeğine ve yeni telefona aktarıma, iPhone’da iCloud
yedeğine. Bu yedeği telefonunun sistemi senin hesabında tutar; biz onu
göremeyiz ve almayız. Yedeklemeyi telefonunun ayarlarından kapatabilirsin.

**Silmek:** Ayarlar → Verilerim → **“Bütün verilerimi sil”** seçeneği,
onayından sonra bu bilgilerin hepsini ve teknik kaydı cihazdan siler;
bu işlem geri alınamaz. Uygulamayı silmek de cihazdaki kaydı siler.
İki durumda da telefonunun **daha önce aldığı yedek** ayrı tutulur:
telefonun yeniden yedekleyene kadar eski kaydı içerebilir ve uygulamayı
yeniden kurduğunda geri yüklenebilir. Bu yedeği telefonunun ya da Google
/ Apple hesabının ayarlarından silebilirsin.

**Kelime veritabanı** (2.834 kelime: NGSL listesinden 2.815 kelime ve 19 gün/ay adı) uygulamanın içinde gelir ve
tamamen çevrim dışı çalışır.

---

## Mikrofon ve ses tanıma (isteğe bağlı)

Cümle Kur’da doğru kurduğun cümleyi sesli söyleyip kontrol edebilirsin.
Bu özellik **tamamen isteğe bağlıdır**; kullanmazsan mikrofon izni hiç
istenmez.

- Mikrofon **yalnız “Sesli söyle” kartındaki “Söyle” düğmesine bastığın
  an** açılır, konuşman bitince kapanır.
- Ses **kaydedilmez ve saklanmaz.** Uygulama sesin kendisini hiçbir
  dosyaya yazmaz; yalnızca telefonun ses tanıma özelliğinin ürettiği
  **yazıyı** hedef cümleyle karşılaştırır, sonra o yazıyı atar.
- Ses tanımayı **telefonunun kendi sistemi** yapar. Telefonunda Android 13
  ya da üstü varsa ve cihaz üzerinde (çevrim dışı) tanımayı destekliyorsa
  uygulama onu kullanır ve ses telefondan çıkmaz.
- Öteki durumlarda uygulama **önce sorar.** Bunlar: Android 13’ten eski
  sürümler (bu sürümlerde ses tanıma motoru çevrim dışı çalışmayı
  garanti etmiyor), cihaz üzerinde tanıması olmayan telefonlar, İngilizce
  tanıma paketi yüklü olmayan telefonlar ve iPhone (uygulama, İngilizce
  konuşmanın iPhone’da cihaz üzerinde tanınacağını doğrulayamıyor).
  - Android’de soru: “Telefonunda konuşmanın cihaz üzerinde tanınacağı
    doğrulanamıyor. Bu özellik için söylediklerin Google’ın servisine
    gönderilebilir; uygulama sesi saklamaz. Devam edilsin mi?”
  - iPhone’da soru: “iPhone’da konuşmanın cihaz üzerinde tanınacağı
    garanti edilemiyor. Bu özellik için söylediklerin Apple’ın servisine
    gönderilebilir; uygulama sesi saklamaz. Devam edilsin mi?”
  - **“Devam et” dersen** ses, telefonunun sistem servisi (Android’de
    genellikle Google’ın ses tanıma servisi, iOS’ta Apple’ın ses tanıma
    servisi) tarafından **kendi gizlilik politikasına göre** işlenir. Bu
    işleme bize ulaşmaz; biz sesi görmeyiz ve almayız.
  - **“Hayır” dersen** ses telefondan çıkmaz ve bu özellik kapalı kalır.
  - Cevabın saklanır, bir daha sorulmaz. Ayarlar ekranındaki **“Bulut
    ses tanımaya izin ver”** anahtarıyla dilediğin zaman değiştirebilirsin.
- İzni dilediğin zaman telefonunun Ayarlar bölümünden geri alabilirsin;
  uygulamanın geri kalanı aynen çalışır.

---

## İnternet bağlantısı

Bizim bir sunucumuz yoktur. Oyunların, derslerin ve ilerlemenin tamamı
internetsiz çalışır; uygulama kendi başına ağa veri göndermez. İnternet
yalnız şu durumlarda devreye girebilir:

- Ayarlar’daki gizlilik politikası bağlantısına ya da Kaynaklar
  ekranındaki sitelere **sen dokunursan** telefonunun tarayıcısı açılır.
  O siteye giriş tarayıcının ve o sitenin kuralına tabidir.
- “Sesli söyle” özelliğinde, sesin telefondan çıkmayacağı doğrulanamıyorsa
  ve **sen izin verdiysen** sistemin ses tanıma servisi (yukarıdaki bölüm).
- Kayıtlı sesi olmayan İngilizce metinleri telefonunun kendi seslendirme
  motoru okur. Uygulama ağ üzerinden çalışan bir ses seçmez; motorun
  varsayılan İngilizce sesini kullanır. Telefonunda bu ses indirilmemişse
  motor, kendi ayarına göre okunacak metni üreticisinin (örneğin
  Google’ın) sunucusunda seslendirebilir. Bu durumda giden şey yalnız
  okunacak İngilizce metindir; senin sesin ya da kişisel bilgin değildir.

Bu sürümde Google Play skor tablosu ya da başka bir çevrim içi sıralama
yoktur. İleride böyle bir özellik eklenirse bu politika, sürüm yayımlanmadan
önce güncellenir.

---

## Hatırlatma bildirimleri

Uygulama günlük çalışma hatırlatması gönderebilir. Bu bildirimler
**tamamen cihazında** kurulur ve çalışır; bir sunucudan gönderilmez ve
bildirim için hiçbir kayıt tutulmaz. Ayarlar’dan kapatabilirsin.

---

## Satın alma

Uygulama ücretsizdir; bu sürümde uygulama içi satın alma **yoktur**.
Mağazanın ödeme sistemine bağlanmaz, ödeme ya da kart bilgisi istemez,
hiçbir içerik kilitli değildir. Uygulamaya ileride reklam ya da başka
bir üçüncü taraf hizmeti eklenirse bu politika o sürüm yayımlanmadan
önce güncellenir.

---

## Çocuklar

CümleKur **13 yaş ve üzeri** kullanıcılar için hazırlanmıştır; 13 yaşın
altındaki çocuklara yönelik değildir. Çocuklardan bilerek bilgi
toplamıyoruz — zaten hiç kimseden kişisel bilgi toplamıyoruz.

---

## Haklarını kullanmak

Bizde tutulan hiçbir kişisel verin yok; bu yüzden bizden silmemizi,
düzeltmemizi ya da dışa aktarmamızı isteyebileceğin bir kayıt da yok.
Cihazındaki bütün veriyi Ayarlar → Verilerim → **“Bütün verilerimi sil”**
ile her zaman silebilirsin (onay istenir, geri alınamaz). Telefonunun
yedeğindeki kopyayı telefonunun ya da Google / Apple hesabının
ayarlarından silebilirsin (yukarıdaki “Silmek” paragrafı).

---

## Değişiklikler

Bu politika değişirse yukarıdaki tarih güncellenir. Veri kullanımını
genişleten bir değişiklik olursa (örneğin çevrim içi bir özellik eklenirse)
yeni sürümden önce politika güncellenir.

## İletişim

Veri sorumlusu: **Arzu Yiğit** (uygulamanın geliştiricisi)

Soruların ve başvuruların için: **yyggttkadir@gmail.com**
