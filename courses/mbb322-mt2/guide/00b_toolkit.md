## Chapter 0: the toolkit {#toolkit}

:::story
Start here if biology isn't your background. Nancy's slides assume you already know how a cell is built, what proteins and genes are, and how electricity works in a membrane. This chapter teaches exactly that background and nothing extra, so every later chapter makes sense without looking anything up. Most of it won't be asked directly, but every chapter after this one uses it.

Tip: anywhere in the guide, tap a word with a dotted underline to get its plain-English definition. The full list is in the glossary near the end.
:::

### 0.1 The cell is a walled city

A cell is a tiny bag of watery fluid with machinery inside. Think of it as a walled city.

- The **plasma membrane** is the city wall. It's a thin, oily film that wraps the whole cell. "Outside" means the fluid around the cell (also called extracellular); "inside" means the cell's own fluid.
- The **cytosol** is the fluid filling the city: the streets where most of the action happens.
- The **nucleus** is the library. It holds the DNA (the instructions) and is wrapped in its own double membrane with pores (nuclear pores) that act as guarded doors. Proteins that need to get in carry a "zip code" called a nuclear localization signal (NLS), which an escort protein called **importin** recognizes; **exportins** carry things back out.
- The **endoplasmic reticulum (ER)** is a maze of membrane tubes. In this unit it matters mainly as a **calcium store**: it keeps Ca2+ locked inside until a signal opens the doors. In muscle, the ER is called the **sarcoplasmic reticulum (SR)**.
- **Mitochondria** are the power plants. They make most of the cell's ATP (energy currency) by a process called **oxidative phosphorylation**, which needs oxygen.
- **Lysosomes** are recycling centers: bubbles full of digestive enzymes that break things down.
- **Vesicles** are small membrane bubbles that act like delivery trucks. **Exocytosis** is a vesicle fusing with the plasma membrane and dumping its contents outside. **Endocytosis** is the reverse: the membrane pinches inward to swallow something into a new vesicle.

:::hook
City wall (membrane), streets (cytosol), library (nucleus), calcium warehouse (ER), power plant (mitochondria), recycling center (lysosome), delivery trucks (vesicles).
:::

Cells sit in **tissues**. **Epithelial cells** form sheets that line surfaces (skin, gut, airways) and rest on a thin mat of proteins called the **basal lamina** (basement membrane). Under that is **connective tissue**: support cells like **fibroblasts** in a mesh of proteins called the **extracellular matrix (ECM)**. You studied these in Midterm 1.

### 0.2 Membranes: why messages can't just walk in

The membrane is a **lipid bilayer**: two layers of fatty molecules (phospholipids) arranged tails-in, heads-out. Each layer is a **leaflet**. The middle is oily (hydrophobic, "water-fearing"), so anything that is charged or large and water-loving can't cross it on its own. That includes ions (Na+, K+, Ca2+, Cl-), sugars, and most hormones and growth factors.

That single fact creates this whole unit. If the message can't come in, the cell needs proteins in the wall that catch the message outside and pass the news inside. Those are receptors.

A few things can slip straight through the oily layer because they're small and uncharged or fatty, like the gas nitric oxide (Lecture 5).

Proteins sit in or on the membrane in different ways (Midterm 1):

- **Transmembrane** proteins cross the membrane. "Seven-pass" means the chain snakes across seven times (GPCRs); "single-pass" means once (RTKs).
- **Lipid-anchored** proteins hang on by a fatty tail, like a boat tied to a dock. Examples: Ras (Lecture 8), G protein subunits, ephrinA with its **GPI anchor**, and Wnt with its **palmitate** (a fatty acid).

:::hook
The membrane is an oil slick. Oil doesn't mix with charged or water-loving things, so they need a door (a channel), a pump, or a receptor to pass the message.
:::

### 0.3 Proteins: the workers

Proteins do almost all the work in a cell. Each one is a chain of building blocks called **amino acids** (20 kinds), folded into a specific 3D shape. The shape decides the job, the way a key's shape decides which lock it opens.

