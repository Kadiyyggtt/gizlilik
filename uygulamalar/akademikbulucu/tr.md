# AkademikBulucu — Gizlilik Politikası

**Son güncelleme:** 14 Eylül 2026

Bu politika **AkademikBulucu** uygulaması için geçerlidir.

---

## Kısaca

**Hesap açmanız gerekmez. Kimliğinizle ilgili hiçbir bilgi istenmez.**

Uygulama akademik makale arar; bu yüzden yazdığınız **arama kelimeleri
internete gider** — aksi hâlde arama yapılamaz. Bu sorgular kaydedilmez,
kimliğinizle ilişkilendirilmez ve reklam için kullanılmaz.

Kaydettiğiniz makaleler, klasörleriniz ve notlarınız **yalnızca
telefonunuzda** durur.

---

## Ne gönderiliyor

Arama yaptığınızda **yalnızca yazdığınız arama kelimesi** gönderilir.

Yol şöyledir:

```
Telefonunuz → AkademikBulucu sunucusu → akademik veritabanları
```

**AkademikBulucu sunucusu** (Cloudflare Workers üzerinde çalışır) sorgunuzu
alır ve şu herkese açık akademik kaynaklara iletir:

- **Crossref** — yayıncıların ortak makale kaydı
- **arXiv** — açık erişim ön baskı arşivi
- **Semantic Scholar** — akademik arama servisi

Sonuçlar birleştirilip size döner.

**Bu istekte gönderilmeyenler:** adınız, e-postanız, telefon numaranız, cihaz
kimliğiniz, konumunuz, reklam kimliğiniz. Böyle bir bilgi uygulamada zaten
hiç istenmez.

## Ne kaydedilmiyor

Sunucumuz arama sorgularınızı **saklamaz.** Sorgu işlenir, sonuç döner ve
kayıt tutulmaz. Kullanıcı hesabı, kullanıcı kimliği veya oturum takibi yoktur;
bir aramayı belirli bir kişiyle ilişkilendirmemiz teknik olarak mümkün değildir.

Sunucuda saklanan tek şey **günlük akademi haber bülteni**dir: herkese aynı
şekilde gösterilen, kullanıcıya özel olmayan bir içerik. Üç gün sonra
kendiliğinden silinir.

## Yapay zekâ özetleri

Bir makalenin özetini sadeleştirmek istediğinizde, o makalenin **başlığı ve
özeti** Google Gemini'ye gönderilir.

- Gönderilen metin, akademik veritabanlarından gelen **herkese açık** makale
  bilgisidir; size ait bir metin değildir.
- Kişisel bilginiz bu isteğe eklenmez.
- Bu özellik yalnızca siz istediğinizde çalışır.

## Telefonunuzda kalanlar

Aşağıdakiler **yalnızca cihazınızda** saklanır, hiçbir yere gönderilmez:

- Kaydettiğiniz makaleler ve klasörleriniz
- Makalelere aldığınız notlar
- Arama geçmişiniz
- Tema tercihi (açık/koyu)

Uygulamayı sildiğinizde bunlar da silinir.

## Toplamadığımız veriler

- Ad, e-posta, telefon numarası
- Hesap veya giriş bilgisi
- Konum
- Kişi listesi, fotoğraflar
- Kullanım istatistiği, analitik veya **bize gönderilen** çökme kaydı
  (aşağıdaki teknik kayıt cihazından hiç çıkmıyor)
- Reklam kimliği

## Cihazınızda kalan teknik kayıt

AkademikBulucu beklenmedik şekilde kapanırsa, ne olduğuna dair kısa bir
teknik kayıt **yalnızca telefonunuzda** tutulur. Bu kayıt hiçbir yere
gönderilmez ve hiçbir sunucuya ulaşmaz.

- **Ayarlar → Teknik Kayıt** bölümünden kendiniz okuyabilirsiniz.
- Aynı yerden tek dokunuşla silebilirsiniz.
- Yazılırken e-posta adresi, dosya yolundaki kullanıcı adı ve uzun sayı
  dizileri temizlenir.
- En fazla 10 kayıt tutulur; yenisi geldiğinde en eski düşer.

Bunu bize göndermenin otomatik bir yolu yoktur. İsterseniz metni kopyalayıp
kendiniz gönderebilirsiniz — karar tamamen sizindir.

Yukarıdaki "toplamıyoruz" listesi bu yüzden doğru kalıyor: kayıt
**toplanmıyor**, yalnızca sizin cihazınızda duruyor.

## Reklam ve satın alma

- **Reklam yoktur.** Hiçbir reklam ağı veya izleme aracı kullanılmaz.
- **Uygulama içi satın alma yoktur.**

## Dış bağlantılar

Bir makaleyi okumak için dokunduğunuzda, yayıncının sitesi ya da PDF
bağlantısı telefonunuzun tarayıcısında açılır. **Açılan bu siteler bize ait
değildir** ve kendi gizlilik politikaları geçerlidir.

## İzinler

Uygulama yalnızca **internet** erişimi kullanır. Konum, mikrofon, kamera,
kişiler, fotoğraf ve depolama izni **istemez.**

Kaynakça dosyalarını dışa aktarırken telefonun kendi paylaşım penceresi
açılır; dosya sizin seçtiğiniz yere gider, bize gönderilmez.

## Çocukların gizliliği

Uygulama akademik araştırma içindir ve çocuklara yönelik değildir. Hiçbir
kullanıcıdan kişisel veri toplanmadığı için çocuklardan da toplanmaz.

## Üçüncü taraf hizmetler

| Hizmet | Ne için | Ne gönderiliyor |
|---|---|---|
| Cloudflare Workers | Uygulamanın kendi sunucusu | Arama kelimesi |
| Crossref | Makale arama | Arama kelimesi |
| arXiv | Açık erişim arama | Arama kelimesi |
| Semantic Scholar | Makale arama | Arama kelimesi |
| Google Gemini | İsteğe bağlı özet | Makalenin başlığı ve özeti |

Hiçbirine kişisel bilginiz gönderilmez.

## Değişiklikler

Bu politika güncellenirse üstteki tarih değişir. Veri işleme davranışı
değişirse uygulama güncellemesinin açıklamasında ayrıca belirtilir.

## İletişim

Sorularınız için: **yyggttkadir@gmail.com**
