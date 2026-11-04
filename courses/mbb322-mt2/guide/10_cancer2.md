## Lecture 10: cancer II, causes and cancer genes {#l10}

This lecture answers two questions: what damages cells into cancer (carcinogens), and which genes, when broken, drive it. The answer to the second question sends you right back to Lectures 5 and 8.

:::story
Chapter 6. The first half of "which genes break": the gas pedals. Some chemicals and radiation damage DNA. The genes that matter most when damaged are proto-oncogenes, and almost all of them are parts of the signaling pathways from Chapters 1 and 4. Expect old friends (Ras, RTKs, PKC) to show up stuck in the ON position.

What you need from before: Ras and the MAPK relay (Lecture 8), DAG and PKC (Lecture 5), the multi-hit model (Lecture 9).
:::

### The big picture in one paragraph

Things that cause cancer come in two kinds: ones that damage DNA directly (and show up on a bacteria test called the Ames test), and ones that don't touch DNA but make cells divide so much that copying errors pile up anyway. The genes that matter when they break come in three kinds: gas pedals (proto-oncogenes), brakes (tumor suppressors) and mechanics (caretakers). This lecture is mostly about gas pedals. Almost every one turns out to be a piece of a growth-signal pathway you already know (RTK, Ras, Raf, Src, Abl, JAK) that got stuck ON. The lecture ends with Gleevec, a drug that jams one of those stuck pedals.

:::hook
"**Damage or push, then a stuck pedal.**" Carcinogens either damage DNA or push cells to divide; the result that matters is a growth pathway stuck ON.
:::

### Mutagen vs carcinogen

:::key
- Mutagen = changes DNA; carcinogen = causes cancer
- Genotoxic carcinogens are both; some mutagens aren't carcinogens; some carcinogens aren't mutagens

*Skim:* The comparison table rows: know the definitions and the summary line.
:::

The short version: a mutagen is judged by what it does to DNA. A carcinogen is judged by whether it causes cancer. Lots of things are both, but not everything.

- A **mutagen** is a physical or chemical agent that makes a permanent change in the DNA sequence that gets passed on (a **mutation**). It can hit anywhere, including DNA that doesn't code for anything, and it doesn't necessarily cause disease.
- A **carcinogen** is anything that causes cancer or clearly raises the rate of cancer. It might do that by mutating DNA, or by changing how fast cells divide, causing inflammation, or helping cells hide from the immune system.

| | Mutagen | Carcinogen |
|---|---|---|
| What it's judged on | the DNA molecule itself | the cell's behavior (growth and tissue control) |
| How it's tested | Ames test (bacteria, mutation rate) | animal studies and human data (tracking who gets tumors) |
| Possible outcomes | harmless variants, genetic disorders like sickle cell anemia, or cell death; cancer is only one possible outcome | malignant tumors and uncontrolled division |
| How it works | always changes the genetic code (swaps, insertions, deletions) | either **genotoxic** (damages DNA) or **non-genotoxic** (no DNA change) |

Her summary line: "All genotoxic carcinogens are mutagens, but not all mutagens are carcinogens, and not all carcinogens are mutagens."

:::easy
Both-boxes trap (the sphingomyelin of this lecture): genotoxic carcinogens are mutagens AND carcinogens. If a student in a question says "it's a carcinogen, so it can't be a mutagen" or "every mutagen is a carcinogen," both are wrong.
:::

{{fig:venn}}

:::hook
Picture two overlapping circles. The overlap is "genotoxic carcinogens." Mutagens outside the overlap mutate bacteria but don't cause cancer in animals. Carcinogens outside the overlap cause cancer without touching DNA (asbestos, phorbol esters). "**Geno-toxic = toxic to genes**," so it lives in the overlap.
:::

:::nancy
Her summary line, "All genotoxic carcinogens are mutagens, but not all mutagens are carcinogens, and not all carcinogens are mutagens," packs three claims into one sentence.

Plain version: draw two overlapping circles. The overlap (genotoxic carcinogens) is in both. Each circle also has a part outside the other: mutagens that don't cause cancer, and carcinogens that don't touch DNA.
:::

### Radiation

:::key
- Radiation damages DNA; repair, death, senescence, or mutation
- Evidence: X-rayed flies (1920s), bomb survivors (leukemia), UV (melanoma)

*Skim:* Repair pathway names: recognize.
:::

The short version: radiation breaks DNA. If the cell fixes it, fine. If not, the cell dies, retires, or survives with mutations.

Radiation damages DNA in several ways: changed bases, breaks in one strand or both strands, and crosslinks (strands stuck together). The cell can try to repair it (base excision repair, homologous recombination, non-homologous end joining).

