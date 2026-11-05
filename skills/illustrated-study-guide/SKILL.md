---
name: "illustrated-study-guide"
description: "Build Ethan's illustrated course study guide (HTML artifact with real slide figures plus SVG diagrams), a matching Anki cloze deck, and DeepTutor Markdown files from lecture slides and transcripts."
---

# Illustrated study guide

Use this when Ethan uploads lecture slides (PDF or PPTX) and maybe transcripts and wants a study package for an exam. Apply the humanizer skill to all prose.

The guide is built by his PRB-StudyEngine repo, the same engine that makes the Lesson Path app and the Anki deck. Follow the "Start from PRB-StudyEngine" and "When he asks for a change" sections of the interactive-lesson-path skill: clone the repo, write only course content, build with `make`, republish to the same links, commit and push.

## Content rules
- Slides are authoritative. Transcripts add emphasis and "she/he flagged this" moments. Skip course logistics.
- Plain, teach-from-scratch English. Define every technical word before it's used. No assumed background.
- Every concept gets exam-ready analogies and mnemonics. Quality over quantity.
- If there are no transcripts, say so in a note at the top and build the "emphasized" boxes from questions the instructor wrote on the slides, labelled that way. Never invent lecture quotes.

## The clarity bar
His test: could he follow it without opening ChatGPT? Sections that failed it listed protein names with no single message tying them together, used terms before defining them, or squeezed clauses into table cells ("the spread tumors (metastases), not the first tumor, usually kill"). So in every section:
1. Open with "The short version:" giving the one message the section passes along, in everyday words ("Axon, don't grow this way. Turn away!").
2. Then "The words you need": define every new term before using it, and re-explain basics the section leans on.
3. Pathways and experiments as numbered steps, one per line, each protein given a job title ("Ephexin is the GEF"), then one line on what the experiment proves.
4. Table cells as full phrases that make sense alone; column headers as plain questions.
5. Short sentences, linked to patterns he already knows.
6. Re-read every table row and key bullet out of context before publishing, and rewrite any that would make him stop.

## Workflow
1. Read everything first. Extract slide text (pdftotext -layout), then rasterize pages and view contact sheets (montage) so figure-only content isn't missed. For PPTX, convert to PDF with LibreOffice first.
2. Write the guide as Markdown source files, one per lecture, with custom markers: `:::key` (2 to 4 takeaways plus an optional `*Skim:*` line, right after each idea's heading), `:::hook`, `:::conn`, `:::trap`, `:::easy`, `:::she`, `:::nancy` (instructor wording, then "Plain version:"), `:::exam` ("On her practice set", see below), `:::note`, `:::q` practice questions, `{{fig:name}}` for custom SVG diagrams, `{{slide:L5-4|caption}}` for real slide figures.
3. Structure: big-picture "one story" opener, a short list of recurring threads, one section per lecture at full card-level detail, worked "how to figure it out" sections (tells, decision approach, practice examples) for anything that is reasoning rather than memorizing, and a one-glance cheat sheet at the end.
4. Real slide figures: keep only slides with a diagram, graph or labeled figure; skip text-only slides. Render with pdftoppm about 130 dpi, trim, resize to about 1100 px, JPEG quality about 72. Verify page numbers against a labeled montage before inserting. Each figure sits next to the concept it explains, with a one-line caption that says what to notice.
5. Custom SVG diagrams only where no slide figure is clean or a simpler plain-English version helps: structure, two-state comparison, step-by-step pathway across a membrane, how-the-parts-connect. One claim each, captioned, colours from CSS classes so they work in light and dark.
6. Build script converts the source to: (a) one HTML page with sticky chip nav, callouts, figures, click-to-enlarge slides and tap-to-define glossary terms, and (b) a Markdown export for DeepTutor (callouts become blockquotes, figures become italic caption lines).
7. Tap-to-define: link glossary terms in every paragraph and callout, once per term per block, so a definition is always one tap away. Never link only the first use per lecture.
8. Check rendering with Playwright: screenshot every diagram in light and dark, check no SVG text runs past the viewBox, check phone width (390 px) has no horizontal scroll. Fix overlapping labels before publishing.
9. Publish the HTML as an artifact with the slide images passed through `files`.

## The instructor's practice set
When he uploads practice questions or a past exam:
- Work out how she tests (for MBB 322: "blocked or locked, predict", compare two systems, "rationalize", "define then explain the rationale", "which is INCORRECT", distractors borrowed from other pathways).
- Add a rose `:::exam` "On her practice set" box at each tested spot with a model answer and why each wrong option fails; add plain explanations for anything she asks that isn't on her slides; flag any mismatch between her question wording and her slides.
- Add her questions to the practice chapter as `:::q` blocks, each tagged `(Her Q10, L5)`, with a short "how she tests" `:::exam` box at the top, and add a row for each to that lecture's "Reading her questions" table.

## Design (match the MBB 322 guides)
- Teal accent #0e7490, orange memory hook #c2410c, amber exam trap #b45309, indigo instructor wording, green key takeaways, rose #be123c practice-set boxes, on a warm off-white (light) and dark slate (dark) ground.
- Callout styles: orange "Memory hook" cards, teal dashed "Connection" cards, amber "Exam trap" cards with a left rule, teal "She emphasized" boxes, rose "On her practice set" boxes.
- Body face Atkinson Hyperlegible, headings Literata, labels JetBrains Mono. Sentence-case headings.

## Anki deck
Use the anki-slide-deck skill to build an .apkg with slide images, instructor wording and practice-set cards. Only fall back to a tab-separated .txt (Field 1 cloze, Field 2 Back Extra; single-quoted HTML attributes; no `<`, `>` or `&` in source text; import as Type Cloze, Tab-separated, Allow HTML on) if he asks for a text import.

## DeepTutor files
The full guide as Markdown plus one condensed notes file per lecture (dense bullet notes, numbers, and an exam traps list), for a DeepTutor Knowledge Hub. Refresh them, and any NotebookLM PDFs, whenever the guide changes.

## Delivery
Publish the guide artifact and send the deck and Markdown files with SendUserFile. Keep the closing message short: what's there, any gaps (like missing transcripts), and anything in her wording that doesn't match her slides.
