"""Settings for MBB 322 (Cell Biology) Midterm 2, Lectures 5 to 11. Copy courses/_template to start a new course."""

SLUG = 'mbb322'                       # short id used in file names, media names and storage keys
INSTRUCTOR = 'Nancy'

# ---------- guide ----------
TITLE = 'MBB 322 Midterm 2 Guide'
EYEBROW = 'MBB 322 · Midterm 2 · Nancy'
GUIDE_MD = 'MBB322_Midterm2_Study_Guide.md'          # Markdown export (DeepTutor, NotebookLM text)
NAV = [('story', 'Story'), ('threads', 'Threads'), ('toolkit', 'Ch 0 Toolkit'), ('mt1', 'MT1 lessons'),
       ('l5', 'L5 GPCRs'), ('l6', 'L6 Synapses'), ('l7', 'L7 Optogenetics'), ('l8', 'L8 RTKs'),
       ('l9', 'L9 Cancer I'), ('l10', 'L10 Cancer II'), ('l11', 'L11 Cancer III'),
       ('glossary', 'Glossary'), ('practice', 'Practice'), ('cheat', 'Cheat sheet')]
LAB_URL = 'https://claude.ai/artifact/3bbKhgTJsos4CqwyVsvP52'   # standalone Pathway Lab, optional
GUIDE_URL = 'https://claude.ai/artifact/384TtCv1LYaSUgLPE1eHD5' # published guide, linked from the app
M3D_NAMES = {'na': 'Na+ channel: three states', 'axon': 'Action potential and myelin', 'syn': 'Synapse: calcium is the send button',
             'sarc': 'Sarcomere: Ca2+, troponin, tropomyosin', 'gp': 'G protein switch', 'opto': 'ChR2 vs halorhodopsin',
             'met': 'Benign vs malignant: the basal lamina'}
DEEPTUTOR_SKIP = ['## What midterm 1', '## Practice in her style']   # sections left out of the DeepTutor copy

# ---------- lesson app ----------
APP_TITLE = 'MBB 322 Lesson Path'
APP_EYEBROW = 'MBB 322 · Midterm 2 · Lectures 5 to 11'
EXAM = '2026-11-06T09:00'
PLAN = [
    {'date': '2026-11-02', 'name': 'Mon', 'lecs': ['l5', 'l6'], 'desc': 'Finish GPCRs, then Synapses'},
    {'date': '2026-11-03', 'name': 'Tue', 'lecs': ['l7', 'l8'], 'desc': 'Optogenetics, then RTKs'},
    {'date': '2026-11-04', 'name': 'Wed', 'lecs': ['l9', 'l10'], 'desc': 'Cancer I and Cancer II'},
    {'date': '2026-11-05', 'name': 'Thu', 'lecs': ['l11', 'review'], 'desc': 'Cancer III, then your review pile'},
]
LECS = [('l5', 'L5', 'GPCRs', 'The doorbell and the switch'), ('l6', 'L6', 'Synapses', 'Wires, sparks and muscle'),
        ('l7', 'L7', 'Optogenetics', 'A light switch for neurons'), ('l8', 'L8', 'RTKs', 'Grow signals and the Ras relay'),
        ('l9', 'L9', 'Cancer I', 'What a cancer cell is'), ('l10', 'L10', 'Cancer II', 'Causes and gas pedals'),
        ('l11', 'L11', 'Cancer III', 'Brakes, Wnt and TGFβ')]
BADGE = {'l5': 'Signal Switcher', 'l6': 'Spark Runner', 'l7': 'Light Wizard', 'l8': 'Relay Racer',
         'l9': 'Tumor Tracker', 'l10': 'Pedal Detective', 'l11': 'Brake Master'}
TRAP_SECTION = 'Nancy-style trap'      # cards.txt section whose cards can join any lecture's checks

# ---------- Anki ----------
DECK_ROOT = 'MBB 322::Midterm 2'
DECK_NAMES = {5: 'L05 GPCRs', 6: 'L06 Synaptic signaling', 7: 'L07 Optogenetics', 8: 'L08 RTKs', 9: 'L09 Cancer I',
              10: 'L10 Cancer II', 11: 'L11 Cancer III', 0: 'L00 Exam strategy and MT1 review'}
APKG = 'MBB322_Midterm2_Anki.apkg'
TAGS = ['MBB322', 'midterm2']
# Keep these IDs fixed once a deck has been imported, so re-imports update cards in place.
MODEL_ID, IO_MODEL_ID = 1607392320, 1607392330
DECK_ID_BASE, IO_DECK_ID_BASE = 2059400200, 2059400300
GUID_TAG, IO_GUID_TAG = 'mbb322-mt2-v2', 'mbb322-io'
WORDING_FILES = ['v3_l5', 'v3_l6', 'v3_l7', 'v3_l8', 'v3_l9', 'v3_l10', 'v3_l11']   # plain back + instructor wording per card
TRAP_CARDS = (126, 139)       # card numbers tagged nancy_trap
REVIEW_CARDS = (140, 145)     # card numbers tagged MT1_review (no lecture deck)

# ---------- NotebookLM PDFs ----------
NOTEBOOKLM = [('toolkit', 'L00_Background_toolkit', 'Background toolkit (read before any lecture)'),
              ('l5', 'L05_GPCRs', 'Lecture 5: G protein coupled receptors'), ('l6', 'L06_Synaptic_signaling', 'Lecture 6: Synaptic signaling and neurons'),
              ('l7', 'L07_Optogenetics', 'Lecture 7: Optogenetics'), ('l8', 'L08_RTKs', 'Lecture 8: Receptor tyrosine kinases'),
              ('l9', 'L09_Cancer_I', 'Lecture 9: Cancer I'), ('l10', 'L10_Cancer_II', 'Lecture 10: Cancer II'), ('l11', 'L11_Cancer_III', 'Lecture 11: Cancer III')]
LEC_TAGS = {5: 'L5_GPCRs', 6: 'L6_Synapses', 7: 'L7_Optogenetics', 8: 'L8_RTKs', 9: 'L9_Cancer_I', 10: 'L10_Cancer_II', 11: 'L11_Cancer_III'}
