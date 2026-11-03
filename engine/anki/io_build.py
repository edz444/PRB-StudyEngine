import json, sys, os
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import COURSE, BUILD, CFG
from io_spec import S, LEC
L = json.load(open(COURSE / 'io' / 'lines.json'))
OUT = str(BUILD / 'io_out'); os.makedirs(OUT, exist_ok=True)
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 26) if os.path.exists('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf') else ImageFont.load_default()
AMBER, RED = (244, 196, 120), (228, 87, 46)
cards = []; problems = []
for fig, targets in S.items():
    lines = L[fig]['lines']; used = set(); boxes = []
    for ans, want in targets:
        bb = []
        for w in want:
            idx = next((i for i, l in enumerate(lines) if i not in used and l[0] == w), None)
            if idx is None: problems.append((fig, w)); continue
            used.add(idx); _, x, y, ww, hh = lines[idx]; bb.append((x, y, x + ww, y + hh))
        if bb:
            boxes.append((ans, [(int((a - 4) * 2), int((b - 3) * 2), int((c + 4) * 2), int((d + 3) * 2)) for a, b, c, d in bb]))
    base = Image.open(BUILD / 'io_png' / f'{fig}.png').convert('RGB')
    for k, (ans, rects) in enumerate(boxes):
        fr = base.copy(); bk = base.copy()
        df, db = ImageDraw.Draw(fr), ImageDraw.Draw(bk)
        for j, (_, rr) in enumerate(boxes):
            for r in rr:
                if j == k:
                    df.rounded_rectangle(r, 6, fill=RED)
                    db.rounded_rectangle(r, 6, outline=RED, width=5)
                else:
                    df.rounded_rectangle(r, 6, fill=AMBER); db.rounded_rectangle(r, 6, fill=AMBER)
        x0 = min(r[0] for r in rects); y0 = min(r[1] for r in rects); x1 = max(r[2] for r in rects); y1 = max(r[3] for r in rects)
        df.text(((x0 + x1) / 2, (y0 + y1) / 2), '?', fill='white', font=font, anchor='mm')
        def save(im, tag):
            im = im.resize((im.width * 3 // 4, im.height * 3 // 4))
            p = f'{OUT}/{CFG.SLUG}_io_{fig}_{k+1}_{tag}.jpg'; im.save(p, quality=82); return os.path.basename(p)
        cards.append({'fig': fig, 'lec': LEC[fig], 'title': L[fig]['title'], 'answer': ans, 'front': save(fr, 'q'), 'back': save(bk, 'a'), 'n': k + 1, 'of': len(boxes)})
json.dump(cards, open(f'{OUT}/cards.json', 'w'))
print(len(cards), 'occlusion cards;', 'unmatched:', problems)
