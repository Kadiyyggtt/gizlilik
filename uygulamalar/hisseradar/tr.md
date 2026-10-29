# HisseRadar Gizlilik Politikası

Son güncelleme: 29 Ekim 2026

HisseRadar, borsa formasyonlarını kısa derslerle öğreten ve her gün BIST ile ABD hisselerinde bu formasyonlara uyanları listeleyen bir eğitim uygulamasıdır. Uygulamayı Kadir Yiğit geliştirir.

## Kısaca
- Hesap yoktur. Ad, e-posta, telefon, konum, rehber ya da fotoğraf istenmez.
- Reklam yoktur, analitik ya da izleme aracı yoktur.
- Uygulamada girdiğin her şey yalnız senin cihazında saklanır. Tek istisna: Hisse bildirimlerini açarsan, takip ettiğin hisse kodları bildirim gönderebilmek için Google Firebase'e iletilir.
- Bildirim için Firebase Cloud Messaging (Google) bir cihaz belirteci kullanır; ayrıntısı aşağıda.

Bu metin aynı zamanda, 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) ve Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ uyarınca hazırlanmış aydınlatma metnidir.

## Veri sorumlusu
KVKK kapsamında veri sorumlusu, uygulamayı bireysel olarak geliştiren gerçek kişi **Kadir Yiğit**'tir. İletişim: yyggttkadir@gmail.com

## İşlenen kişisel veriler, amaç ve hukuki sebep
Uygulamada kişisel veri sayılabilecek veriler yalnız bildirimle ilgilidir ve yalnız sen bir bildirimi açtığında işlenir:

| Veri | Amaç | Hukuki sebep | Toplama yöntemi | Ne zaman sona erer |
|---|---|---|---|---|
| Firebase bildirim belirteci | Açtığın bildirimleri cihazına ulaştırmak | Açık rıza (KVKK m. 5/1) | Bildirimi açtığında cihazdaki Firebase kütüphanesiyle, otomatik yolla | Bildirimleri kapattığında ya da uygulamayı sildiğinde |
| Firebase kurulum kimliği | Belirtecin doğru cihaza bağlı kalması | Açık rıza (KVKK m. 5/1) | Aynı şekilde, otomatik yolla | Bildirimleri kapattığında ya da uygulamayı sildiğinde |
| Takip ettiğin hisse kodları (yalnız hisse bildirimlerini açarsan) | Takip ettiğin hisse ilk hedefe ulaşınca sana bildirim göndermek | Açık rıza (KVKK m. 5/1) | Ayarlar'da "Hisse bildirimleri"ni açtığında, her hisse için bir bildirim konusuna abonelikle | Hisse bildirimlerini kapattığında, hisseyi takipten çıkardığında, bildirim iznini geri aldığında ya da uygulamayı sildiğinde |

Bu kimlikler yalnız bildirim için kullanılır; reklam, profil çıkarma ya da başka bir amaçla işlenmez. Bildirimi açman bu işlemeye açık rıza vermendir; bildirim açmadan uygulamanın geri kalanını kullanabilirsin.

Hisse bildirimlerini açarsan, takip ettiğin hisse kodları bildirim gönderebilmek için Google Firebase'e iletilir. Hisse bildirimleri varsayılan olarak kapalıdır. Bunun dışında cihazında tutulan veriler (takip listesi, ders ilerlemesi, sanal ve gerçek portföy, ayarlar) geliştiriciye ya da başka bir sunucuya ulaşmaz. Bu yüzden geliştirici açısından kişisel veri işleme sayılmaz; bunları yalnız sen görür, yalnız sen silersin.

## Cihazında saklananlar
Aşağıdakiler telefonunda, uygulamanın kendi deposunda tutulur. Hisse bildirimlerini açmadığın sürece hiçbiri bir sunucuya gönderilmez:

