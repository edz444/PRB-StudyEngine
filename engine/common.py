"""Shared paths and course settings. Pick a course with COURSE=courses/<name> (default: the only course folder)."""
import os, sys, importlib.util
from pathlib import Path

ENGINE = Path(__file__).resolve().parent
ROOT = ENGINE.parent

def _default_course():
    cs = sorted(p for p in (ROOT / 'courses').iterdir() if p.is_dir() and not p.name.startswith('_'))
    return cs[0]

COURSE = Path(os.environ.get('COURSE') or _default_course())
if not COURSE.is_absolute(): COURSE = (ROOT / COURSE).resolve()
OUT = COURSE / 'out'          # finished files to publish or import
BUILD = COURSE / 'build'      # intermediate files (diagram PNGs, occlusion images, lesson data)
SLIDES = COURSE / 'slides'    # rendered slide figures, L5-4.jpg (gitignored)
for d in (OUT, BUILD): d.mkdir(parents=True, exist_ok=True)

for p in (COURSE / 'content', COURSE / 'anki', ENGINE / 'guide'):
    if str(p) not in sys.path: sys.path.insert(0, str(p))

def load_cfg():
    spec = importlib.util.spec_from_file_location('course_cfg', COURSE / 'course.py')
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

CFG = load_cfg()
