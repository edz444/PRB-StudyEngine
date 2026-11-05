"""Pack the lesson data, pathway boards and guide CSS into one self-contained app page (out/lessons/<slug>-lesson-path.html)."""
import json, re, os, sys, shutil, importlib
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import ENGINE, COURSE, OUT, BUILD, SLIDES, CFG

t = open(ENGINE / 'lessons' / 'app_template.html', encoding='utf-8').read()
css = open(ENGINE / 'guide' / 'style.css', encoding='utf-8').read()
d = json.load(open(BUILD / 'lessons.json', encoding='utf-8'))
try:
    d['boards'] = importlib.import_module('boards').P    # hand-written pathway boards, optional
except ModuleNotFoundError:
    d['boards'] = {}
data = json.dumps(d, ensure_ascii=False).replace('</', '<\\/')
cfg = json.dumps({'slug': CFG.SLUG, 'exam': CFG.EXAM, 'plan': CFG.PLAN, 'eyebrow': CFG.APP_EYEBROW,
                  'guideUrl': getattr(CFG, 'GUIDE_URL', ''),
                  'guideSub': getattr(CFG, 'GUIDE_SUB', 'slide figures and worked questions')}, ensure_ascii=False).replace('</', '<\\/')
out = (t.replace('/*GUIDECSS*/', css).replace('/*DATA*/', data).replace('/*CFG*/', cfg)
        .replace('/*APP_TITLE*/', CFG.APP_TITLE))
S = OUT / 'lessons'
(S / 'slides').mkdir(parents=True, exist_ok=True)
page = S / f'{CFG.SLUG}-lesson-path.html'
page.write_text(out, encoding='utf-8')
imgs = sorted(set(re.findall(r'slides/(L\d+-\d+\.jpg)', data)))
missing = [f for f in imgs if not (SLIDES / f).exists()]
for f in imgs:
    if (SLIDES / f).exists(): shutil.copy(SLIDES / f, S / 'slides' / f)
if (OUT / 'lab.html').exists(): shutil.copy(OUT / 'lab.html', S / 'lab.html')
print(len(out) // 1024, 'KB page;', len(imgs) - len(missing), 'slide images', '; missing: ' + ', '.join(missing) if missing else '')
print('publish:', page)
