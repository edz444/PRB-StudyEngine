---
name: "interactive-lesson-path"
description: "Build Ethan's game-style interactive study app from lecture slides: bite-sized lessons with mission checklists, one idea per screen, quick checks, stars, XP, boss levels, badges, a day plan to the exam and a Panaboard board view. Use whenever he wants to study a course, make it easy to follow, or turn notes into lessons."
---

# Interactive lesson path

Ethan learns best when material is broken into tiny steps he can tick off, with rewards for momentum. Long walls of text stall him, even when the explanations are good. He also learns by hand-writing a lot onto a Panaboard (a whiteboard that scans and prints), often putting ideas from different lectures on the same board. So every lesson needs a full, multi-page board-ready version, not just a short summary. This skill turns a course's lectures into a published HTML artifact that works like a learning game, built the way the MBB 322 Midterm 2 "Lesson Path" was built.

Apply the humanizer skill to all prose. Plain English first, every technical word defined inline, analogies and mnemonics everywhere. Write it so someone with no background in the subject could follow it.

## Inputs
- Lecture slides (PDF or PPTX). Extract text with `pdftotext -layout`; rasterize pages and look at contact sheets so figure-only slides aren't missed. Convert PPTX to PDF with LibreOffice first.
- Optional: transcripts, past exams with his marks (use them to learn the instructor's question style), the exam date.
- If an illustrated guide already exists (see the illustrated-study-guide skill), reuse its Markdown sources instead of rewriting.

## Step 1: write the content as a plain-English guide first
The app is cut from a structured guide, so the guide comes first. One Markdown file per lecture, with these blocks (each becomes its own screen later):
- A `:::story` box: where this lecture sits in the course story and what it needs from before.
- "The big picture in one paragraph", plus a one-line mnemonic for the whole lecture.
- One `###` (or `####`) section per idea. Each starts with a `:::key` bubble: 2 to 4 short focus bullets plus an optional `*Skim:*` line naming low-priority details. Then a line starting "The short version:" that gives the idea in everyday words, then the details in short paragraphs, tables for any comparison, and `:::hook` memory tricks.
- `:::trap` and `:::easy` boxes for exam traps, especially "both boxes" questions (something that belongs to two categories at once) and order or swap traps.
- `:::nancy` boxes (rename to the instructor's name if the course has a different one). Quote the instructor's exact slide wording wherever it's harder than the idea (jargon, typos, a word used loosely), then give the plain version, so exam phrasing never throws him.
- `:::she` boxes for questions the instructor wrote on the slides. Never invent lecture quotes.
- Slide figures `{{slide:L5-4|what to notice}}` (only slides with real figures, about 130 dpi, about 1100 px wide, JPEG quality about 72) and SVG diagrams for pathways.
- At the end of each lecture: a "How to figure it out" method section, a "Reading her questions" table (question wording, what it tests, how you get tricked), and a "Lecture X on one page" table (part, plain-English job, memory trick).
- Keep every fact from the slides. Check by script that all numbers, bold terms and figures from the source survive any rewrite.

## Step 2: cut the guide into lessons
Build the guide HTML, then parse it with BeautifulSoup into JSON:
- Each lecture becomes a unit. Lesson 0 is "Start here: the big picture" (story box, big picture, whole-lecture mnemonic).
- Every heading followed by a `:::key` bubble becomes one lesson. Its key bullets become the mission objectives and its skim line becomes "Don't sweat". A parent heading with no key bubble becomes a group label on the path.
- Each block becomes a card (one screen). Merge short paragraphs up to about 70 words and split long ones at sentence breaks into chunks of about 55 words. Lists longer than 6 items split into chunks of 5. Callouts, figures and tables each get their own card. "The short version" becomes a large "big idea" card. Keep a card's sub-heading as a kicker label.
- The method, question-wording and one-page sections become the boss level and the badge reward screen.
- Quick checks: reuse the course's Anki cloze cards (see the anki-slide-deck skill). Assign each card to the lesson whose text shares the most words with it. Practice questions in the instructor's style go to the boss level, and multiple-choice ones become tappable options.
- Add a glossary (term, match strings, definition) for tap-to-define popovers. Wrap only the first use of each term per lesson.

## Step 3: the app
One self-contained HTML page with the lesson JSON inline. Slide images and any companion tools go through `files`. Vanilla JS, no framework needed.
- Home: days-to-exam countdown, XP, lessons done, today's mission from a day plan (split the lectures over the days left, with the last day for review), a big green Continue button that opens the next unfinished lesson, and a review-pile button. Each lecture is a colored unit card with a progress ring, a locked or unlocked badge, a "Board cheat sheet" button, and a zig-zag path of lesson bubbles (the next one pulses, done ones show stars) ending in a boss node.
- Lesson player, full screen: close button, segmented progress bar, a Board toggle, and a thumb-reach footer with Back and a big Next button.
  1. Mission: the objectives as a read-only checklist, plus "Don't sweat".
  2. Cards, one per screen, with the text cards on a card panel at about 19 px. Capitalize the first letter of a big-idea card after stripping "The short version:".
  3. Quick checks: cloze blanks show "?" pills to tap and reveal, then the explanation and trick, then "Got it" or "Missed it". Misses go into the review pile.
  4. "Tick what you can do now": objectives as checkboxes.
  5. Reward: confetti, 1 to 3 stars from the check score, +XP (10 per lesson plus 5 per check), a random cheer and how many lessons are left.
- Boss level: mission, method and question-wording cards, practice questions, 6 random checks from the lecture, then a badge screen with a medal, +50 XP and the one-page summary table to screenshot. Give each lecture a fun badge name (for example "Signal Switcher").
- Review pile: replays missed checks; "Got it" removes a card from the pile.
- Save progress in localStorage, wrapping every access in try/catch, and say on the page that it lives in this browser. Use the URL hash only for plain names like `#l5-3`.

## Step 4: board view (Panaboard)
He writes a lot on the board, because writing by hand is how things stick for him. Give him the whole lesson in board form, never just the short version, split over pages he can flip.

### Look
- A white board with a grey frame in a marker-style font (Patrick Hand). It stays white in dark mode on purpose.
- Four marker colors: black for must-know points and notes, blue for pathways and the instructor's wording, green for tricks (★), red for traps (✗).
- Two columns on wide screens, one on phones.

### Pathway boards
Write these by hand for each lecture rather than auto-extracting them:
- a title
- the main chain of steps, top to bottom, 5 to 9 boxes so it fits on a board
- off switches
- what breaks it (toxins, drugs, mutations)
- a memory trick
- which lessons it attaches to

In the board view, draw the steps as boxes joined by arrows.

### Lesson board pages
- Page 1 is the overview: must know (the objectives), the attached pathway drawn as boxes and arrows, up to 3 tricks and 3 traps, and a "Skip on the board" line.
- Pages 2 and up are the full notes. Each lesson card becomes a board block:
  - the card's sub-heading as an underlined section title
  - the big idea in a blue box
  - every sentence of a text card as its own bullet, keeping bold terms underlined
  - lists kept as they are
  - tables redrawn as ruled grids
  - the instructor's wording as a blue block with "Plain version" on its own line
  - slide questions as "? She asks:"
  - connections as "↔ Link:"
  - figures under "Sketch this", tap to enlarge
- Paginate by weight, about 300 words a page: text counts its words plus 14, a figure counts 140, a table counts 40 plus its words. Head each notes page "notes n/N".

### Navigation
- ‹ › arrows and page dots above and below the board.
- "Page x of y" shown, and the top bar shows "Board x/y".
- The footer's Next becomes "Next board page" until the last page, then "Back to lesson". Back becomes "Prev page".
- Swipe left and right on phones (a horizontal move of more than 70 px).
- A "Jump to any board" select lists every lesson in every lecture (grouped by lecture) plus each lecture's cheat sheet, so he can pull ideas from different lectures onto one whiteboard. Picking one opens that lesson straight into board view at page 1.

### Lecture board cheat sheet
Every pathway for the lecture, then the one-page table as board rows: part in black, job in blue, trick in green.

## Design
The visual language is an energetic kids'-game style, done cleanly: Baloo 2 for display, Atkinson Hyperlegible for reading, a distinct color per lecture, chunky rounded buttons with a bottom shadow, pulsing next node, pop animations, and confetti that respects prefers-reduced-motion. Light and dark tokens. Never use emoji as section markers.

## Checks before publishing
Run Playwright at 1280 px and 390 px, in light and dark:
- no page errors
- page scrollWidth equals the viewport width
- play one lesson end to end: tap the blanks, mark Got it, tick the objectives, finish, confirm the reward and the XP saved
- play one boss level
- open a board view, flip through every page while checking for sideways overflow, use the jump menu to open a board in another lecture, and open a cheat sheet

Test it the way the live page is served: page as UTF-8, web fonts blocked so the page can't hang. Wait about 300 ms before screenshots, because cards fade in. Known pitfalls:
- a lightbox class name colliding with button label classes
- the guide CSS putting borders on h2 and h3, including the board title
- `.bigbtn` needing box-sizing:border-box
- `[hidden]` needing `!important` on display:block elements

Publish with an icon, then tell him in a few lines how to start (tap Continue), how the board pages and jump menu work, and that progress saves per browser.