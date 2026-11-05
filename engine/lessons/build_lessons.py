"""Cut the built guide into bite-sized lessons with objectives, cards, cloze checks and boss questions."""
import re, json, sys, os, html as H
from bs4 import BeautifulSoup, NavigableString
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import COURSE, OUT, BUILD, CFG
from glossary import G

SRC = open(OUT / 'index.html', encoding='utf-8').read()
soup = BeautifulSoup(SRC, 'html.parser')
main = soup.find('main')

LECS = CFG.LECS
BADGE = CFG.BADGE

def words(t): return len(t.split())
def txt(el): return re.sub(r'\s+', ' ', el.get_text(' ')).strip()

def split_para(p):
    """Split a long paragraph into sentence groups of about 55 words."""
    t = p.decode_contents()
    if words(p.get_text()) <= 75: return [f'<p>{t}</p>']
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z(])', t)
    out, cur = [], ''
    for s in parts:
        if cur and words(BeautifulSoup(cur + ' ' + s, 'html.parser').get_text()) > 55:
            out.append(f'<p>{cur}</p>'); cur = s
        else:
            cur = (cur + ' ' + s).strip()
    if cur: out.append(f'<p>{cur}</p>')
    return out

def card_kind(el):
    c = el.get('class') or []
    if el.name == 'aside':
        for k in ('exam', 'hook', 'trap', 'nancy', 'easy', 'she', 'conn', 'story', 'note'):
            if f'co-{k}' in c: return k
        return 'note'
    if el.name == 'figure' or 'slide' in c or 'fig' in c: return 'fig'
    if 'tbl' in c: return 'table'
    if el.name in ('ul', 'ol'): return 'list'
    if 'labbox' in c: return 'lab'
    return 'text'

def lecture_nodes(lid):
    h2 = main.find('h2', id=lid); nodes = []
    n = h2.find_next_sibling()
    while n is not None and n.name != 'h2':
        nodes.append(n); n = n.find_next_sibling()
    return h2, nodes

def build_cards(nodes):
    cards, buf, pend, lead = [], [], None, None
    def add(k, h):
        nonlocal pend, lead
        if lead and k == 'list': h = lead + h     # "Three words first:" stays on the same screen as its list
        elif lead: cards.append({'k': 'text', 'h': lead, 'kick': pend}); pend = None
        lead = None
        cards.append({'k': k, 'h': h, 'kick': pend}); pend = None
    def flush():
        nonlocal buf
        if buf: add('text', ''.join(buf)); buf = []
    for el in nodes:
        if not hasattr(el, 'name') or el.name is None: continue
        cls = el.get('class') or []
        if 'm3d' in cls or el.find(class_='m3d'): continue
        if el.name in ('h3', 'h4'):
            flush(); pend = txt(el); continue
        k = card_kind(el)
        if k == 'text' and el.name == 'p':
            t = txt(el)
            if t.startswith('The short version:'):
                flush(); add('big', el.decode_contents().replace('The short version:', '', 1)); continue
            kids = [c for c in el.contents if not (isinstance(c, str) and not c.strip())]
            if len(kids) == 1 and getattr(kids[0], 'name', None) in ('strong', 'b'):
                flush(); pend = t.rstrip('.:'); continue          # a bold-only line labels the next screen
            nxt = el.find_next_sibling()
            if t.endswith(':') and nxt is not None and nxt.name in ('ul', 'ol') and words(t) <= 12:
                flush(); lead = str(el); continue                # a short lead-in line rides with its list
            for piece in split_para(el):
                pw = words(BeautifulSoup(piece, 'html.parser').get_text())
                cur = words(BeautifulSoup(''.join(buf), 'html.parser').get_text()) if buf else 0
                if buf and cur + pw > 70: flush()
                buf.append(piece)
            continue
        flush()
        if k == 'list' and len(el.find_all('li', recursive=False)) > 6:
            lis = el.find_all('li', recursive=False)
            for a in range(0, len(lis), 5):
                add('list', f'<{el.name}>' + ''.join(str(x) for x in lis[a:a+5]) + f'</{el.name}>')
            continue
        add(k, str(el))
    flush()
    return [c for c in cards if c['h'].strip()]

