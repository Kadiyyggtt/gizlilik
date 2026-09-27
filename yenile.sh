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
         "pastelpals PastelPals" "fama FAMA" "blokoblast BlokoBlast" \
         "siberciningunlugu SibercininGunlugu" \
         "akademikbulucu AkademikBulucu" \
         "okkacisi OkKacisi" "renksiralama RenkSiralama"; do
  set -- $p
  # Proje klasörü masaüstünde yoksa (silinmiş olabilir) buradaki kopya korunur;
  # asıl metin o zaman uygulamanın GitHub deposundadır.
  if [ -d "../$2" ]; then
    cp "../$2/GIZLILIK-POLITIKASI.md" "uygulamalar/$1/tr.md"
    cp "../$2/PRIVACY-POLICY.md"      "uygulamalar/$1/en.md"
  else
    echo "• $2 klasörü yok, mevcut kopya korundu: uygulamalar/$1"
  fi
done
python3 uret.py
