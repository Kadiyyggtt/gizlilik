#!/usr/bin/env python3
"""
GİZLİLİK POLİTİKASI SİTESİ — ÜRETİCİ.

Altı uygulamanın Türkçe ve İngilizce gizlilik politikasını, mağazaların
isteyebileceği KALICI ADRESLERE sahip sayfalara çevirir.

Neden elle yazılmış küçük bir Markdown dönüştürücü: tek bağımlılık
eklememek için. Kullanılan Markdown çok dar bir alt küme (başlık, paragraf,
liste, tablo, kalın, kod, alıntı, yatay çizgi, bağlantı) ve hepsi burada
karşılanıyor. Bilinmeyen bir işaretle karşılaşırsa metni OLDUĞU GİBİ
bırakıyor — sessizce kaybetmiyor.

Politikaların ASLİ KOPYASI her uygulamanın kendi deposunda. Burası
yalnızca yayın yeri; `yenile.sh` onları buraya kopyalıyor.
"""

import html
import json
import pathlib
import re
from datetime import date

KOK = pathlib.Path(__file__).parent
UYGULAMALAR = json.loads((KOK / 'uygulamalar.json').read_text())


def satir_ici(metin: str) -> str:
    """Kalın, kod, bağlantı — kaçışlar yapıldıktan SONRA uygulanıyor."""
    m = html.escape(metin)
    m = re.sub(r'`([^`]+)`', r'<code>\1</code>', m)
    m = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', m)
    m = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2">\1</a>', m)
    m = re.sub(r'&lt;(https?://[^&]+)&gt;', r'<a href="\1">\1</a>', m)
    return m


def markdown_html(kaynak: str) -> str:
    # HTML yorumları (`<!-- ... -->`) yayına girmez. Politikaların başındaki
    # "YAYIN ADRESİ" notu bir yorumdur; 29 Eylül 2026'da BlokoBlast'ın yayındaki
    # sayfasının tepesinde bu not kaçırılmış ham metin olarak görünüyordu.
    kaynak = re.sub(r'<!--.*?-->', '', kaynak, flags=re.DOTALL)
    cikti: list[str] = []
    satirlar = kaynak.split('\n')
    i = 0
    while i < len(satirlar):
        s = satirlar[i]
        duz = s.strip()

        if not duz:
            i += 1
            continue

        if duz == '---':
            cikti.append('<hr>')
            i += 1
            continue

        baslik = re.match(r'^(#{1,4})\s+(.*)$', duz)
        if baslik:
            n = len(baslik.group(1))
            cikti.append(f'<h{n}>{satir_ici(baslik.group(2))}</h{n}>')
            i += 1
            continue

        # Tablo: başlık satırı + ayraç satırı
        if duz.startswith('|') and i + 1 < len(satirlar) and re.match(r'^\|[\s:|-]+\|$', satirlar[i + 1].strip()):
            def hucreler(satir: str) -> list[str]:
                return [h.strip() for h in satir.strip().strip('|').split('|')]

            basliklar = hucreler(duz)
            i += 2
            govde = []
            while i < len(satirlar) and satirlar[i].strip().startswith('|'):
                govde.append(hucreler(satirlar[i]))
                i += 1
            bas = ''.join(f'<th>{satir_ici(h)}</th>' for h in basliklar)
            sat = ''.join('<tr>' + ''.join(f'<td>{satir_ici(h)}</td>' for h in r) + '</tr>' for r in govde)
            cikti.append(f'<table><thead><tr>{bas}</tr></thead><tbody>{sat}</tbody></table>')
            continue

        if duz.startswith('> '):
            blok = []
            while i < len(satirlar) and satirlar[i].strip().startswith('>'):
                blok.append(satirlar[i].strip().lstrip('>').strip())
                i += 1
            cikti.append(f'<blockquote>{satir_ici(" ".join(blok))}</blockquote>')
            continue

        # Listeler.
        #
        # DEVAM SATIRLARI ÖĞEYE KATILIYOR. İlk yazımda her satır ayrı bir
        # öğeydi ve iki satıra yayılan bir öğe ikiye bölünüyordu; ortasında
        # kalın yazı varsa `**` işareti ekranda ÇİĞ kalıyordu. İki sayfada
        # tam olarak bu oldu (ŞantiyeSefi EN, CümleKur TR).
        def liste_topla(isaret: str, baslangic: int) -> tuple[list[str], int]:
            ogeler: list[str] = []
            j = baslangic
            while j < len(satirlar):
                t = satirlar[j]
                if re.match(isaret, t.strip()):
                    ogeler.append(re.sub(isaret, '', t.strip()))
                    j += 1
                # Girintili ve boş olmayan satır: önceki öğenin devamı
                elif ogeler and t.startswith((' ', '\t')) and t.strip():
                    ogeler[-1] += ' ' + t.strip()
                    j += 1
                else:
                    break
            return ogeler, j

        if re.match(r'^[-*]\s+', duz):
            ogeler, i = liste_topla(r'^[-*]\s+', i)
            cikti.append('<ul>' + ''.join(f'<li>{satir_ici(o)}</li>' for o in ogeler) + '</ul>')
            continue

        if re.match(r'^\d+\.\s+', duz):
            ogeler, i = liste_topla(r'^\d+\.\s+', i)
            cikti.append('<ol>' + ''.join(f'<li>{satir_ici(o)}</li>' for o in ogeler) + '</ol>')
            continue

        # Paragraf: boş satıra kadar
        paragraf = []
        while i < len(satirlar) and satirlar[i].strip() and not re.match(r'^(#{1,4}\s|[-*]\s|\d+\.\s|\||>|---$)', satirlar[i].strip()):
            paragraf.append(satirlar[i].strip())
            i += 1
        if paragraf:
            cikti.append(f'<p>{satir_ici(" ".join(paragraf))}</p>')

    return '\n'.join(cikti)


