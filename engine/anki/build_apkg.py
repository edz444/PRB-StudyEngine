"""Build an Anki .apkg (cloze) with the matching lecture slide image in Back Extra."""
import re, sys, os, genanki
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import COURSE, OUT, BUILD, SLIDES as _SL, CFG
from imgmap import M
from traps import T
from figmap import F
B = {}
for _m in CFG.WORDING_FILES:
    B.update(__import__(_m).B)
FIGDIR = str(BUILD / 'figpng')
SLIDES = str(_SL)
P = CFG.SLUG
ITAG = re.sub(r'[^a-z0-9]+', '_', CFG.INSTRUCTOR.lower()).strip('_')
# Lecture tags, e.g. {5: 'L5_GPCRs'}; default is built from DECK_NAMES.
LTAG = getattr(CFG, 'LEC_TAGS', None) or {k: f'L{k}_' + re.sub(r'[^A-Za-z0-9]+', '_', re.sub(r'^L\d+\s*', '', v)).strip('_') for k, v in CFG.DECK_NAMES.items() if k}
TEAL, ORANGE, AMBER = '#0e7490', '#c2410c', '#b45309'
model = genanki.Model(CFG.MODEL_ID, f'{P.upper()} Cloze v2 (slides, no scroll)', model_type=genanki.Model.CLOZE,
  fields=[{'name': 'Text'}, {'name': 'Back Extra'}],
  templates=[{'name': 'Cloze', 'qfmt': '{{cloze:Text}}', 'afmt': '{{cloze:Text}}<hr>{{Back Extra}}'}],
  css='.card{font-family:Arial,sans-serif;font-size:20px;text-align:left;color:black;background:white} .cloze{font-weight:bold;color:#0e7490} .nightMode .cloze{color:#38b2cc} img{max-width:100%;height:auto;border:1px solid #ccc;border-radius:6px;margin-top:8px}')
