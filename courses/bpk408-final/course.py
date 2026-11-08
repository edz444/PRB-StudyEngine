"""Settings for BPK 408W (Cellular Physiology Lab) final quiz, Weeks 1 to 8."""

SLUG = 'bpk408'
INSTRUCTOR = 'Agata'

# ---------- guide ----------
TITLE = 'BPK 408W Final Quiz Guide'
EYEBROW = 'BPK 408W · Final Quiz · Agata'
GUIDE_MD = 'BPK408W_Final_Study_Guide.md'
NAV = [('story', 'Story'), ('threads', 'Threads'),
       ('l1', 'W1 Cells'), ('l2', 'W2 Microscopy'), ('l3', 'W3-4 Myocardin'), ('l4', 'W5 RNA'),
       ('l5', 'W6 Staining'), ('l6', 'W7 ddPCR'), ('l7', 'W8 Analysis'),
       ('glossary', 'Glossary'), ('practice', 'Practice'), ('cheat', 'Cheat sheet')]
LAB_URL = ''
GUIDE_URL = 'https://claude.ai/artifact/NXuHf3sS5T8u3ZX8Ed5FyQ'
GUIDE_SUB = 'slide figures and worked questions'
M3D_NAMES = {}
DEEPTUTOR_SKIP = ['## Practice, worked']

# ---------- lesson app ----------
APP_TITLE = 'BPK 408W Lesson Path'
APP_EYEBROW = 'BPK 408W · Final Quiz · Weeks 1 to 8'
EXAM = '2026-11-09T09:00'
# One-day cram: Sunday is the only study day, exam Monday morning.
PLAN = [
    {'date': '2026-11-08', 'name': 'Sun', 'lecs': ['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'review'], 'desc': 'All eight weeks today, then your review pile'},
]
LECS = [('l1', 'W1', 'Week 1', 'Growing and counting cells'),
        ('l2', 'W2', 'Week 2', 'Fluorescence microscopy'),
        ('l3', 'W3-4', 'Weeks 3-4', 'Myocardin and transfection'),
        ('l4', 'W5', 'Week 5', 'RNA and reverse transcription'),
        ('l5', 'W6', 'Week 6', 'Staining and imaging'),
        ('l6', 'W7', 'Week 7', 'Droplet digital PCR'),
        ('l7', 'W8', 'Week 8', 'Reading ddPCR data')]
BADGE = {'l1': 'Cell Counter', 'l2': 'Light Bender', 'l3': 'Gene Switcher', 'l4': 'RNA Wrangler',
         'l5': 'Actin Imager', 'l6': 'Droplet Reader', 'l7': 'Threshold Boss'}
TRAP_SECTION = 'exam traps'

# ---------- Anki ----------
DECK_ROOT = 'BPK 408W::Final Quiz'
DECK_NAMES = {1: 'W1 Cells', 2: 'W2 Microscopy', 3: 'W3-4 Myocardin', 4: 'W5 RNA',
              5: 'W6 Staining', 6: 'W7 ddPCR', 7: 'W8 Analysis', 0: 'W0 Exam strategy'}
APKG = 'BPK408W_Final_Anki.apkg'
TAGS = ['BPK408W', 'final']
# Fixed once imported, so re-imports update cards in place.
MODEL_ID, IO_MODEL_ID = 1811400801, 1811400802
DECK_ID_BASE, IO_DECK_ID_BASE = 2411400800, 2411400900
GUID_TAG, IO_GUID_TAG = 'bpk408-final', 'bpk408-io'
WORDING_FILES = ['wording_l1', 'wording_l2', 'wording_l3', 'wording_l4', 'wording_l5', 'wording_l6', 'wording_l7']
TRAP_CARDS = (0, -1)
REVIEW_CARDS = (0, -1)

# ---------- NotebookLM ----------
NOTEBOOKLM = [('l1', 'W1_Cells', 'Week 1: growing and counting cells'),
              ('l2', 'W2_Microscopy', 'Week 2: fluorescence microscopy'),
              ('l3', 'W34_Myocardin', 'Weeks 3-4: myocardin and transfection'),
              ('l4', 'W5_RNA', 'Week 5: RNA and reverse transcription'),
              ('l5', 'W6_Staining', 'Week 6: staining and imaging'),
              ('l6', 'W7_ddPCR', 'Week 7: droplet digital PCR'),
              ('l7', 'W8_Analysis', 'Week 8: reading ddPCR data')]
LEC_TAGS = {1: 'W1_Cells', 2: 'W2_Microscopy', 3: 'W34_Myocardin', 4: 'W5_RNA', 5: 'W6_Staining', 6: 'W7_ddPCR', 7: 'W8_Analysis'}
PRACTICE_TAG = 'her_practice_set'
