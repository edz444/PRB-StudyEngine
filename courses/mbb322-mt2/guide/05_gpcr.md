## Lecture 5: G protein coupled receptors {#l5}

Textbook pages 892-910. This is the biggest lecture in the unit, and every later lecture borrows parts from it.

:::story
Chapter 1 of the story. A cell is wrapped in a greasy membrane that most messages can't cross. So how does a hormone floating outside tell the inside of the cell to do something? This chapter builds the answer: a doorbell on the outside (the receptor), a switch that flips when the bell rings (the G protein), and small messengers inside that run around spreading the news (cAMP, IP3, Ca2+). Every later chapter reuses at least one of these parts.

What you need from before: Chapter 0 (membranes, proteins, phosphorylation, what a kinase is). Lecture 4 already mentioned GPCRs, GEFs and GAPs; this chapter goes deep on them.
:::

### The big picture in one paragraph

Think of a house with no mail slot. The mail carrier (a hormone) can't get in, so she rings the doorbell (the receptor). The doorbell is wired to a light switch inside (the G protein). When the switch flips on, it starts a chain of people inside shouting the news to each other (second messengers and kinases), and by the end the whole house is doing something: burning sugar, beating faster, seeing light. The whole lecture is just different versions of this house. What changes is which switch, which shouting chain, and what the house ends up doing.

:::hook
The chain to memorize for the whole lecture is **R-G-E-M-K**: Receptor, G protein, Effector, Messenger, Kinase. "Real Good Effort Makes Kings." Almost every pathway in L5 fits this order.
:::

### What a GPCR is

:::key
- 7 passes; N-terminus outside, C-terminus inside
- Ligand binds outside, G protein binds the inside loops
- One ligand can hit different GPCRs in different tissues with opposite effects (epinephrine: β raises cAMP, α2 lowers it)

*Skim:* Over 700 GPCRs in humans and the list of ligand types: know they exist, don't memorize the list.
:::

The short version: a GPCR is the doorbell. It sits in the membrane, the signal touches the outside part, and the inside part grabs the switch.

A **G protein coupled receptor (GPCR)** is one long protein that weaves in and out of the membrane seven times, like a thread stitched through fabric seven times. Its start (the N-terminus) is outside the cell and its end (the C-terminus) is inside. Because it crosses seven times, people also call it a "seven-pass" or "7TM" (seven transmembrane) receptor. The signal binds on the outside face. The G protein grabs the loops on the inside face.

:::hook
"7 stitches, N out, C in." Picture sewing: you start the needle outside (N), stitch 7 times, and end inside (C).
:::

Some facts she lists about them:

- GPCRs are in all eukaryotes (cells with a nucleus: animals, plants, fungi). Humans have more than 700 of them.
- They run sight, smell and taste (every taste except sour).
- The signals that bind them (called **ligands**, which just means "anything that binds a receptor") are a huge mix: proteins, peptides (short chains of amino acids), amino acid relatives like epinephrine, fatty acids, smell molecules, and even particles of light (photons).

One signal can fit many different GPCRs. Those receptors usually sit in different tissues and cause different results. Epinephrine (adrenaline) binds β-adrenergic receptors in the liver and heart, which raise cAMP, and α2-adrenergic receptors elsewhere, which lower cAMP. Same key, different locks, opposite results.

:::conn
This is the first time you see the unit's biggest idea: what a signal does depends on which receptor and which cell it lands on, not on the signal itself. A doorbell that rings in a bakery and a doorbell that rings in a fire station get very different responses.
:::

### The trimeric G protein: the switch

:::key
- Gα holds GDP (off) or GTP (on); Gβγ is a stuck-together pair
- The receptor is a GEF: it makes Gα drop GDP so GTP can jump in
- GTP-bound Gα and Gβγ split, and EITHER can activate an effector
- Gα turns itself off by hydrolyzing GTP (built-in timer)

*Skim:* 21 Gα / 6 Gβ / 12 Gγ counts: recognize, low priority.
:::

The short version: the G protein is a light switch made of three pieces. GTP means ON, GDP means OFF. The receptor flips it on; the switch flips itself off after a while.

The G protein is **heterotrimeric**, which just means "three different pieces" (hetero = different, trimer = three parts). The pieces are Gα, Gβ and Gγ.

- **Gα** is the important one. It holds a small molecule that is either **GDP** (OFF) or **GTP** (ON).
- **Gβ and Gγ** always stay stuck together as a pair, called **Gβγ** ("G beta-gamma").
- Gα and Gγ each have a fatty tail that anchors them to the inside face of the membrane, so the whole switch stays parked right under the receptor.

How the switch works, step by step (her six-step cycle):

1. Resting. Gα holds GDP and is stuck to Gβγ. Everything is OFF.
2. Doorbell rings. A ligand binds the GPCR on the outside, and the receptor changes shape.
3. Receptor pries the switch open. The changed receptor grabs the G protein and makes Gα let go of its GDP. A protein that does this "swap help" is called a **GEF** (guanine nucleotide exchange factor). So the receptor is acting as a GEF.
4. GTP jumps in. The cytosol has far more GTP than GDP floating around, so GTP drops into the empty pocket almost at once.
5. The switch splits. With GTP inside, Gα changes shape and lets go of Gβγ and the receptor. Now Gα-GTP and Gβγ are both free and both active. Either one can go switch on an **effector** (the protein that actually does a job, like an enzyme or an ion channel).
6. Built-in timer turns it off. Gα slowly cuts its own GTP into GDP + Pi (this cutting with water is called **hydrolysis**, and an enzyme that does it to GTP is a **GTPase**). Gα-GDP lets go of the effector and rejoins Gβγ. Back to OFF.

{{fig:gcycle}}

{{3d:gp|Step through ligand binding, the GDP-to-GTP swap and the split, then switch on cholera toxin and watch it never turn off.}}