- **Domains** are self-contained modules within a protein, like Lego pieces with separate jobs. A receptor tyrosine kinase has a binding domain outside, a membrane-crossing piece, and a **kinase domain** inside. An **SH2 domain** is a module that grabs phosphorylated tyrosines.
- A **conformational change** is a change in shape. This is the cell's basic switch: something binds, the protein changes shape, and its activity changes.
- A **dimer** is two proteins stuck together; a **homodimer** is two copies of the same one; **trimer** = three; **heterotrimeric** = three different pieces.

Amino acid names you'll see, with their one-letter codes: glycine (Gly, G), tyrosine (Tyr, Y), serine (Ser, S), threonine (Thr, T), arginine (Arg, R), histidine (His, H), valine (Val, V), glutamine (Gln, Q), proline (Pro, P), asparagine (Asn, N), lysine (Lys, K), cysteine (Cys, C).

How to read mutation names: "Gly12" means the 12th amino acid, a glycine. "R206H" means arginine (R) at position 206 changed to histidine (H). "Tyr 527" is tyrosine number 527.

### 0.4 Binding: ligands, receptors and how tight

- A **ligand** is any molecule that binds a specific protein. A hormone binding its receptor is a ligand binding.
- A **receptor** is a protein that binds a signal and changes shape in response.
- **Affinity** is how tightly two things stick. It's measured by the **Kd** (dissociation constant): the lower the Kd, the tighter the binding. MT1 asked which value reflects affinity: Kd.
- An **agonist** is a drug that binds a receptor and switches it on like the real hormone; an **antagonist** binds and blocks it.

### 0.5 Energy, enzymes and the two big switches

An **enzyme** is a protein that speeds up a chemical reaction. The molecule it acts on is its **substrate**.

**ATP** is the cell's energy coin. Splitting off a phosphate (ATP → ADP + phosphate) releases energy. **GTP** is a close cousin (GTP → GDP + phosphate) used mainly as an on/off token. Splitting with water like this is called **hydrolysis**.

The cell flips proteins on and off in two main ways, and nearly every pathway in this unit uses one or both:

1. **Phosphorylation.** A **kinase** is an enzyme that sticks a phosphate group (from ATP) onto a protein. A **phosphatase** takes it off. Kinases are named by which amino acid they tag: **tyrosine kinases** tag tyrosine; **serine/threonine kinases** tag serine or threonine. A phosphate is bulky and negatively charged, so it changes a protein's shape or creates a new docking spot. What that does depends on the protein. In this unit a phosphate can switch an enzyme on, switch one off, create a landing pad for SH2 domains, mark a protein for destruction, or uncover a hidden address label.
2. **GTP switches (G proteins).** A **GTPase** is a protein that holds either GTP (ON) or GDP (OFF), and slowly hydrolyzes its own GTP, which acts as a timer. Two helpers control it: a **GEF** (guanine nucleotide exchange factor) swaps GDP out so GTP can get in (turns it ON); a **GAP** (GTPase-activating protein) speeds up the hydrolysis (turns it OFF). Lecture 5's heterotrimeric G proteins and Lecture 8's Ras both work this way.

:::hook
Phosphate = a sticky note that changes what a protein does. GTP = a light switch with a built-in timer; GEF flips it on, GAP flips it off.
:::

### 0.6 Genes: from instructions to proteins

- **DNA** is the instruction manual. A **gene** is one instruction: the recipe for one protein.
- DNA is packed into **chromosomes**. Humans have 23 pairs; you get one of each pair from each parent. So you have **two copies** of almost every gene. The two versions are called **alleles**. (This "two copies" idea is the key to tumor suppressors in Lecture 11.)
- **Transcription** copies a gene into a messenger molecule, **mRNA**. **Translation** reads the mRNA to build the protein. "A gene is turned on" means it is being transcribed.
- Each gene has a **promoter** in front of it: the on-switch region where transcription starts. **Enhancers** are extra control regions that boost it.
- **Transcription factors** are proteins that bind those DNA regions and turn genes on (or off). A **co-activator** helps a transcription factor switch a gene on without binding DNA itself (β-catenin, Lecture 11). A **repressor** keeps a gene off (Groucho, Lecture 11).
- DNA is wrapped around spool proteins called **histones**; DNA plus histones is **chromatin**. Loosely packed chromatin can be read; tightly packed **heterochromatin** is silent.
- **Early response genes** are genes a cell switches on within minutes of a growth signal (c-fos, Lecture 8).

