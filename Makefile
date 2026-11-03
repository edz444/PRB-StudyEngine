# Study engine: lecture slides -> plain-English guide, Lesson Path app, Anki deck, NotebookLM PDFs.
# Pick a course with COURSE=courses/<name> (defaults to the first folder in courses/).
COURSE ?= $(firstword $(filter-out courses/_template,$(wildcard courses/*)))
export COURSE
PY ?= python3
NODE ?= NODE_PATH=$$(npm root -g):node_modules node

.PHONY: all guide lessons anki occlusion notebooklm check clean help
help:
	@echo "make guide       build the illustrated guide (out/index.html) + Markdown export"
	@echo "make lessons     build the Lesson Path app (out/lessons/)"
	@echo "make anki        build the Anki deck with slide images, diagrams and image occlusion (out/*.apkg)"
	@echo "make notebooklm  one PDF per lecture for NotebookLM (out/notebooklm/)"
	@echo "make all         everything above"
	@echo "make check       test the guide and app at desktop and phone widths"
	@echo "COURSE=$(COURSE)"

guide:
	$(PY) engine/guide/build.py

lessons: guide
	$(PY) engine/lessons/build_lessons.py
	$(PY) engine/lessons/assemble.py

occlusion: guide
	$(NODE) engine/tools/figpng.js
	$(NODE) engine/tools/io_lines.js
	$(PY) engine/anki/io_build.py

anki: occlusion
	$(PY) engine/anki/build_apkg.py

notebooklm: guide
	$(NODE) engine/tools/notebooklm_pdf.js

all: guide lessons anki notebooklm

check: lessons
	$(NODE) engine/tools/check.js

clean:
	rm -rf $(COURSE)/out $(COURSE)/build