:::hook
**GDP = Gone Dead Phase. GTP = Go Time Protein.** And notice the receptor never "gives" energy to the G protein. It just opens the door so GTP can walk in. The receptor is a doorman, not a battery.
:::

:::hook
Think of Gα as a toaster. Pushing the lever down (GTP in) turns it on. A timer inside pops it back up (GTP cut to GDP) without anyone touching it. Cholera toxin, later in this lecture, is like gluing the lever down.
:::

There are many versions of each piece: 21 different Gα subunits (made from 16 genes), 6 Gβ and 12 Gγ. Mixing and matching them gives many different G proteins, each wired to a different effector. That is how one simple switch design can control so many different things.

{{slide:L5-4|Her six-step cycle: watch Gα drop GDP, pick up GTP, leave to hit the effector, then hydrolyze and rejoin Gβγ.}}

:::nancy
She writes: "Ligand binding to GPCR induces a conformational change which in turn alters the conformation of the trimeric G protein. Alteration of the α-subunit of the G protein allows it to exchange GDP for GTP."

Plain version: the receptor changes shape, that bends the G protein, and the bend lets Gα drop GDP and pick up GTP. "Conformation" just means shape. "Heterotrimeric" just means three different pieces.
:::

#### The main kinds of Gα (her Table 15-1)

:::key
- Gαs raises cAMP, Gαi lowers it, Gαq activates PLC (IP3 + DAG)
- Gαt (transducin) is the odd one: it LOWERS cGMP via PDE
- Three effector families: adenylyl cyclase, PLC, ion channels

*Skim:* Every example receptor in the table: learn β-adrenergic, α2, muscarinic, odorant and rhodopsin; skim the rest.
:::

Each kind of Gα is wired to a different effector. The letters are worth learning because she uses them in questions.

| Gα class | What it switches on (effector) | What happens to the messenger | Example receptors |
|---|---|---|---|
| Gαs (s = stimulatory) | adenylyl cyclase | cAMP goes up | β-adrenergic (epinephrine), glucagon, serotonin, vasopressin |
| Gαi (i = inhibitory) | adenylyl cyclase (turns it down); K+ channel (via Gβγ) | cAMP goes down; membrane voltage changes | α2-adrenergic, muscarinic acetylcholine |
| Gαolf (olf = olfactory, smell) | adenylyl cyclase | cAMP goes up | odorant receptors in the nose |
| Gαq | phospholipase C | IP3 and DAG go up | α1-adrenergic |
| Gαo | phospholipase C | IP3 and DAG go up | acetylcholine receptor in endothelial cells |
| Gαt (t = transducin) | cGMP phosphodiesterase | cGMP goes DOWN | rhodopsin in rod cells |

:::hook
**s = Speeds up cAMP, i = Inhibits cAMP, q = "Quick calcium" (PLC, IP3, Ca2+), t = Transducin for sighT, olf = Olfaction (smell).** The odd one out is t: it's the only one where the messenger goes down.
:::

The effectors in this lecture come in three families, and the rest of the chapter takes them one at a time:

