<!-- YAYIN ADRESİ — mağaza formuna bu yazılacak.
     Türkçe:   https://kadiyyggtt.github.io/gizlilik/uygulamalar/blokoblast/tr.html
     English:  https://kadiyyggtt.github.io/gizlilik/uygulamalar/blokoblast/en.html
     Bu dosya aslı; site ~/Desktop/gizlilik deposundan yayımlanıyor.
     Burada değiştirdikten sonra: bash ~/Desktop/gizlilik/yenile.sh -->

# Bloko Blast — Gizlilik Politikası

**Son güncelleme:** 19 Ekim 2026

Bloko Blast bir bulmaca oyunudur. Bu metin, oyunun hangi bilgilere
dokunduğunu ve dokunmadığını açıkça anlatır.

**Kısa cevap: biz hiçbir bilgi toplamıyoruz.** Hesap yok, reklam yok,
oynamak için internet gerekmiyor, sana sorulan hiçbir izin yok. Tek
istisna isteğe bağlı **Google Play skor tablosudur**: Play Oyunlar
hesabınla girersen skorun ve oyuncu kimliğin Google'a gider (aşağıda).

---

## Toplamadığımız şeyler

Oyun şunları **istemiyor ve toplamıyor:**

- Ad, e-posta, telefon numarası, doğum tarihi
- Konum
- Rehber, takvim, fotoğraf, dosya
- Kamera ve mikrofon
- **Reklam kimliği** — oyunda reklam yoktur
- Kullanım istatistiği, **bize gönderilen** çökme raporu, analiz aracı
  (aşağıdaki teknik kayıt cihazından hiç çıkmıyor)

## Cihazında kalan teknik kayıt

Bloko Blast beklenmedik şekilde kapanırsa, ne olduğuna dair kısa bir teknik kayıt
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

## İzinler

**Sana sorulan hiçbir izin yok.** Konum, kamera, mikrofon, kişiler,
fotoğraf ve depolama izinlerinin hiçbiri istenmiyor.

Mağaza sayfasında beş teknik izin görünebilir. Bunlar Android'in kurulumda
kendiliğinden verdiği, onay kutusu çıkarmayan izinlerdir:

| İzin | Neden |
|---|---|
| Titreşim | Parça yerleşince ve satır patlayınca kısa titreşim — Ayarlar'dan kapatılabilir |
| Ses ayarları | Oyun seslerinin telefonun kendi müziğini kesmemesi için |
| İnternet | Yalnız isteğe bağlı Google Play skor tablosu için. **Oyunun kendisi internetsiz çalışır** — uçak modunda da eksiksiz oynanır |
| Ağ bağlantılarını görme | Android'in ses çalma kütüphanesi (AndroidX Media3) ekliyor. Oyun bu bilgiyi okumaz, hiçbir yere göndermez |
| Telefonun uykuya geçmesini önleme | Aynı ses kütüphanesi ekliyor (ses çalarken kesilmesin diye). Oyun ekranı kendisi açık tutmaz |

Hesap sistemi **yoktur.**

---

## İnternet

**Oyun internetsiz çalışır.** Uçak modunda da tamamen oynanır. İnternete
yalnız Google Play skor tablosu (Play Oyunlar hesabınla girdiysen)
bağlanır; çevrimdışıyken skor sessizce atlanır, oyun beklemez.

---

## Google Play skor tablosu (isteğe bağlı)

Bloko Blast Android sürümünde Google Play Oyun Hizmetleri'nin **skor
tablosunu** kullanabilir (günlük, haftalık ve tüm zamanlar; ilk 10 ve
senin sıran). Bu özellik **isteğe bağlıdır**: Google Play Oyunlar
hesabınla girmezsen hiçbir şey gönderilmez ve oyun bugünkü gibi tamamen
cihazında kalır.

Girersen, Google'ın kendi açıklamasına göre
(developer.android.com/games/pgs/data-collection):

- **Oyuncu kimliğin** (Play Oyunlar takma adın ve avatarın) bu oyunla
  paylaşılır ve skor tablosunda görünür.
- **Skorların** (oyun skorun ve Günlük Meydan Okuma skorun) Google'ın sunucularına gönderilir ve skor
  tablosunda gösterilir.
- Play Oyun Hizmetleri kendi kararlılığı için **analiz ve tanılama**
  verisi toplar.
- Veriler aktarım sırasında **HTTPS ile şifrelenir**.
- Profilinin kimlere görüneceğini (herkes / yalnız arkadaşlar / yalnız
  sen) Play Oyunlar ayarlarından **sen seçersin**.
- Bu verileri Play Oyunlar profilinden (play.google.com/games/profile)
  ya da Google Hesabından (myaccount.google.com) **silebilirsin**.

Bu veriler **Google'a gider, bize gelmez**: e-posta adresini, gerçek
adını ya da konumunu görmüyoruz. Google'ın işlemesi Google Gizlilik
Politikası'na tabidir (policies.google.com/privacy).

iOS sürümünde skor tablosu yoktur; orada hiçbir şey gönderilmez.


---

## Cihazında saklananlar

Yalnız **kendi cihazında** şunlar tutuluyor:

- En yüksek skorun, oynadığın oyun sayısı, en yüksek combo'n, coin'lerin,
  günlük serin ve Günlük Meydan Okuma skorun
- Yarım kalan oyunun (kaldığın yerden devam edebilmen için)
- Açtığın temalar ve ayarların (ses, titreşim, dil)

Bu bilgiler cihazdan çıkmaz (yalnız yukarıdaki skor tablosu skoru, giriş
yaptıysan Google'a gider). Oyunu silersen hepsi silinir.

---

## Reklam, satın alma ve ölçüm

Oyunda **reklam yok, uygulama içi satın alma yok, ölçüm/analiz aracı
yok.** İlk sürüm bilerek böyle çıkıyor.

İleride bunlardan biri eklenirse bu politika **önceden** güncellenir ve
değişiklik oyun içinde bildirilir. Bugün itibarıyla hiçbiri yoktur.

---

## Çocuklar

Bloko Blast çocuklara yönelik bir uygulama olarak sunulmamaktadır.
Oyunda reklam ve satın alma yoktur; skor tablosu isteğe bağlıdır ve
Google Play Oyunlar hesabıyla girilmeden hiçbir şey göndermez.

---

## Haklarını kullanmak

Tuttuğumuz hiçbir kişisel verin olmadığı için bizde silinecek, düzeltilecek
ya da dışa aktarılacak bir kaydın da yok. Skor tablosu verilerini Play
Oyunlar profilinden ya da Google Hesabından silebilirsin. Cihazındaki oyun ilerlemesini,
oyunu silerek tamamen kaldırabilirsin.

## İletişim

Soruların için: **yyggttkadir@gmail.com**
