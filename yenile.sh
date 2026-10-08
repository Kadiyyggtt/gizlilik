#!/bin/bash
# Politikaların ASLİ KOPYASI her uygulamanın kendi deposunda.
# Bu betik onları buraya kopyalayıp sayfaları yeniden üretir.
#
#   bash ~/Desktop/gizlilik/yenile.sh && git -C ~/Desktop/gizlilik add -A \
#     && git -C ~/Desktop/gizlilik commit -m "politikalar güncellendi" \
#     && git -C ~/Desktop/gizlilik push
set -eu
cd "$(dirname "$0")"
for p in "namazvakti NamazVakti" "cumlekur CumleKur" \
         "blokoblast BlokoBlast" \
         "okkacisi OkKacisi" "renksiralama RenkSiralama" "legionrun LegionRun" \
         "minimalistsniper MinimalistSniper" \
         "jellymerge JellyMerge" "cozyshelf CozyShelf" "hexastack HexaStack" \
         "orbitjump OrbitJump" "tinyisles TinyIsles"; do
  set -- $p
  # Güncel kopyalar 29 Eylül 2026'dan beri ~/Desktop/OYUNLAR altında; masaüstündeki
  # eski OkKacisi/RenkSiralama klasörleri bayat kaldı ve yayındaki politikayı iki gün
  # "reklam var" diye gösterdi. Önce OYUNLAR'a bakılır.
  # Proje klasörü hiçbir yerde yoksa (silinmiş olabilir) buradaki kopya korunur;
  # asıl metin o zaman uygulamanın GitHub deposundadır.
  # 5 Ekim 2026'dan beri uygulamalar harici SSD'de. Önce orası; SSD takılı
  # değilse eski yollara düşülür. Kopyalamadan önce o depo origin/main ile
  # aynı olmalı (bayat SSD kopyası bir kez eski politikayı yayına taşımıştı).
  SSD="/Volumes/Yer/mobil uygulamalar/$2"
  if [ -f "$SSD/GIZLILIK-POLITIKASI.md" ]; then
    mkdir -p "uygulamalar/$1"
    cp "$SSD/GIZLILIK-POLITIKASI.md" "uygulamalar/$1/tr.md"
    cp "$SSD/PRIVACY-POLICY.md"      "uygulamalar/$1/en.md"
    if [ -f "$SSD/POLITICA-DE-PRIVACIDAD.md" ]; then
      cp "$SSD/POLITICA-DE-PRIVACIDAD.md" "uygulamalar/$1/es.md"
    fi
  elif [ -d "../OYUNLAR/$2" ]; then
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