- Branch 1: adenylyl cyclase (makes cAMP)
- Branch 2: phospholipase C (makes IP3 and DAG, which release Ca2+)
- Branch 3: ion channels (change the cell's voltage)

### Branch 1: adenylyl cyclase and cAMP

:::key
- Adenylyl cyclase: ATP → cAMP (+ pyrophosphate)
- PDE destroys cAMP → 5'-AMP (the eraser)
- Gαs = gas pedal, Gαi = brake on the same cyclase; the cell sums them
:::

The short version: adenylyl cyclase is a factory that turns ATP into cAMP. cAMP is the "shout" inside the cell, and an enzyme called PDE erases it.

**Adenylyl cyclase** is a big enzyme in the membrane. It takes ATP and turns it into **cyclic AMP (cAMP)**. In chemistry terms, it snips off two phosphates (as a piece called pyrophosphate, PPi) and bends the last phosphate back onto the sugar to close a ring. That ring is why it's called "cyclic." The reaction keeps going forward because another enzyme immediately breaks up the pyrophosphate, so it can't go backwards.

cAMP is a **second messenger**. The hormone outside is the first messenger. cAMP carries the news around inside, so it's the second. It doesn't last long: an enzyme called **cAMP phosphodiesterase (PDE)** opens the ring and turns cAMP into plain 5'-AMP, which does nothing.

:::hook
cAMP is chalk on a board. Adenylyl cyclase writes it, PDE is the eraser. The message only stays as long as someone keeps writing faster than the eraser wipes.
:::

The same adenylyl cyclase can be pushed up or pulled down, like a gas pedal and a brake on one car:

- Gas pedal: "stimulatory" hormones (epinephrine at β-receptors, glucagon, ACTH) bind receptors linked to **Gαs**, which turns the cyclase ON.
- Brake: "inhibitory" hormones (PGE1, adenosine) bind receptors linked to **Gαi**, which turns the cyclase DOWN.
- The cell adds up both at once. The final cAMP level is the result.

{{slide:L5-8|Left side Gαs pushes the cyclase on, right side Gαi pulls it down; the table below lists what each tissue does with the extra cAMP.}}

{{fig:camp_cascade}}

{{lab:camp|Gs / cAMP (cholera, PDE inhibitor, beta-blocker)}}

#### Same cAMP, different jobs in different tissues

:::key
- Same cAMP, different response, because PKA finds different targets in each cell

*Skim:* The full tissue table: know heart (faster), liver/muscle (glycogen breakdown), kidney (water). Skim the rest.
:::

Her table shows that a rise in cAMP does something different in every tissue:

| Tissue | Hormone that raises cAMP | What the cell does |
|---|---|---|
| Thyroid | TSH | makes thyroid hormone |
| Adrenal cortex | ACTH | makes cortisol |
| Ovary | LH | makes progesterone |
| Muscle, liver | adrenaline, glucagon | breaks down glycogen (stored sugar) |
| Bone | parathormone | breaks down (resorbs) bone |
| Heart | adrenaline | beats faster and harder |
| Kidney | vasopressin | takes water back into the blood |
| Fat | (hormone not named on her slide) | breaks down fat (triglycerides) |

:::conn
The cAMP molecule is identical in every one of these cells. What differs is which proteins PKA finds to phosphorylate in that cell. Think of cAMP as a fire alarm: the alarm sounds the same in a school and a hospital, but each building has its own drill. This is the "same signal, different response" thread.
:::

#### Drugs that copy or block hormones

:::key
- Agonist = mimics and turns ON (often tighter, lower Kd)
- Antagonist = sits in the site and BLOCKS
- Isoproterenol: agonist, opens airways (asthma). Alprenolol: beta-blocker antagonist, slows heart
:::

The short version: an agonist is a fake key that turns the lock. An antagonist is a fake key that jams it.

- An **agonist** binds the receptor and turns it ON, copying the real hormone. Agonists often grip tighter than the real hormone. Grip strength is measured by **Kd** (the dissociation constant); a lower Kd means a tighter grip. Example: **isoproterenol (IP)** binds β-adrenergic receptors on the airway muscle more tightly than epinephrine does, and it makes that muscle relax, opening the airways. It treats asthma and chronic bronchitis.
- An **antagonist** binds the receptor and just sits there, so the real hormone can't get in and nothing happens. Example: **alprenolol (AP)** blocks β-adrenergic receptors on heart muscle, which normally speed up the heart. Drugs like this are called **beta-blockers**. They slow the heart and treat some irregular heartbeats (arrhythmias).

:::hook
**Agonist = "Agrees"** with the hormone and does its job. **Antagonist = the "Anti" guy** blocking the door. And Kd works like golf: the lower the score, the better (tighter) the binding.
:::

:::nancy
She writes the drugs as letters: IP (isoproterenol), AP (alprenolol), EP (epinephrine), and says the agonist has a "lower Kd than EP."

Plain version: Kd is grip strength, and lower Kd means a tighter grip, like a lower golf score being better. So isoproterenol grips the receptor harder than epinephrine does.
:::

#### Protein kinase A (PKA)

:::key
- cAMP binds the R subunits, which release active C subunits
- Binding is cooperative (2nd cAMP binds more easily) → sharp switch
- PKA is a Ser/Thr kinase
:::

The short version: PKA is the worker that cAMP wakes up. It's kept asleep by a pair of "babysitter" pieces, and cAMP takes the babysitters away.

cAMP's main job is to switch on **protein kinase A (PKA)**. A kinase is an enzyme that sticks phosphate groups onto other proteins, and PKA puts them on the amino acids serine and threonine (so it's called a Ser/Thr kinase).

Asleep, PKA is a four-piece block: two **regulatory (R)** pieces sitting on two **catalytic (C)** pieces. "Catalytic" means "the part that does the work." Each R piece has two spots where cAMP can bind. When cAMP fills those spots, the R pieces change shape and let go, and the freed C pieces go phosphorylate their targets.

cAMP binding is **cooperative**. That means once the first cAMP binds, the second one binds more easily (its Kd drops). It's like a jar lid: the first turn is hard, then it spins off. Cooperativity makes PKA act like a sharp on/off switch instead of a slow dimmer, so a small rise in cAMP flips PKA from mostly off to mostly on.

{{slide:L5-13|Follow the free C subunit of PKA through the nuclear pore to phosphorylate CREB at a CRE.}}

:::hook
PKA's R pieces are a parking brake. cAMP releases the brake and the C pieces drive away. **R = Restrains, C = Catalyzes.**
:::

:::nancy
She writes: "binding of the first cAMP molecule lowers the Kd for binding of the second cAMP."

Plain version: once one cAMP is on, the second one sticks more easily. That's all "cooperative" means.
:::

#### Glycogen: one hormone, two opposite moves that point the same way

:::key
- PKA turns glycogen synthase OFF and phosphorylase kinase ON
- Phosphorylation can inhibit; always check which enzyme
- Chain: PKA → phosphorylase kinase → phosphorylase → glycogen breakdown
:::

The short version: in a fight-or-flight moment, epinephrine makes the liver stop saving sugar and start spending it, using one kinase to do both.

**Glycogen** is how liver and muscle store glucose: long branched chains of glucose, like a pantry. When you need fuel fast, epinephrine starts this chain:

epinephrine → β-adrenergic GPCR → Gαs → adenylyl cyclase → cAMP → PKA

PKA then does two things at once:

1. It phosphorylates **glycogen synthase** (the enzyme that builds glycogen), and that turns it **OFF**. Building stops.
2. It phosphorylates **glycogen phosphorylase kinase**, and that turns it **ON**. That kinase then phosphorylates and turns on **glycogen phosphorylase**, which chops glucose units off glycogen. Breakdown starts.

So the cell stops filling the pantry and starts emptying it, both from one signal. Two moves, one goal: more sugar now.

:::hook
"**S**ynthase gets **S**topped, **P**hosphorylase gets **P**owered." Same phosphate tag, opposite effects.
:::

:::trap
Phosphorylation does not always mean "activate." PKA's phosphate turns glycogen synthase OFF and turns phosphorylase kinase ON. Always check which enzyme is getting the phosphate before you decide what happens.
:::

:::nancy
Her sentence chains three enzymes with almost the same name: "phosphorylating and activating the enzyme glycogen phosphorylase kinase which then phosphorylates and activates glycogen phosphorylase which then degrades glycogen."