| If... | Then... |
|---|---|
| repair works | the cell lives normally |
| repair fails | the cell dies (apoptosis or necrosis), stops dividing (senescence), or survives with mutations that can lead to cancer |

Evidence that radiation causes mutations and cancer:

- 1920s: X-raying fruit flies caused mutations.
- After WWII: atomic bomb survivors got more cancers, especially leukemia.
- **UV light** raises melanoma (skin cancer) rates.

:::hook
Radiation evidence in time order: "**Flies, bombs, sun.**"
:::

### The Ames test

:::key
- his- Salmonella; count his+ revertants
- Rat liver extract activates indirect carcinogens
- Ames positive ≠ carcinogen; Ames negative ≠ safe
:::

The short version: use bacteria that are broken in one gene and count how many get "un-broken" by the chemical. More un-breaking = more mutations = mutagen.

The **Ames test** uses bacteria to check whether a chemical causes mutations.

1. Start with broken bacteria. Use a *Salmonella* strain with a mutation that stops it making histidine (an amino acid). It can only grow if you give it histidine. This is written **his-**.
2. Activate the chemical. Mix the test chemical with **rat liver extract**, to copy how a liver would process it (explained in the next section).
3. Starve them. Spread the bacteria on a plate with only a tiny bit of histidine and let them grow.
4. Count survivors. Only bacteria that get a new mutation that fixes the original defect can make their own histidine and grow into colonies. These are **revertants** (his+, "reverted" to normal).
5. Compare with a control plate with no chemical (it still has a few natural revertants). Many more colonies with the chemical = mutagen.

{{slide:L10-4|The rat liver extract step is there so indirect carcinogens get activated before they meet the bacteria.}}

A chemical that heavily mutates bacteria has a very high chance of being a genotoxic carcinogen in humans.

:::trap
Some chemicals mutate bacteria very well but are neutralized in mammals by DNA repair, or can't get into animal cells. Those are mutagens but not carcinogens. A positive Ames test doesn't prove carcinogen; a negative Ames test doesn't rule out carcinogen (it could be non-genotoxic).
:::

:::hook
**Ames = "Asks Microbes about Errors in Sequence."** It tests mutation, not cancer. Think of it as fixing a flat tire by accident: only a new mutation can patch the his- hole.
:::

:::exam
Her practice version of this question says the Ames test uses "a specialized strain of E. coli." Her slide only says "bacteria," and the classic strain is his- *Salmonella*. Don't throw out the right option over the species name. Pick the option that says the test detects mutagens by counting reverse mutations in a bacterial strain. The other options test things the Ames test never measures, like membrane damage, entry into S phase, ryanodine receptors or toxicity.
:::

### Indirect carcinogens and cytochrome P450

:::key
- Liver P450 oxidizes them into electrophiles that attack DNA
- Aflatoxin and benzo[a]pyrene → epoxides on guanine
- Indirect is still GENOTOXIC
:::

The short version: some chemicals are harmless until the liver tries to clean them up, and the cleanup step turns them into DNA attackers.

**Indirect carcinogens** are usually unreactive and often don't dissolve in water. They only become dangerous after the liver changes them.

The **cytochrome P450** enzymes are a family of liver enzymes (in the ER membrane) whose normal job is detox. They add oxygen to fatty, water-insoluble drugs and waste molecules (which would otherwise build up in membranes) to make them water-soluble, so the kidneys can flush them out.

For certain chemicals, that step creates a very unstable, electron-hungry molecule, an **electrophile** ("electron lover"; her slide calls it an electrophilic radical). It immediately attacks the electron-rich bases of nearby DNA, causing copying errors and mutations.

Classic examples:

| Chemical | Where it's found | What P450 makes | What it attacks |
|---|---|---|---|
| **Aflatoxin** | a mold on peanuts and grains | aflatoxin-2,3-epoxide | guanine (G) in DNA |
| **Benzo[a]pyrene** | coal tar and cigarette smoke | benzo[a]pyrene diol epoxide (several P450 steps) | guanine (G) in DNA |

That's why the Ames test adds rat liver extract. Without the P450 enzymes, these chemicals would look harmless.

{{slide:L10-6|Both chemicals end up as epoxides bound to guanine in DNA, but only after P450 works on them.}}

:::hook
P450 is a cleanup crew that sometimes turns a sleeping dog into a rabid one. The liver meant to flush it out and armed it instead. Both examples end as an **epoxide on G**: "**E**poxides **G**rab **G**uanine."
:::

:::trap
"Indirect" doesn't mean "weak" or "non-genotoxic." Indirect carcinogens ARE genotoxic; they just need activation first. Non-genotoxic is a separate category.
:::

:::nancy
She writes: "this oxidation process creates a highly unstable, electron-deficient intermediate, an electrophilic radical... It immediately attacks the electron-rich bases of nearby DNA."

