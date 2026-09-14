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
         "akademikbulucu AkademikBulucu"; do
  set -- $p
  cp "../$2/GIZLILIK-POLITIKASI.md" "uygulamalar/$1/tr.md"
  cp "../$2/PRIVACY-POLICY.md"      "uygulamalar/$1/en.md"
done
python3 uret.py