STIL = """
:root{--zemin:#FAF9FC;--kart:#FFFFFF;--yazi:#22202A;--soluk:#5E5A6B;
       --cizgi:#E6E2ED;--vurgu:VURGU}
@media(prefers-color-scheme:dark){:root:not([data-tema="acik"]){
  --zemin:#131218;--kart:#1C1B23;--yazi:#F0EEF5;--soluk:#A39FB0;--cizgi:#2C2A35}}
*{box-sizing:border-box}
body{margin:0;background:var(--zemin);color:var(--yazi);line-height:1.65;
     font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
     font-size:17px}
.sar{max-width:760px;margin:0 auto;padding:0 20px 80px}
header{padding:36px 0 8px}
.geri{display:inline-block;color:var(--soluk);text-decoration:none;font-size:15px;margin-bottom:22px}
.geri:hover{color:var(--vurgu)}
.rozet{display:inline-flex;align-items:center;gap:10px;background:var(--kart);
       border:1px solid var(--cizgi);border-radius:999px;padding:7px 16px;font-size:14px;
       color:var(--soluk);margin-bottom:18px}
h1{font-size:32px;line-height:1.2;margin:.2em 0 .5em;letter-spacing:-.5px}
h2{font-size:22px;margin:2.1em 0 .5em;padding-top:.4em;border-top:1px solid var(--cizgi)}
h2:first-of-type{border-top:0}
h3{font-size:18px;margin:1.6em 0 .4em}
p{margin:.85em 0}
ul,ol{margin:.85em 0;padding-left:24px}
li{margin:.3em 0}
hr{border:0;border-top:1px solid var(--cizgi);margin:2em 0}
strong{font-weight:650}
code{background:var(--kart);border:1px solid var(--cizgi);border-radius:5px;
     padding:1px 6px;font-size:.88em}
blockquote{margin:1.2em 0;padding:14px 18px;background:var(--kart);
           border-left:3px solid var(--vurgu);border-radius:0 10px 10px 0;color:var(--soluk)}
table{width:100%;border-collapse:collapse;margin:1.2em 0;font-size:15.5px;display:block;overflow-x:auto}
th,td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--cizgi)}
th{color:var(--soluk);font-weight:600;font-size:13.5px;letter-spacing:.4px;text-transform:uppercase}
a{color:var(--vurgu)}
.diller{display:flex;gap:8px;margin:0 0 26px}
.diller a{display:inline-block;padding:7px 15px;border-radius:9px;font-size:14.5px;
          text-decoration:none;border:1px solid var(--cizgi);color:var(--soluk);background:var(--kart)}
.diller a.etkin{background:var(--vurgu);color:#fff;border-color:var(--vurgu)}
footer{margin-top:56px;padding-top:20px;border-top:1px solid var(--cizgi);
       color:var(--soluk);font-size:14px}
.liste{display:grid;gap:12px;margin-top:28px}
.uyg{display:block;background:var(--kart);border:1px solid var(--cizgi);border-radius:14px;
     padding:18px 20px;text-decoration:none;color:inherit}
.uyg:hover{border-color:var(--vurgu)}
.uyg .ust{display:flex;align-items:center;gap:12px}
.uyg .ad{font-size:19px;font-weight:650}
.uyg .em{font-size:26px;line-height:1}
.uyg .cm{color:var(--soluk);font-size:15px;margin-top:7px}
.uyg .bg{margin-top:12px;font-size:14px;color:var(--vurgu)}
"""


