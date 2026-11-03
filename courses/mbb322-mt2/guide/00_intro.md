# MBB 322 midterm 2 guide: signaling, neurons and cancer

Lectures 5 to 11, told as one story in seven chapters. GPCRs, synaptic signaling, optogenetics, RTKs, and Cancer I, II and III.

:::note
How to use this guide: read it top to bottom like a story. Each chapter opens with a "Where we are in the story" box (what you need from before and what this chapter adds) and closes with "Reading her questions," a table of the question wordings she uses, what each one is really testing, and how people get tricked. Built from Nancy's slides only (no transcripts this time). Seven 3D models sit inside the chapters (look for "Open 3D model"): drag to rotate, step through, and try the toxin buttons. For the signaling pathways, the "Break it yourself" buttons open that pathway in the companion [Pathway Lab](https://claude.ai/artifact/3bbKhgTJsos4CqwyVsvP52), where you knock out parts, apply drugs and mutations, and rebuild each relay from memory. The "She emphasized" boxes come from the questions she wrote right on her slides, like "Consequence?" or "How could RTKs activate Ras???". When a lecturer puts a question on a slide, that question is usually a preview of an exam question. The purple "Her wording, decoded" boxes quote her exact slide wording wherever it is harder than the idea itself (jargon, typos, a word used loosely), then give the plain version, so the exam phrasing never throws you. The chapters teach it the easy way; these boxes connect the easy way back to how she will ask it. Every part of every lecture starts with a green "Key takeaways" bubble: the few points to lock in before you read, plus a "Skim" line for details that are on the slides but are low priority, so you know where to spend your attention.
:::

## The one story {#story}

Every cell in your body is constantly getting messages from outside: hormones, neurotransmitters, growth factors, even light. The problem is that most of these messages can't get inside. They bump into the plasma membrane (the fatty outer skin of the cell) and stop. So the cell needs a way to pass the news through the wall without the messenger itself coming in.

That is the whole unit. A **receptor** (a protein that sits in the membrane and grabs one specific signal) catches the message on the outside, changes shape, and that shape change starts a chain reaction on the inside. Each step in the chain switches on the next, often by sticking a phosphate group onto it (phosphorylation) or by swapping GDP for GTP. At the end, something useful happens: a muscle contracts, a gene turns on, a cell divides.

Here is how the seven lectures fit into that one story:

1. GPCRs (L5) are the first kind of receptor. They grab a signal and hand the news to a G protein, a little GTP-powered on/off switch, which then makes **second messengers** (small, fast inside-the-cell messengers like cAMP, IP3 and Ca2+).
2. Synaptic signaling (L6) is what happens when the "signal" is electrical. Neurons fire action potentials by opening and closing ion channels, then talk to the next cell by releasing neurotransmitters. Ca2+ shows up again as the trigger.
3. Optogenetics (L7) puts the ion channel and rhodopsin ideas to work: scientists borrowed a light-gated channel from algae and put it into neurons, so they can switch specific neurons on or off with a flash of light.
4. RTKs (L8) are the second kind of receptor. They are enzymes themselves (tyrosine kinases), and their main job is telling cells to grow and divide through the Ras to MAP kinase chain.
5. Cancer I (L9) asks what a cancer cell actually is: a cell that ignores the "stop dividing" rules, escapes its tissue, and spreads.
6. Cancer II (L10) connects the two halves. Most cancer genes are broken pieces of the signaling pathways from L5 and L8. A Ras that can't turn off, an RTK that fires with no ligand, a kinase fused to the wrong partner. Cancer is signaling that won't shut up.
7. Cancer III (L11) finishes the cancer story with the brakes: tumor suppressor genes like Rb, which have to lose both copies, plus two more pathways (Wnt and TGFβ) whose broken parts drive colon cancer. It ends by putting every cancer gene on one map.

{{fig:storymap}}

:::conn
If you remember one sentence: signaling is a relay of switches, and cancer is what happens when a gas pedal gets stuck ON (oncogene) or a brake gets cut (tumor suppressor).
:::

## Threads that run through every lecture {#threads}

These ideas repeat over and over. If you spot one in a question, you already know half the answer.

- Every switch needs an OFF button. G proteins hydrolyze their GTP, phosphodiesterases destroy cAMP, Na+ channels inactivate, neurotransmitters get pumped away, RTKs get eaten by endocytosis, Ras has GAPs. Nancy loves asking "what happens if the off switch breaks?" The answer is always: the signal stays on (cholera toxin, Ras G12 mutation, sarin, VHL, a β-catenin the destruction complex can't catch).
- GTP means ON, GDP means OFF. This is true for heterotrimeric G proteins (L5), Ras (L8), and Rho (L8). GEFs swap GDP out for GTP (turn on). GAPs speed up GTP hydrolysis (turn off).
- Phosphorylation is the cell's universal "flip a switch" move. Kinases add phosphates, phosphatases remove them. PKA, PKC and the TGFβ receptors phosphorylate Ser/Thr. RTKs, Src, Abl and JAK phosphorylate Tyr. But a phosphate doesn't always mean ON: it can switch an enzyme off (glycogen synthase, c-Src), mark a protein for destruction (β-catenin), or uncover an address label (Smads).
- Amplification. One hormone molecule can lead to millions of product molecules because every step activates many copies of the next step.
- Ca2+ is the universal trigger. It pops up in GPCR signaling (IP3 releases it), in synapses (it triggers vesicle release), in muscle (it moves tropomyosin), and in optogenetics (ChR2 lets it in).
- Electrochemical gradients decide which way ions flow. Na+ and Ca2+ rush in, K+ leaks out, Cl- usually goes in. Opening a channel lets ions run downhill, which changes the voltage.
- Same signal, different response. Epinephrine makes liver cells break down glycogen and makes heart cells beat faster. The response depends on which receptor and which downstream machinery the cell has.
- Destroy-to-control. Some signals work by stopping a protein from being destroyed: HIF without oxygen (L9), β-catenin with Wnt (L11). If a question mentions ubiquitin or the proteasome, ask what happens when the destruction stops.
- Experiments as logic puzzles. Dominant negatives, constitutively active mutants, antibodies, temperature-sensitive mutants, FRET. Nancy tests whether you can read an experiment and say what it proves.
