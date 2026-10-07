#!/bin/bash
# Politikaların ASLİ KOPYASI her uygulamanın kendi deposunda.
# Bu betik onları buraya kopyalayıp sayfaları yeniden üretir.
#
#   bash ~/Desktop/gizlilik/yenile.sh && git -C ~/Desktop/gizlilik add -A \
#     && git -C ~/Desktop/gizlilik commit -m "politikalar güncellendi" \
#     && git -C ~/Desktop/gizlilik push
set -eu
cd "$(dirname "$0")"
for p in "namazvakti NamazVakti" "santiyesefi SantiyeSefi" "cumlekur CumleKur" \
         "pastelpals PastelPals" "blokoblast BlokoBlast" \
         "okkacisi OkKacisi" "renksiralama RenkSiralama" "legionrun LegionRun" \
         "minikciftlik MinikCiftlik" "minimalistsniper MinimalistSniper"; do
  set -- $p
  # Güncel kopyalar 29 Eylül 2026'dan beri ~/Desktop/OYUNLAR altında; masaüstündeki
  # eski OkKacisi/RenkSiralama klasörleri bayat kaldı ve yayındaki politikayı iki gün
  # "reklam var" diye gösterdi. Önce OYUNLAR'a bakılır.
  # Proje klasörü hiçbir yerde yoksa (silinmiş olabilir) buradaki kopya korunur;
  # asıl metin o zaman uygulamanın GitHub deposundadır.
  if [ -d "../OYUNLAR/$2" ]; then
    cp "../OYUNLAR/$2/GIZLILIK-POLITIKASI.md" "uygulamalar/$1/tr.md"
    cp "../OYUNLAR/$2/PRIVACY-POLICY.md"      "uygulamalar/$1/en.md"
    if [ -f "../OYUNLAR/$2/POLITICA-DE-PRIVACIDAD.md" ]; then
      cp "../OYUNLAR/$2/POLITICA-DE-PRIVACIDAD.md" "uygulamalar/$1/es.md"
    fi
  elif [ -d "../$2" ]; then
    cp "../$2/GIZLILIK-POLITIKASI.md" "uygulamalar/$1/tr.md"
    cp "../$2/PRIVACY-POLICY.md"      "uygulamalar/$1/en.md"
    if [ -f "../$2/POLITICA-DE-PRIVACIDAD.md" ]; then
      cp "../$2/POLITICA-DE-PRIVACIDAD.md" "uygulamalar/$1/es.md"
    fi
  else
    echo "• $2 klasörü yok, mevcut kopya korundu: uygulamalar/$1"
  fi
done
python3 uret.py
