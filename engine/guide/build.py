"""Build the illustrated guide (out/index.html), the inline lab page and the Markdown export from courses/<name>/guide/*.md."""
import re, glob, os, sys, html, importlib
import markdown
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import COURSE, OUT as _OUT, CFG
# Course diagrams: any content/diagrams*.py module that registers SVGs into FIGS (see dlib.py).
FIGS = {}
for _f in sorted(glob.glob(str(COURSE / 'content' / 'diagrams*.py'))):
    _m = importlib.import_module(os.path.basename(_f)[:-3])
    FIGS.update(getattr(_m, 'FIGS', {}))
from glossary import G as GLOSS

SRC = str(COURSE / 'guide')
OUT = str(_OUT)
import json
gl = "## Glossary {#glossary}\n\nEvery technical term in the guide, in plain English, with where it comes up. Background terms are taught in Chapter 0.\n\nGLOSSBODYMARK\n"
open(f"{SRC}/97_glossary.md","w").write(gl)
files = sorted(glob.glob(f"{SRC}/*.md"))
raw = "\n\n".join(open(f).read() for f in files)

LABEL = {"hook": "Memory hook", "conn": "Connection", "trap": "Exam trap", "she": "She emphasized", "note": "About this guide", "easy": "Easy marks: don't lose these", "story": "Where we are in the story", "nancy": "Her wording, decoded", "key": "Key takeaways", "exam": "On her practice set"}
callout_re = re.compile(r"^:::(\w+)\n(.*?)\n:::\s*$", re.S | re.M)
fig_re = re.compile(r"\{\{fig:([a-z_0-9]+)(?:\|[^}]*)?\}\}")
slide_re = re.compile(r"\{\{slide:(L(\d+)-(\d+))\|([^}]*)\}\}")
m3d_re = re.compile(r"\{\{3d:([a-z]+)\|([^}]*)\}\}")
lab_re = re.compile(r"\{\{lab:([a-z]+)\|([^}]*)\}\}")
LAB_URL = getattr(CFG, "LAB_URL", "")
M3D_NAMES = getattr(CFG, "M3D_NAMES", {})

# ---------------- HTML -----------------
tokens = {}
def tok(htmlstr):
    k = f"ZZTOK{len(tokens)}ZZ"
    tokens[k] = htmlstr
    return f"\n\n{k}\n\n"

def co(m):
    t, body = m.group(1), m.group(2)
    if t == "q":
        q, a = body.split("\n???\n")
        return tok(f'<div class="pq">{markdown.markdown(q)}<details><summary>Show answer</summary>{markdown.markdown(a)}</details></div>')
    inner = markdown.markdown(body, extensions=["tables"])
    return tok(f'<aside class="co co-{t}"><p class="co-lab">{LABEL[t]}</p>{inner}</aside>')

def fig(m):
    n = m.group(1)
    svg, cap = FIGS[n]
    return tok(f'<figure class="diagram"><div class="dg-wrap">{svg}</div><figcaption><span class="fig-tag">Diagram</span>{html.escape(cap)}</figcaption></figure>')

def slide(m):
    sid, L, p, cap = m.groups()
    return tok(f'<figure class="slide"><button class="zoom" type="button" aria-label="Enlarge slide L{L} page {p}"><img src="slides/{sid}.jpg" loading="lazy" alt="Lecture {L} slide {p}: {html.escape(cap)}"></button>'
               f'<figcaption><span class="fig-tag">Her slide, L{L} p{p}</span>{html.escape(cap)}</figcaption></figure>')

h = callout_re.sub(co, raw)
h = fig_re.sub(fig, h)
h = slide_re.sub(slide, h)
def m3d(m):
    sid, cap = m.groups(); nm = M3D_NAMES[sid]
    return tok(f'<figure class="m3d" data-scene="{sid}"><div class="m3d-stage"><button type="button" class="m3d-cover m3d-open" aria-label="Open 3D model: {html.escape(nm)}"><img src="m3d/{sid}.jpg" alt="Preview of the 3D model: {html.escape(nm)}" loading="lazy"><span class="m3d-play">Open 3D model</span></button><button type="button" class="m3d-close" hidden>Close 3D</button></div><div class="m3d-ui" hidden></div><figcaption><span class="fig-tag">3D model</span><b>{html.escape(nm)}.</b> {html.escape(cap)}</figcaption></figure>')
h = m3d_re.sub(m3d, h)
def labl(m):
    pid, txt = m.groups()
    return tok(f'<div class="labbox"><button type="button" class="labbtn" data-lab="{pid}" aria-expanded="false"><span class="lab-o">Break it yourself in Pathway Lab: {html.escape(txt)}</span><span class="lab-c">Close Pathway Lab</span></button><div class="labframe" hidden></div></div>')
h = lab_re.sub(labl, h)
body = markdown.markdown(h, extensions=["tables", "attr_list"])
for k, v in tokens.items():
    body = body.replace(f"<p>{k}</p>", v)