- Ders ilerlemesi ve sınav puanların
- Takip listen ve oluşturduğun adlı listeler (hisse bildirimlerini açarsan yalnız hisse kodları, bildirim konusu olarak Google Firebase'e iletilir; liste adları iletilmez)
- Sanal portföyün (sanal para, sanal işlemler ve geçmişi)
- Gerçek portföyün: Girdiğin hisse adedi ve ortalama maliyet
- Rozetler ve gün serisi
- Ayarlar (tema, vade tercihi, açtığın bildirimler)

Uygulamayı silersen bu veriler de silinir. Bizim elimizde bir kopyası yoktur, bu yüzden geri getirilemez.

## İnternet kullanımı
Uygulama tarama sonuçlarını, grafik verisini ve geçmiş kayıtlarını herkese açık JSON dosyaları olarak GitHub Pages'ten (GitHub, Inc., ABD) indirir: kadiyyggtt.github.io/hisseradar-veri. Bu isteklerde hesap ya da cihaz kimliği gönderilmez; sonuç herkes için aynıdır. Her internet isteğinde olduğu gibi, dosyaları barındıran GitHub isteği karşılarken IP adresini ve temel cihaz bilgisini (user agent) görür ve bunları kendi gizlilik bildirimine göre işler. Uygulamanın aracı kurumla, banka ya da ödeme sistemiyle hiçbir bağlantısı yoktur.

## Bildirimler (Firebase Cloud Messaging)
Bildirimler Google'ın Firebase Cloud Messaging hizmetiyle gönderilir. Bunun için Firebase, cihazına özgü bir **bildirim belirteci** ve bir **Firebase kurulum kimliği** üretir ve Google sunucularında tutar. Bu kimlikler adına, e-postana ya da bir hesaba bağlı değildir; reklam ya da izleme için kullanılmaz. Bizim belirteç saklayan bir sunucumuz yoktur: Cihazın yalnız açtığın "konulara" abone olur ve mesaj o konuya gönderilir.

Konular ve nereden kapatıldıkları:

- **Tarama bildirimi:** Bir formasyonda yeni eşleşme olunca. İlgili tarama ekranındaki anahtardan açılıp kapatılır.
- **Hisse hedef bildirimi:** Takip ettiğin hisse ilk hedefe ulaşınca. Varsayılan olarak kapalıdır; Ayarlar'daki "Hisse bildirimleri" anahtarıyla açılıp kapatılır. Açarsan, takip ettiğin hisse kodları bildirim gönderebilmek için Google Firebase'e iletilir: Cihazın her hisse için "hedef-BIST-THYAO" gibi bir konuya abone olur, Google da hangi cihazın hangi konuya abone olduğunu bilir. Hisseyi takipten çıkarınca o hissenin konusundan, anahtarı kapatınca bütün hisse konularından çıkılır.
- **Sabah brifingi:** Hafta içi sabah. Ayarlar'dan kapatılır.
- **Haftalık özet:** Pazar. Ayarlar'dan kapatılır.

Android 13 ve üstünde uygulama bildirim iznini ilk bildirimi açtığında ister; izni istediğin zaman telefonun ayarlarından geri alabilirsin. Uygulama her açılışta ve öne her gelişinde izni denetler; izin yoksa bütün konulardan çıkar. Uygulamayı silince abonelikler ve belirteç de geçersiz olur.

## Yurt dışına aktarım
Bildirim belirteci, kurulum kimliği ve hisse bildirimlerini açtıysan takip ettiğin hisse kodlarının konu abonelikleri, Firebase Cloud Messaging hizmeti için Google LLC'nin (ABD) sunucularında işlenir. Bu yurt dışına aktarım, KVKK m. 9 kapsamında açık rızana dayanır (m. 9/6-a). Bilmen gereken risk şudur: ABD için Kişisel Verileri Koruma Kurulunun verdiği bir yeterlilik kararı yoktur ve bu veriler orada ABD mevzuatına tabi olabilir. Bir bildirimi açmak bu aktarıma rıza vermektir; bütün bildirimleri kapattığında ya da uygulamayı sildiğinde aktarım durur.

Tarama verisi GitHub Pages'ten (GitHub, Inc., ABD) indirilir; bu istekte hesap ya da cihaz kimliği gönderilmez. GitHub'ın isteği karşılarken gördüğü IP adresini geliştirici almaz ve saklamaz.

## Saklama süresi
Bildirim belirteci, kurulum kimliği ve konu abonelikleri, bildirim açık kaldığı sürece Google sunucularında durur. Bildirimleri kapattığında ya da uygulamayı sildiğinde geçersiz olur. Geliştirici tarafında hiçbir kayıt tutulmaz: Belirteç, IP adresi ya da kullanım bilgisi saklayan bir sunucu yoktur.

## KVKK kapsamındaki hakların
KVKK m. 11 uyarınca veri sorumlusuna başvurarak şu haklarını kullanabilirsin:

- Kişisel verinin işlenip işlenmediğini öğrenme
- İşlenmişse buna ilişkin bilgi isteme
- İşlenme amacını ve amacına uygun kullanılıp kullanılmadığını öğrenme
- Yurt içinde ya da yurt dışında aktarıldığı üçüncü kişileri bilme
- Eksik ya da yanlış işlenmişse düzeltilmesini isteme
- KVKK m. 7'deki şartlar çerçevesinde silinmesini ya da yok edilmesini isteme
- Düzeltme ve silme işlemlerinin, verinin aktarıldığı üçüncü kişilere bildirilmesini isteme
- Yalnız otomatik sistemlerle analiz edilmesi sonucu aleyhine bir sonuç çıkmasına itiraz etme
- Kanuna aykırı işlenmesi sebebiyle zarara uğrarsan zararın giderilmesini isteme

**Başvuru yolu:** Başvurunu yyggttkadir@gmail.com adresine e-postayla gönderebilirsin; Veri Sorumlusuna Başvuru Usul ve Esasları Hakkında Tebliğde sayılan diğer yollar da (yazılı başvuru, kayıtlı elektronik posta) geçerlidir. Başvuruna en geç 30 gün içinde ve ücretsiz cevap verilir. Geliştirici belirteci tutmadığı için seni tanıyamaz; bildirim verisini silmenin en hızlı yolu bildirimleri kapatmak ya da uygulamayı silmektir.

Başvurun reddedilirse, cevabı yetersiz bulursan ya da 30 gün içinde cevap alamazsan Kişisel Verileri Koruma Kuruluna şikâyette bulunabilirsin (KVKK m. 14).

## Yedek dosyası
Ayarlar'dan "Yedek al" dediğinde takip listesi, ders ilerlemesi, sanal ve gerçek portföy ve ayarlar tek bir dosyaya yazılır. Dosyayı nereye kaydedeceğini ya da kime göndereceğini sen seçersin; uygulama onu hiçbir sunucuya yüklemez. Dosyayı paylaşırsan içeriğini de paylaşmış olursun.

## Paylaşım kartı
Hisse ekranında "Kartı paylaş" dediğinde formasyon kartı cihazında bir görsele dönüştürülür ve telefonun paylaşım ekranı açılır. Görseli nereye göndereceğini sen seçersin. Görseli iPhone'da fotoğraflarına kaydetmek istersen yalnız fotoğraf ekleme izni istenir; fotoğraflarına erişilmez.

## Dersi dinleme
"Dersi dinle" seçeneği ders metnini cihazının kendi ses motoruyla okur. Uygulama metni ya da sesi hiçbir sunucuya göndermez; mikrofon kullanılmaz.

## Reklam ve satın alma
Bu sürümde reklam, analitik ve satın alma yoktur. Eklenirse bu politika önceden güncellenir ve uygulama içinde duyurulur.

## Çocuklar
Uygulama yetişkinlere yöneliktir; 18 yaş altına hitap etmez ve 18 yaş altından bilerek veri toplanmaz.

## Yatırım tavsiyesi değildir
Uygulamadaki dersler ve tarama sonuçları eğitim amaçlıdır; yatırım tavsiyesi değildir. Alım satım kararı ve sonuçları kullanıcıya aittir.

## Değişiklikler
Politika değişirse bu sayfa ve üstteki tarih güncellenir.

## İletişim
Sorular için: yyggttkadir@gmail.com