Plain version: the liver's cleanup step makes a molecule that's desperate for electrons, and it grabs them from DNA, which damages it.
:::

### Non-genotoxic carcinogens

:::key
- No DNA change, Ames negative; work by forcing division or blocking death
- Asbestos: chronic inflammation (mesothelioma)
- TPA: mimics DAG, locks PKC on
:::

The short version: these never touch DNA. They make cells divide so much that normal copying mistakes pile up faster.

**Non-genotoxic carcinogens** cause cancer without touching DNA or changing its sequence. They test **negative** on the Ames test.

How they work: every time a cell copies its DNA, a few random mistakes happen. If you force cells to divide a lot, or stop them from dying, those mistakes pile up faster, which speeds up the multi-hit process from Lecture 9.

| Agent | What it does in the cell | How it drives cancer | Tumors |
|---|---|---|---|
| Asbestos (physical irritant) | tiny mineral fibers lodge in tissue for good; immune cells can't digest them | constant inflammation floods the area with growth factors and forces endless repair divisions | mesothelioma and lung cancer |
| Phorbol esters / TPA (signal copycat) | copy DAG and permanently switch on PKC | constant fake growth signals (MAPK pathway) push already-mutated cells to multiply fast | skin carcinomas (classic research model) |

:::hook
"**Asbestos = a splinter that never comes out. TPA = a fake DAG that never leaves.**" Neither touches DNA; both keep cells dividing.
:::

:::conn
Phorbol esters are a Lecture 5 molecule in disguise. DAG normally switches on PKC briefly, then gets used up. TPA looks like DAG but doesn't go away, so PKC never turns off.
:::

:::nancy
Her table calls TPA a "Receptor Mimic."

Plain version: TPA mimics DAG, the second messenger that switches on PKC. If asked what it copies, say DAG. "Forcing pre-mutated cells into rapid clonal expansion" just means making already-mutated cells multiply fast.
:::

### Viruses and bacteria

:::key
- Small share of human cancers; HPV (cervical), H. pylori (stomach)
- HPV integration releases its growth genes in the basal layer

*Skim:* The full virus table: know HPV and H. pylori; skim the rest.
:::

The short version: a few viruses and one bacterium cause a small share of human cancers.

Viruses cause a small percentage of human cancers. The evidence comes from finding viruses inside patients' tumors and from tracking who gets which cancer, where.

| Virus or bacterium | Cancer |
|---|---|
| papillomavirus (HPV) | warts, cervical carcinoma |
| hepatitis B and C | liver cancer |
| Epstein-Barr virus | Burkitt's lymphoma, nasopharyngeal carcinoma (back of the nose and throat) |
| human herpesvirus 8 | Kaposi's sarcoma |
| HTLV-1 | adult T-cell leukemia |
| *Helicobacter pylori* (a bacterium) | stomach cancer (appears to be a major cause) |

**How papillomavirus can lead to cervical cancer:**

- Normally, the virus's proteins keep its own copying under control in the outer cell layers. You get a harmless growth (a wart).
- If the virus's DNA gets stitched into the host chromosome (**integrates**), the viral genes that push cells to divide can escape control.
- Those proteins get made nonstop and drive division in the **basal layer** (the bottom, dividing layer), and the tumor can move toward malignancy.

{{slide:L10-10|Left: controlled replication gives a wart. Right: integrated viral genes drive the basal layer to proliferate.}}

:::hook
HPV is a houseguest. Staying in the guest room (not integrated) = a wart. Moving into the master bedroom (integrated into the chromosome) = taking over the house.
:::

### The genetic basis of cancer

:::key
- Three classes: proto-oncogenes, tumor suppressors, caretakers
- Drivers vs passengers
:::

The short version: hundreds of genes can be involved, sorted into three teams: gas pedals, brakes and mechanics.

**Cancer-critical genes** are genes whose change often helps cause cancer. Finding them is hard because:

- a typical cancer needs a whole set of mutations, and the set differs between patients
- different mutations affect each other in different ways
- most mutations in a tumor are "**passengers**" that don't do anything; you have to tell them apart from the "**drivers**"

:::hook
Passengers ride along, drivers steer. A tumor has a few drivers and lots of passengers.
:::

Several hundred genes are changed again and again in human cancers. They come in three classes:

| Class | Normal job | What goes wrong | Car part |
|---|---|---|---|
| **Proto-oncogenes** | push growth when told to | **gain** of function: too active or too much | gas pedal, stuck down |
| **Tumor suppressor genes** | stop growth, kill damaged cells | **loss** of function | brakes, failed |
| **Caretaker genes** | look after DNA | lost, so the genome becomes unstable | mechanic, gone |

