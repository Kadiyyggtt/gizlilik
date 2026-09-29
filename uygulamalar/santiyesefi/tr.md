<!-- YAYIN ADRESİ — mağaza formuna bu yazılacak.
     Türkçe:   https://kadiyyggtt.github.io/gizlilik/uygulamalar/santiyesefi/tr.html
     English:  https://kadiyyggtt.github.io/gizlilik/uygulamalar/santiyesefi/en.html
     Bu dosya aslı; site ~/Desktop/gizlilik deposundan yayımlanıyor.
     Burada değiştirdikten sonra: bash ~/Desktop/gizlilik/yenile.sh -->

# Şantiye Şefi — Gizlilik Politikası

**Son güncelleme:** 29 Eylül 2026
**Geliştirici:** Kadir Yiğit
**İletişim:** yyggttkadir@gmail.com

---

## Kısacası

**Şantiye Şefi hiçbir bilgi toplamıyor.**

Reklam yok. Satın alma yok. Hesap yok. Sunucu yok. Oyun internet
olmadan tamamen çalışıyor.

Oyunun cihazın dışına çıkan tek işlemi **paylaşma**; o da **ebeveyn
kapısı** arkasında ve isteğe bağlı: çocuk kasabasının resmini aileye
göndermek isterse, resim telefonun kendi paylaşım penceresiyle
gönderiliyor.

Bu sürümde 18 binanın hepsi (ana kasaba ve Büyük Şehir) ücretsiz ve
açık.

---

## Toplanmayan bilgiler

Bu uygulama şunların **hiçbirini** toplamıyor, saklamıyor veya
paylaşmıyor:

- İsim, e-posta, telefon numarası veya başka kişisel bilgi
- Konum
- Fotoğraf, kamera veya mikrofon kaydı
- Rehber, takvim veya cihazdaki diğer dosyalar
- Reklam kimliği veya benzeri takip tanımlayıcıları
- Kullanım istatistikleri, analitik veri veya **bize gönderilen** çökme raporları
  (aşağıdaki teknik kayıt cihazından hiç çıkmıyor)

---

## Cihazında kalan teknik kayıt

Şantiye Şefi beklenmedik şekilde kapanırsa, ne olduğuna dair kısa bir teknik kayıt
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

## Paylaşma

Oyunda bir **paylaş** düğmesi var. Basıldığında:

1. Önce **ebeveyn kapısı** çıkıyor — iki basamaklı bir çarpma sorusu.
   Çocuğun tek başına geçmesi beklenmiyor; bu, Google Play Families
   politikasının zorunlu kıldığı bir adım.
2. Soru doğru cevaplanırsa oyun, kasabanın **resmini** oluşturuyor ve
   telefonun **kendi paylaşım penceresini** açıyor.
3. Resmi nereye göndereceğine (WhatsApp, e-posta, galeriye kaydetme…)
   **tamamen kullanıcı karar veriyor.**

Önemli noktalar:

- Resim **bizim sunucumuza gitmiyor** — bizim sunucumuz yok.
- Resimde sadece oyundaki kasaba çizimi var; çocuğa ait hiçbir bilgi,
  isim veya fotoğraf yok.
- Paylaşma **hiç kullanılmasa da** oyun tamamen çalışıyor.
- Resim gönderildikten sonra ne olduğu, seçilen uygulamanın kendi
  gizlilik politikasına tabi.

---

## Cihazda saklanan bilgiler

Oyun, **sadece kendi cihazında** saklanan şu bilgileri tutuyor:

- Bitirdiğin binalar ve kasabanın durumu
- Yarım kalan bir işin ilerlemesi
- **Albümdeki resimler** (aşağıda ayrıca anlatılıyor)
- Ses, titreşim ve dil tercihin

Bu bilgiler cihazdan **hiçbir yere gönderilmiyor**. Uygulamayı silersen
hepsi silinir. Oyun içindeki Ayarlar ekranından **Kasabayı sıfırla**
diyerek de her zaman silebilirsin.

---

## Albüm — cihazda kalan resimler

Bir bina bitince oyun, o yapının bir **resmini** çekip uygulamanın kendi
albümüne koyuyor. Bu resim:

- **Oyunun kendi çizimidir.** Kameraya, galeriye ya da telefondaki
  başka hiçbir resme erişim YOKTUR ve istenmez.
- **Sadece bu cihazda**, uygulamanın kendi klasöründe durur. Hiçbir
  yere gönderilmez, hiç kimse göremez.
- Albüm **en fazla 24 resim** tutar; dolduğunda en eski resim
  kendiliğinden silinir. Böylece çocuğun telefonu dolmaz.
- Her resim albümden **tek tek silinebilir**.
- Uygulama silinince bütün resimler de silinir.

Albümdeki bir resmi dışarı göndermek **paylaşma** sayılır: önce ebeveyn
kapısı açılır, sonra telefonun kendi paylaşım penceresi gelir.

---

## İzinler

Uygulamanın Android'de istediği izinler:

| İzin | Neden |
|---|---|
| `VIBRATE` | Kazarken ve panel yerleştirirken hafif titreşim |
| `INTERNET` | Uygulama çatısının (React Native) kendiliğinden eklediği izin; oyun hiçbir yere **bağlanmıyor** |

Mikrofon, kamera, konum, rehber, depolama ve mağaza faturalandırma
(`BILLING`) izinleri **bilerek engellenmiştir** — uygulamanın bunlara
ihtiyacı yok.

---

## Çocuklar

Bu oyun çocuklar için tasarlandı ve Google Play **Families** programının
kurallarına göre yapıldı.

- Reklam yok — ne kişiselleştirilmiş ne de başka türlü.
- Bu sürümde uygulama içi satın alma yok. 18 binanın hepsi ücretsiz,
  hiçbiri kilitli değil.
- Uygulama dışına çıkan tek işlem **paylaşma**, o da ebeveyn kapısı
  arkasında ve isteğe bağlı.
- Sohbet, mesajlaşma veya başka kullanıcılarla etkileşim yok.
- Çocuklardan hiçbir bilgi istenmiyor ve toplanmıyor.

Hiçbir veri toplanmadığı için COPPA ve GDPR-K kapsamında ebeveyn onayı
gerektiren bir işlem yapılmıyor.

---

## Üçüncü taraflar

Uygulamada **hiçbir reklam ağı, analitik aracı veya ödeme hizmeti
yok.** Şantiye Şefi hiçbir veriyi kimseyle paylaşmıyor çünkü hiçbir
veri toplamıyor.

---

## Değişiklikler

İleride oyuna reklam ya da satın alma eklenirse bu politika önce
güncellenecek ve değişiklik uygulamanın mağaza sayfasında duyurulacak.
(29 Eylül 2026: bu sürüm satın almasız; Büyük Şehir dahil bütün
binalar ücretsiz.)

---

## Sorular

Aklına takılan bir şey olursa: **yyggttkadir@gmail.com**