Plain version: PKA → phosphorylase KINASE → phosphorylase → glycogen chopped up. Write it as an arrow chain and the sentence stops being confusing.
:::

#### Signal amplification

:::key
- Each step activates many of the next, so 1 hormone → 10^8 glucose-1-phosphate

*Skim:* Exact numbers at each step: know start (1) and end (10^8), skim the middle.
:::

The short version: each step turns on many copies of the next, so a tiny bit of hormone moves a mountain of sugar.

Each active molecule switches on many of the next, like a phone tree where every person calls ten more. Her numbers:

1 epinephrine → 100 active G proteins and adenylyl cyclases → 10,000 cAMP → 10,000 active PKA → 100,000 active phosphorylase kinase → 1,000,000 active glycogen phosphorylase → 100,000,000 glucose-1-phosphate

That's how a few hormone molecules in your blood free up a huge amount of sugar in seconds.

:::hook
Count the zeros: **1, 100, 10^4, 10^4, 10^5, 10^6, 10^8.** The only step that doesn't grow is cAMP to PKA (10,000 stays 10,000), because each cAMP just releases a PKA, it doesn't make more.
:::

{{slide:L5-12|Read the right-hand column: the count multiplies at almost every step, from 1 hormone to 10^8 glucose-1-phosphate.}}

#### cAMP can also turn on genes

:::key
- PKA C enters the nucleus, phosphorylates CREB
- CREB + CBP bind the CRE and turn on genes (slow effect)
:::

The short version: some PKA walks into the nucleus and flips on genes, so cAMP has a fast effect (seconds) and a slow effect (hours).

Some freed PKA C pieces travel through the nuclear pores into the nucleus. There they phosphorylate **CREB** (cAMP response element binding protein), a **transcription factor** (a protein that switches genes on). Phosphorylated CREB teams up with a partner called **CBP** (CREB-binding protein) and switches on genes that have a **CRE** (cAMP response element) in front of them. The CRE is a short stretch of DNA that works like a landing pad for CREB.

| Fast effect | Slow effect |
|---|---|
| PKA phosphorylates enzymes already in the cytosol | PKA phosphorylates CREB in the nucleus |
| seconds | minutes to hours |
| example: glycogen breakdown | example: new proteins made from CRE genes |

:::hook
CREB lands on the CRE: "CREB on the CRE, CBP comes to see."
:::

### Turning the cAMP signal off

:::key
- Three off switches: hormone lets go, Gα hydrolyzes GTP, PDE destroys cAMP
- Cholera toxin ADP-ribosylates Gαs → can't hydrolyze GTP → stuck ON → diarrhea
- 'Can't hydrolyze GTP' or 'can't be down regulated' = signal stays on
:::

:::she
"What would happen if trimeric G proteins could not be down regulated?" and "Consequence?" next to cholera toxin. She also put the three off switches on their own slide.
:::

The short version: there are three off switches. The hormone falls off, the G protein times out, and PDE erases the cAMP.

1. The hormone falls off. When Gα has GTP bound, the receptor's grip on the hormone gets weaker (its affinity drops), so the hormone lets go.
2. The G protein times out. Gα-GTP cuts its own GTP quickly, so adenylyl cyclase stops.
3. The messenger gets erased. cAMP phosphodiesterase (PDE) breaks cAMP down to 5'-AMP.

:::hook
Three off switches = **"Let go, Time out, Wipe out."** Receptor lets go of hormone, G protein times out, PDE wipes out cAMP.
:::

**Cholera toxin** shows what happens when off-switch number 2 breaks. The toxin is an enzyme made by the cholera bacterium. It takes a chemical group called ADP-ribose from NAD+ and sticks it onto Gαs (this is called **ADP-ribosylation**). Gαs with that tag on it can't cut its GTP anymore, so it's stuck ON forever. In your intestine cells, adenylyl cyclase runs nonstop and cAMP stays high. The cells pump chloride and water into the gut. The consequence: huge amounts of watery diarrhea and dangerous dehydration.

:::hook
Cholera "glues the gas pedal down." Gαs can't let go of GTP, so cAMP floods the gut cell and water pours out.
:::

:::trap
Cholera toxin doesn't add more hormone or more receptors. It breaks Gα's built-in timer. Any time a question says a G protein "can't hydrolyze GTP," the answer is "signal stays on."
:::

:::nancy
She asks "What would happen if trimeric G proteins could not be down regulated?" and writes "Change in affinity of hormone for receptor when Gα is in GTP bound form."

Plain version: "could not be down regulated" means the G protein can't switch off, so the answer is always "the signal stays on." "Change in affinity" means the receptor's grip on the hormone gets weaker, so the hormone falls off. Her "Consequence?" next to cholera toxin is asking you to finish the chain: Gαs stuck on, cAMP high, water pours into the gut.
:::

### Branch 2: phospholipase C, IP3, DAG and calcium

:::key
- Gαq → PLC-β (the effector enzyme) cuts PIP2
- IP3 (water-soluble) → opens ER Ca2+ channels
- DAG (lipid) stays in membrane → with Ca2+ activates PKC
- PIP2 comes from PI → PI4P → PIP2 (two kinases)

*Skim:* Fura-2 dye details: just know it shows Ca2+ rising.
:::

:::she
"What is PIP2 and where does it come from??" and "What do IP3 and DAG do??"
:::

The short version: phospholipase C cuts a membrane lipid in half. The water-loving half floats off and releases calcium. The fatty half stays in the membrane and switches on PKC.

**Where PIP2 comes from.** **PIP2** (full name phosphatidylinositol 4,5-bisphosphate) is a lipid in the inside layer of the plasma membrane. It starts life as **phosphatidylinositol (PI)**, a lipid whose head is a six-sided ring called inositol. Two kinases add phosphates to that ring, both using ATP:

