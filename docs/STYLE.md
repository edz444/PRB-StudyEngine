# Style

## Writing

- **Write for a beginner.** Explain everything for someone with no background in the subject. Plain English first, then the technical term, defined inline the first time it appears.
- **Keep every fact.** Every fact from the slides stays in. A rewrite changes the wording, never the content. Check by script that every number, bolded term and figure survives.
- **Teach with comparisons.** Every idea gets an analogy or a real-life comparison. Every list worth memorizing gets a mnemonic that is memorable and actually exam-useful (for example "A Kid Should Panic": APC, K-ras, Smad4, p53).
- **Flag tricks.**
  - Exam traps get their own box, especially "both boxes" items (something that belongs in two categories) and order or swap traps.
  - When the instructor's slide wording is harder than the idea (jargon, typos, a word used loosely), quote it and give the plain version.
  - Never invent instructor quotes.
- **No AI-writing patterns.** None of these: em dashes, "not X but Y", groups of three by reflex, bold-label bullets, Title Case headings, chatbot filler. Straight quotes only. Run the humanizer skill over all prose.

## Anki backs, in order

1. Plain explanation (teal `#0e7490`).
2. **Memory hook:** (orange `#c2410c`).
3. Indigo box: **How [instructor] words it:** her quote, plus a red **Heads-up** line when her wording is harder.
4. Amber box: **Exam trap:**.
5. "Lecture N, slide P", then the slide image.
6. "Diagram", then the matching diagram PNG.

The card template is `{{cloze:Text}}<hr>{{Back Extra}}`, with no `id=answer`, so the card stays at the top when it flips.

## Guide look

- Teal accent, orange hooks, amber traps, indigo instructor-wording boxes, green key takeaways.
- Fonts: Atkinson Hyperlegible for body text, Literata for headings, JetBrains Mono for labels.
- Every diagram works in light and dark mode and fits a 390 px phone without the page scrolling sideways.

## Lesson Path look

- Baloo 2 for display text, a distinct color per lecture, chunky buttons, and a pulsing next lesson.
- Confetti and pop animations respect reduced-motion settings.
- **Board view.** A white Panaboard in a marker font (Patrick Hand):
  - black for must-know points and notes
  - blue for pathways and the instructor's wording
  - green for tricks (★)
  - red for traps (✗)
  - pathways drawn as boxes with arrows, 5 to 9 steps
  - the full lesson as notes, paginated at about 300 words
- **Navigation.**
  - Back works everywhere, and "Prev lesson" jumps across lessons.
  - Space or 4 goes forward, 1 or ← goes back.
  - Swipe on phones.
  - Tap the progress bar to jump.
