---
name: "interactive-lesson-path"
description: "Build Ethan's game-style interactive study app from lecture slides: bite-sized lessons with mission checklists, one idea per screen, quick checks, stars, XP, boss levels, badges, a day plan to the exam and a Panaboard board view. Use whenever he wants to study a course, make it easy to follow, or turn notes into lessons."
---

# Interactive lesson path

Ethan learns best when material is broken into tiny steps he can tick off, with rewards for momentum. Long walls of text stall him, even when the explanations are good. He also learns by hand-writing a lot onto a Panaboard (a whiteboard that scans and prints), often putting ideas from different lectures on the same board. So every lesson needs a full, multi-page board-ready version, not just a short summary. This skill turns a course's lectures into a published HTML artifact that works like a learning game, built the way the MBB 322 Midterm 2 "Lesson Path" was built.

Apply the humanizer skill to all prose. Write it so someone with no background in the subject could follow it.

He strongly prefers interactive, visual, tap-through study tools over long wordy pages or PDFs. When he asks for a summary, cheat sheet, refresher or review, build it as a short, card-based mode inside the app first; a printable sheet is a bonus, never the main answer.

## Start from PRB-StudyEngine, every time
He wants every course to get this exact app, so never rebuild it from this description when the engine is available. The working code lives in his private GitHub repo **PRB-StudyEngine** (shared engine in `engine/`, one folder per course in `courses/`, plus a working sample course in `courses/_template` and the finished MBB 322 course in `courses/mbb322-mt2`).

1. Get the engine. Look for it with list_repos (query "PRB-StudyEngine"), attach it with add_repo and clone it. If it isn't reachable, ask him to attach it or upload `PRB-StudyEngine.zip`, then unzip it into its own folder. Fall back to rebuilding from the rest of this file only if neither works, and say so.
2. Read `README.md`, `docs/NEW_COURSE.md`, `docs/MARKERS.md` and `docs/STYLE.md` before writing anything.
3. `cp -r courses/_template courses/<course>-<exam>`, fill in `course.py` (titles, lectures, badges, exam date, day plan, new Anki IDs), and put the slide PDFs in `source/` (never committed).
4. Write only course content: the guide Markdown, glossary, diagrams, pathway boards, cards and wording files, following the clarity bar below.
5. `COURSE=courses/<name> make all check`, then publish `out/index.html` and `out/lessons/<slug>-lesson-path.html` as artifacts with their `slides/` and `lab.html` files, and send the .apkg.
6. A new feature he asks for goes into `engine/` so every course gets it, then gets described in this skill. Commit with clear messages and push when the repo is attached; otherwise hand him a fresh zip made with `git archive` (never zip the working folder, because the build folders hold instructor slide images).

The rest of this file describes what the engine does and the standard the content must meet.

## Inputs
- Lecture slides (PDF or PPTX). Extract text with `pdftotext -layout`; rasterize pages and look at contact sheets so figure-only slides aren't missed. Convert PPTX to PDF with LibreOffice first.
- Optional: transcripts, past exams with his marks, the instructor's practice questions, the exam date.
- If an illustrated guide already exists (see the illustrated-study-guide skill), reuse its Markdown sources instead of rewriting.

## The clarity bar (most important)
He judges every lesson by one test: could he follow it without opening ChatGPT? Twice he had to (ephrin signaling, and a benign vs malignant table cell that read "the spread tumors (metastases), not the first tumor, usually kill"). Write every section like this:

1. Open with the one message the whole section passes along, in everyday words. Example: "The whole chain passes one message along: Axon, don't grow this way. Turn away!"
2. Next, a "The words you need" list that defines every new term before it's used ("The growth cone is the moving tip of a growing axon. It explores and decides which way to grow, like a GPS."). Never use a term first and define it later. Re-explain basics the section relies on (axon, actin, GEF) even if an earlier lecture covered them.
3. Pathways as numbered steps, one step per line, each protein given a job title: "ephrinA1 is the stop sign. EphA4 is the receptor. Ephexin is the GEF. RhoA is the switch. The growth cone collapses."
4. Experiments as numbered steps, then one line saying what it proves and why.
5. Every table cell must read as a full phrase that makes sense on its own. No squeezed clauses, no shorthand like "Gain-of-function, one copy enough (dominant)". Column headers ask a plain question ("Does it stay in one place?").
6. Key-takeaway bullets are short full sentences, not arrow strings. Arrow chains are fine only inside a pathway step list.
7. Short sentences. Tie new ideas to a pattern he already knows ("same wiring as RTK, Sos, Ras, pointed at a different target").
8. Self-check before publishing: read each table row, key bullet and lesson card alone, out of context. If any one would make him stop and ask what it means, rewrite it.

