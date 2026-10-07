# Gizlilik Politikaları

Mobil uygulamaların gizlilik politikaları, Türkçe ve İngilizce.

**https://kadiyyggtt.github.io/gizlilik/**

| Uygulama | Türkçe | English |
|---|---|---|
| 🕌 Namaz Vakti | [tr](uygulamalar/namazvakti/tr.md) | [en](uygulamalar/namazvakti/en.md) |
| 📚 CümleKur | [tr](uygulamalar/cumlekur/tr.md) | [en](uygulamalar/cumlekur/en.md) |
| 🧩 BlokoBlast | [tr](uygulamalar/blokoblast/tr.md) | [en](uygulamalar/blokoblast/en.md) |
| ➡️ Ok Kaçışı | [tr](uygulamalar/okkacisi/tr.md) | [en](uygulamalar/okkacisi/en.md) |
| 🧪 Renk Sıralama | [tr](uygulamalar/renksiralama/tr.md) | [en](uygulamalar/renksiralama/en.md) |
| 🛡️ Legion Run | [tr](uygulamalar/legionrun/tr.md) | [en](uygulamalar/legionrun/en.md) |

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