PI → (PI kinase adds a phosphate at spot 4) → PI4P → (PIP kinase adds one at spot 5) → PI(4,5)P2 = **PIP2**

:::hook
Count the P's: PI has 0 extra phosphates, PI4P has 1, PIP2 has 2, and the IP3 cut from it has 3. "**0, 1, 2, 3**: each kinase adds one, PLC cuts the head off with three."
:::

**The cut.** Some GPCRs are wired to **Gαq**, and Gαq switches on the effector **phospholipase C-β (PLC-β)**. PLC-β is the effector enzyme here. It cuts PIP2 into two pieces, and both pieces are second messengers:

{{slide:L5-18|Find the two products: IP3 floats off to the ER Ca2+ channel, DAG stays in the membrane next to PKC.}}

| Piece | What it is | Where it goes | What it does |
|---|---|---|---|
| **IP3** (inositol 1,4,5-trisphosphate) | the water-soluble head | floats into the cytosol | opens **IP3-gated Ca2+ channels** on the ER (endoplasmic reticulum, the cell's calcium storage tank), so Ca2+ floods out |
| **DAG** (diacylglycerol) | the fatty tail | stays in the membrane | together with Ca2+, pulls **protein kinase C (PKC)** to the membrane and switches it on. In liver, PKC phosphorylates and turns off glycogen synthase. |

{{fig:plc_pathway}}

{{lab:plc|Gq / PLC / Ca2+ (TPA, IP3 phosphatase)}}

:::hook
PLC "cuts the PIP2 sandwich." The head (IP3) swims away to open the calcium vault. The tail (DAG) stays home in the membrane to wake up PKC. **"IP3 goes, DAG stays."**
:::

You can watch calcium rise with a dye called **fura-2**, which glows differently when it binds Ca2+. In her picture, a resting adrenal cell looks yellow (low Ca2+). After the hormone angiotensin activates a GPCR → PLC-β → IP3, the cell turns green and blue (high Ca2+).

:::easy
Both-boxes trap: PLC-β is an enzyme (the effector), so it is NOT a second messenger. IP3 and DAG are the second messengers, and only IP3 dissolves in water. DAG stays in the membrane. MT1 already tested the DAG half of this.
:::

{{slide:L5-19|Yellow means low Ca2+, green and blue mean high. Same cell before and after angiotensin.}}

#### What calcium does

:::key
- Ca2+ works mostly through calmodulin (4 Ca2+ sites)
- Ca2+/CaM activates CaM-kinase II, myosin light chain kinase, and PDE (so Ca2+ can lower cAMP)
- CaM-kinase II stays 50-80% active after Ca2+ leaves (memory)

*Skim:* Table 15-3 tissue list: skim.
:::

The short version: calcium is a general alarm, and calmodulin is the receiver that turns the alarm into action.

A rise in Ca2+ in the cytosol does different things in different tissues (her Table 15-3):

- pancreas: releases digestive enzymes
- salivary gland: releases amylase
- smooth muscle: contracts
- liver: breaks down glycogen
- platelets: clump together (aggregation)
- mast cells: release histamine
- fibroblasts: copy DNA

Most of these go through **calmodulin** ("calcium-modulated protein"), a small dumbbell-shaped protein with four Ca2+ spots. When all four fill, calmodulin changes shape and wraps around target proteins to switch them on. Ca2+/calmodulin switches on:

- some transcription factors
- kinases, such as myosin light chain kinase (for muscle) and **CaM-kinase II**
- phosphatases, and other enzymes such as cAMP phosphodiesterase (so calcium can turn the cAMP branch down; the branches talk to each other)

:::hook
Calmodulin is a hand with four fingers. Fill all four fingers with calcium and the hand closes around its target.
:::

**CaM-kinase II remembers.** It's a ring of 12 kinase pieces. Ca2+/calmodulin switches some on, and an active piece phosphorylates the piece next to it (**autophosphorylation**, "phosphorylating itself"). Once a piece has that phosphate, it stays 50-80% active even after the calcium and calmodulin are gone. So the ring keeps a memory of past calcium spikes, a bit like a doorbell that keeps faintly ringing after you let go.

{{slide:L5-22|The 12-subunit ring: once neighbors phosphorylate each other, the ring stays 50-80% active with no Ca2+ around.}}

:::nancy
Her calmodulin slide lists "activation of phosphatases (e.g. cAMP phosphodiesterase)."

Plain version: strictly, PDE is a phosphodiesterase, not a phosphatase, but she groups it there. If she asks what Ca2+/calmodulin turns on, "cAMP phosphodiesterase" is in her list.
:::

#### Turning the Ca2+ signal off

:::key
- Pumps (to ER and outside), Na+/Ca2+ exchanger, binding proteins
- IP3 → IP2 by a phosphatase closes the ER channels
- Cytosol ~10^-7 M vs outside ~10^-3 M
:::

The short version: pump the calcium away, soak it up, and stop making IP3.

Cells keep calcium in the cytosol very low (about 10^-7 M) compared with outside the cell (about 10^-3 M). That's a 10,000-fold difference, so even a small release makes a big jump the cell notices. To end a calcium signal:

- Pump it away. Ca2+ pumps (using ATP) push Ca2+ out of the cell and back into the ER.
- Trade it out. A Na+/Ca2+ exchanger in the plasma membrane lets Na+ in and uses that flow to push Ca2+ out.
- Soak it up. Calcium-binding proteins in the cytosol grab it, and mitochondria take some in.
- Stop the trigger. A phosphatase removes a phosphate from IP3 (making IP2), so the ER channels close.

:::conn
DAG and PKC come back in Lecture 10. Phorbol esters (TPA) are cancer-promoting chemicals that copy DAG and lock PKC on. Same pathway as here, just broken.
:::

### Branch 3: ion channels and the membrane potential

The short version: cells are tiny batteries, negative on the inside. Ion channels are gates that let charged atoms flow, which changes the battery's voltage.

#### Gated and non-gated channels

:::key
- Non-gated: always open (resting K+ channel)
- Gated by voltage, ligand (outside or inside), or stretch
:::

An **ion** is an atom with an electric charge, like Na+ (sodium), K+ (potassium), Cl- (chloride) and Ca2+ (calcium). An **ion channel** is a protein tunnel through the membrane that lets one kind of ion through.

- **Non-gated** channels are always open. The main example is the resting K+ channel, which constantly leaks K+ out.
- **Gated** channels open only when something triggers them:

| Gate type | What opens it | Example |
|---|---|---|
| voltage-gated | a change in the membrane's voltage | Na+ channel in neurons (L6) |
| ligand-gated, outside ligand | a signal binding on the outside | acetylcholine receptor |
| ligand-gated, inside ligand | something binding on the inside | cGMP or Ca2+ |
| mechanically gated | the membrane being stretched or pushed | touch, hearing |

:::hook
Gates open by **V-L-M**: Voltage, Ligand, Mechanical. "**V**ery **L**oud **M**usic opens the door."
:::

#### Electrochemical gradients

:::key
- Net push = concentration gradient + membrane potential
- Resting potential about -70 mV, near the K+ equilibrium potential
- K+ high inside, Na+ high outside; Na+/K+ ATPase builds the K+ gradient
- Channels never pump: Na+ in = depolarize, K+ out = hyperpolarize

*Skim:* The 59 mV beaker numbers: know the idea (voltage moves toward the permeable ion), not the exact value.
:::

The short version: two forces push ions. One is "go where it's less crowded." The other is "opposite charges attract." Add them and you know which way an ion will flow.

- The **concentration gradient** pushes an ion from where there's a lot of it to where there's little, like people spilling out of a packed room.
- The **electrical gradient** (the membrane potential) pulls positive ions toward the negative side, like a magnet.
- Together they make the **electrochemical gradient**, the real overall push.

Almost every cell has a voltage across its membrane. In a typical mammal cell, the **resting membrane potential is about -70 mV**. That means the inside is negative compared with the outside.

Key concentrations (her Table 11-2):

| Ion | Inside (mM) | Outside (mM) | Where it's crowded |
|---|---|---|---|
| K+ | about 139 | 4 | inside |
| Na+ | about 12 | 145 | outside |
| Cl- | about 4 | 116 | outside |
| Ca2+ | under 0.0002 | 1.8 | outside (by a lot) |

:::hook
"**K+ is the King of the Kitchen** (inside). **Na+ lives in the salty Sea** (outside)." Your blood is basically salty seawater (Na+, Cl-), and your cells are potassium bags. Everything except K+ is crowded outside.
:::

**Why -70 mV?** The resting K+ channels let K+ leak out, because there's way more K+ inside. Each K+ that leaves carries a plus charge out and leaves a minus charge behind. The inside gets more and more negative, until that negative charge pulls back on K+ just as hard as the crowding pushes it out. That tie point is the **K+ equilibrium potential**, around -59 to -90 mV depending on the cell. The resting potential sits close to it because at rest the membrane is mostly leaky to K+.

Who keeps K+ crowded inside in the first place? The **Na+/K+ ATPase**, a pump that spends one ATP to push 3 Na+ out and bring 2 K+ in.

:::hook
Pump math: "**3 out, 2 in, 1 ATP.**" Sodium leaves, potassium comes home.
:::

Her beaker experiment: a membrane that only lets K+ through ends up with the inside at -59 mV. A membrane that only lets Na+ through ends up at +59 mV. Whichever ion the membrane lets through drags the voltage toward that ion's own equilibrium point.

Only a very thin layer of ions right next to the membrane has to move to make these voltages. The overall concentrations in the cell barely change. A tiny change in numbers, a big change in voltage.

:::trap
Opening a channel doesn't pump ions. Ions only flow downhill along their electrochemical gradient, like water. Open a Na+ channel and Na+ rushes in, making the inside less negative (that's **depolarizing**). Open a K+ channel and K+ rushes out, making it more negative (**hyperpolarizing**). Pumps like the Na+/K+ ATPase are what build the hill in the first place.
:::