NAMES = CFG.DECK_NAMES
decks = {k: genanki.Deck(CFG.DECK_ID_BASE + k, f'{CFG.DECK_ROOT}::{v}') for k, v in NAMES.items()}
media, n = set(), 0
for line in open(COURSE / 'anki' / 'cards.txt', encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'): continue
    n += 1
    cloze, rest = line.split('|||'); expl, hook = rest.split('~~~')
    trap = None
    if '^^^' in hook: hook, trap = hook.split('^^^')
    trap = (trap or T.get(n) or '').strip() or None
    cloze, expl, hook = cloze.strip(), expl.strip(), hook.strip()
    for part in (cloze, expl, hook, trap or ''):
        assert not re.search(r'[<>&\t]', part), (n, part)
    nb = B[n]; expl = nb['e']
    for part in (nb['e'], nb['nw'], nb['hu'] or ''):
        assert not re.search(r'[<>&\t]', part), (n, part)
    back = (f"<div style='color:{TEAL}'>{expl}</div><br>"
            f"<div><span style='color:{ORANGE};font-weight:bold'>Memory hook:</span> {hook}</div>")
    back += (f"<br><div style='background:#eef2ff;color:#1e1b4b;border-left:4px solid #4338ca;padding:6px 10px;border-radius:4px'>"
             f"<span style='color:#4338ca;font-weight:bold'>How {CFG.INSTRUCTOR} words it:</span> {nb['nw']}")
    if nb['hu']:
        back += (f"<div style='margin-top:6px'><span style='color:#be123c;font-weight:bold'>Heads-up, her wording is harder than it needs to be:</span> {nb['hu']}</div>")
    back += "</div>"
    if trap:
        back += f"<br><div style='background:#f8ead2;color:#5a3405;border-left:4px solid {AMBER};padding:6px 10px;border-radius:4px'><span style='color:{AMBER};font-weight:bold'>Exam trap:</span> {trap}</div>"
    tags = list(CFG.TAGS)
    img = M.get(n)
    if img:
        L, p = img; fn = f'{P}_L{L}-{p}.jpg'; src = f'{SLIDES}/L{L}-{p}.jpg'
        assert os.path.exists(src), src
        media.add((fn, src))
        back += f"<div style='margin-top:10px;font-size:13px;color:#666'>Lecture {L}, slide {p}</div><img src='{fn}'>"
        tags.append(LTAG[L])
    fg = F.get(n)
    if fg:
        fn2 = f'{P}_fig_{fg}.png'; src2 = f'{FIGDIR}/{fg}.png'
        assert os.path.exists(src2), src2
        media.add((fn2, src2))
        back += f"<div style='margin-top:12px;font-size:13px;color:#666'>Diagram</div><img src='{fn2}'>"
    lo, hi = CFG.TRAP_CARDS
    if lo <= n <= hi: tags.append(f'{ITAG}_trap')
    lo, hi = CFG.REVIEW_CARDS
    if lo <= n <= hi: tags = [CFG.TAGS[0], 'MT1_review']
    if trap: tags.append('has_trap')
    if B[n]['hu']: tags.append(f'{ITAG}_wording_harder')
    if 'lec' in B[n]: tags.append(getattr(CFG, 'PRACTICE_TAG', 'practice_set'))
    decks[img[0] if img else B[n].get('lec', 0)].add_note(genanki.Note(model=model, fields=[cloze, back], tags=tags, guid=genanki.guid_for(CFG.GUID_TAG, cloze)))
# ---------- image occlusion notes ----------
import json as _json
_iof = BUILD / 'io_out' / 'cards.json'
IO = _json.load(open(_iof)) if _iof.exists() else []
io_model = genanki.Model(CFG.IO_MODEL_ID, f'{P.upper()} Image Occlusion (baked masks)',
  fields=[{'name':'Header'},{'name':'Front'},{'name':'Back'},{'name':'Answer'},{'name':'Extra'}],
  templates=[{'name':'Occlusion','qfmt':"<div class='ioh'>{{Header}}</div><div class='ioq'>Name the part under the red box</div>{{Front}}",
              'afmt':"<div class='ioh'>{{Header}}</div><div class='ioa'>{{Answer}}</div>{{Back}}<div class='iox'>{{Extra}}</div>"}],
  css=".card{font-family:Arial,sans-serif;font-size:19px;text-align:left;color:black;background:white} .ioh{font-weight:bold;color:#0e7490;margin-bottom:4px} .ioq{color:#c2410c;font-size:15px;margin-bottom:8px} .ioa{background:#fbe3d6;border-left:4px solid #c2410c;padding:6px 10px;border-radius:4px;margin-bottom:8px;font-weight:bold} .iox{color:#666;font-size:14px;margin-top:6px} img{max-width:100%;height:auto;border:1px solid #ccc;border-radius:6px}")
iodecks = {k: genanki.Deck(CFG.IO_DECK_ID_BASE + k, f'{CFG.DECK_ROOT}::{v}::Image occlusion') for k, v in NAMES.items() if k}
for c in IO:
    for f in (c['front'], c['back']):
        media.add((f, str(BUILD / 'io_out' / f)))
    lec = LTAG[c['lec']]
    iodecks[c['lec']].add_note(genanki.Note(model=io_model,
        fields=[f"{c['title']} ({c['n']} of {c['of']})", f"<img src='{c['front']}'>", f"<img src='{c['back']}'>", c['answer'],
                "Amber boxes hide the other labels; the red box is this card's answer."],
        tags=list(CFG.TAGS)+['image_occlusion',lec], guid=genanki.guid_for(CFG.IO_GUID_TAG, c['fig'], c['n'])))
# copy media with prefixed names
_md = BUILD / 'media'; _md.mkdir(exist_ok=True); files = []
for fn, src in sorted(media):
    dst = str(_md / fn); open(dst, 'wb').write(open(src, 'rb').read()); files.append(dst)
pkg = genanki.Package([decks[k] for k in sorted(decks)] + [iodecks[k] for k in sorted(iodecks)]); pkg.media_files = files
out = str(OUT / CFG.APKG)
pkg.write_to_file(out)
print(n, 'notes,', len(files), 'images ->', out, os.path.getsize(out)//1024, 'KB')
