# Gizlilik Politikaları

Mobil uygulamaların gizlilik politikaları, Türkçe ve İngilizce (Minik Çiftlik ayrıca İspanyolca).

**https://kadiyyggtt.github.io/gizlilik/**

| Uygulama | Türkçe | English |
|---|---|---|
| 🕌 Namaz Vakti | [tr](uygulamalar/namazvakti/tr.md) | [en](uygulamalar/namazvakti/en.md) |
| 🚜 Şantiye Şefi | [tr](uygulamalar/santiyesefi/tr.md) | [en](uygulamalar/santiyesefi/en.md) |
| 📚 CümleKur | [tr](uygulamalar/cumlekur/tr.md) | [en](uygulamalar/cumlekur/en.md) |
| 🎀 PastelPals | [tr](uygulamalar/pastelpals/tr.md) | [en](uygulamalar/pastelpals/en.md) |
| 🧩 BlokoBlast | [tr](uygulamalar/blokoblast/tr.md) | [en](uygulamalar/blokoblast/en.md) |
| ➡️ Ok Kaçışı | [tr](uygulamalar/okkacisi/tr.md) | [en](uygulamalar/okkacisi/en.md) |
| 🧪 Renk Sıralama | [tr](uygulamalar/renksiralama/tr.md) | [en](uygulamalar/renksiralama/en.md) |
| 🛡️ Legion Run | [tr](uygulamalar/legionrun/tr.md) | [en](uygulamalar/legionrun/en.md) |
| 🐣 Minik Çiftlik | [tr](uygulamalar/minikciftlik/tr.md) | [en](uygulamalar/minikciftlik/en.md) · [es](uygulamalar/minikciftlik/es.md) |

## Bu depo neden açık

Google Play ve App Store, gizlilik politikasının **herkesin erişebileceği bir
adreste** yayımlanmasını istiyor. Uygulamaların kaynak kodu gizli depolarda;
burada yalnızca politikalar var.

## Nasıl güncellenir

Politikaların aslı her uygulamanın kendi deposunda. Orada değiştirdikten sonra:

```bash
bash yenile.sh          # .md dosyalarını kopyalar ve HTML sayfaları üretir
git add -A && git commit -m "politikalar güncellendi" && git push
```

`uret.py` küçük bir Markdown → HTML dönüştürücü; tek bir bağımlılık
eklememek için elle yazıldı.
