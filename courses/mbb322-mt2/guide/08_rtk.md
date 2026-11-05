## Lecture 8: receptor tyrosine kinases {#l8}

Textbook pages 911-919. RTKs are the second big family of receptors, and they're the ones most tied to cell growth and cancer.

:::story
Chapter 4. Back to receptors, now the ones that tell cells to grow and divide. An RTK is a receptor that is also a kinase. Its main road to the nucleus runs through Ras, a one-piece cousin of the Lecture 5 G protein, and then a relay of three kinases (Raf, MEK, ERK). Hold on to Ras: when it breaks, it's one of the most common causes of cancer (Chapter 6).

What you need from before: GEF turns on, GAP turns off, GTP = ON (Lecture 5); phosphorylation as an on/off tag (Chapter 0).
:::

### The big picture in one paragraph

A growth factor grabs two RTKs and pulls them together into a pair. Each one sticks phosphate tags on the other's tail. Those tags are landing pads. An adaptor protein called GRB2 lands on one and brings along Sos, which flips Ras ON. Ras starts a relay race of three kinases (Raf, MEK, ERK), each passing the baton to the next. The last runner, ERK, goes into the nucleus and switches on genes that make the cell divide. To stop, the cell swallows the receptor and digests it. The rest of the lecture is how scientists proved this order (fly eyes, glowing proteins) and a second use of RTKs: steering growing nerve fibers with Eph receptors.

:::hook
The main road: growth factor → RTK → GRB2 → Sos → Ras → Raf → MEK → ERK → nucleus. The classic for the last four: **"Ras Rarely Makes Errors"** (Ras, Raf, MEK, ERK).
:::

### What an RTK is

:::key
- Outside ligand domain, ONE transmembrane helix, inside tyrosine kinase
- Enzyme-coupled receptor; vs GPCR (7 passes, no enzyme)
- Ligands are mostly growth factors (EGF, PDGF, FGF, NGF, VEGF, insulin)

*Skim:* 60 genes / 20 subfamilies and the outside-domain types: recognize only.
:::

The short version: a receptor with its own built-in kinase engine. It crosses the membrane once.

A **receptor tyrosine kinase (RTK)** is an **enzyme-coupled receptor**, meaning the receptor itself is an enzyme. Every RTK has three parts:

1. a part **outside** that grabs the signal (ligand-binding domain)
2. **one** helix crossing the membrane
3. a part **inside** that is a **tyrosine kinase**: an enzyme that sticks phosphate groups onto the amino acid tyrosine

Humans have more than 60 RTK genes in about 20 subfamilies (EGF receptor, insulin receptor, NGF receptor, PDGF receptor, FGF receptor, VEGF receptor, Eph receptor, and more). The outside parts look very different from each other (cysteine-rich domains, immunoglobulin-like domains, fibronectin-like domains) because each grabs a different signal. The inside kinase is the shared engine.

| | GPCR (L5) | RTK (L8) |
|---|---|---|
| Crosses the membrane | 7 times | once |
| Has its own enzyme? | no, uses a G protein | yes, a tyrosine kinase inside |
| Turns on by | changing shape, acting as a GEF for the G protein | pairing up and phosphorylating each other |
| Typical job | fast responses (sugar, heart rate, senses) | growth, division, survival |

:::trap
A GPCR crosses the membrane 7 times and has no enzyme of its own. An RTK crosses once and is itself a kinase. A favorite compare-and-contrast question.
:::

:::hook
"**GPCR sews seven stitches, RTK pokes through once and brings its own tools.**"
:::

**What RTKs control:** proliferation (cell division), survival, differentiation (becoming a specialized cell type) and metabolism.

**What turns them on (her Table 15-4):** mostly growth factors.

| Ligand | What it's for |
|---|---|
| EGF (epidermal growth factor) | growth of skin and lining cells |
| insulin, IGF-1 (insulin-like growth factor) | metabolism and growth |
| NGF (nerve growth factor) | survival of some neurons |
| PDGF (platelet-derived growth factor) | growth of connective tissue cells |
| M-CSF (macrophage colony-stimulating factor) | making macrophages (immune cells) |
| FGF (fibroblast growth factor) | growth and development |
| VEGF (vascular endothelial growth factor) | growing new blood vessels |
| ephrins | blood vessel growth and steering axons |

These were found three ways: as growth factors that make certain cells grow, while studying human cancers (mutant receptors that make cells divide with no signal at all), and as developmental mutants in worms, flies and mice.

### How an RTK turns on

:::key
- Ligand → dimerize → cross-phosphorylate activation lips → more P-Tyr
- FGF needs heparan sulfate
- EGFR forms an asymmetric dimer (activator + receiver)
:::

The short version: pair up, tag each other, put out landing pads.

1. Pair up (dimerization). The ligand makes two single receptors (monomers) come together into a pair (a **dimer**).
2. Tag each other (cross-phosphorylation, also called trans-autophosphorylation). Each kinase sticks a phosphate on the other one's **activation lip**, a loop that was blocking the kinase's working spot. With the lip moved, the kinase gets much more active.
3. Tag more. Now fully active, each kinase phosphorylates more tyrosines on the receptor tails.
4. Landing pads (docking). Those phosphorylated tyrosines (written **P-Tyr**, phosphotyrosine) become landing spots for signaling proteins.