:::hook
**Depolarize = "De-negative"** (moving toward zero or positive). **Hyperpolarize = "Hyper-negative"** (even more negative than rest).
:::

#### G proteins that open K+ channels in the heart

:::key
- Heart: ACh → muscarinic GPCR (Gi) → Gβγ opens K+ channels
- K+ out → hyperpolarize → slower heartbeat
- The subunit is Gβγ, NOT Gα
:::

The short version: the "calm down" nerve slows the heart by having Gβγ open K+ channels.

Many receptors for neurotransmitters are GPCRs whose effectors are Na+ or K+ channels. In heart muscle, the vagus nerve (the body's "calm down" nerve) releases **acetylcholine**. It binds the **muscarinic acetylcholine receptor**, a GPCR wired to Gi. The freed **Gβγ** pair (not Gα-GTP) binds K+ channels and opens them. K+ flows out, the inside gets more negative (hyperpolarized), and the heart cell takes longer to reach its firing point. The heart beats slower.

:::hook
"**Vagus = Very slow**": acetylcholine, muscarinic receptor, Gβγ opens K+, slower beat. And "beta-gamma opens the gate" for this one example.
:::

:::trap
In the muscarinic heart example, Gβγ carries the signal, not Gα. She wrote this on the slide. If a question asks which piece opens the K+ channel, the answer is Gβγ.
:::

:::nancy
She writes: "Note that the signal subunit (and not Gα-GTP) is transduced via the Gβγ."

Plain version: in this heart example, the Gβγ half is the one that opens the K+ channel. Gα isn't the messenger here.
:::

### Vision: a GPCR that responds to light

:::key
- Rhodopsin = opsin + 11-cis-retinal; light → all-trans
- Transducin → PDE → cGMP DOWN → channels CLOSE → rod HYPERpolarizes
- Dark: channels open, -30 mV, constant transmitter release
- Vitamin A makes retinal; deficiency = night blindness

*Skim:* Amplification numbers (500 transducins, 250 channels): skim.
:::

The short version: in the eye, light is the "hormone." Light makes the messenger go DOWN and channels CLOSE, which is the opposite of what you'd guess.

**Rod cells** in the retina handle black-and-white vision in dim light. Their outer part is a stack of membrane discs packed with **rhodopsin**, a GPCR that is triggered by light.

Rhodopsin has two parts:

- **opsin**, the 7-pass protein
- **11-cis-retinal**, a small light-catching molecule (a **chromophore**, "color carrier") bolted onto a lysine in opsin

When light hits, 11-cis-retinal straightens out into **all-trans-retinal** in about a trillionth of a second. "Cis" means bent and "trans" means straight, so light literally unbends the molecule. That shape change switches on opsin (now called meta-rhodopsin II), which switches on the G protein **transducin (Gt)**.

:::hook
"Light **straightens** retinal": cis (bent, like a C) to trans (straight, across). Bent = dark-ready, straight = light just hit.
:::

**Here's the twist that makes vision feel backwards.**

| | In the dark | In the light |
|---|---|---|
| cGMP level | high | low (PDE destroys it) |
| cGMP-gated channels | open, Na+ and Ca2+ leak in | closed |
| rod voltage | depolarized, about -30 mV | hyperpolarized (more negative) |
| neurotransmitter release | constant | drops |
| what the brain reads | dark | light |

The chain in the light: rhodopsin → transducin → Gαt switches on **cGMP phosphodiesterase (PDE)** → cGMP gets broken down → the **cGMP-gated cation channels** close → the rod hyperpolarizes → less neurotransmitter is released. The brain reads that drop as "light."

{{fig:rod_dark_light}}

{{lab:rod|rod vision (lights on, PDE knockout)}}

:::hook
Rods are **night owls**: busy in the dark, and light shuts them up. Light = less cGMP = channels shut = quiet rod.
:::

**Amplification in vision** is huge. One rhodopsin → about 500 transducins → 500 PDEs → about 10^5 cGMP broken down → about 250 channels closed → 10^6 to 10^7 Na+ ions blocked per second → the voltage changes by about 1 mV. That's how your eye can detect a single photon.

:::easy
Direction trap: in vision the second messenger (cGMP) goes DOWN, the channels CLOSE, and the rod HYPERpolarizes. Say all three directions out loud when you study this.
:::

{{slide:L5-35|The red arrows count down the amplification from one photon to a 1 mV change, and the bottom shows the cGMP channel closing.}}

:::trap
Vision uses PDE as the effector, and the second messenger goes DOWN. Everywhere else in this lecture the second messenger goes up. Don't assume "GPCR = more second messenger."
:::

:::she
Human Perspective on vitamin A and vision. Retinal is made from vitamin A (which comes from β-carotene in carrots, sweet potatoes and yellow vegetables). Some retinal gets oxidized into retinoic acid, a dead end for vision, so it has to be replaced. Night blindness is an early sign of not getting enough vitamin A.
:::

:::hook
"Carrots help you see in the dark" is half true: carrots give β-carotene → vitamin A → retinal. Run low and the night owl rods go first.
:::

:::nancy
She writes that rods are "active in the dark" and that retinal "isomerizes to the trans configuration."

Plain version: "active" means releasing neurotransmitter, and light is what quiets them. "Isomerizes to trans" means the bent molecule straightens out (cis = bent, trans = straight).
:::

### Smell

:::key
- Odorant → OR → Gαolf → AC3 → cAMP → CNG channel opens
- Ca2+ then opens a Cl- channel and Cl- LEAVES (more depolarization)
- Smell raises cAMP to open; vision lowers cGMP to close

*Skim:* 1000 mouse / 350 human receptor counts: low priority.
:::

The short version: smell works like the cAMP branch, but the cAMP opens a channel directly, and a chloride trick boosts the signal.

**Odorant receptors (ORs)** are GPCRs on the tiny hair-like cilia of smell neurons in your nose. Mice have about 1000 kinds; humans have about 350.

The chain: odorant → OR → **Gαolf** → **adenylyl cyclase 3 (AC3)** → cAMP → cAMP opens a **CNG channel** (cyclic nucleotide-gated, meaning "opened by cAMP or cGMP") → Na+ and Ca2+ flow in → the neuron depolarizes.

The booster: the incoming Ca2+ also opens a **Ca2+-activated Cl- channel**. These neurons are unusual because they keep Cl- high inside. So when the Cl- channel opens, Cl- flows OUT. Negative charge leaving makes the inside even less negative, which adds more depolarization.

cAMP also switches on genes that help these neurons grow their axons and stay alive.

{{slide:L5-36|Spot the two channels: CNG lets cations in, then Ca2+ opens the Cl- channel and Cl- leaves.}}

:::conn
Smell and vision both end at cyclic-nucleotide-gated channels, but they run in opposite directions. Smell RAISES cAMP to OPEN channels. Vision LOWERS cGMP to CLOSE channels.
:::

:::hook
"Smell **Swells** (cAMP up, channels open), Sight **Sinks** (cGMP down, channels close)."
:::

:::nancy
This slide is a figure pasted from a journal review, so the text is dense and runs into the article around it.

Plain version, the one fact people miss: these neurons keep Cl- high inside, so when the Ca2+-activated Cl- channel opens, Cl- leaves and the cell gets MORE excited. That's the opposite of the usual "Cl- calms a neuron" rule.
:::

### Nitric oxide: a gas as a signal

:::key
- ACh → Ca2+/CaM → NO synthase makes NO from arginine (endothelium)
- NO diffuses into smooth muscle → guanylyl cyclase → cGMP → relax
:::

The short version: a gas made in one cell drifts into the next cell and tells the blood vessel to relax.

**Nitric oxide (NO)** relaxes blood vessels. The chain crosses two cells:

1. **In the endothelial cell** (the inner lining of the blood vessel): acetylcholine binds a GPCR → IP3 and Ca2+ go up → Ca2+/calmodulin switches on **NO synthase** → NO synthase makes NO from the amino acid arginine.
2. NO crosses over. NO is a tiny gas, so it doesn't need a receptor on the surface. It just slips through both membranes into the smooth muscle cell next door.
3. In the smooth muscle cell: NO switches on **guanylyl cyclase**, which makes cGMP. cGMP makes the muscle relax, and the vessel widens.

{{slide:L5-37|NO is made in the endothelial cell and simply diffuses into the smooth muscle cell next door.}}

:::hook
**NO = "Now Open"** the blood vessel. It's a gas, so it ignores the doorbell and walks straight into the muscle cell.
:::

:::conn
Compare the two "cyclases": **adenylyl cyclase** makes cAMP (A for ATP), **guanylyl cyclase** makes cGMP (G for GTP). Swap the letter, swap the messenger.
:::

### How to figure it out: "what happens if this step breaks?" {#howto-perturb}

This is the most common style of question in this unit. You get a pathway and one broken part (a toxin, a drug, a mutation) and you predict the result.

How to spot this kind of question: words like toxin, inhibitor, blocker, mutant, "cannot hydrolyze," "constitutively active" (always on), "dominant negative," "lacks," "knockout."

A method that works every time:

1. **Write the chain** from signal to result. Example: epinephrine → receptor → Gαs → adenylyl cyclase → cAMP → PKA → glycogen breakdown.
2. Find the broken link and ask: stuck ON or stuck OFF?
   - Break an OFF switch (GTPase, PDE, phosphatase, reuptake, inactivation) and the pathway is stuck ON.
   - Break or block an ON part (receptor, kinase, cyclase) and the pathway is stuck OFF.
3. Everything after the break follows that state. Everything before it doesn't matter, and adding more hormone can't fix a break further down.
4. **Translate to the body** using the tissue: gut cells lose water, heart slows, rod stays depolarized.

:::hook
"**Break a brake, it races. Break an engine, it stalls.**"
:::

Practice:

- A drug blocks cAMP phosphodiesterase in liver cells. PDE is an off switch for cAMP, so cAMP stays high, PKA stays on, and glycogen breakdown is bigger and lasts longer after epinephrine.
- A mutant Gαs can't bind GTP. The ON step fails. Adenylyl cyclase never turns on, so epinephrine can't raise cAMP in that cell.
- A rod cell's PDE is knocked out. Light can't lower cGMP. The cGMP-gated channels stay open, the rod stays depolarized and keeps releasing neurotransmitter as if it were dark. Those rods can't detect light.
- A cell has a drug that blocks the phosphatase that removes IP3's phosphate. IP3 hangs around, the ER Ca2+ channels stay open longer, and the calcium signal lasts longer.
- (Extra practice, not on her slides.) Pertussis toxin (whooping cough) locks Gαi in its OFF (GDP) form. Gαi is normally a brake on adenylyl cyclase. Removing a brake means cAMP goes UP. Two negatives make a positive; watch for that.

### Reading her questions on this lecture {#read-l5}

| If the question says... | She's testing... | How you'd get tricked |
|---|---|---|
| "non-hydrolyzable GTP" or "cannot hydrolyze GTP" | Broken off switch: signal stays on | Thinking the G protein can't activate |
| "cholera toxin" | Gαs stuck ON, cAMP high | Saying it adds hormone or blocks the receptor |
| "PDE inhibitor" | cAMP stays high longer | Saying it starts the signal |
| "which is NOT a second messenger" | PLC-β is an enzyme; DAG isn't water-soluble | Picking DAG when the option list includes PLC-β |
| "PKA phosphorylates glycogen synthase" | Phosphorylation can inhibit | Assuming phosphorylated = active |
| "agonist" / "antagonist" | Mimic vs block | Swapping them; beta-blockers are antagonists |
| "acetylcholine slows the heart" | Muscarinic GPCR, Gβγ opens K+ | Naming Gα-GTP as the subunit |
| "light hits a rod" | cGMP down, channels close, hyperpolarize | Assuming the second messenger rises |
| "open a K+ (or Cl-) channel" | Hyperpolarization | Forgetting which side each ion is high on |

### Lecture 5 on one page

| Part | Plain-English job | Remember it by |
|---|---|---|
| GPCR | doorbell, 7 stitches through the membrane | "N out, C in" |
| G protein (Gα + Gβγ) | light switch: GTP on, GDP off | toaster with a timer |
| Gαs / Gαi | gas pedal / brake on adenylyl cyclase | s = speeds, i = inhibits |
| cAMP + PDE | the shout, and the eraser | chalk and eraser |
| PKA | worker held by R "babysitters" | R restrains, C catalyzes |
| Gαq → PLC-β → IP3 + DAG | cut the PIP2 sandwich | IP3 goes, DAG stays |
| Ca2+ → calmodulin | general alarm, four-finger hand | CaM-kinase II remembers |
| Channels, -70 mV | battery, negative inside | K+ king of the kitchen |
| Rods | light lowers cGMP, channels close | night owls |
| Smell | cAMP opens CNG, Cl- leaves | smell swells, sight sinks |
| NO | gas crosses into muscle, cGMP relaxes | Now Open |
