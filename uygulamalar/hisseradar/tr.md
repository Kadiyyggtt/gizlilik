# HisseRadar Gizlilik Politikası

Son güncelleme: 25 Ekim 2026

HisseRadar, borsa formasyonlarını kısa derslerle öğreten ve her gün BIST ile ABD hisselerinde bu formasyonlara uyanları listeleyen bir eğitim uygulamasıdır. Uygulamayı Kadir Yiğit geliştirir.

## Kısaca
- Hesap yoktur. Ad, e-posta, telefon, konum, rehber ya da fotoğraf istenmez.
- Reklam yoktur, analitik ya da izleme aracı yoktur.
- Uygulamada girdiğin her şey yalnız senin cihazında saklanır.
- Bildirim için Firebase Cloud Messaging (Google) bir cihaz belirteci kullanır; ayrıntısı aşağıda.

## Cihazında saklananlar
Aşağıdakiler yalnız telefonunda, uygulamanın kendi deposunda tutulur ve hiçbir sunucuya gönderilmez:

- Ders ilerlemesi ve sınav puanların
- Takip listen ve oluşturduğun adlı listeler
- Sanal portföyün (sanal para, sanal işlemler ve geçmişi)
- Gerçek portföyün: Girdiğin hisse adedi ve ortalama maliyet
- Rozetler ve gün serisi
- Ayarlar (tema, vade tercihi, açtığın bildirimler)

Uygulamayı silersen bu veriler de silinir. Bizim elimizde bir kopyası yoktur, bu yüzden geri getirilemez.

## İnternet kullanımı
Uygulama tarama sonuçlarını, grafik verisini ve geçmiş kayıtlarını herkese açık JSON dosyaları olarak GitHub Pages'ten (GitHub, Inc.) indirir: kadiyyggtt.github.io/hisseradar-veri. Bu isteklerde hesap ya da cihaz kimliği gönderilmez; sonuç herkes için aynıdır. Her internet isteğinde olduğu gibi, dosyaları barındıran GitHub isteği karşılarken IP adresini ve temel cihaz bilgisini (user agent) görür ve bunları kendi gizlilik bildirimine göre işler. Uygulamanın aracı kurumla, banka ya da ödeme sistemiyle hiçbir bağlantısı yoktur.

## Bildirimler (Firebase Cloud Messaging)
Bildirimler Google'ın Firebase Cloud Messaging hizmetiyle gönderilir. Bunun için Firebase, cihazına özgü bir **bildirim belirteci** ve bir **Firebase kurulum kimliği** üretir ve Google sunucularında tutar. Bu kimlikler adına, e-postana ya da bir hesaba bağlı değildir; reklam ya da izleme için kullanılmaz. Bizim belirteç saklayan bir sunucumuz yoktur: Cihazın yalnız açtığın "konulara" abone olur ve mesaj o konuya gönderilir.

Konular ve nereden kapatıldıkları:

- **Tarama bildirimi:** Bir formasyonda yeni eşleşme olunca. İlgili tarama ekranındaki anahtardan açılıp kapatılır.
- **Hisse hedef bildirimi:** Takip ettiğin hisse ilk hedefe ulaşınca. Hisseyi takipten çıkarınca kapanır.
- **Sabah brifingi:** Hafta içi sabah. Ayarlar'dan kapatılır.
- **Haftalık özet:** Pazar. Ayarlar'dan kapatılır.

Android 13 ve üstünde uygulama bildirim iznini ilk bildirimi açtığında ister; izni istediğin zaman telefonun ayarlarından geri alabilirsin. Uygulamayı silince abonelikler ve belirteç de geçersiz olur.

## Yedek dosyası
Ayarlar'dan "Yedek al" dediğinde takip listesi, ders ilerlemesi, sanal ve gerçek portföy ve ayarlar tek bir dosyaya yazılır. Dosyayı nereye kaydedeceğini ya da kime göndereceğini sen seçersin; uygulama onu hiçbir sunucuya yüklemez. Dosyayı paylaşırsan içeriğini de paylaşmış olursun.

## Paylaşım kartı
Hisse ekranında "Kartı paylaş" dediğinde formasyon kartı cihazında bir görsele dönüştürülür ve telefonun paylaşım ekranı açılır. Görseli nereye göndereceğini sen seçersin. Görseli iPhone'da fotoğraflarına kaydetmek istersen yalnız fotoğraf ekleme izni istenir; fotoğraflarına erişilmez.

## Dersi dinleme
"Dersi dinle" seçeneği ders metnini cihazının kendi ses motoruyla okur. Uygulama metni ya da sesi hiçbir sunucuya göndermez; mikrofon kullanılmaz.

## Reklam ve satın alma
Bu sürümde reklam, analitik ve satın alma yoktur. Eklenirse bu politika önceden güncellenir ve uygulama içinde duyurulur.

## Çocuklar
Uygulama yetişkinlere yöneliktir; 18 yaş altından bilerek veri toplanmaz.

## Yatırım tavsiyesi değildir
Uygulamadaki dersler ve tarama sonuçları eğitim amaçlıdır; yatırım tavsiyesi değildir. Alım satım kararı ve sonuçları kullanıcıya aittir.

## Değişiklikler
Politika değişirse bu sayfa ve üstteki tarih güncellenir.

## İletişim
Sorular için: yyggttkadir@gmail.com