def fix_kickers(nodes):
    """Insert kicker labels: return list of (heading, nodes-run) to keep sub-heading text visible."""
    return nodes

# ---------- cloze cards ----------
# Each card belongs to the lecture named in the section header above it ("# ---------- L5 GPCRs ----------").
cloze = []
n = 0; sec = ''
for line in open(COURSE / 'anki' / 'cards.txt', encoding='utf-8'):
    l = line.strip()
    if l.startswith('#'):
        sec = l; continue
    if not l: continue
    n += 1
    c, rest = l.split('|||'); e, hook = rest.split('~~~')
    hook = hook.split('^^^')[0]
    m = re.search(r'\bL(\d+)\b', sec)
    lec = ('l' + m.group(1)) if m and ('l' + m.group(1)) in {x[0] for x in LECS} else None
    trap = getattr(CFG, 'TRAP_SECTION', '\0') in sec
    cloze.append({'n': n, 'c': c.strip(), 'hook': hook.strip(), 'lec': lec, 'trap': trap})
B = {}
for mname in CFG.WORDING_FILES:
    B.update(__import__(mname).B)
for c in cloze:
    if c['n'] in B and B[c['n']].get('lec'): c['lec'] = 'l' + str(B[c['n']]['lec'])   # practice-set cards name their lecture
    if c['n'] in B: c['e'] = B[c['n']]['e']
    else: c['e'] = ''
def lec_of(n): return cloze[n - 1]['lec']
STOP = set('the a an and or of to in is are be by for with on as it its that this from at which can not no into when than then so their they them one two three more less all any each other also only most often'.split())
def toks(s): return set(w for w in re.findall(r'[a-z0-9α-ωβγ+\-]{3,}', s.lower()) if w not in STOP)

# ---------- practice questions ----------
prac = []
_pf = COURSE / 'guide' / '98_practice.md'
ptxt = open(_pf, encoding='utf-8').read() if _pf.exists() else ''
for m in re.finditer(r':::q\n(.*?)\n\?\?\?\n(.*?)\n:::', ptxt, re.S):
    q, a = m.group(1).strip(), m.group(2).strip()
    q = re.sub(r'^\d+\\?\.\s*', '', q)
    opts = re.split(r'\s(?=[A-E]\.\s)', q)
    item = {'q': opts[0], 'a': a}
    mt = re.match(r'\((Her [^,]+), L(\d+)\)\s*', item['q'])
    if mt:
        item['lec'] = 'l' + mt.group(2); item['q'] = mt.group(1) + ': ' + item['q'][mt.end():]; item['hers'] = True
    if len(opts) >= 3:
        item['opts'] = [re.sub(r'^[A-E]\.\s*', '', o) for o in opts[1:]]
        mm = re.match(r'([A-E])\.', a)
        item['ans'] = 'ABCDE'.index(mm.group(1)) if mm else None
    prac.append(item)

