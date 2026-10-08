<!-- YAYIN ADRESİ — mağaza formuna bu yazılacak.
     Türkçe:   https://kadiyyggtt.github.io/gizlilik/uygulamalar/okkacisi/tr.html
     English:  https://kadiyyggtt.github.io/gizlilik/uygulamalar/okkacisi/en.html
     Bu dosya aslı; site ~/Desktop/gizlilik deposundan yayımlanıyor.
     Burada değiştirdikten sonra: bash ~/Desktop/gizlilik/yenile.sh -->

# Ok Kaçışı — Gizlilik Politikası

**Son güncelleme:** 8 Ekim 2026

Ok Kaçışı bir bulmaca oyunudur. Bu metin, oyunun hangi bilgilere
dokunduğunu ve dokunmadığını açıkça anlatır.

**Kısa cevap:** Hesap yok, kayıt yok, bizim sunucumuz yok. Bu sürümde
**reklam yok, uygulama içi satın alma yok.** Biz hiçbir bilgi toplamıyoruz;
oyun internetsiz oynanır. Tek istisna isteğe bağlı **Google Play skor
tablosudur**: Play Oyunlar hesabınla girersen ilerleme sayıların ve oyuncu
kimliğin Google'a gider (aşağıda).

---

## Toplamadığımız şeyler

Oyun şunları **istemiyor ve toplamıyor:**

- Ad, e-posta, telefon numarası, doğum tarihi
- Konum
- Rehber, takvim, fotoğraf, dosya
- Kamera ve mikrofon
- Reklam kimliği ya da başka bir cihaz kimliği
- Kullanım istatistiği, çökme raporu, analiz aracı

Hesap sistemi **yoktur.** Bize ait bir sunucu **yoktur.** Oyuna üçüncü
taraf reklam, ölçüm ya da analiz kütüphanesi eklenmemiştir. (İsteğe bağlı
Google Play skor tablosunun kendi tanılama verisi aşağıda anlatılıyor.)

## İzinler

**Sana sorulan hiçbir izin yok.** Konum, kamera, mikrofon, kişiler,
fotoğraf ve depolama izinlerinin hiçbiri istenmiyor. iOS'ta "izleme izni"
penceresi de çıkmaz — izleme yapılmıyor.

Mağaza sayfasında görünebilecek teknik izinler, Android'in kurulumda
kendiliğinden verdiği ve onay kutusu çıkarmayan izinlerdir:

| İzin | Neden |
|---|---|
| Titreşim | Ok çarpınca ve bölüm bitince kısa titreşim — Ayarlar'dan kapatılabilir |
| Ses ayarları | Oyun seslerinin telefonun kendi müziğini kesmemesi için |
| İnternet | Yalnız isteğe bağlı Google Play skor tablosu için (açık olduğu sürümde) — oyunun kendisi internetsiz çalışır ve başka hiçbir yere bağlanmaz. İzin, Expo'nun standart parçalarıyla pakette bulunur |
| Ağ bağlantılarını görme | Ses çalan kütüphaneden (AndroidX Media3) gelir; oyun bu bilgiyi okumaz, hiçbir yere göndermez |
| Telefonun uykuya geçmesini önleme | Aynı ses kütüphanesinden gelir; oyun bunu kullanmaz ve arka planda ses çalmaz |

Pakette ayrıca Android'in kendi kütüphanesinin uygulama içi güvenlik için
tanımladığı bir iç izin (`…DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION`) bulunur;
sana sorulmaz ve başka uygulamalara hiçbir şey açmaz.

Android'in reklam kimliği izni (AD_ID) uygulamada **açıkça engellenmiştir.**

---

## İnternet

Oyun internetsiz çalışır: bölümler telefonunda üretilir, ilerlemen
telefonunda saklanır. İnternete yalnız Google Play skor tablosu (Play
Oyunlar hesabınla girdiysen) bağlanır; çevrimdışıyken skor sessizce
atlanır, oyun beklemez.

---

## Google Play skor tablosu (isteğe bağlı)

Ok Kaçışı Android sürümünde Google Play Oyun Hizmetleri'nin **skor
tablosunu** kullanabilir (günlük, haftalık ve tüm zamanlar; ilk 10 ve
senin sıran). Bu özellik **isteğe bağlıdır**: Google Play Oyunlar
hesabınla girmezsen hiçbir şey gönderilmez ve oyun bugünkü gibi tamamen
cihazında kalır.

Girersen, Google'ın kendi açıklamasına göre
(developer.android.com/games/pgs/data-collection):

- **Oyuncu kimliğin** (Play Oyunlar takma adın ve avatarın) bu oyunla
  paylaşılır ve skor tablosunda görünür.
- **Skorların** (bitirdiğin en yüksek bölüm ve toplam yıldızın) Google'ın sunucularına gönderilir ve skor
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

- Hangi bölüme geldiğin ve bölüm başına yıldızların
- Yarım bıraktığın bölümün hamleleri, canları ve kullandığın ipuçları
  (uygulamayı kapatıp açınca kaldığın yerden devam edebilmen için)
- Ayarların (ses, titreşim, dil)

Bunlar hiçbir yere gönderilmez (yalnız yukarıdaki skor tablosu sayıları,
giriş yaptıysan Google'a gider). **Ayarlar → Oyunu sıfırla** ile hepsini
silebilirsin; oyunu silmek de tamamını kaldırır.

---

## Sonraki sürümler

İleride bir güncelleme reklam ya da başka bir özellik eklerse, bu politika
o güncelleme **yayımlanmadan önce** değiştirilir ve neyin değiştiği burada
yazar.

---

## Çocuklar

Ok Kaçışı çocuklara özel bir uygulama olarak sunulmamaktadır; biz hiçbir
kişisel veri toplamıyoruz, reklam yok; skor tablosu isteğe bağlıdır ve
Google Play Oyunlar hesabıyla girilmeden hiçbir şey göndermez.

---

## Haklarını kullanmak

Bizde tuttuğumuz hiçbir kişisel verin olmadığı için bizden silinecek,
düzeltilecek ya da dışa aktarılacak bir kaydın da yok. Cihazındaki
ilerlemeyi oyun içinden sıfırlayabilir ya da oyunu silerek tamamen
kaldırabilirsin. Skor tablosu verilerini Play Oyunlar profilinden ya da
Google Hesabından silebilirsin.

## İletişim

Soruların için: **yyggttkadir@gmail.com**
