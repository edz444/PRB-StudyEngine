# Starting a new course

## 1. Copy the template

```bash
cp -r courses/_template courses/bio101-mt1
export COURSE=courses/bio101-mt1
```

Edit `course.py`:

- **Names.** Titles, nav, lectures (`LECS`), badges, deck names, exam date and the day plan.
- **Anki IDs.** Pick new random IDs for `MODEL_ID`, `IO_MODEL_ID`, `DECK_ID_BASE` and `IO_DECK_ID_BASE`, plus a new `GUID_TAG` and `IO_GUID_TAG`. Never change them after the first import, or Anki will make duplicates instead of updating cards.

The template is a tiny working course. Run `make all check` once to see every output before replacing its content.

## 2. Slides

Put the PDFs in `source/`. For PPTX files, convert first: `soffice --headless --convert-to pdf deck.pptx`.

```bash
python engine/tools/prep_slides.py text  5 source/Lecture_5.pdf          # slide text, for quoting her wording
python engine/tools/prep_slides.py sheet 5 source/Lecture_5.pdf          # numbered contact sheet to spot figure slides
python engine/tools/prep_slides.py figs  5 source/Lecture_5.pdf 4 8 12   # slides/L5-4.jpg ... (real figures only)
```

## 3. Write the guide

Write one Markdown file per lecture in `guide/`, numbered so they sort in reading order (`05_gpcr.md`). Follow [MARKERS.md](MARKERS.md) and [STYLE.md](STYLE.md).

Also add:

- `content/glossary.py`: every technical term.
- `content/diagrams*.py`: SVG diagrams.
- `content/boards.py`: hand-written pathway boards.
- `guide/98_practice.md`: practice questions in her style.

Then:

```bash
make guide        # check out/index.html in a browser
make lessons      # check out/lessons/<slug>-lesson-path.html
```

## 4. Anki

- Write `anki/cards.txt` and one wording file per lecture (`WORDING_FILES` in `course.py`).
- Map cards to slides in `imgmap.py` and to diagrams in `figmap.py`.
- For image occlusion, list each diagram's labels with `node engine/tools/io_extract.js --all`, then choose targets in `io_spec.py`.

```bash
make anki         # out/<APKG>
```

## 5. Check and publish

```bash
make check        # guide + app at 1280 and 390 px, a lesson, a board, a boss level
make notebooklm   # out/notebooklm/*.pdf
```

To publish:

- **Guide:** publish `out/index.html` as a Claude artifact, passing `slides/`, `m3d/` and `lab.html` as files.
- **App:** publish `out/lessons/<slug>-lesson-path.html` with its `slides/` and `lab.html`.
- **Link them:** put the guide's URL in `GUIDE_URL` and rebuild the app so it links back to the guide.