:::hook
**Gas pedal, brakes, mechanic.** When the mechanic is gone, every other part breaks faster.
:::

### Proto-oncogenes and oncogenes

:::key
- Gain-of-function, one copy enough (dominant)
- Four routes: point mutation/deletion, regulatory, amplification, rearrangement
- Amplification and regulatory = too much NORMAL protein; point/fusion = HYPERACTIVE protein
:::

The short version: a normal growth gene (proto-oncogene) becomes a cancer gene (oncogene) when it's made too active or made too much. One bad copy is enough.

A **proto-oncogene** is a normal gene, usually involved in controlling cell division, that a mutation can turn into a cancer-promoting **oncogene**. This is usually a **gain-of-function** change: the protein becomes overactive or there's way too much of it. One mutation in one of the two copies is enough to switch it on (it's **dominant**).

:::hook
"**Proto**" means "first" or "original": the proto-oncogene is the original, normal version. The oncogene is the broken one.
:::

:::exam
Her Q6 gives you three clues and asks what kind of gene it is. The mutant gene is present once, the other copy is normal, and putting the mutant gene into normal cells transforms them. That's an oncogene, for two reasons.

- One bad copy is enough, so the change is dominant (gain of function).
- Adding it to normal cells transforms them. That's the NIH 3T3 transfection test from this lecture, which is how mutant Ras was found.

A tumor suppressor fails both clues: it needs both copies lost, and adding a gene can't remove a brake the cell already has.
:::

Four ways to turn a proto-oncogene into an oncogene (her Fig 20-22):

