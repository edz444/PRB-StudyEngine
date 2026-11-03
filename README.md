# Study engine

Turn a course's lecture slides into a full study kit, in my style:

- **Illustrated guide.** One web page told as a story, in plain English, with every technical word defined inline. It has memory hooks, exam traps, "her wording, decoded" boxes, key-takeaway bubbles, her real slide figures, SVG diagrams, optional 3D models and a Pathway Lab, plus tap-to-define terms.
- **Lesson Path app.** The guide cut into bite-sized lessons, one idea per screen, with:
  - a mission checklist
  - quick checks, stars and XP
  - a review pile
  - boss levels and badges
  - a day plan to the exam
  - a multi-page Panaboard board view you can flip through and copy by hand
- **Anki deck (.apkg).** Plain-English cloze cards with the slide image and diagram on the back. Each back has a memory hook, an exam trap, and the instructor's exact wording with a heads-up when it's harder than the idea. The deck has one subdeck per lecture and baked-in image occlusion cards.
- **NotebookLM PDFs.** One per lecture, for video and audio overviews.
- **Markdown export.** For DeepTutor or any other AI tutor.

The first course in here is MBB 322 (Cell Biology) Midterm 2, Lectures 5 to 11.

## Quick start

```bash
pip install -r requirements.txt
npm install && npx playwright install chromium
sudo apt install poppler-utils        # pdftoppm, pdftotext, pdfinfo

make all                              # builds the first course in courses/
make check                            # tests the guide and app at desktop and phone widths
COURSE=courses/mbb322-mt2 make anki   # build one thing for one course
```

Everything lands in `courses/<name>/out/`:

| File | What it is |
|---|---|
| `index.html` (+ `slides/`, `m3d/`, `lab.html`) | the guide; publish as a Claude artifact or open locally |
| `lessons/<slug>-lesson-path.html` (+ `slides/`, `lab.html`) | the Lesson Path app |
| `<APKG>` | the Anki deck; import over the old one and cards update in place |
| `notebooklm/*.pdf` | one PDF per lecture |
| `<GUIDE_MD>` and `deeptutor_<GUIDE_MD>` | Markdown exports |

## Start a new course

See [docs/NEW_COURSE.md](docs/NEW_COURSE.md). In short:

1. `cp -r courses/_template courses/bio101-mt1`, then fill in `course.py`.
2. Put the slide PDFs in `source/`, then extract the text and pick the figure slides with `engine/tools/prep_slides.py`.
3. Write the guide in `guide/*.md` using the markers in [docs/MARKERS.md](docs/MARKERS.md). Write the cards in `anki/cards.txt` and the instructor-wording files.
4. `COURSE=courses/bio101-mt1 make all check`.

The quickest way is to hand the slides to Claude with the skills in `skills/` loaded. They describe the whole method, including the writing style (see [docs/STYLE.md](docs/STYLE.md)).

## Layout

```
engine/                   shared code, same for every course
  common.py               course paths and settings loader (COURSE=courses/<name>)
  guide/                  build.py (guide + Markdown), dlib.py (SVG diagrams), style.css, page.js, term.js
  lessons/                build_lessons.py (cut guide into lessons), assemble.py, app_template.html
  anki/                   build_apkg.py (deck), io_build.py (image occlusion)
  tools/                  prep_slides.py, figpng.js, io_lines.js, io_extract.js, notebooklm_pdf.js, check.js
courses/
  _template/              a tiny working course to copy
  mbb322-mt2/             MBB 322 Midterm 2
    course.py             every course-specific setting (titles, nav, exam date, day plan, deck names, IDs)
    guide/                the guide, one Markdown file per lecture
    content/              glossary, diagrams, pathway boards, optional 3D scenes
    anki/                 cards.txt, per-card plain backs + instructor wording, slide/diagram maps, occlusion spec
    lab/                  optional interactive Pathway Lab
    slides/ source/       instructor files, never committed
skills/                   the Claude skills that write the content in this style
docs/                     markers, style rules, new-course walkthrough
```

## Privacy

Instructor slide PDFs, extracted slide text and rendered slide images are gitignored. The guide quotes short pieces of slide wording for study, so keep this repo private.
