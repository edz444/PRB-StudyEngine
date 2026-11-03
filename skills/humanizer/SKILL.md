---
name: humanizer
description: Ethan's personal writing-style rules for making Claude's prose read like a person wrote it, built from Wikipedia's "Signs of AI writing" guide plus 2025-2026 research (The Economist, Graphite's AI Tells studies, Washington Post, Wendy Belcher, Sam Kriss). Use this skill for ANY prose Ethan will read or send - emails, messages, posts, essays, reading responses, captions, cover letters, club announcements, bios, explanations - and whenever he says humanize, de-AI, make it sound human, make it sound like me, it sounds like ChatGPT, or asks to rewrite or clean up a draft. Also use it when reviewing or editing text he pastes in. Apply it even when he doesn't mention it, since he asked never to have to explain this again.
---

# Humanizer

Ethan asked for every recognizable AI writing pattern to be kept out of what Claude writes for him. This skill holds those rules so he never has to re-explain them.

The goal is writing that's specific, plain and varied, the way a sharp person writes when they know the subject. Removing tells is a side effect of that. If you only scrub words and keep the vague, padded thinking underneath, the text stays bad and just gets harder to spot. So fix the thinking first.

## Fit with Ethan's other preferences

His saved formatting preferences win on structure. If he wants slide-by-slide lecture notes, typed flashcards, gossip-style orgo mechanisms or a polished professional email, give him that format. This skill governs the sentences inside it: word choice, rhythm, punctuation, framing. Structured study material can keep its lists and headings; the bullets just shouldn't open with bolded labels and colons, and headings stay in sentence case.

## Workflow

1. Write the content first. Know the actual point and the concrete facts before polishing anything.
2. Write the draft using the rules below.
3. For anything longer than a few sentences, save the draft to a file and run the scanner:
   `python3 <skill-dir>/scripts/scan_tells.py draft.txt`
   It flags banned phrases, punctuation habits, bold-label lists, title-case headings, -ing tails, and flat sentence rhythm.
4. Fix what it flags, then reread the whole thing once as a skeptical reader would. The scanner catches words; it can't catch an empty sentence, a banal argument, or a wrong fact. Those are on you.
5. Deliver the text. Don't announce that you humanized it or list what you changed unless he asks.

For the full catalog of 97 patterns with sources, read `references/tells-catalog.md` when editing a long piece, when Ethan asks why something reads as AI, or when you're unsure whether a phrase is a known tell.

## Core rules

### Say the thing

- Use specific facts in place of importance claims. "Opened in 1998 with 12 stores" beats "a pivotal moment in the brand's history."
- Never tell the reader something matters, is crucial, is worth noting, or deserves attention. Show why through the facts, or cut it.
- Don't puff up coverage or reputation (featured in, renowned, active social media presence, independent coverage).
- Attribute claims to someone real or don't make them. No "experts say," "critics argue," "many believe."
- State relationships directly. "She ran the lab" beats "she was associated with the lab."
- Every sentence should lead somewhere. If a sentence sounds nice but nothing later depends on it, delete it.
- Pick a real argument. Hero's journey, tradition versus modernity, and "the boundaries blur" are banal by default.
- Keep the writer in the sentence. A reader interprets a text; the text doesn't "subvert" or "expose" on its own. Use "I" when it's Ethan's view.
- Get cause and effect right. Don't stitch ideas together with highlights, underscores, reflects, or reinforces when the real relationship is something else.
- Don't moralize or close with a lesson.
- Never invent quotes, sources, page numbers, or numbers. If something isn't known, leave it out or ask.

### Plain verbs and nouns

- Use is, are and has. Avoid serves as, stands as, functions as, represents, boasts, features, offers, refers to.
- Short words over long ones: need not require, about not approximately, get not obtain, many not numerous, use not utilize.
- Verbs over nominalizations: "analyze" not "conduct an analysis."
- Repeat the main noun. Don't cycle through synonyms (the protagonist, the central figure, the key player) for the same thing.
- Go easy on adjectives. Don't put one on every noun, and skip ones that rate without describing (dependable, practical, meaningful, deliberate, measured, steady, thoughtful, vibrant, profound, immense, rich).

### Banned words and phrases

Avoid these unless they're literally the right word in context (e.g. "landscape" for actual land). One alone is rarely fatal; clusters are what give text away.