## Staying locked in (ADHD-friendly by design)
He asked for the app to be as ADHD-friendly as possible. He keeps time with his own physical timer, so the app's job is to keep him moving and never make him re-find his place. These features are core, not extras:
- Quick checks mixed into the lesson: each check sits two screens after the card it best matches (by shared words), at most one check per card where possible, so he answers something every minute or so instead of reading a long run first.
- A rose "Cram path: only what she tests" button on home. It strings together, lecture by lecture, every lesson with a practice-set box (its big idea, the `exam` box and its traps, each labelled with the lecture and lesson) followed by that lecture's practice questions. It remembers its place and the home button says which stop it picks up at.
- A streak counter on the lesson-name line ("7 in a row"), counting Got it and right multiple-choice answers in a row; a miss resets it. Every 5 in a row shows a toast, and every 10 adds confetti.
- Resume at the exact screen: the app saves the current lesson and screen on every screen, and the home button becomes "Pick up where you left off" with the lesson and screen number until that lesson is finished.
- A Park button in the lesson top bar opens a small box to type a stray thought (Enter saves, Escape cancels) without leaving the lesson. Parked thoughts wait on home with a Done button each.
- Blue shooting stars on must-memorize facts. Every flashcard (cloze) answer is something to memorize, so the lesson builder finds where each answer is taught, first in the lesson holding that quick check and then anywhere in the lecture, and wraps that exact phrase in a blue highlight with a small shooting-star icon (at most 7 per lesson; skip generic answers like "both" or "high"). The board view shows them as a blue underline with the star. Each mission screen carries the one-line legend: "Blue shooting star = memorize this exact fact."
On phones (under about 440 px) the top-bar buttons go icon-only so the progress bar keeps its width.

## Step 1: write the content as a plain-English guide first
The app is cut from a structured guide, so the guide comes first. One Markdown file per lecture, with these blocks (each becomes its own screen later):
- A `:::story` box: where this lecture sits in the course story and what it needs from before.
- "The big picture in one paragraph", plus a one-line mnemonic for the whole lecture.
- One `###` (or `####`) section per idea. Each heading is followed immediately by a `:::key` bubble: 2 to 4 short focus bullets plus an optional `*Skim:*` line naming low-priority details. Then a line starting "The short version:" with the one message, then the words you need, then the details following the clarity bar, and `:::hook` memory tricks.
- `:::trap` and `:::easy` boxes for exam traps, especially "both boxes" questions (something that belongs to two categories at once) and order or swap traps.
- `:::nancy` boxes (rename for another instructor). Quote the instructor's exact slide wording wherever it's harder than the idea (jargon, typos, a word used loosely), then give the plain version, so exam phrasing never throws him.
- `:::she` boxes for questions the instructor wrote on the slides. Never invent lecture quotes.
- `:::exam` boxes, labeled "On her practice set", wherever her practice questions or past exams test that spot (see the practice set section).
- Slide figures `{{slide:L5-4|what to notice}}` (only slides with real figures, about 130 dpi, about 1100 px wide, JPEG quality about 72) and SVG diagrams for pathways.
- At the end of each lecture: a "How to figure it out" method section, a "Reading her questions" table (question wording, what it tests, how you get tricked), and a "Lecture X on one page" table (part, plain-English job, memory trick).
- Keep every fact from the slides. Check by script that all numbers, bold terms and figures from the source survive any rewrite.