| # | What happens to the DNA | What protein you get |
|---|---|---|
| 1 | **deletion or point mutation** in the coding part | a **hyperactive** protein, made in normal amounts |
| 2 | **regulatory mutation** (in the gene's on/off switch region) | a **normal** protein, made in huge amounts |
| 3 | **gene amplification** (many extra copies of the gene) | a **normal** protein, made in huge amounts |
| 4 | **chromosome rearrangement** | either a strong switch from elsewhere drives the gene (normal protein, too much) or the gene fuses with another gene (a hyperactive **fusion protein**) |

{{slide:L10-12|Four columns, four mechanisms. The bottom row tells you whether the protein is normal or hyperactive.}}

{{fig:onco_mechanisms}}

:::trap
Gene amplification and regulatory mutation make a normal protein, just too much of it. Point mutation and fusion make an abnormal, hyperactive protein. Ask "too much of a normal thing, or a broken thing?"
:::

:::hook
"**Better engine or more engines.**" Point mutation and fusion = a souped-up engine. Amplification and regulatory mutation = the same engine, many copies.
:::

### Discovering oncogenes through viruses

:::key
- RSV (retrovirus) carries src, a non-receptor tyrosine kinase
- v-src is a stolen, mutated copy of the cell's c-src
:::

The short version: a chicken virus carried a cancer gene that turned out to be a stolen, broken copy of a normal chicken gene.

Viruses cause few human cancers but are big causes in some animals, and studying them is how oncogenes were found.

**Rous sarcoma virus (RSV)** infects chickens and causes sarcomas. It's a **retrovirus**: an RNA virus that copies its RNA backwards into DNA (reverse transcription) and inserts that DNA into the host's chromosomes. RSV carries the usual retrovirus genes (*gag*, *pol*, *env*) plus one extra gene, the **oncogene *src***. Src makes a **non-receptor tyrosine kinase**: a tyrosine kinase that floats in the cytosol and isn't part of a receptor.

Then the surprise: normal cells in chickens and other animals have a very similar gene, **c-src** (c for cellular). It's a proto-oncogene. The virus's version (**v-src**) was accidentally picked up by an ancestor virus from a cell it infected, and then it mutated into an oncogene. Other retroviruses turned out to carry other stolen-and-mutated genes, which pointed researchers to the matching proto-oncogenes in normal cells.

{{slide:L10-14|c-Src and v-Src domain maps: v-Src is missing the tail end that carries Tyr 527.}}

:::hook
**v-src is a stolen and souped-up copy** of the cell's own c-src. The virus is a car thief that modified the engine. "**c = cell's own, v = virus's stolen copy.**"
:::

### The first human oncogene: RasD

:::key
- Tumor DNA into NIH 3T3 → foci → mutant Ras
- Ras mutated in ~30% of cancers
:::

The short version: they put human tumor DNA into mouse cells, looked for the cells that went crazy, and found mutant Ras.

1. Take DNA from human tumor cells.
2. Put it into a mouse cell line (**NIH 3T3**) that doesn't normally form tumors.
3. Grow them for 2 weeks.
4. Some cells form **foci** (clumps of transformed cells growing on top of the normal layer).
5. Trace the DNA in those foci. It carried a mutant Ras.

The mutation is a single-letter change (point mutation) that stops Ras from cutting its GTP. Ras is mutated in about **30% of cancers**.

{{slide:L10-15|Transfect, culture two weeks, look for foci, extract the DNA. That DNA carried a mutant Ras.}}

:::conn
This is the exact RasD (glycine 12) from Lecture 8. Lecture 8 used it as a lab tool to prove Ras is downstream of RTKs; here it's the cause of about a third of human cancers.
:::

### Most oncogenes are in growth-signaling pathways

:::key
- Oncogenes sit at every step of growth signaling
- neu: Val→Gln in TM, dimerizes without ligand; erbB: EGFR missing ligand domain
- -mab = antibody, -nib = kinase inhibitor

*Skim:* Individual drug names: know a couple per class, skim the rest.
:::

The short version: nearly every oncogene is a part of a "grow" pathway.

Her table groups oncogenes by what their protein does:

| Protein type | Examples |
|---|---|
| growth factors | v-sis (PDGF) |
| receptors | erbB (EGF receptor), HER2 |
| membrane GTP-binding proteins | K-ras, H-ras, N-ras |
| non-receptor protein kinases | B-raf, src, Bcr-Abl |
| transcription factors | myc, jun, fos |
| cell cycle / cell death controllers | cyclin D, Cdk4, Bcl-2 |

:::hook
Follow the signal from outside to nucleus: **signal, receptor, switch, kinase, gene switch, cell cycle.** Every stop on the road has an oncogene.
:::

Ways the RTK-Ras-MAPK pathway turns into a cancer pathway:

- RTKs that work with no ligand.
  - The ***neu*** oncogene (from the Her2 receptor) has a single valine → glutamine change in the membrane-crossing part, which makes the receptors pair up without any ligand.
  - The ***erbB*** oncogene is an EGF receptor with its ligand-grabbing part cut off, so it's always on.
- **RasD**, stuck holding GTP.
- Always-on MAPK parts, like B-Raf mutations (common in melanoma).

:::she
"Some anticancer drugs that target the RTK-Ras-MAPK pathway." Her figure: RTK inhibitors (trastuzumab, gefitinib, erlotinib, cetuximab, bevacizumab), B-Raf inhibitors (dabrafenib, vemurafenib), Raf inhibitors (regorafenib, sorafenib), MEK inhibitors (refametinib, selumetinib, trametinib). NF1 (a Ras-GAP) is shown as a natural brake on Ras.
:::

{{slide:L10-18|Each red name is a drug placed at the step it blocks, from the receptor down to MEK.}}

:::hook
Drug name endings tell you what they hit. **-mab = monoclonal antibody** (a big protein that blocks the receptor from outside; "mab" = **m**onoclonal **a**nti**b**ody). **-nib = small molecule kinase inhibitor** (a small drug that gets inside and plugs the kinase; "nib" = i**n**hi**b**itor). Bevacizumab blocks VEGF, which links back to angiogenesis.
:::

### c-Src: an internal off switch removed

:::key
- P-Tyr527 binds Src's own SH2 → inactive; Csk adds it
- Lose Tyr527 → always on (v-Src)
- Phosphorylation INHIBITS here
:::

The short version: normal Src locks itself shut by grabbing its own tail. The virus version has no tail lock, so it's always on.

In normal c-Src, a phosphorylated **tyrosine 527** near the tail folds back and sticks into Src's own SH2 domain. That clamps the kinase into an inactive shape. Another kinase, **Csk**, puts that phosphate on Tyr 527. In v-Src (and cancer mutants), Tyr 527 is deleted or changed, so the clamp can't form and the kinase is always active.

{{slide:L10-19|P-Tyr527 tucked into the SH2 pocket holds the kinase shut. Delete it and the clamp is gone.}}

{{fig:src}}

:::trap
Here phosphorylation inhibits. P-Tyr527 turns Src OFF. Removing the phosphate site turns it ON permanently. Another case where "phosphorylated" doesn't mean "active."
:::

:::hook
Src is a dog that keeps itself calm by **biting its own tail**. Cut off the tail (v-Src) and it runs wild. "**527 = the tail tyrosine; Csk = 'C-Src Kinase' that sets the lock.**"
:::

:::conn
Src uses its own SH2 domain to grab its own phosphotyrosine. That's the Lecture 8 SH2/P-Tyr Velcro used as a self-lock.
:::

### Bcr-Abl: an oncogene made by a chromosome swap

:::key
- 9;22 fusion → always-on kinase → CML
- Second hit (p53/RB) → acute leukemia
- Bcr-Abl phosphorylates JAK2 and STAT5
- Src, Abl, JAK are NON-receptor tyrosine kinases
:::

The short version: the chromosome swap from Lecture 9 glues two genes together, and the combined protein is a kinase that never shuts off.

**Abl** is a kinase that floats in the cytosol (non-receptor). Normal c-Abl helps actin filaments branch and helps cells push out extensions, so its main job is controlling the cell's skeleton and shape. What **bcr** normally does is unknown.

:::easy
Category trap: Src, Abl and JAK are tyrosine kinases that are NOT receptors (non-receptor tyrosine kinases). Only RTKs are receptor and kinase in one protein.
:::

In the 9;22 swap (the Philadelphia chromosome, Lecture 9), the front part of *bcr* (on chromosome 22) gets fused to most of *abl* (on chromosome 9). The result is a **Bcr-Abl fusion protein** that is always active.

- If this happens in a blood-forming cell in the bone marrow, white blood cells multiply: **chronic myelogenous leukemia (CML)**.
- If a Bcr-Abl cell then also loses a tumor suppressor (p53 or RB), it becomes **acute** leukemia.

Bcr-Abl also phosphorylates proteins that normal Abl doesn't touch, including the kinase **JAK2** and the transcription factor **STAT5**. So it hijacks the JAK-STAT pathway (next section).

{{fig:bcrabl}}

:::hook
"**Bcr-Abl: 22 lends its head, 9 lends its body.**" Bcr (chromosome **22**) is the front, Abl (chromosome **9**) is the rest. **Chronic** first, then **acute** after a second hit on a brake.
:::

:::nancy
She writes: "Bcr-Abl chimeric oncoprotein is constitutively active and able to phosphorylate signal transduction molecules that are not normal substrates for c-Abl."

Plain version: Bcr-Abl is a two-part fused protein that's always on, and it tags proteins normal Abl never touches (like JAK2 and STAT5). "Hematopoietic" on the same slide means blood-forming.
:::

### Cytokine receptors and the JAK-STAT pathway

:::key
- Receptor has no kinase; JAK is stuck to it
- JAK → P-Tyr → STAT docks (SH2) → STAT phosphorylated → dimer → nucleus
- Shortest route to genes in the unit

*Skim:* Table 15-6 cytokine list: know Epo → JAK2/STAT5; skim the rest.
:::

The short version: a receptor with no kinase of its own borrows one (JAK). JAK tags STAT, and STAT walks straight into the nucleus. It's the shortest road from membrane to genes in the unit.

**Cytokines** are a family of small signaling molecules that cells release, especially important for blood and immune cells. They include interleukins, lymphokines, tumor necrosis factor and interferons (which trigger inflammation and fight infections).

**Cytokine receptors** have no kinase of their own. Instead, each one is permanently attached to a cytosolic tyrosine kinase called a **JAK** (Janus kinase). JAKs phosphorylate and switch on transcription factors called **STATs** (signal transducers and activators of transcription).

The pathway:

1. The cytokine binds, and two receptors come together.
2. The two JAKs phosphorylate each other (switching on), then phosphorylate tyrosines on the receptor tails.
3. STAT proteins land on those phosphotyrosines using their **SH2 domains**.
4. JAK phosphorylates the STATs.
5. The phosphorylated STATs let go, pair up (each STAT's SH2 grabs the other's phosphotyrosine), move into the nucleus and switch on genes.

{{slide:L10-23|Follow the phosphates: JAKs on receptor tails, STATs docking with SH2, STAT dimers into the nucleus.}}

{{fig:jakstat}}

{{lab:jak|JAK-STAT and Bcr-Abl (CML, Gleevec, the skier)}}

:::hook
**JAK is "Janus,"** the Roman god with two faces: one face on the receptor, one on STAT. **STAT** is also the doctor word for "right now": it's the fastest road to the nucleus.
:::

:::exam
Her Q19 asks which statement about cytokine receptors is incorrect. The false one is "the intracellular domain has a tyrosine kinase domain." That's the whole point of cytokine receptors: they have no kinase of their own and borrow JAK. The true options are that they bind JAK tightly, the Epo receptor is one, they bind interleukins, and they end in transcription factors (STATs).
:::

| | RTK (L8) | Cytokine receptor + JAK (L10) |
|---|---|---|
| Kinase | built into the receptor | a separate protein (JAK) stuck to it |
| Docks on P-Tyr with SH2 | GRB2 | STAT |
| Road to nucleus | Ras → Raf → MEK → ERK (long) | STAT goes straight in (short) |

:::conn
JAK-STAT is like an RTK split in two: the receptor does the grabbing, JAK does the kinase work. And the STAT road is the shortest route from membrane to genes in the whole unit: no second messenger, no kinase relay.
:::

Examples from her Table 15-6:

| Cytokine | JAK(s) | STAT(s) | What it does |
|---|---|---|---|
| interferon-γ | JAK1, JAK2 | STAT1 | activates macrophages |
| interferon-α | Tyk2, JAK1 | STAT1, STAT2 | resistance to viruses |
| erythropoietin (Epo) | JAK2 | STAT5 | makes red blood cells |
| prolactin | JAK1, JAK2 | STAT5 | milk production |
| growth hormone | JAK2 | STAT1, STAT5 | growth (via IGF-1) |
| GM-CSF | JAK2 | STAT5 | makes granulocytes and macrophages |

:::hook
**JAK2 and STAT5 are the workhorses**: they show up for Epo, prolactin, GM-CSF and (with STAT1) growth hormone. And they're exactly what Bcr-Abl hijacks.
:::

:::nancy
She writes: "Cytokines are stably associated with the cytoplasmic tyrosine kinases called Janus Kinases (JAKs)."

Plain version: she means the cytokine RECEPTORS are stuck to JAKs. The cytokine is the signal outside the cell; the JAK is attached to the receptor's tail inside.
:::

#### Erythropoietin

:::key
- Epo (kidney) keeps red-cell precursors alive; no EpoR = pale embryo
- The skier: truncated, always-on EpoR → more red cells, not cancer

*Skim:* Medal counts: fun, low priority.
:::

The short version: Epo is the kidney's "make more red blood cells" signal. Without it, red cell precursors die.

**Erythropoietin (Epo)** is a cytokine made by the kidney. It tells red-blood-cell precursors in the bone marrow (called **CFU-E**) to survive and become red blood cells. Without Epo, those precursors die by apoptosis. Her photos: a mouse embryo lacking the Epo receptor (-/-) is pale with no red blood cells; the normal one (+/+) is red.

{{slide:L10-22|Epo receptor knockout (-/-) embryo is pale: no red blood cells without Epo signaling.}}

:::she
Human Perspective: Finnish cross-country skier Eero Mäntyranta won 7 Olympic medals (3 gold) between 1960 and 1972. He had an inherited dominant mutation that truncated his Epo receptor. The shortened receptor was constitutively active, so he made more red blood cells and carried more oxygen. A natural "gain-of-function" that helped instead of causing cancer.
:::

:::hook
"**Epo = Erythro (red) + poietin (making).**" The skier had a natural, legal version of blood doping: a shortened receptor that never shut off. **7 medals, 3 gold.**
:::

### Gleevec

:::key
- Imatinib sits in Bcr-Abl's ATP pocket
- First drug aimed at a signaling protein unique to tumor cells (2001)
- Targets the protein; cells still have the Philadelphia chromosome
:::

The short version: a drug that plugs the ATP slot of Bcr-Abl so it can't tag anything.

**Gleevec (imatinib)** blocks Bcr-Abl. It sits in the **ATP-binding pocket** of the Bcr-Abl kinase, so the kinase can't use ATP to phosphorylate its targets (like JAK2 and STAT5), and the tumor cells can't multiply. Approved in **2001**, it was the first cancer drug designed to target a signaling protein found only in tumor cells.

{{slide:L10-24|Imatinib sits in the kinase pocket, so substrates like JAK2 and STAT5 never get phosphorylated.}}

:::hook
Gleevec is a wad of gum stuck in Bcr-Abl's ATP slot. No ATP fits, no phosphates get passed on, no leukemia signal. Its real name ends in **-nib**: ima**tinib**, a kinase inhibitor.
:::

:::trap
Gleevec targets the protein (the enzyme), not the gene or the chromosome swap. Cells still carry the Philadelphia chromosome; the fusion protein just can't work.
:::

### How to figure it out: classify the carcinogen {#howto-carcinogen}

How to spot it: a question describes an agent with test results (Ames positive or negative, animal tumors yes or no, needs liver extract or not) and asks what category it is.

Steps:

1. Ames positive? It's a mutagen.
2. Causes tumors in animals or more cancer in people? It's a carcinogen.
3. **Both yes** → genotoxic carcinogen. Then: did the Ames test only turn positive with liver extract (called **S9**)? If yes, it's an **indirect** genotoxic carcinogen (P450-activated). If not, it's direct.
4. **Ames negative but causes cancer** → **non-genotoxic carcinogen**. Then find the mechanism: inflammation (asbestos) or copying a growth signal (phorbol esters).
5. **Ames positive but no cancer in animals** → mutagen, not carcinogen (repaired in mammals, or can't get into animal cells).

:::hook
Two yes/no questions decide it: "**Does it mutate? Does it cause cancer?**" Then one bonus: "**Did it need the liver?**"
:::

Practice:

- Chemical X: Ames negative without liver extract, strongly positive with it; liver tumors in rats. Indirect genotoxic carcinogen, like aflatoxin.
- Chemical Y: Ames negative either way; mice painted with it after a single low dose of a mutagen get many skin tumors. Non-genotoxic promoter, like TPA.
- Chemical Z: Ames strongly positive; no tumors in mice at any dose. Mutagen, not carcinogen.
- Fiber W: Ames negative; exposed workers get mesothelioma decades later. Non-genotoxic carcinogen through constant inflammation, like asbestos.

### How to figure it out: oncogene or tumor suppressor? {#howto-onco}

How to spot it: a question describes a mutation and its effect, or gives data about one copy versus two copies.

1. Does the mutation make a protein **more active or more abundant**? Gain of function → **oncogene**. One mutant copy is enough (dominant at the cell level).
2. Does it **destroy** a protein that normally stops division, kills damaged cells, or repairs DNA? Loss of function → **tumor suppressor** or caretaker. Usually both copies have to be lost.
3. Is the protein a growth-signal part (RTK, Ras, Raf, Src, Abl, JAK, Myc)? Its cancer version is almost always gain-of-function.
4. Is it p53, RB, APC, a DNA repair enzyme, or a GAP like NF1? Its cancer version is loss-of-function.

:::hook
"**Gas pedals get stuck (one copy). Brakes get cut (both copies).**"
:::

:::easy
Both-boxes trap: NF1 is a Ras-GAP and a tumor suppressor. Its loss switches on an oncogene pathway, but NF1 itself is never the oncogene.
:::

Practice:

- HER2 gene amplified in breast cancer → too much normal receptor → oncogene.
- Both copies of APC lost in colon cells → tumor suppressor.
- A Ras-GAP (NF1) deleted → Ras stays on → NF1 is a tumor suppressor, even though its loss switches on an oncogene pathway.
- VHL lost → HIF never destroyed → VHL is a tumor suppressor.
- The skier's shortened Epo receptor → always active → gain-of-function (acts like an oncogenic mutation, though it caused extra red cells, not cancer).

### Reading her questions on this lecture {#read-l10}

| If the question says... | She's testing... | How you'd get tricked |
|---|---|---|
| "Ames positive" | Mutagen (not proof of carcinogen) | Equating mutagen with carcinogen |
| "needs liver extract" | Indirect genotoxic carcinogen (P450) | Calling it non-genotoxic |
| "Ames negative, causes tumors" | Non-genotoxic (asbestos, TPA) | Saying it can't be a carcinogen |
| "phorbol ester" | Mimics DAG, PKC always on | Forgetting the Lecture 5 link |
| "v-src vs c-src" | Viral copy is a stolen, mutated cellular gene | Thinking the virus invented it |
| "amplification" | Too much normal protein | Calling the protein abnormal |
| "Tyr 527" | Phosphorylation turns Src OFF | Assuming phosphorylated = active |
| "Gleevec" | Blocks the ATP pocket of Bcr-Abl | Saying it removes the translocation |
| "cytokine receptor kinase" | JAK, a separate protein | Saying the receptor has its own kinase |

### Lecture 10 on one page

| Idea | Plain English | Remember it by |
|---|---|---|
| Mutagen vs carcinogen | changes DNA vs causes cancer; overlap = genotoxic | two circles |
| Radiation | breaks DNA; flies, bomb survivors, UV | flies, bombs, sun |
| Ames test | his- Salmonella, count revertants, rat liver extract | asks microbes about errors |
| P450 | liver detox that arms aflatoxin and benzo[a]pyrene | epoxides grab guanine |
| Non-genotoxic | asbestos (inflammation), TPA (fake DAG) | splinter, fake DAG |
| Viruses | HPV, hep B/C, EBV, HHV-8, HTLV-1, H. pylori | guest room vs master bedroom |
| Three gene classes | proto-oncogene, tumor suppressor, caretaker | gas, brakes, mechanic |
| Four routes to oncogene | point/deletion, regulatory, amplification, rearrangement | better engine or more engines |
| src | v-src stolen from c-src by RSV | car thief |
| RasD | first human oncogene, NIH 3T3 foci, 30% | stuck at noon |
| Pathway oncogenes | neu, erbB, RasD, B-Raf; -mab vs -nib drugs | every stop has an oncogene |
| c-Src lock | P-Tyr527 in own SH2; Csk sets it | dog biting its tail |
| Bcr-Abl | 22 head + 9 body, always on, CML | then acute after a second hit |
| JAK-STAT | borrowed kinase, STAT straight to nucleus | Janus, STAT = right now |
| Epo | kidney signal, CFU-E survive; the skier | natural blood doping |
| Gleevec | plugs ATP pocket of Bcr-Abl, 2001 | gum in the slot |