def sayfa(baslik: str, vurgu: str, govde: str) -> str:
    return f"""<!doctype html>
<html lang="tr"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(baslik)}</title>
<style>{STIL.replace('VURGU', vurgu)}</style>
</head><body><div class="sar">{govde}</div></body></html>"""


bugun = date.today().strftime('%d.%m.%Y')
uretilen = 0

DILLER = [('tr', 'Türkçe'), ('en', 'English'), ('es', 'Español')]
GERI = {'tr': 'Tüm uygulamalar', 'en': 'All apps', 'es': 'Todas las apps'}

for u in UYGULAMALAR:
    klasor = KOK / 'uygulamalar' / u['slug']
    # tr ve en zorunlu; es yalnız dosyası varsa (Minik Çiftlik üç dilde).
    mevcut = [(d, e) for d, e in DILLER if d in ('tr', 'en') or (klasor / f'{d}.md').exists()]
    for dil, etiket in mevcut:
        kaynak = (klasor / f'{dil}.md').read_text()
        icerik = markdown_html(kaynak)
        baglantilar = '\n    '.join(
            ('<a class="etkin" href="%s.html">%s</a>' if d == dil else '<a href="%s.html">%s</a>') % (d, e)
            for d, e in mevcut)
        govde = f"""
<header>
  <a class="geri" href="../../index.html">← {GERI[dil]}</a>
  <div class="rozet">{u['emoji']} {html.escape(u['ad'])}</div>
  <div class="diller">
    {baglantilar}
  </div>
</header>
{icerik}
<footer>Kadir Yiğit · yyggttkadir@gmail.com · {bugun}</footer>"""
        hedef = klasor / f'{dil}.html'
        hedef.write_text(sayfa(f"{u['ad']} — Gizlilik Politikası", u['vurgu'], govde))
        uretilen += 1

# Kapak
kartlar = ''.join(f"""
<a class="uyg" href="uygulamalar/{u['slug']}/tr.html">
  <div class="ust"><span class="em">{u['emoji']}</span><span class="ad">{html.escape(u['ad'])}</span></div>
  <div class="cm">{html.escape(u['cumle'])}</div>
  <div class="bg">Gizlilik Politikası · Privacy Policy →</div>
</a>""" for u in UYGULAMALAR)

kapak = f"""
<header>
  <h1>Gizlilik Politikaları</h1>
  <p style="color:var(--soluk);margin-top:-.2em">
    Aşağıdaki uygulamaların hiçbiri kişisel veri toplamıyor. Her politikanın
    Türkçe ve İngilizce sürümü var.
  </p>
</header>
<div class="liste">{kartlar}</div>
<footer>Kadir Yiğit · yyggttkadir@gmail.com · Son güncelleme {bugun}</footer>"""

(KOK / 'index.html').write_text(sayfa('Gizlilik Politikaları', '#5B3E99', kapak))
print(f'{uretilen} politika sayfası + kapak üretildi')
