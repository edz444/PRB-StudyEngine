---
name: "anki-slide-deck"
description: "Build Ethan's Anki .apkg deck from lecture slides: plain-English cloze cards with the slide image and diagrams in Back Extra, memory hooks, exam traps, the instructor's exact wording, per-lecture subdecks and image occlusion cards. Use whenever he asks for Anki cards, flashcards for Anki, or an Anki deck."
---

# Anki slide deck

Build an importable `.apkg`, not a text file, so the slide images travel with the cards. This is the format refined for MBB 322 Midterm 2. Apply the humanizer skill to all text. Plain English first, then technical terms, with every unfamiliar word explained.

## Clarity
Every back must make sense on its own, read cold weeks later. Open with the one thing the card is about in everyday words, define any term before using it, give pathway steps in order with a job title for each protein ("Ephexin is the GEF"), and never squeeze clauses together. If he would need to look something up to understand the back, rewrite it.

## Card source format
Write `cards.txt`, one note per line, grouped under `# ---------- L5 Name ----------` headers:

`CLOZE ||| EXPLANATION ~~~ HOOK ^^^ TRAP`

- CLOZE: one fact per card with `{{c1::...}}` blanks. Put the tested word in the blank, not the whole sentence. Two or three blanks at most, numbered when they should be asked separately. Never put `<`, `>`, `&` or tabs in any field (the build asserts this), so write "more than 80%", not ">80%".
- EXPLANATION: an everyday-words version with an analogy ("PDE is the eraser").
- HOOK: a mnemonic or comparison that is memorable and actually exam-useful.
- TRAP (optional): how the instructor could trick him, especially "both boxes" items, order and swap traps, and "phosphorylated doesn't always mean active".

Card numbers come from line order. Once a deck is out, only append new cards at the end of the file (under a new header if needed), never insert in the middle, or every map keyed by card number shifts.

Keep the cloze text stable once a deck has been given to him. The note ID is made from it (`genanki.guid_for(tag, cloze)`), so a re-import updates his cards in place and keeps his review history. Put improvements on the back.

## Instructor wording (separate per-lecture files)
For each card add `dict(e=..., nw=..., hu=...)` in `v3_lN.py`, keyed by card number:
- `e`: the plain-English back (it replaces EXPLANATION).
- `nw`: "How [instructor] words it", quoted from her slide text or her practice questions (read the extracted text; never invent wording).
- `hu`: a heads-up, only where her phrasing is harder than the idea. Examples: "Cytokines are stably associated with JAKs" means the receptors; "co-receptor Groucho" is really a co-repressor; a slide number that applies more narrowly than stated. Tag those notes `nancy_wording_harder` (use the instructor's name).

Add a matching callout to the study guide for each heads-up so the two stay consistent.

## Practice-set cards
When he uploads the instructor's practice questions, add a card per tested idea at the end of `cards.txt`, with backs in `v3_prac.py`:
- `nw` quotes her question and her answer option.
- Add `lec=N` to each entry. It files the card in that lecture's subdeck even when there's no slide image, and adds the practice tag (`her_practice_set`) so he can drill just those.
- The trap says why her wrong options fail (often a true fact from another pathway).
- Use `hu` for any mismatch with her slides (E. coli vs Salmonella in the Ames test).
- Add `v3_prac` to every place that loads the wording files, including the lesson app builder.

## Back layout (no scrolling on flip)
The note type is cloze with fields Text and Back Extra. Template: `{{cloze:Text}}<hr>{{Back Extra}}`. Never add `id=answer`, which makes Anki scroll down on flip; the card must stay at the top. The Back Extra order:
1. The explanation in teal (#0e7490).
2. A bold orange (#c2410c) "Memory hook:" line.
3. An indigo box headed "How Nancy words it:" containing her quote and, if present, a red "Heads-up, her wording is harder than it needs to be:" line.
4. An amber box headed "Exam trap:" (#b45309 rule on a light amber background), if the card has a trap.
5. A small grey caption "Lecture N, slide P", then the slide image.
6. An optional caption "Diagram", then a clean PNG of the matching SVG diagram.

CSS: Arial 20 px, left-aligned, cloze in bold teal (lighter teal in night mode), images `max-width:100%` with a thin border and rounded corners.

## Slide images
- `imgmap.py` maps card number to (lecture, page). Only map slides with a real figure that supports that card, and check page numbers against a labeled contact sheet.
- Render with pdftoppm at about 130 dpi, trim, resize to about 1100 px, JPEG quality about 72. Name media with a prefix (`mbb322_L5-4.jpg`) so they never clash with his other decks.
- `figmap.py` maps cards to diagram PNGs rendered from the guide's SVGs in light theme. Only map a diagram that actually shows the card's idea.

## Decks and tags
- Subdecks: `Course::Exam::L05 Name`, one per lecture, plus `L00 Exam strategy and MT1 review` for cards that span lectures. A card's subdeck comes from its slide image, or its `lec` value when it has no slide. Image occlusion goes in `::Image occlusion` children of each lecture.
- Tags: course, exam, lecture tag, `has_trap`, the instructor-trap tag for question-style cards, `her_practice_set`, and `MT1_review` for past-exam lessons.
- Include instructor-style trap cards built from his past exam: verdict plus the molecular feature that proves it, which is how short answers are marked.

## Image occlusion (baked masks)
Use a separate note type with fields Header, Front, Back, Answer and Extra. For each key figure:
- Find the label positions (OCR or by hand) in `io_spec.py`. Build each card with PIL: on the front, every label is covered by an amber box and the target label by a red box with "?"; the back shows the target revealed with the others still covered.
- One card per label. Skip duplicate labels that would give an answer away, and skip labels that are not exam-relevant.
- Header: "Figure title (n of N)". Front: "Name the part under the red box".
- The note ID comes from the figure and the label number.

## Build and verify
Build with genanki (`pip install genanki --break-system-packages`), one Package containing every deck and all media. Before delivering:
- Assert every note has a back entry and no field contains `<`, `>` or `&` in source text.
- Confirm every media file exists and is packaged.
- Unzip the .apkg, open collection.anki2 with sqlite, check new notes landed in the right subdecks with the right tags, render one note's back to HTML with Playwright, and look at it.
- Check special characters survive (Greek letters, arrows). Never run sed character classes on UTF-8 files; edit in Python instead.

Deliver the .apkg with SendUserFile. Tell him to import it over the existing deck: same fronts means his cards update in place with no duplicates. Name the tags he can use to drill the confusing-wording cards and the practice-set cards.