:::hook
DNA is the cookbook in the library, mRNA is a photocopied recipe carried to the kitchen, and the protein is the dish. Transcription factors decide which recipes get photocopied.
:::

### 0.7 Protein lifetimes: destruction as a control knob

Cells control signals partly by destroying the messengers.

- **Ubiquitin** is a small protein tag. Enzymes called **E3 ubiquitin ligases** attach it to proteins that should be removed. A chain of ubiquitins is a "trash" label; the **proteasome**, a barrel-shaped shredder, destroys the tagged protein. HIF (Lecture 9) and β-catenin (Lecture 11) are controlled this way: a signal works by stopping their destruction.
- A single ubiquitin (mono-ubiquitination) on a membrane receptor tags it for **endocytosis** and digestion in the **lysosome** instead (RTKs, Lecture 8).

### 0.8 Ions and electricity

- An **ion** is a charged atom: Na+ (sodium), K+ (potassium), Ca2+ (calcium) and H+ (proton) are positive; Cl- (chloride) is negative. **Cations** are positive ions; **anions** are negative.
- A **concentration gradient** means more of something on one side than the other. Things drift from high to low, like a crowd leaving a packed room.
- The **membrane potential** is the voltage across the membrane, measured in millivolts (mV). At rest the inside is about **-70 mV** (negative compared with outside).
- **Depolarization** means the inside becomes less negative (moving toward zero or positive). **Hyperpolarization** means more negative. A neuron fires when depolarization reaches a **threshold**.
- The rule that decides everything: positive charge coming in, or negative charge going out, depolarizes. Positive charge going out, or negative charge coming in, hyperpolarizes.
- Three kinds of membrane machines move ions. A **channel** is a door: when open, ions rush downhill on their own, very fast. A **pump** uses energy (ATP, or light for halorhodopsin) to push ions, even uphill. A **transporter** carries molecules across, often by coupling to another ion's downhill flow (an **antiporter** swaps one thing in for another out).
- The **Na+/K+ pump** constantly pushes Na+ out and K+ in. That's why Na+ is high outside and K+ is high inside, the gradients every neuron runs on.

:::hook
Charge in = up (depolarize); charge out or negative in = down (hyperpolarize). Channels are doors, pumps are bouncers that push people around.
:::

### 0.9 Dividing, specializing, dying

Background for the cancer chapters (her slides assume it):

- The **cell cycle** is the series of steps a cell goes through to divide: grow (G1), copy its DNA (S phase), grow and check (G2), then split (mitosis, M phase). Cells that aren't dividing are **quiescent** (resting).
- Enzymes called **CDKs** (cyclin-dependent kinases), switched on by partner proteins called **cyclins**, push the cell from one stage to the next. **CDK inhibitors** like p15 (Lecture 11) are brakes on them. Rb (Lecture 11) is a brake at the entry to S phase.
- **Checkpoints** are stop signs where the cell checks for problems. **p53** is the classic checkpoint protein: when DNA is damaged, it stops the cycle so the cell can repair, or triggers suicide if the damage is too bad.
- **Apoptosis** is programmed cell death: a tidy, controlled suicide that removes damaged or unneeded cells. Cancer cells often evade it.
- **Differentiation** is a cell becoming a specialized type (a muscle cell, a neuron). Specialized cells usually divide less.
- **Senescence** is a permanent stop to dividing. **Replicative senescence** happens after a set number of divisions, counted by shrinking telomeres (Lecture 9).
- **Stem cells** are unspecialized cells that can keep dividing to replace tissue.

### 0.10 Mutations: how genes break