{{slide:L8-3|Three panels: monomers, ligand-bound dimer with phosphorylated activation lips, then extra phosphotyrosines.}}

{{fig:rtk_activation}}

:::hook
"**Pair up, poke each other, put out landing pads.**" Two people who each can't reach their own back, so they scratch each other's.
:::

:::exam
Her Q20: "how do the intracellular kinase domains become activated?" The answer is cross-phosphorylation: each kinase phosphorylates tyrosines on its partner's activation lip.

Her other options each borrow a different part of the unit. A phosphatase removes phosphates, so it would switch things off. SH2 domains belong to adaptors like GRB2, and Ras doesn't need to be grabbed by the RTK. Swapping GDP for GTP is what G proteins and Ras do. Cbl is the E3 ubiquitin ligase that tags RTKs for shutdown.
:::

Two variations she showed:

- FGF receptor: two FGF molecules plus **heparan sulfate** (a long sugar chain sticking off the cell surface) bind together with two receptors. FGF holds on tightly to heparan sulfate, and heparan sulfate is needed for the receptor to switch on well. Many RTKs pair up this way.
- EGF receptor: the two kinases form a lopsided (**asymmetric**) pair. One kinase (the "activator") pushes on the other (the "receiver") to switch it on. A lopsided handshake, not a mirror-image one.

{{slide:L8-5|The receiver and activator kinase domains sit at an angle, not mirror-image.}}

:::hook
FGF needs a **sugar** helper (heparan sulfate): "FGF has a sweet tooth." EGF does a lopsided handshake: "**E**GF = **E**lbow nudge."
:::

:::nancy
Two naming slips on these slides. The FGF title says "heparin sulfate" while the text says "heparan sulfate"; treat them as the same thing (heparan sulfate is the right name). And the EGF slide is titled "activation of the EFG receptor," a typo for EGF.

She also writes "formation of an asymmetric kinase domain dimer." Plain version: the two kinase halves aren't mirror images; one switches the other on.
:::

### Docking: SH2 and PTB domains

:::key
- P-Tyr = docking sites for SH2 (common) and PTB (less common) proteins
- Docking can activate by location, or the protein gets phosphorylated

*Skim:* Domain sizes and the Asn-Pro-X-Tyr motif: low priority.
:::

The short version: special "Velcro" parts on other proteins stick to the phosphate tags.

Proteins that grab phosphotyrosines have special parts (domains) for it:

| Domain | Size | What it grabs | How common |
|---|---|---|---|
| **SH2** (Src homology 2) | about 100 amino acids | a P-Tyr plus the few amino acids next to it | 115 human proteins have one |
| **PTB** (phosphotyrosine-binding) | 100-150 amino acids | usually an Asn-Pro-X-Tyr pattern | less common |

The amino acids next to each P-Tyr decide which SH2 protein lands there, so one active receptor can collect a specific set of partners.

Landing on the receptor can switch a protein on in two ways: just by bringing it to the membrane where its target is, or because the receptor then phosphorylates it.

{{slide:L8-6|SH2 and PTB proteins line up on different phosphotyrosines of the same activated receptor.}}

:::hook
The P-Tyr is one side of the Velcro, and the SH2 domain is the other side. "**SH2 = Sticks to pHospho-tyrosine.**"
:::

### Turning RTKs off: swallow and digest

:::key
- Off switch: endocytosis + lysosome degradation
- Mono-ubiquitination by c-Cbl marks the receptor
- Kinase activity triggers its own removal (HER1)
- Exception: NGF endocytosis carries a survival signal to the cell body

*Skim:* HER1 10-15 h / 10-fold numbers: skim.
:::

The short version: the cell eats the active receptor and breaks it down.

