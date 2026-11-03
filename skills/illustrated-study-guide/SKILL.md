---
name: "illustrated-study-guide"
description: "Build Ethan's illustrated course study guide (HTML artifact with real slide figures plus SVG diagrams), a matching Anki cloze deck, and DeepTutor Markdown files from lecture slides and transcripts."
---

# Illustrated study guide

Use this when Ethan uploads lecture slides (PDF or PPTX) and maybe transcripts and wants a study package for an exam. Apply the humanizer skill to all prose.

## Content rules
- Slides are authoritative. Transcripts add emphasis and "she/he flagged this" moments. Skip course logistics.
- Plain, teach-from-scratch English. Define every technical word inline the first time. No assumed background.
- Every concept gets exam-ready analogies and mnemonics. Quality over quantity.
- If there are no transcripts, say so in a note at the top and build the "emphasized" boxes from questions the instructor wrote on the slides, labelled that way. Never invent lecture quotes.

## Workflow
1. Read everything first. Extract slide text (pdftotext -layout), then rasterize pages and view contact sheets (montage) so figure-only content isn't missed. For PPTX, convert to PDF with LibreOffice first.
2. Write the guide as Markdown source files, one per lecture, with custom markers: `:::hook`, `:::conn`, `:::trap`, `:::she`, `:::note` blocks, `{{fig:name}}` for custom SVG diagrams, `{{slide:L5-4|caption}}` for real slide figures.
3. Structure: big-picture "one story" opener, a short list of recurring threads, one section per lecture at full card-level detail, worked "how to figure it out" sections (tells, decision approach, practice examples) for anything that is reasoning rather than memorizing, and a one-glance cheat sheet at the end.
4. Real slide figures: keep only slides with a diagram, graph or labeled figure; skip text-only slides. Render with pdftoppm about 130 dpi, trim, resize to about 1100 px, JPEG quality about 72. Verify page numbers against a labeled montage before inserting. Each figure sits next to the concept it explains, with a one-line caption that says what to notice.
5. Custom SVG diagrams only where no slide figure is clean or a simpler plain-English version helps: structure, two-state comparison, step-by-step pathway across a membrane, how-the-parts-connect. One claim each, captioned, colours from CSS classes so they work in light and dark.
6. Build script converts the source to: (a) one HTML page with sticky chip nav, callouts, figures, click-to-enlarge slides, and (b) a Markdown export for DeepTutor (callouts become blockquotes, figures become italic caption lines).
7. Check rendering with Playwright: screenshot every diagram in light and dark, check no SVG text runs past the viewBox, check phone width (390 px) has no horizontal scroll. Fix overlapping labels before publishing.
8. Publish the HTML as an artifact with the slide images passed through `files`.

## Design (match the MBB 322 guides)
- Teal accent #0e7490, orange memory hook #c2410c, amber exam trap #b45309, on a warm off-white (light) and dark slate (dark) ground.
- Callout styles: orange "Memory hook" cards, teal dashed "Connection" cards, amber "Exam trap" cards with a left rule, teal "She emphasized" boxes.
- Body face Atkinson Hyperlegible, headings Literata, labels JetBrains Mono. Sentence-case headings.

## Anki cloze deck
- Write a template file, one card per line: `CLOZE ||| EXPLANATION ~~~ HOOK`.
- Script builds a tab-separated .txt: Field 1 cloze text, Field 2 Back Extra = teal explanation div (#0e7490), `<br>`, orange "Memory hook:" label (#c2410c) plus hook. Single-quoted HTML attributes, `<br>` only, no real newlines, no header row.
- Never put <, > or & in the source text (write "less than").
- Verify: exactly one tab per line, no angle brackets in the cloze field, every card has a hook, cloze braces balanced.
- Import settings to tell him: Type Cloze, Fields separated by Tab, Field 1 to Text, Field 2 to Back Extra, Allow HTML on.

## DeepTutor files
- The full guide as Markdown plus one condensed notes file per lecture (dense bullet notes, numbers, and an exam traps list), for a DeepTutor Knowledge Hub.

## Delivery
- Publish the guide artifact, send the Anki .txt and the Markdown files with SendUserFile. Keep the closing message short: what's there, import settings, any gaps (like missing transcripts).