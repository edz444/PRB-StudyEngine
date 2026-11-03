"""Course settings. Copy this folder to courses/<course-exam> and fill in every value."""

SLUG = 'bio101'                         # short id for file names, media names and saved progress
INSTRUCTOR = 'Dr. Lee'                  # used in "How Dr. Lee words it" boxes and tags

# ---------- guide ----------
TITLE = 'BIO 101 Midterm 1 Guide'
EYEBROW = 'BIO 101 · Midterm 1 · Dr. Lee'
GUIDE_MD = 'BIO101_Midterm1_Study_Guide.md'
NAV = [('story', 'Story'), ('l1', 'L1 Cells'), ('glossary', 'Glossary')]   # (heading id, menu label)
LAB_URL = ''                            # optional interactive pathway lab
GUIDE_URL = ''                          # fill in after the guide is published, so the app can link to it
M3D_NAMES = {}                          # optional 3D models (see content/atlas_*.js in mbb322-mt2)
DEEPTUTOR_SKIP = []

# ---------- lesson app ----------
APP_TITLE = 'BIO 101 Lesson Path'
APP_EYEBROW = 'BIO 101 · Midterm 1 · Lecture 1'
EXAM = '2027-02-12T09:00'
PLAN = [{'date': '2027-02-10', 'name': 'Wed', 'lecs': ['l1'], 'desc': 'Lecture 1'},
        {'date': '2027-02-11', 'name': 'Thu', 'lecs': ['review'], 'desc': 'Review pile'}]
LECS = [('l1', 'L1', 'Cells', 'What a cell is made of')]    # (heading id, code, short name, tagline)
BADGE = {'l1': 'Cell Starter'}
TRAP_SECTION = 'trap cards'             # a cards.txt section whose cards can join any lecture's checks

# ---------- Anki ----------
DECK_ROOT = 'BIO 101::Midterm 1'
DECK_NAMES = {1: 'L01 Cells', 0: 'L00 Exam strategy'}
APKG = 'BIO101_Midterm1_Anki.apkg'
TAGS = ['BIO101', 'midterm1']
# Pick new random 10-digit IDs for every course, then never change them (re-imports update cards in place).
MODEL_ID, IO_MODEL_ID = 1707000101, 1707000102
DECK_ID_BASE, IO_DECK_ID_BASE = 2107000100, 2107000300
GUID_TAG, IO_GUID_TAG = 'bio101-mt1', 'bio101-io'
WORDING_FILES = ['wording_l1']
TRAP_CARDS = (0, -1)                    # card number range tagged <instructor>_trap (empty here)
REVIEW_CARDS = (0, -1)

# ---------- NotebookLM ----------
NOTEBOOKLM = [('l1', 'L01_Cells', 'Lecture 1: Cells')]
