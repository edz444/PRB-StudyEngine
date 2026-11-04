# Guide markers

The guide is plain Markdown plus a few markers. `engine/guide/build.py` turns them into styled boxes, figures and widgets. `engine/lessons/build_lessons.py` then cuts them into lesson screens.

## Structure the lesson builder relies on

- One `## Lecture N: name {#lN}` per lecture. The id must match `LECS` and `NAV` in `course.py`.
- `### The big picture in one paragraph` right after the story box. It becomes "Start here".
- Each idea is a `###` or `####` heading followed **immediately** by a `:::key` box. That pair is what makes a lesson. A heading without a key box becomes a group label on the path.
- `### How to figure it out: ... {#howto-...}` and `### Reading her questions on this lecture {#read-lN}` become the boss level.
- `### Lecture N on one page` with a 3-column table (part, plain-English job, memory trick) becomes the badge screen and the board cheat sheet.

## Boxes

```
:::story        where this lecture sits in the course story, and what it needs from before
:::key          2 to 4 bullet takeaways, then an optional line:  *Skim:* low-priority details
:::hook         memory trick or analogy
:::conn         connection to another lecture
:::trap         exam trap
:::easy         easy marks: "both boxes", order and swap traps
:::she          a question the instructor wrote on her slide (never invent quotes)
:::nancy        her exact wording, then "Plain version: ..." (label set in build.py LABEL)
:::exam         how her practice set or past exams test this spot, with a model answer
:::note         note about the guide itself
:::q            practice question, then a line with ???, then the answer
```

Each box starts with `:::type` on its own line and ends with `:::` on its own line.

## Instructor practice questions

In `98_practice.md`, start a question with `(Her Q10, L5)` to send it to that lecture's boss level. Tagged questions go first in the boss level. Anki cards written from her practice set get `lec=N` in their wording entry, which picks the subdeck and adds the `PRACTICE_TAG` tag.

## Paragraph conventions

- Start each section's first paragraph with `The short version:`. It becomes the big-idea screen.
- Bold a term the first time it appears, and define it in the same sentence.
- Put every comparison in a table. Tables become ruled grids on the board view.

## Figures and widgets

```
{{slide:L5-4|what to notice on this slide}}     courses/<name>/slides/L5-4.jpg
{{fig:gcycle}}                                   SVG diagram registered in content/diagrams*.py
{{3d:gp|caption}}                                optional 3D model (content/atlas_*.js, M3D_NAMES)
{{lab:camp|label}}                               opens the Pathway Lab inline at #camp
```

## Anki card line

```
CLOZE ||| EXPLANATION ~~~ MEMORY HOOK ^^^ EXAM TRAP (optional)
```

- Group lines under `# ---------- L5 Name ----------` headers. The header names the lecture.
- Keep the cloze text fixed once a deck has been imported, because the note ID comes from it.
- Never use `<`, `>` or `&` in a card. Write "more than 80%".
- The plain back, instructor wording and heads-up live in `anki/<WORDING_FILES>.py` as `B = {card_number: dict(e=..., nw=..., hu=...)}`.
