# Bu deponun sahipliği (taslak)

Bu depo (`~/Desktop/gizlilik`, yayın adresi `https://kadiyyggtt.github.io/gizlilik/`) bütün uygulamaların gizlilik politikası ve kullanım koşulları sayfalarını yayımlar. Mağazalar bu adreslere bağlanır; yayındaki metin uygulamanın gerçek davranışıyla aynı olmak zorundadır.

## Kural

1. **Siteyi yalnız site oturumu üretir ve yayımlar.** Bu depoda dosya değiştirme, `git add`, `commit` ve `push` yalnız site oturumunun işidir.
2. **Uygulama oturumları yalnız kendi depolarındaki kaynağı günceller:** `GIZLILIK-POLITIKASI.md`, `PRIVACY-POLICY.md`, varsa `POLITICA-DE-PRIVACIDAD.md` ve `KULLANIM-KOSULLARI.md`. Değişikliği kendi depolarına commit edip gönderir, sonra site oturumuna haber verir.
3. **`uret.py` ve `yenile.sh` başka oturumda çalıştırılmaz.** İkisi de bütün uygulamaların sayfalarını yeniden yazar; başka oturumda çalıştırılınca başka uygulamaların sayfaları da değişir.

## Haber verme

Uygulama oturumu Kadir'e şu satırı yazar; Kadir bunu site oturumuna iletir:

```
Site güncellemesi: <uygulama>, kaynak commit <kimlik>, değişen: <tr / en / es / koşullar>, kısa özet: <bir cümle>
```

## Site oturumunun yayın adımları

1. Kaynak deponun `origin/main` ile aynı olduğunu doğrula (bayat SSD kopyası bir kez eski politikayı yayına taşıdı).
2. Kaynağı bu depoya kopyala: `uygulamalar/<slug>/tr.md`, `en.md`, varsa `es.md` ve `kosullar.md` (Ermenice'de `KULLANIM-KOSULLARI.md` → `kosullar.md`). Ermenice `yenile.sh` listesinde değildir, elle kopyalanır.
3. `python3 uret.py` ile sayfaları üret.
4. Yalnız o uygulamanın dosyalarını ekle: `git add -- uygulamalar/<slug>/...` (gerekirse `index.html`). `git add -A` kullanılmaz.
5. Başka uygulamaların sayfalarının değişmediğini, depo kopyasında (`git worktree`) eski ve yeni çıktıyı karşılaştırarak doğrula.
6. Gönder, sonra yayındaki sayfayı indirip kaynak metinle paragraf paragraf karşılaştır.

## Neden

- 27 Ekim 2026'da sekiz oyunun politikası (Google Play skor tablosu açıklaması) bu depoya kopyalandı ama yayımlanmadı. Yayındaki sayfalar üç gün boyunca, kodda zaten bulunan skor tablosundan söz etmedi.
- 30 Ekim 2026 07:15'te başka bir oturum eski `uret.py`'yi çalıştırdı; Ermenice Türkçe sayfasının yerel kopyasından "Kullanım Koşulları" sekmesi düştü (gönderilmeden yakalandı).