A **mutation** is a permanent change in the DNA sequence. Types used in Lectures 8 to 11:

- **Point mutation**: one DNA letter changed. A **missense** mutation swaps one amino acid for another (Ras G12). A **nonsense** or **truncating** mutation creates an early "stop," so the protein comes out chopped short.
- **Deletion** (a piece removed) and **insertion** (a piece added). A **frameshift** is an insertion or deletion that scrambles every amino acid after it.
- **Gene amplification**: extra copies of a gene, so too much of a normal protein.
- **Translocation**: two chromosomes swap pieces. It can fuse two genes into one (Bcr-Abl).
- **Aneuploidy**: the wrong number of chromosomes.
- **Gain-of-function**: the protein does more (overactive, always on). **Loss-of-function**: the protein does less or nothing.
- **Dominant** (in a cell): one changed copy is enough to show the effect. **Recessive**: both copies must be changed.
- **Germline / inherited** mutations are in egg or sperm, so they're in every cell of the child. **Somatic** mutations happen in one body cell during life and are passed only to that cell's descendants.
- **Epigenetic** changes switch a gene's activity without changing its sequence (methylation, Lecture 11).

### 0.11 How biologists find things out

Nancy loves asking what an experiment proves. These are the tools:

- **Knockout / loss-of-function mutant**: remove or break a gene and see what fails.
- **Constitutively active** mutant: a version stuck ON. If it causes the effect with no signal, the protein is sufficient.
- **Dominant negative**: a broken version that still grabs its partners and jams them, so it blocks the normal protein even when the normal protein is present. It's a loss-of-function tool despite the word "dominant."
- **Antibodies**: proteins that stick very specifically to one target. Injected into cells, they can block that target; in staining, they light it up.
- **Fluorescent proteins** (GFP, YFP): glowing tags fused to a protein to see where it is.
- **Microinjection** (injecting directly into a cell), **transfection** (getting DNA into cultured cells), **transgenic** animals (carrying an added gene).
- **Cell culture**: growing cells in a dish.
- **Model organisms**: species that are easy to study and share our biology. Yeast, the worm C. elegans, the fruit fly Drosophila, the frog Xenopus, zebrafish, mice, and the alga Chlamydomonas.
- **Genetic screen**: mutate many animals and look for ones with a particular defect to find the genes involved. An **enhancer screen** looks for mutations that make a weak defect worse; a **suppressor screen** looks for ones that make it better. A **temperature-sensitive** mutant works at one temperature and fails at another, so you can weaken a pathway on demand.
- **Epistasis**: ordering genes in a pathway by combining mutations. When an ON mutation and an OFF mutation are combined, the result looks like whichever gene is **downstream** (later in the chain).
- **FRET**: a glow-based ruler that only lights up when two labeled proteins are touching.
- **Patch clamp**: a tiny glass electrode that records a cell's electrical activity.

### 0.12 Signaling vocabulary

- **Signaling pathway / cascade**: a relay of proteins, each switching on the next, from the signal at the membrane to the response inside.
- **First messenger**: the outside signal (hormone, neurotransmitter, growth factor). **Second messenger**: a small inside molecule made in response that spreads the news fast (cAMP, cGMP, IP3, DAG, Ca2+).
- **Effector**: the protein that actually produces the output, like an enzyme or channel switched on by a G protein.
- **Upstream** means earlier in the chain, **downstream** later.
- **Amplification**: each active step switches on many copies of the next, so one signal molecule ends in millions of products.
- **Adaptor** proteins have no enzyme activity; they just link two other proteins (GRB2). **Scaffold** proteins hold a whole set of pathway proteins together like a tool belt.
- **Cross-talk**: one pathway accidentally (or deliberately) affecting another.
- Signal reach (MT1): **autocrine** (a cell signals itself), **paracrine** (nearby cells), **endocrine** (hormones through the blood to distant cells).
- **Hormones** travel through the blood; **growth factors** tell cells to divide or survive; **cytokines** are signals mainly for blood and immune cells; **neurotransmitters** carry signals across a synapse between nerve cells.