# ---------- assemble ----------
DATA = []
for lid, code, name, tag in LECS:
    h2, nodes = lecture_nodes(lid)
    lessons, cur, group = [], None, None
    intro_nodes, boss_nodes, onepage = [], [], None
    mode = 'intro'
    i = 0
    while i < len(nodes):
        el = nodes[i]
        nxt = nodes[i + 1] if i + 1 < len(nodes) else None
        if el.name in ('h3', 'h4'):
            t = txt(el)
            if el.get('id', '').startswith('howto') or el.get('id', '').startswith('read-'):
                mode = 'boss'; boss_nodes.append(el); i += 1; continue
            if 'on one page' in t:
                mode = 'one'; i += 1; continue
            if t.startswith('The big picture'):
                mode = 'intro'; intro_nodes.append(el); i += 1; continue
            if nxt is not None and nxt.name == 'aside' and 'co-key' in (nxt.get('class') or []):
                mode = 'lesson'
                objs = [txt(li) for li in nxt.find_all('li')]
                sk = nxt.find('em')
                skim = txt(sk.parent).replace('Skim:', '').strip() if sk else None
                cur = {'title': t, 'group': group, 'obj': objs, 'skim': skim, 'nodes': []}
                lessons.append(cur); i += 2; continue
            if mode != 'boss':
                group = t; mode = 'group'; i += 1; continue
        if mode == 'intro': intro_nodes.append(el)
        elif mode == 'lesson': cur['nodes'].append(el)
        elif mode == 'boss': boss_nodes.append(el)
        elif mode == 'one':
            if onepage is None and 'tbl' in (el.get('class') or []): onepage = str(el)
        i += 1
    # intro lesson
    story = [x for x in intro_nodes if x.name == 'aside' and 'co-story' in (x.get('class') or [])]
    intro = {'title': 'Start here: the big picture', 'group': None, 'skim': None,
             'obj': ['I know what this lecture is about in one sentence', 'I know which earlier ideas it builds on', 'I have the one-line memory trick for the whole lecture'],
             'cards': build_cards(intro_nodes)}
    out_lessons = [intro]
    for L in lessons:
        L['cards'] = build_cards(L.pop('nodes'))
        out_lessons.append(L)
    # assign cloze checks by token overlap
    lt = [toks(L['title'] + ' ' + ' '.join(L['obj']) + ' ' + ' '.join(BeautifulSoup(c['h'], 'html.parser').get_text() for c in L['cards'])) for L in out_lessons]
    for L in out_lessons: L['checks'] = []
    pool = [c for c in cloze if lec_of(c['n']) == lid] + [c for c in cloze if c['trap']]
    for c in pool:
        ct = toks(re.sub(r'\{\{c\d::(.*?)\}\}', r'\1', c['c']) + ' ' + c['e'])
        sc = [len(ct & t) / (1 + len(t) ** 0.35) for t in lt]
        best = max(range(len(sc)), key=lambda j: sc[j])
        if lec_of(c['n']) is None and sc[best] < 2.2: continue
        if best == 0 and len(out_lessons) > 1:
            best = max(range(1, len(sc)), key=lambda j: sc[j])
        out_lessons[best]['checks'].append(c)
    # boss questions
    bt = toks(' '.join(txt(x) for x in nodes))
    boss_q = []
    for q in prac:
        s = len(toks(q['q'] + ' ' + q['a']) & bt)
        q.setdefault('_s', {})[lid] = s
    DATA.append({'id': lid, 'code': code, 'name': name, 'tag': tag, 'badge': BADGE[lid], 'title': txt(h2),
                 'lessons': out_lessons, 'boss_cards': build_cards(boss_nodes), 'onepage': onepage})
# give each practice question to its best lecture
for q in prac:
    best = q.get('lec') or max(q['_s'], key=lambda k: q['_s'][k])
    for D in DATA:
        if D['id'] == best: D.setdefault('boss_q', []).append({k: v for k, v in q.items() if k not in ('_s', 'lec')})
for D in DATA: D.setdefault('boss_q', [])
for D in DATA: D['boss_q'].sort(key=lambda q: not q.get('hers'))

# cloze → simple structure
for D in DATA:
    for L in D['lessons']:
        L['checks'] = [{'n': c['n'], 'c': c['c'], 'e': c['e'], 'hook': c['hook']} for c in L['checks']]

GL = [{'t': t, 'm': m, 'd': d} for t, m, d, w in G]
json.dump({'lecs': DATA, 'gloss': GL}, open(BUILD / 'lessons.json', 'w'), ensure_ascii=False)
for D in DATA:
    nl = len(D['lessons']); nc = sum(len(L['cards']) for L in D['lessons']); nk = sum(len(L['checks']) for L in D['lessons'])
    empty = [L['title'][:30] for L in D['lessons'] if not L['checks']]
    print(D['code'], 'lessons', nl, 'cards', nc, 'checks', nk, 'boss_q', len(D['boss_q']), 'boss_cards', len(D['boss_cards']), 'onepage', bool(D['onepage']), 'nocheck', len(empty))
print(os.path.getsize(BUILD / 'lessons.json') // 1024, 'KB')