## The instructor's practice set
When he uploads practice questions, read them for how she tests, then emphasize everywhere:
- Name her styles. For MBB 322 these were: about half "X is blocked, locked open or can't turn off, predict what happens"; compare-two-systems short answers; "rationalize" a rule from first principles; "define, then explain the rationale" for a drug; "which is INCORRECT" with four true options; multiple-choice distractors that are true facts from a different pathway.
- Add an `:::exam` box at each tested spot with a model answer and why each wrong option fails. Write a short plain explanation for anything she asks that isn't on her slides (batimastat and MMPs, for example).
- Flag mismatches between her questions and her slides (E. coli vs Salmonella in the Ames test; CFP/YFP vs her slide's YFP plus red dye) so the wording never throws him.
- Put every question in `98_practice.md` as `:::q` blocks under "Her Midterm 2 practice set", each starting with a visible tag like `(Her Q10, L5)`. Multiple-choice options go on one line as `A. ... B. ...` and the answer starts with the letter.
- Add matching Anki cards (see the anki-slide-deck skill).

## Step 2: cut the guide into lessons
Build the guide HTML, then parse it with BeautifulSoup into JSON:
- Each lecture becomes a unit. Lesson 0 is "Start here: the big picture" (story box, big picture, whole-lecture mnemonic).
- Every heading followed by a `:::key` bubble becomes one lesson. Its key bullets become the mission objectives and its skim line becomes "Don't sweat". A parent heading with no key bubble becomes a group label on the path.
- Each block becomes a card (one screen). Merge short paragraphs up to about 70 words and split long ones at sentence breaks into chunks of about 55 words. Lists longer than 6 items split into chunks of 5. Callouts (including `exam`), figures and tables each get their own card. "The short version" becomes a large "big idea" card. Keep a card's sub-heading as a kicker label.
- The method, question-wording and one-page sections become the boss level and the badge reward screen.
- Quick checks: reuse the course's Anki cloze cards (see the anki-slide-deck skill). Load every wording file, including the practice-set one, or the build fails with a KeyError. Each card belongs to the lecture in its section header, or to its `lec` value for practice-set cards; never guess a card's lecture from its number (that sent Lecture 6 checks into Lecture 11). Within its lecture, assign each card to the lesson whose text shares the most words with it.
- Boss questions: a `(Her Qn, Lx)` tag routes the question to that lecture's boss level and it goes first; untagged ones go to the lecture with the most shared words. Multiple-choice ones become tappable options.
- Multiple choice must not give itself away. Write every option to about the same length and detail, so the right one is never the obviously longest (it was in 18 of 21 of hers). The app shuffles the options each time a question is shown and rewrites letter references in the explanation ("C.", "A is backwards") to match; questions with options like "A and B" keep their order. Check by script that no correct option is noticeably the longest.
- Add a glossary (term, match strings, definition) for tap-to-define popovers.

## Step 3: the app
One self-contained HTML page with the lesson JSON inline. Slide images and any companion tools go through `files`. Vanilla JS, no framework needed.
- Home: days-to-exam countdown, XP, lessons done, today's mission from a day plan (split the lectures over the days left, with the last day for review), a big green Continue (or "Pick up where you left off") button, the Cram path button, a review-pile button, a "Parked thoughts" section and a "Saved to revisit" section. Each lecture is a colored unit card with a progress ring, a locked or unlocked badge, a "Board cheat sheet" button, and a zig-zag path of lesson bubbles (the next one pulses, done ones show stars, saved ones show a bookmark, lessons with an `exam` card show a small rose "◎ tested" chip) ending in a boss node. Each unit's lesson list opens and closes with a chevron; finished units start closed, and the choice is saved.
- Lesson player, full screen: close button, segmented progress bar (tap to jump), a small line under it naming the lecture, lesson number and lesson title (with the streak counter at its right end), a Save button, a Park button, a Board toggle, and a thumb-reach footer with Back and a big Next button.
  1. Mission: the objectives as a read-only checklist, plus "Don't sweat".
  2. Cards, one per screen, text cards on a panel at about 19 px. Capitalize the first letter of a big-idea card after stripping "The short version:".
  3. Quick checks, mixed in between the cards as described above: cloze blanks show "?" pills to tap and reveal, then the explanation and trick, then "Got it" or "Missed it". Misses go into the review pile.
  4. "Tick what you can do now": objectives as checkboxes.
  5. Reward: confetti, 1 to 3 stars from the check score, +XP (10 per lesson plus 5 per check), a random cheer and how many lessons are left.
- Navigation: Back works on every screen, including the first, where it becomes "Prev lesson" across lessons. Keys: Space, 4 or → for next; 1 or ← for back. Read `e.code` first so number-pad keys work with Num Lock off. On a quick check, each forward key press reveals the next blank, and once all are shown it presses Got it. The down arrow is the miss key: the first press reveals every blank, the second presses Again (Missed it in lessons). Swipe on phones.
- Save: the Save button stores the lesson, the current screen and an optional note. The home "Saved to revisit" list shows them with "Open at screen N" and Remove.
- Tap-to-define: link glossary terms fresh every time a screen renders, once per term per screen, inside tables too. Never keep a session-wide "already linked" set; that made definitions vanish when he went back.
- Boss level: mission, method and question-wording cards, practice questions (hers first), 6 random checks from the lecture, then a badge screen with a medal, +50 XP and the one-page summary table to screenshot. Give each lecture a fun badge name (for example "Signal Switcher").
- Review pile: replays missed checks; "Got it" removes a card from the pile.
- Quick refresher per lecture: a row of lecture chips on home (and a Refresher button on each unit) opens a short deck. It starts with an intro card, then for every lesson one big key-point card (lesson title, its key bullets as numbered chips, a one-line "Remember" trick in green and a one-line "Don't fall for" trap in amber, each cut to about 26 to 30 words) followed by up to two quick-fire cloze cards from that lesson. The miss button reads "Again" and puts the card back once at the end of the deck. It remembers its place per lecture (the chip shows "stop N"), takes about 10 minutes a lecture, and ends on a medal screen.
- Cheat sheet per lecture: a "Cheat sheet" button on each unit opens a full-screen, scrollable sheet built from what the lecture already contains, in this order: On one page, Don't get tricked (all trap and easy-marks boxes), Ways to remember (all hooks), Compare and contrast (every table except the one-page and question tables), Her wording decoded, Must memorize (every flashcard with the answer filled in blue), How she asks (the question-wording table), and On her practice set (closed by default). Each item carries its lesson name as a small label, sections fold, tabs switch lectures, and definitions are tappable. On phones, tables stack each row as a labelled card. A Print button prints it cleanly (no dotted underlines, no orphaned headings), and the same view is exported as one PDF per lecture.
- Save progress in localStorage under keys like `l9-3` (lecture id plus lesson index), wrapping every access in try/catch, and say on the page that it lives in this browser. Use the URL hash only for plain names like `#l5-3`.

## When he asks for a change
He studies in the app and sends quick, casual messages, often a screenshot of the one spot that bothered him ("seeing some weird explanations", "when i clicked this it opened a page", "should be able to go back"). Handle every request the same way:

1. Read the screenshot as an example, not the whole job. Find the cause and fix it everywhere it applies. One confusing table cell means checking every table in that lecture and the ones after it; one missing back button means back on every screen.
2. Fix it in the live build and in `engine/` (or the course folder) in PRB-StudyEngine, so the next course gets it too.
3. Keep his progress: never reorder or rename lessons (see below).
4. Re-test the exact thing he reported with Playwright, plus `make check`.
5. Republish to the same artifact URLs he already has. Never hand him a new link for an update.
6. Commit and push, and refresh any other outputs the change touches (Anki deck, NotebookLM PDFs, DeepTutor Markdown).
7. Reply in one or two plain sentences: what changed and where to see it. No recap of steps.

When he says "update the skill", "fix all of these in the skill" or similar, fold every fix from the session into all three skills that share this method (this one, illustrated-study-guide and anki-slide-deck), propose them together, and copy the same text into the repo's `skills/` folder.

Every feature he has asked for so far is listed in this file. Never drop one while adding another.

## Rewriting later without losing progress
Progress, stars and saved lessons are keyed by lesson position. When he asks for clearer explanations mid-course, rewrite the text inside sections but keep every lesson heading, its `:::key` pairing and the order the same. Snapshot the lesson title list before and confirm lesson counts match after.

## Step 4: board view (Panaboard)
He writes a lot on the board, because writing by hand is how things stick for him. Give him the whole lesson in board form, never just the short version, split over pages he can flip.

### Look
- A white board with a grey frame in a marker-style font (Patrick Hand). It stays white in dark mode on purpose.
- Four marker colors: black for must-know points and notes, blue for pathways and the instructor's wording, green for tricks (★), red for traps (✗) and practice-set boxes (◎).
- Two columns on wide screens, one on phones. SVG figures on the board use `min-width:0; width:100%` so they never overflow a phone.

### Pathway boards
Write these by hand for each lecture rather than auto-extracting them: a title, the main chain of steps top to bottom (5 to 9 boxes so it fits on a board), off switches, what breaks it (toxins, drugs, mutations), a memory trick, and which lessons it attaches to. In the board view, draw the steps as boxes joined by arrows.

### Lesson board pages
- Page 1 is the overview: must know (the objectives), the attached pathway drawn as boxes and arrows, up to 3 tricks and 3 traps (practice-set boxes count as traps), and a "Skip on the board" line.
- Pages 2 and up are the full notes. Each lesson card becomes a board block:
  - the card's sub-heading as an underlined section title
  - the big idea in a blue box
  - every sentence of a text card as its own bullet, keeping bold terms underlined
  - lists kept as they are
  - tables redrawn as ruled grids
  - the instructor's wording as a blue block with "Plain version" on its own line
  - slide questions as "? She asks:"
  - connections as "↔ Link:"
  - practice-set boxes as a red "◎ On her practice set" heading, then one bullet per sentence or list item, with any table as a grid
  - figures under "Sketch this", tap to enlarge
- Paginate by weight, about 300 words a page: text counts its words plus 14, a figure counts 140, a table counts 40 plus its words. Head each notes page "notes n/N".

### Navigation
- ‹ › arrows and page dots above and below the board.
- "Page x of y" shown, and the top bar shows "Board x/y".
- The footer's Next becomes "Next board page" until the last page, then "Back to lesson". Back becomes "Prev page". The same keys work.
- Swipe left and right on phones (a horizontal move of more than 70 px).
- A "Jump to any board" select lists every lesson in every lecture (grouped by lecture) plus each lecture's cheat sheet, so he can pull ideas from different lectures onto one whiteboard. Picking one opens that lesson straight into board view at page 1.

### Lecture board cheat sheet
Every pathway for the lecture, then the one-page table as board rows: part in black, job in blue, trick in green.

## Design
The visual language is an energetic kids'-game style, done cleanly: Baloo 2 for display, Atkinson Hyperlegible for reading, a distinct color per lecture, chunky rounded buttons with a bottom shadow, pulsing next node, pop animations, and confetti that respects prefers-reduced-motion. Light and dark tokens; the practice-set rose color needs both. Never use emoji as section markers.

## Checks before publishing
Run Playwright at 1280 px and 390 px, in light and dark:
- no page errors
- page scrollWidth equals the viewport width
- play one lesson end to end: tap the blanks, mark Got it, tick the objectives, finish, confirm the reward and the XP saved
- go forward several screens, then back, then reopen the lesson, and confirm the number of tappable terms on each screen is the same every time
- play one boss level and confirm her questions come first with tappable options
- confirm quick checks are spread between cards, the streak counter climbs and resets, Park saves a thought to home, closing mid-lesson turns Continue into "Pick up where you left off" at the same screen, and the Cram path opens, labels each stop and remembers its place
- open a board view, flip through every page while checking for sideways overflow, use the jump menu to open a board in another lecture, and open a cheat sheet

Test it the way the live page is served: page as UTF-8, web fonts blocked so the page can't hang. Wait about 300 ms before screenshots, because cards fade in. Known pitfalls:
- a lightbox class name colliding with button label classes
- the guide CSS putting borders on h2 and h3, including the board title
- `.bigbtn` needing box-sizing:border-box
- `[hidden]` needing `!important` on display:block and inline-flex elements (top-bar buttons included); the Got it / Missed it row (`.gm`, display:flex) showed before the blanks were revealed until `.gm[hidden]` was forced
- a home-screen local variable named `P` shadowing the player state inside home click handlers; open lessons through a top-level helper
- sed character classes corrupting UTF-8 arrows and Greek letters (edit in Python instead)

Publish with an icon, then tell him in a few lines how to start (tap Continue), how the board pages and jump menu work, and that progress saves per browser. Mirror every change into PRB-StudyEngine, run `make check`, and commit.