RTK signals are shut down by **receptor-mediated endocytosis** (the membrane pinches inward and swallows the receptor into a bubble) and then **degradation in lysosomes** (the cell's digestion compartments).

Her example: **HER1**, a human EGF receptor, normally lasts 10-15 hours on the cell surface. After binding EGF, swallowing speeds up about 10-fold and most receptors get destroyed. HER1 mutants with no kinase activity don't get this speed-up, so the receptor's own activity is what triggers its removal. It signals, then it signs its own eviction notice.

The tag that marks receptors for this is **mono-ubiquitination**: adding a single **ubiquitin** (a small protein used as a label). The enzyme that adds it is **c-Cbl**.

Swallowing can also carry a signal somewhere. **NGF** binds its receptor at the tip of an axon. The receptor and NGF are swallowed into a bubble and carried all the way back along the axon to the cell body, where they deliver a "stay alive" signal.

:::conn
Every pathway needs an off switch. For GPCRs it was the G protein's timer and PDE. For RTKs it's eating the receptor. A mutant RTK that can't be tagged or swallowed keeps signaling, which is one road to cancer.
:::

:::hook
"**c-Cbl = Cell's Bouncer Label.**" One ubiquitin sticker and the receptor gets thrown out.
:::

:::nancy
She writes: "average half life on cell surface of ~10-15 hours" and "Covalent modification of receptors by mono-ubiquitinylation promote endocytosis."

Plain version: a receptor normally lasts about 10-15 hours on the surface, and sticking one ubiquitin label on it gets it swallowed and digested.
:::

### Ras: the small GTPase in the middle

:::key
- Ras = small monomeric GTPase, lipid-anchored; GTP on, GDP off
- GEF turns on (Sos), GAP turns off (NF1)
- Ras is NOT the trimeric G protein

*Skim:* The superfamily list (Rheb, Rap1, Arf, Rab, Ran): skim, except Rho/Rac/Cdc42 which come back.
:::

The short version: Ras is a one-piece on/off switch, the same GTP-ON idea as Lecture 5's G protein.

Almost every RTK can switch on the **Ras/MAP kinase pathway**.

**Ras** is a **small monomeric GTPase**: a single-piece protein (the Lecture 5 G protein had three pieces) that holds GTP (ON) or GDP (OFF). A fatty tail anchors it to the inside face of the plasma membrane.

Two helpers control it, just like the Lecture 5 switch:

- **GEF** (guanine nucleotide exchange factor) pulls GDP out so GTP can get in. Turns Ras **ON**.
- **GAP** (GTPase-activating protein) speeds up Ras's very slow cutting of GTP. Turns Ras **OFF**.

| | Heterotrimeric G protein (L5) | Ras (L8) |
|---|---|---|
| Pieces | three (α, β, γ) | one |
| Turned on by | the GPCR acting as GEF | Sos (a GEF) brought by GRB2 |
| Turned off by | its own fairly quick GTPase timer | GAP needed, because its own timer is very slow |
| Anchored by | lipid tails on α and γ | lipid tail(s) |

Other small GTPases in the same family (the **Ras superfamily**), from her table:

| GTPase | Job |
|---|---|
| Rheb | activates mTOR for cell growth |
| Rap1 | on her table (no job given) |
| Rho, Rac, Cdc42 | pass signals to the actin skeleton (later this lecture) |
| Arf | vesicle coats |
| Rab | vesicle traffic |
| Ran | transport in and out of the nucleus |

:::easy
Both-boxes trap: Ras is a G protein AND a proto-oncogene product. It is a monomeric (single-piece) G protein, so don't lump it with the three-piece Gαβγ from Lecture 5.
:::

{{fig:ras_switch}}

:::hook
**GEF = "Gets Engine Fired"** (on). **GAP = "Gives Ability to Pause"** (off).
:::

:::she
"How could RTKs activate Ras???" written in big pink letters. Then the answer: adaptor proteins.
:::

### Adaptors link RTKs to Ras: GRB2 and Sos

:::key
- GRB2: SH2 binds receptor P-Tyr, SH3 holds Sos
- Sos (GEF) is pulled next to Ras and swaps GDP for GTP
- Answer to 'how could RTKs activate Ras': GRB2 + Sos
:::

The short version: GRB2 is a matchmaker with no enzyme of its own. It sticks to the receptor and drags Sos close to Ras.

1. EGF binds, the receptors pair up and phosphorylate their tyrosines.
2. **GRB2**, an **adaptor protein** (it has no enzyme activity, it just connects things), grabs a P-Tyr on the receptor with its **SH2 domain**. GRB2 also has two **SH3 domains**, which grab proline-rich stretches on other proteins.
3. GRB2's SH3 domains are holding **Sos**, a Ras-GEF. So when GRB2 lands on the receptor, it pulls Sos to the membrane, right next to Ras.
4. Sos pulls GDP out of Ras. GTP jumps in. Ras is ON and lets go of Sos.

{{slide:L8-11|The last step: Sos swaps GDP for GTP and active Ras lets go.}}

{{fig:ras_mapk}}

{{lab:rtk|RTK / Ras / MAPK (RasD, Gefitinib, MEK inhibitor, NF1 loss)}}

:::hook
GRB2 is the "**GRaB 2**" adaptor: one hand (SH2) grabs the receptor's P-Tyr, the other two hands (SH3) grab Sos. "**SH2 to the receptor, SH3 to Sos.**" And **Sos** sounds like **S.O.S.**: the call that rescues Ras from OFF.
:::

:::nancy
Her answer to "How could RTKs activate Ras???" is just the slide title "Adaptor proteins link RTKs to Ras."

Plain version: on the exam, name them. GRB2 is the adaptor (SH2 to the receptor, SH3 to Sos) and Sos is the GEF that flips Ras on. "Adaptor proteins" alone may not get full marks.
:::

### Proving Ras works downstream of RTKs

:::key
- Anti-Ras antibody or dominant negative Ras blocks proliferation
- Active Ras causes proliferation with no growth factor
- RasD = Gly12 mutation, GAP can't act, stuck ON; ~30% of tumors
:::

The short version: block Ras and growth factors stop working; make Ras always-on and you don't need growth factors.

| Experiment on fibroblasts (connective tissue cells) | Result |
|---|---|
| add PDGF or EGF | cells divide |
| inject antibodies against Ras | division blocked |
| add a **dominant negative** Ras | division blocked |
| add a **constitutively active** (always ON) Ras | cells divide with no growth factor at all |

What "dominant negative" means: a broken version of a protein that still grabs its partners and jams them, so it blocks the normal protein even when the normal one is present. Think of a broken key stuck in a lock. It's a loss-of-function tool, even though "dominant" sounds strong.

:::she
"What kind of mutation would result in constitutively activated Ras???"
:::

Always-ON Ras is called **RasD** (D for dominant). The classic mutation is at amino acid number 12. Swapping the normal **glycine 12** for any other amino acid (except proline) stops GAP from working on Ras. Ras can't cut its GTP, so it's locked ON. About **30% of human tumors** carry a hyperactive Ras.

:::trap
RasD doesn't grab GTP "harder." It can't get rid of GTP, because GAP can't help it cut. Same logic as cholera toxin on Gαs: a broken OFF switch.
:::

:::hook
"**Glycine 12 is the off-button.** Change it and Ras is stuck at noon (12 o'clock), the brightest point of the day, always ON." And "**30% of tumors**": roughly one in three.
:::

:::nancy
She writes that the glycine 12 change "blocks the functional binding of GAP proteins and in essence locks Ras in the active GTP-bound state."

Plain version: GAP can't do its job, so Ras can't turn off. "Constitutively active" = always on. "Dominant negative" sounds strong, but it's a blocker: a broken protein that jams the normal one.
:::

### The fly eye: genetics finds the pathway

:::key
- R8 shows Boss → activates Sevenless (RTK) on R7 precursor (contact-dependent)
- No signal → becomes a cone cell, no R7
- sev + RasD → R7 back → Ras is downstream of Sev
- Enhancer/suppressor screens (temp-sensitive Sev) found Drk (GRB2) and Sos

*Skim:* 800 ommatidia / 12 accessory cells: low priority.
:::

The short version: a fly cell needs a touch from its neighbor to become photoreceptor R7. Breaking the receptor removes R7; adding always-on Ras puts it back.

The fruit fly (*Drosophila*) eye is made of about 800 units called **ommatidia** ("little eyes"). Each has **8 light-sensing cells (R1-R8)** and 12 helper cells. The light-sensing cells are recruited one at a time, and **R7 is the last one**. To become R7, the cell needs a signal from its neighbor **R8**.

:::she
"What do you hypothesize would happen if there was no signal from R8??" Answer: the R7 precursor doesn't become R7; it becomes a cone cell (a non-neural lens-secreting cell) instead.
:::

The players:

- The future R7 cell carries an RTK called **Sevenless (Sev)**.
- R8 carries the matching ligand, **Boss** ("bride of sevenless"), a seven-pass membrane protein stuck in R8's surface.
- Because Boss is attached to R8, R8 has to physically touch R7. This is **contact-dependent signaling**.
- A *sev* mutant fly has no R7 (that's where the name "seven-less" comes from). A *boss* mutant looks the same.

The key experiment: a ***sev* mutant that also makes RasD** gets its R7 back. Always-on Ras skips around the missing receptor. That proves Ras works **downstream** (later in the chain) of Sev.

{{slide:L8-15|Wild type, sev mutant, and sev + RasD side by side. The double mutant gets its R7 back.}}

{{fig:r7_epistasis}}

:::hook
**Sevenless lacks R7. Boss is the "Bride"** who has to touch Sevenless for R7 to happen. No touch, no R7, and the cell settles for being a cone cell.
:::

**Finding the rest of the chain.** Just looking for more flies missing R7 didn't work, because breaking the later parts (Ras, Raf, MAPK) kills the fly, and dead flies don't grow eyes. So researchers used flies with a **temperature-sensitive Sev** (one that works only partly at a certain temperature) and ran **enhancer and suppressor screens**: they looked for new mutations that made the eye worse (enhancers) or better (suppressors). Those genes had to be in the same pathway. The screens found **Drk** (the fly version of GRB2) and **Sos**.

:::hook
Enhancer screen = "make a weak problem worse." Suppressor screen = "make it better." Either way, the gene you find is on the same road.
:::

:::nancy
She writes "Signaling from R8 is necessary to induce R7 fate" and calls Boss "a seven pass transmembrane receptor protein" on R8.

Plain version: "induce R7 fate" = make the cell become R7. Boss is the ligand here (it activates Sevenless) even though she calls it a receptor protein; it's the 7-pass protein sitting on R8.
:::

### Measuring Ras activation with FRET

:::key
- FRET only when two labels touch (bound)
- Showed Ras-GTP rising minutes after EGF

*Skim:* Exact wavelengths: low priority.
:::

The short version: FRET is a glow trick that only works when two labeled proteins are touching, so it shows the moment Ras turns on.

**FRET (fluorescence resonance energy transfer):** when two glowing molecules get within a few nanometers of each other, the first can pass its energy straight to the second. You shine the color that excites the first, but you see the second one's color come out. It's a molecular "are you two touching?" test.

Her experiment:

- Ras was fused to **YFP** (glows yellow).
- A protein that only grabs Ras-GTP (the Ras-binding part of Raf) was labeled with a **red dye**.
- Shine 476 nm light.
  - Ras OFF (GDP): the red probe isn't attached, you see **yellow (528 nm)**.
  - Add EGF, Ras ON (GTP): the red probe grabs Ras, energy jumps across, you see **red (617 nm)**.
- The graph shows active Ras rising, peaking a few minutes after EGF, then falling.

{{slide:L8-17|Yellow means Ras is off, red (FRET) means the probe has grabbed Ras-GTP. The curve peaks a few minutes after EGF.}}

:::trap
FRET only gives a signal when the two labeled molecules are very close (bound). So FRET = "they're interacting." No FRET = "they're apart." It doesn't measure how much protein there is.
:::

:::exam
Her Q22 uses a different pair of labels than her slide: CFP (cyan) on Ras and YFP (yellow) on the Ras-binding domain of Raf. The labels change between versions of this experiment, but the logic stays the same.

1. Growth factor binds the RTK, GRB2 brings Sos, and Sos (a GEF) loads Ras with GTP.
2. Only Ras-GTP binds Raf's Ras-binding domain.
3. Binding brings CFP and YFP within a few nanometers, so energy jumps from CFP to YFP.

So the FRET signal increases after the growth factor. You shine the light that excites CFP and you see YFP's yellow come out.

Why her wrong options fail: Ras stays anchored at the membrane and doesn't go to the nucleus. Sos swaps GDP for GTP and turns Ras on. Hydrolyzing GTP to GDP is GAP's job.
:::

:::hook
"**Yellow = alone, Red = Ras is Ready.**"
:::

### The MAP kinase module

:::key
- Ras → Raf (MAPKKK) → MEK (MAPKK) → ERK (MAPK)
- Active Raf alone = proliferation; dead Raf blocks even RasD
:::

The short version: a relay race of three kinases. Each one phosphorylates and wakes the next.

Active Ras switches on a chain of three kinases called a **MAP kinase module** (MAP = mitogen-activated protein; a **mitogen** is anything that makes a cell divide):

Ras-GTP → **Raf** (a MAPKKK) → **MEK** (a MAPKK) → **ERK** (a MAPK)

The names count down: Raf is a "kinase kinase kinase" (the kinase that switches on the kinase that switches on the kinase), MEK is a "kinase kinase," and ERK is the final "kinase." This module is found from yeast to humans.

:::hook
"**Ras Rarely Makes Errors**": Ras, Raf, MEK, ERK, in that order. (Funny, because a Ras that can't turn off is the most common error in cancer.) Count the K's backwards: **3 K's, 2 K's, 1 K** for Raf, MEK, ERK.
:::

Experiments that put Raf after Ras:

- Always-on Raf makes cells divide with no signal from above.
- Broken Raf blocks division even when RasD is present.

### MAPK turns on genes

:::key
- ERK → nucleus → ~100 early response genes
- c-fos: SRE with SRF + TCF; ERK phosphorylates TCF
- This TCF is NOT the Wnt TCF

*Skim:* p90RSK: recognize.
:::

The short version: ERK walks into the nucleus and switches on "early response" genes like c-fos.

Active ERK moves into the nucleus and phosphorylates transcription factors. When growth factor (EGF or PDGF) is added to **quiescent** cells (resting, not dividing), about 100 genes switch on quickly. These are the **early response genes**.

An important one is **c-fos**, a transcription factor cells need to move through the cell cycle. Here's how it switches on:

- In front of the c-fos gene is a DNA landing pad called the **serum response element (SRE)**. (It's named that because growth factors in **serum**, the liquid part of blood, switch it on.)
- **SRF** (serum response factor) sits on the SRE together with **TCF** (ternary complex factor).
- **ERK phosphorylates TCF**, which turns on c-fos.
- ERK also switches on another kinase, **p90RSK**, which phosphorylates SRF.

{{slide:L8-19|ERK enters the nucleus and phosphorylates TCF, which sits with SRF on the SRE of the c-fos gene.}}

:::hook
"**SRF Sits on the SRE; TCF is The Contact ERK phosphorylates.**" Compare with Lecture 5: CREB sits on the CRE and PKA phosphorylates it. Same idea, different pathway.
:::

| | cAMP pathway (L5) | MAPK pathway (L8) |
|---|---|---|
| Kinase that enters nucleus | PKA | ERK |
| DNA landing pad | CRE | SRE |
| Factor that gets phosphorylated | CREB | TCF (and SRF via p90RSK) |
| Example gene / result | CRE genes | c-fos, cell cycle |

:::nancy
She writes "quiescent cultured mammalian cells" and uses TCF for "ternary complex factor."

Plain version: "quiescent" = resting, not dividing. And this TCF is NOT the Wnt TCF in Lecture 11 (T-cell factor). Same three letters, different protein.
:::

### Scaffolds prevent crosstalk

:::key
- Scaffolds hold one module's kinases together → no crosstalk
- Yeast: Ste5 (mating), Pbs2 (osmotic)

*Skim:* Counts of modules and MAPKs: skim.
:::

The short version: scaffold proteins hold each relay team together so teams don't pass the baton to the wrong runner.

Cells have several MAP kinase modules. Budding yeast has at least six; mammals have at least five, built from 12 MAPKs, 7 MAPKKs and 7 MAPKKKs. Some modules share parts. So how does yeast's "time to mate" signal avoid accidentally switching on its "too much salt" response?

**Scaffold proteins** hold the three kinases of one module together in one complex, like a tool belt or a team bus. In yeast:

- **Ste5** is the scaffold for the mating response kinases.
- **Pbs2** is both a kinase and a scaffold for the salt-stress (osmotic) response, which makes glycerol.

This prevents **crosstalk** (one pathway accidentally switching on another).

{{slide:L8-20|Two yeast MAPK modules share "kinase A" but stay separate because each sits on its own scaffold.}}

:::hook
"**Ste5 = Sex** (mating), **Pbs2 = Pickles** (salty)." Each team rides its own bus.
:::

### RTKs and the actin skeleton: Rho GTPases

:::key
- Some RTKs don't switch on genes. They reshape the cell's skeleton instead
- They do it through three small switches: Cdc42, Rac and Rho
- Cdc42 makes finger spikes, Rac makes flat sheets, Rho makes thick cables
:::

The short version: so far, RTKs told the nucleus "divide." Some RTKs instead tell the cell's skeleton "change shape." That's how a growing nerve fiber steers.

First, the word you need. **Actin** is the cell's skeleton: long protein strands that can be built up, torn down or squeezed to change the cell's shape.

Some RTKs switch on the **Rho family GTPases**. These are small on/off switches, just like Ras (GDP = off, GTP = on). The difference is what they control. Ras sends a message to the nucleus. The Rho family rebuilds actin.

There are three to know, and each one builds a different shape:

| Switch | What it builds | What it looks like |
|---|---|---|
| **Cdc42** | **filopodia** | thin finger-like spikes poking out of the edge |
| **Rac** | **lamellipodia** | a flat, wide sheet at the edge, with ruffles |
| **Rho** | **stress fibers** | thick ropes of actin stretched across the cell |

Growing nerve fibers use these shapes to steer toward the right target. That steering is called **axon guidance**, and it's where the rest of this lecture goes.

{{slide:L8-21|Same cell type, four looks: resting, then with active Cdc42 (finger spikes), Rac (flat sheets) and Rho (thick cables).}}

:::hook
"**C**dc42 = **C**rawling fingers (filopodia). **R**ac = **R**uffles (lamellipodia). **R**ho = **R**opes (stress fibers)."
:::

#### Growth cones

:::key
- The growth cone is the moving tip of a growing axon, like the neuron's GPS
- Its fingers (filopodia) feel around; its palm (lamellipodia) spreads out
:::

The short version: the tip of a growing nerve fiber is a little hand that feels its way to the right place.

The words you need:

- A **neuron** is a nerve cell.
- Its **axon** is the long wire that grows out of it to reach another cell.
- The **growth cone** is the moving tip at the end of a growing axon. It explores the area around it and decides which way to grow, like a GPS.

While the nervous system is being built, every axon has to grow out and find its correct target. The growth cone does the finding. It's built like a hand feeling around in the dark:

- **filopodia**, the fingers: thin spikes filled with long, bundled actin strands
- **lamellipodia**, the palm: flat sheets filled with a criss-crossed mesh of actin
- **microtubules**, the wrist: stiffer tubes running up the axon into the middle of the cone

If the growth cone touches something it likes, it keeps going. If it touches a "go away" signal, it pulls back and the axon turns. The next three lessons are about one "go away" signal.

#### The retinotopic map

:::key
- Eye neurons connect to the brain's tectum in an orderly, flipped map
- Front of the eye goes to the back of the tectum, and back goes to front
- The back of the tectum PUSHES certain axons away. Nothing pulls them to the front
:::

The short version: eye neurons wire up to the brain in a neat, flipped map, and they find their spots because some areas push them away.

The words you need:

- **Retinal ganglion cells (RGCs)** are the neurons in the retina (the back of the eye) that send the picture to the brain. Their axons form the optic nerve.
- The **optic tectum** is the part of a fish's brain where those axons land.
- **Anterior** means front. **Posterior** means back.

The axons don't land randomly. They form a flipped map:

- Neurons from the **front** of the retina connect to the **back** of the tectum.
- Neurons from the **back** of the retina connect to the **front** of the tectum.

Because each spot on the retina connects to a matching spot on the tectum, the picture stays in order. That point-to-point wiring is the **retinotopic map** ("retina-place map").

How did scientists figure out what guides them? They grew eye neurons on alternating stripes of membrane taken from the front and back of the tectum.

- Neurons from the **back** of the retina avoided the stripes from the **back** of the tectum.
- Neurons from the **front** of the retina grew happily on both kinds of stripe.

So something on the back of the tectum pushes back-of-the-eye axons away.

{{slide:L8-26|Top: axons from the back of the eye stop at the stripes from the back of the tectum. Bottom: axons from the front of the eye grow over both.}}

:::trap
The front of the tectum does not attract these axons. The back of the tectum repels them. She put this on the slide, so expect it as a true/false or "which is correct" option.
:::

:::hook
The map is **crossed**: "back goes front, front goes back." And it works by **pushing away**, like a "keep out" sign, not like a magnet.
:::

:::nancy
She writes: "The preference for posterior neurons to avoid posterior tectum is not due to the attractive nature of anterior tectum, but a repulsive factor on posterior tectum."

Plain version: the back of the tectum pushes these axons away. Nothing is pulling them to the front.
:::

#### Ephrin and Eph receptors

:::key
- The "keep out" sign is ephrinA on the tectum, highest at the back
- The axon reads it with the EphA receptor (an RTK); axons from the back of the eye have lots of EphA
- ephrinA is GPI-anchored and binds EphA; ephrinB crosses the membrane, binds EphB and can signal backwards
- Eph receptors are the biggest RTK family (13 in humans)
:::

The short version: the tectum holds up a "keep out" sign called ephrin. Axons read the sign with a receptor called Eph. The more receptor an axon has, the sooner it gets pushed away.

Meet the two players:

- **ephrinA** is the "keep out" sign. It's a protein stuck on the surface of the tectum cells. There's a little at the front of the tectum and a lot at the back. That uneven spread is called a **gradient**.
- **EphA** is the receptor on the axon that reads the sign. It's an RTK, so it's built like the receptors from the start of this lecture.

Now put them together:

1. Axons from the **back** of the retina carry **lots** of EphA, so they're very sensitive to the sign.
2. As they grow into the tectum, ephrinA gets stronger the further back they go.
3. They hit their "too much, stop" point early, near the **front** of the tectum.
4. Axons from the **front** of the retina carry **little** EphA. They barely notice the sign, so they keep growing to the **back**.

That's how the map gets flipped. Proof: in animals missing the EphA receptor, back-of-the-eye axons are no longer pushed away from the back of the tectum.

{{fig:ephrin_map}}

Some facts about the family she lists:

- **Eph receptors** are the largest family of RTKs, with 13 in humans.
- There are two kinds of ephrin, and each binds its own kind of receptor. They differ in how they're attached to the membrane.

| | ephrinA | ephrinB |
|---|---|---|
| How it's attached | by a **GPI anchor**, a fatty tether that holds it on the outer surface only | it's **transmembrane**, meaning it goes all the way through the membrane and has a tail inside the cell |
| Which receptor it binds | **EphA** (8 kinds) | **EphB** (5 kinds) |
| Can it send a signal into its own cell? | not in her slides | yes, through its inside tail (this is **reverse signaling**) |

Because the sign and the receptor are both stuck in cell membranes, the two cells have to touch, and the message can go either way:

- **Forward signaling**: the message goes into the cell that has the Eph receptor. That's the axon getting pushed away.
- **Reverse signaling**: the message goes into the cell that has the ephrin. Only ephrinB can do this, because only it has a tail inside the cell for signaling proteins to grab.

Beyond axons, Eph and ephrin also shape how blood vessels grow, draw borders between tissues and guide moving cells. Most of these jobs end the same way: by changing the actin skeleton.

:::easy
Swap trap: ephrin**A** = GPI-**A**nchored, binds Eph**A**. ephrin**B** = goes all the way through (transmembrane), binds Eph**B**, and can signal **B**ack into its own cell.
:::

:::hook
**Eph = "Eww, push away."** The more EphA an axon has, the more it hates ephrinA, so it stops early, at the front.
:::

:::nancy
This slide is a figure pasted from a review article, and the article's text runs into her labels, so it reads as a jumble.

Plain version, all you need from it: ephrinA is GPI-anchored and binds EphA (8 kinds). ephrinB goes through the membrane, binds EphB (5 kinds) and can signal back into its own cell (reverse signaling). There are 13 Eph receptors in humans.
:::

#### Growth cone collapse through Ephexin and RhoA

:::key
- Whole message: "Axon, don't grow this way. Turn away!"
- ephrinA1 (stop sign) → EphA4 (receptor) → Ephexin (GEF) → RhoA (switch) → actin squeezes → growth cone collapses
- A dominant negative Ephexin blocks the collapse, which proves Ephexin is needed
:::

The short version: the whole chain passes one message along: "Axon, don't grow this way. Turn away!"

Last lesson explained where the stop sign is. This one explains how the axon actually backs off. There are a lot of protein names, but each one just hands the message to the next.

1. **ephrinA1 is the stop sign.** It sits on the tectum cell and touches the growth cone.
2. **EphA4 is the receptor.** It reads the stop sign and switches on.
3. **Ephexin is the GEF.** A GEF is the "on" helper for a small switch: it lets the switch drop GDP and pick up GTP. Ephexin does this for RhoA.
4. **RhoA is the switch.** Once it holds GTP, it's on, and it makes myosin (the motor protein) squeeze the actin skeleton.
5. **The growth cone collapses.** The squeezed tip shrinks back, and the axon turns away.

{{slide:L8-29|Follow the chain down: EphA4 switches on Ephexin, Ephexin switches on RhoA, and actin-myosin squeezing collapses the growth cone.}}

How do we know Ephexin is needed? Researchers put a **dominant negative Ephexin** into eye neurons. A dominant negative is a broken copy that jams the pathway even when the normal copy is there. With it, ephrinA could no longer collapse the growth cones. Remove Ephexin and the message stops, so Ephexin must be part of the chain.

:::conn
This is the same wiring you learned with Ras, pointed at a different target. Before: RTK → Sos (a GEF) → Ras (a switch) → the cell divides. Here: RTK → Ephexin (a GEF) → RhoA (a switch) → the growth cone collapses. Same pattern of receptor, then GEF, then GTPase. Different job at the end.
:::

:::hook
"**Ephexin = Eph's EXit sign.**" It flips RhoA on, and RhoA pulls the hand back.
:::

### How to figure it out: ordering genes in a pathway (epistasis) {#howto-epistasis}

Nancy likes experiments that put genes in order. This is **epistasis analysis**: when two mutations have opposite effects, the double mutant looks like whichever one is **downstream** (later in the chain).

How to spot it: a question gives you single mutants and a double mutant, or "always-on X in a cell missing Y," or a dominant negative added to an activated cell.

Steps:

1. Write each single mutant's result. One should be "pathway OFF" (loss-of-function, like *sev* or dominant-negative Raf) and one "pathway ON" (gain-of-function, like RasD or always-on Raf).
2. Look at the double mutant.
3. Whichever single mutant it looks like, that gene is downstream. Why: if the downstream part is stuck ON, the upstream part doesn't matter. If the downstream part is broken, nothing upstream can get through.

:::hook
"**The last domino decides.**" Whatever's closest to the end wins the double mutant.
:::

Practice:

- *sev* (no R7) + RasD (extra R7 activity) → R7 present. Looks like RasD, so Ras is downstream of Sev.
- RasD (divides) + broken Raf (no division) → no division. Looks like the Raf loss, so Raf is downstream of Ras.
- Always-on Raf + antibody against Ras → cells still divide. Raf is downstream; blocking Ras above it can't stop it.
- Always-on EGFR + dominant-negative Ras → no division. Ras is downstream of the receptor.
- *boss* mutant + RasD → R7 present (same logic as *sev*, since Boss is upstream of Sev).
- EphA-mutant retina on a normal tectum → posterior neurons grow into the posterior tectum. Without the receptor there's no push, so the receptor is needed to read the ephrin gradient.

:::trap
Dominant-negative is a loss-of-function tool even though "dominant" sounds strong. It blocks the normal protein. Constitutively active is the gain-of-function tool.
:::

### Reading her questions on this lecture {#read-l8}

| If the question says... | She's testing... | How you'd get tricked |
|---|---|---|
| "how many times does it cross" | RTK once, GPCR seven | Mixing them up |
| "how could RTKs activate Ras" | GRB2 (SH2 + SH3) brings Sos (GEF) | Saying the RTK phosphorylates Ras |
| "Ras Gly12 mutant" | GAP can't act, stuck ON | Saying it binds GTP more tightly |
| "dominant negative" | A loss-of-function tool | Reading "dominant" as stronger |
| "double mutant" | Epistasis: looks like the downstream gene | Picking the upstream gene |
| "no R7 cell" | sev or boss mutant; becomes a cone cell | Thinking the cell dies |
| "FRET signal increases" | The two labeled proteins bound | Thinking it measures amount, not contact |
| "CFP-Ras and YFP-Raf RBD, add growth factor" | Ras-GTP binds Raf, FRET goes up | Thinking Sos turns Ras off, or Ras leaves for the nucleus |
| "how do the kinase domains become activated" | Cross-phosphorylation of each other's activation lip | Picking the GDP/GTP swap (that's Ras) or a phosphatase |
| "posterior retinal axons" | Repelled by high ephrinA in posterior tectum | Saying anterior tectum attracts them |
| "ephrinA vs ephrinB" | GPI-anchored vs transmembrane (reverse signaling) | Swapping them |

### Lecture 8 on one page

| Part | Plain-English job | Remember it by |
|---|---|---|
| RTK | receptor with its own kinase, crosses once | brings its own tools |
| Activation | pair up, tag each other, landing pads | scratching each other's backs |
| FGF / EGF variations | heparan sulfate helper / lopsided pair | sweet tooth / elbow nudge |
| SH2, PTB | Velcro for P-Tyr | SH2 sticks |
| Off switch | c-Cbl mono-ubiquitin, swallow, digest | the bouncer label |
| Ras, GEF, GAP | one-piece switch; GEF on, GAP off | Gets Engine Fired / Gives Ability to Pause |
| GRB2 + Sos | matchmaker brings the GEF | SH2 to receptor, SH3 to Sos; S.O.S. |
| RasD | Gly12 mutant, GAP can't act, stuck ON | stuck at noon; 30% of tumors |
| Fly eye | Boss (R8) touches Sev (R7); RasD rescues | Bride of Sevenless |
| FRET | glow only when touching | yellow alone, red ready |
| MAPK module | Raf → MEK → ERK relay | Ras Rarely Makes Errors |
| c-fos | ERK → TCF on SRE with SRF | SRF sits on the SRE |
| Scaffolds | keep relay teams apart | Ste5 sex, Pbs2 pickles |
| Rho family | Cdc42 fingers, Rac ruffles, Rho ropes | C, R, R |
| Eph/ephrin | push axons away; A = GPI, B = transmembrane | Eww, Push away |
| Ephexin → RhoA | growth cone collapse | Eph's EXit sign |
| Epistasis | double mutant looks like the downstream gene | last domino decides |