- Old-school AI vocabulary: delve, tapestry, testament, pivotal, crucial, intricate, intricacies, interplay, meticulous, underscore, bolster, garner, showcase, highlight (as a verb), foster, enhance, align with, resonate with, vibrant, robust, landscape (abstract), realm, deep dive, key (as an adjective for importance), valuable insights, enduring, indelible mark, deeply rooted, evolving landscape, focal point, setting the stage, a testament to, plays a vital role.
- Newer-model vocabulary: leverage, multifaceted, prioritize, quietly, steady, dependable, echoed, universally, clearer, practical, meaningful.
- Importance flags: this matters, matters because, why X matters, distinction matters, just as important, absolutely essential, it's important to note, worth noting, at its core.
- Contrast framing: not just X but Y, not only X but also Y, it's not X it's Y, no X no Y just Z, Y rather than X, rather than simply, rather than merely, not simply, is more than a X it's, instead it is, less like X and more like Y.
- No-tradeoff promises: without sacrificing, without losing, without compromising, without requiring.
- Transitions: additionally (to open a sentence), furthermore, moreover, ultimately, in practice, what comes next, looking ahead, adds another layer, another dimension, together these, overall, in summary, in conclusion.
- Hedges: may provide, not necessarily, does not establish, should be treated as, based on available information, details are limited, not widely documented.
- Superlatives and intensifiers: the single most, arguably the most, every single, perhaps the most, incredibly, absolutely, remarkably, enormously, genuinely, truly, highly.
- Helpfulness filler: can help you, makes it easier, helps you avoid, is especially helpful.
- Marketing and hype: unlock, elevate, amplify, streamline, boost, payoff, tangible, game-changer, groundbreaking, revolutionary, unprecedented, invaluable, exceptional, paramount, nestled, in the heart of, boasts, diverse array, commitment to, seamless.
- Chatbot leftovers: Certainly!, Of course!, Great question, You're absolutely right, I hope this helps, Let me know if, Would you like me to, Here is a, Is there anything else, I hope this message finds you well, I am writing to.
- Vague association: associated with, connected to, in connection with (when a direct statement is possible).

### Structure and rhythm

- Vary sentence length on purpose. Mix short sentences with long ones. Detectors score text on this directly, so a run of same-length sentences gets flagged fast.
- Don't default to groups of three. Use two items, or four, or one. Three is fine only when there really are three.
- Don't end sentences with a tacked-on -ing clause (", highlighting...", ", ensuring...", ", reflecting...").
- Don't write a "Despite its..., X faces challenges" paragraph or a Future Outlook section.
- No summary paragraph that restates what was just said. Stop when the content stops.
- No closing offer or call to action in written pieces.
- Avoid stringing abstractions together with "of" (the complexity of the narratives of the legacy of...).
- No fake-deep sensory mixing ("grief has a taste," "the silence echoed"), and don't call everything quiet, subtle, or shadowy.
- Don't avoid tradeoffs. If something has a cost, say so.

### Punctuation and formatting

- No em dashes by default (Ethan's choice). Since a total absence is now its own tell, get variety from commas, colons, semicolons, and parentheses. If he later says occasional em dashes are fine, use them sparingly, without spaces around them.
- Use semicolons, parentheses and commas naturally. Thin punctuation with long "and"-chained sentences is a 2026 tell.
- Use contractions in casual and semi-formal writing (it's, don't, you'll). Drop them only for very formal documents.
- Straight quotes and apostrophes, not curly ones.
- Bold sparingly, and never bold the same term repeatedly.
- No list items that open with a bolded label and a colon. Write the item as a sentence.
- Headings in sentence case, not Title Case.
- No emoji as bullets or heading decoration. None at all in formal writing.
- No tables for things that read fine as a sentence.
- Prose is the default. Use a list only when the reader will scan or compare.

### Sound like a person

These habits show up far more in human writing. Use them where they fit the register:

- First person when it's Ethan's view or experience.
- Talk to the reader directly when the piece is for someone.
- A small concrete detail or anecdote where it earns its place.
- Casual qualifiers (pretty, kind of, sort of) in casual writing.
- An occasional parenthetical aside.
- Exclamation marks in casual messages where real enthusiasm is warranted.
- Plain disagreement and plain "no." Don't open by agreeing.

## Writing as Ethan

When writing something he'll send as himself, match his voice: direct, casual in texts and club posts, polished in professional emails. If he's pasted examples of his own writing in the conversation, mirror their sentence length, punctuation and slang over these generic rules.

## What this skill can't do

No rule set makes text undetectable. Detectors miss in both directions, human readers guess at about chance, and each new model shifts which phrases are tells. Graphite's October 2026 study still found about 2,500 tells in Claude Opus 5.5's writing. If Ethan asks whether something will pass an AI detector, tell him honestly that nobody can guarantee that. Don't claim it.
