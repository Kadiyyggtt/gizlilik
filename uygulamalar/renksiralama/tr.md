<!-- YAYIN ADRESİ — mağaza formuna bu yazılacak.
     Türkçe:   https://kadiyyggtt.github.io/gizlilik/uygulamalar/renksiralama/tr.html
     English:  https://kadiyyggtt.github.io/gizlilik/uygulamalar/renksiralama/en.html
     Bu dosya aslı; site ~/Desktop/gizlilik deposundan yayımlanıyor.
     Burada değiştirdikten sonra: bash ~/Desktop/gizlilik/yenile.sh -->

# Renk Sıralama — Gizlilik Politikası

**Son güncelleme:** 8 Ekim 2026

Renk Sıralama bir bulmaca oyunudur. Bu metin, oyunun hangi bilgilere
dokunduğunu ve dokunmadığını açıkça anlatır.

**Kısa cevap:** Bu sürümde reklam yok, satın alma yok, hesap yok, bizim
sunucumuz yok. Biz hiçbir bilgi toplamıyoruz; oyun tamamen
çevrimdışı oynanır. Tek istisna isteğe bağlı **Google Play skor
tablosudur**: Play Oyunlar hesabınla girersen ilerlemen ve oyuncu kimliğin
Google'a gider (aşağıda).

---

## Toplamadığımız şeyler

Oyun şunları **istemiyor ve toplamıyor:**

- Ad, e-posta, telefon numarası, doğum tarihi
- Konum
- Rehber, takvim, fotoğraf, dosya
- Kamera ve mikrofon
- Reklam kimliği ya da başka bir cihaz kimliği
- Kullanım istatistiği, analiz aracı, bize gönderilen çökme raporu

Hesap sistemi **yoktur.** Bize ait bir sunucu **yoktur.** Oyunda üçüncü
taraf reklam ya da ölçüm yazılımı **yoktur.** (İsteğe bağlı Google Play
skor tablosunun kendi tanılama verisi aşağıda anlatılıyor.)

## İzinler

**Sana sorulan hiçbir izin yok.** Konum, kamera, mikrofon, kişiler,
fotoğraf ve depolama izinlerinin hiçbiri istenmiyor. iOS'ta "izleme izni"
penceresi çıkmaz.

Mağaza sayfasında görünebilecek teknik izinler, Android'in kurulumda
kendiliğinden verdiği ve onay kutusu çıkarmayan izinlerdir:

| İzin | Neden |
|---|---|
| Titreşim | Top yerleşince ve tüp tamamlanınca kısa titreşim — Ayarlar'dan kapatılabilir |
| Ses ayarları | Oyun seslerinin telefonun kendi müziğini kesmemesi için |
| İnternet | Yalnız isteğe bağlı Google Play skor tablosu için — oyunun kendisi internetsiz çalışır |
| Ağ durumunu görme | Oyun seslerini çalan Android ses kütüphanesi (AndroidX Media3) kendiliğinden ekler; oyun bununla hiçbir şey göndermez |
| Cihazı uyanık tutma | Aynı ses kütüphanesi kendiliğinden ekler |

Android'in kendi kütüphanesi ayrıca yalnız oyunun kendi içinde kullanılan
bir iç izin ekler (`…DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION`); başka
uygulamalara hiçbir şey açmaz, sana hiçbir şey sormaz.

Skor tablosu açık olmayan sürümlerde Google Play Oyun Hizmetleri
kütüphanesi pakette **hiç yoktur**.

Reklam kimliği izni (Android) açıkça **engellenmiştir.**

---

## Reklam ve satın alma

Bu sürümde **reklam yok** ve **uygulama içi satın alma yok.** Oyunun
tamamı, bütün yardımcılarıyla (geri al, ipucu, ekstra tüp) ücretsizdir.

İleride bir güncellemeyle reklam eklenirse, bu politika o güncellemeden
**önce** değiştirilir ve neyin paylaşıldığı burada tek tek yazılır.

---

## İnternet

Oyun internetsiz çalışır: bölümler telefonunda üretilir, ilerlemen
telefonunda saklanır. İnternete yalnız Google Play skor tablosu (Play
Oyunlar hesabınla girdiysen) bağlanır; çevrimdışıyken skor sessizce
atlanır, oyun beklemez.

---

## Google Play skor tablosu (isteğe bağlı)

Renk Sıralama Android sürümünde Google Play Oyun Hizmetleri'nin **skor
tablosunu** kullanabilir (günlük, haftalık ve tüm zamanlar; ilk 10 ve
senin sıran). Bu özellik **isteğe bağlıdır**: Google Play Oyunlar
hesabınla girmezsen hiçbir şey gönderilmez ve oyun bugünkü gibi tamamen
cihazında kalır.

Girersen, Google'ın kendi açıklamasına göre
(developer.android.com/games/pgs/data-collection):

- **Oyuncu kimliğin** (Play Oyunlar takma adın ve avatarın) bu oyunla
  paylaşılır ve skor tablosunda görünür.
- **Skorların** (bitirdiğin en yüksek bölüm) Google'ın sunucularına gönderilir ve skor
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

- Hangi bölüme geldiğin ve tamamladığın en yüksek bölüm
- Yarım kalan bölümün (kaldığın yerden devam edebilmen için)
- Açtığın ve seçtiğin top görünümleri ile temalar
- Ayarların (ses, titreşim, dil, renk körü modu)
- **Teknik kayıt:** oyun beklenmedik şekilde kapanırsa kısa bir hata
  kaydı (en fazla 10 kayıt). Kayıt telefonda kalır, bize gönderilmez;
  **Ayarlar → Teknik kayıt** ekranından görebilir ve silebilirsin.

Bunlar hiçbir yere gönderilmez (yalnız yukarıdaki skor tablosu sayısı,
giriş yaptıysan Google'a gider). **Ayarlar → Oyunu sıfırla** ile
ilerlemeyi silebilirsin; oyunu silmek de tamamını kaldırır.

---

## Çocuklar

Renk Sıralama çocuklara yönelik bir uygulama olarak sunulmamaktadır.
Hesap ve reklam yoktur, biz veri toplamıyoruz; skor tablosu isteğe
bağlıdır ve Google Play Oyunlar hesabıyla girilmeden hiçbir şey göndermez.

---

## Haklarını kullanmak

Bizde tuttuğumuz hiçbir kişisel verin olmadığı için bizden silinecek,
düzeltilecek ya da dışa aktarılacak bir kaydın da yok. Cihazındaki
ilerlemeyi oyun içinden sıfırlayabilir ya da oyunu silerek tamamen
kaldırabilirsin. Skor tablosu verilerini Play Oyunlar profilinden ya da
Google Hesabından silebilirsin.

## İletişim

Soruların için: **yyggttkadir@gmail.com**