assert "ZZTOK" not in body
gb = '<dl id="glossary-body">' + "".join(f'<dt>{html.escape(t)}</dt><dd>{html.escape(d)} <span class="gw">{html.escape("Background (Chapter 0)" if w=="background" else w)}</span></dd>' for t,_,d,w in sorted(GLOSS,key=lambda x:x[0].lower())) + '</dl>'
body = body.replace("<p>&lt;&lt;GLOSSBODY&gt;&gt;</p>", gb).replace("<p>GLOSSBODYMARK</p>", gb)
assert "GLOSSBODYMARK" not in body
body = body.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
# promote first h1 into hero
body = re.sub(r"<h1>(.*?)</h1>\s*<p>(.*?)</p>", r'<header class="hero"><p class="eyebrow">'+html.escape(CFG.EYEBROW)+r'</p><h1>\1</h1><p class="sub">\2</p></header>', body, count=1)

nav = CFG.NAV
navhtml = "".join(f'<a href="#{i}">{t}</a>' for i, t in nav)
railhtml = "".join(f'<a href="#{i}"><span class="rl">{t}</span><span class="rp">0%</span><span class="rb"><i></i></span></a>' for i, t in nav)

css = open(os.path.join(os.path.dirname(__file__), "style.css")).read()
js = open(os.path.join(os.path.dirname(__file__), "page.js")).read()
D = os.path.dirname(__file__)
gjson = json.dumps([{"t":t,"m":m,"d":d,"w":w} for t,m,d,w in GLOSS], ensure_ascii=False).replace("</","<\\/")
termjs = open(D+"/term.js").read()
_ad = COURSE / "content"
atlas = "".join(open(_ad / f).read() for f in ("atlas_head.js", "atlas_scenes.js", "atlas_tail.js") if (_ad / f).exists())  # optional 3D models
page = f"""<title>{html.escape(CFG.TITLE)}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Literata:opsz,wght@7..72,500;7..72,700&family=JetBrains+Mono:wght@500&display=swap">
<style>{css}</style>
<nav class="topnav" aria-label="Sections"><div class="navin">{navhtml}</div></nav>
<div class="vprog" aria-hidden="true"><i></i><b></b></div>
<main class="wrap">{body}</main>
<div class="lightbox" id="lb" hidden><button type="button" class="lb-close" aria-label="Close">Close</button><img alt=""></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
<script>window.GLOSS={gjson};</script>
<script>{js}</script>
<script>{termjs}</script>
<script>{atlas}</script>
"""
os.makedirs(OUT, exist_ok=True)
open(f"{OUT}/index.html", "w").write(page)
_labf = COURSE / "lab" / "pathway-lab.html"
_lab = open(_labf).read() if _labf.exists() else ""
if _lab: open(f"{OUT}/lab.html", "w").write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">' + _lab.replace('<style>', '<style>html,body{margin:0}', 1) + '</head></html>')

# ---------------- Markdown for DeepTutor -----------------
def co_md(m):
    t, b = m.group(1), m.group(2).strip()
    if t == "q":
        q, a = b.split("\n???\n")
        return f"{q}\n\nAnswer: {a}"
    lines = b.split("\n")
    lines[0] = f"{LABEL[t]}: " + lines[0]
    return "\n".join("> " + l if l else ">" for l in lines)
md = callout_re.sub(co_md, raw)
md = fig_re.sub(lambda m: f"*Diagram: {FIGS[m.group(1)][1]}*", md)
md = m3d_re.sub(lambda m: f"*3D model ({M3D_NAMES[m.group(1)]}): {m.group(2)}*", md)
md = lab_re.sub("", md)
md = slide_re.sub(lambda m: f"*Slide figure (Lecture {m.group(2)}, slide {m.group(3)}): {m.group(4)}*", md)
md = re.sub(r"\s*\{#[a-z0-9-]+\}", "", md)
md = md.replace("GLOSSBODYMARK", "\n".join(f"- {t}: {d} ({w})" for t,_,d,w in sorted(GLOSS,key=lambda x:x[0].lower())))
md = re.sub(r"\n{3,}", "\n\n", md)
open(f"{OUT}/{CFG.GUIDE_MD}", "w").write(md)
# DeepTutor copy: the same Markdown minus the sections listed in DEEPTUTOR_SKIP
_parts = re.split(r"(?m)^(?=## )", md)
open(f"{OUT}/deeptutor_{CFG.GUIDE_MD}", "w").write("".join(p for p in _parts if not any(p.startswith(x) for x in getattr(CFG, "DEEPTUTOR_SKIP", []))))
import json as _j
_j.dump(getattr(CFG, "NOTEBOOKLM", []), open(f"{OUT}/notebooklm.json", "w"))
print("ok", len(page) // 1024, "KB html;", len(FIGS), "diagrams")
