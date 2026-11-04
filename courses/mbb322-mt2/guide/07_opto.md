## Lecture 7: optogenetics {#l7}

A short lecture with a clean storyline: a light-sensing protein from pond algae became a remote control for neurons. On her first slide, Karl Deisseroth, Peter Hegemann and Georg Nagel got the 2026 Nobel Prize in Physiology or Medicine for the discoveries behind **optogenetics**: using light to switch chosen nerve cells on or off in a living brain.

:::story
Chapter 3, a short detour that puts Chapters 1 and 2 to work. From Lecture 6: a neuron fires when Na+ rushes in. So if you had a sodium door that opened when you shone a light on it, you could fire any neuron you wanted with a flash. This chapter is that story, from pond algae to mice that wake up, drink or attack on command.

What you need from before: rhodopsin and retinal (Lecture 5), depolarize vs hyperpolarize (Lecture 6).
:::

### The big picture in one paragraph

Scientists found a protein in a tiny swimming alga that opens a door for positive ions when blue light hits it. They put the gene for that protein into the neurons of a mouse, ran a thin glass fiber into its brain, and shone light down it. Every flash made those neurons fire. Now they could ask "what does this group of neurons do?" by switching them on and watching the mouse. Other light proteins do the opposite and silence neurons. That's the whole lecture.

The name tells you the method: "**opto**" (light) + "**genetics**" (you put a gene into the cells you want to control).

:::hook
Optogenetics is a **TV remote for neurons**. The gene installs the receiver in chosen cells, the light is the button.
:::

### Where it started: Chlamydomonas

:::key
- Chlamydomonas: green alga, model organism, where channelrhodopsins came from
- Known for cilia work: IFT, ciliopathies (Bardet-Biedl, polycystic kidney)

*Skim:* Flagella pH-shock detail: low priority.
:::

The short version: a little green swimming cell that scientists already loved for studying cilia turned out to hold the light-sensing door.

*Chlamydomonas reinhardtii* is a single-celled green alga with two **flagella** (whip-like tails it swims with). It's a **model organism**: a species scientists study because it's easy to grow, and what they learn applies to other living things too.

It was already famous for cilia and flagella research before optogenetics:

- **Intraflagellar transport (IFT)** was discovered in it. IFT is the two-way traffic of protein particles up and down the flagellum that builds and maintains cilia, like trains running on a track inside the tail.
- Cilia are very similar in all eukaryotes, so findings in Chlamydomonas helped explain human **ciliopathies** (genetic diseases of cilia) such as Bardet-Biedl syndrome and polycystic kidney disease.
- Its flagella can be popped off whole with a single pH shock (a quick change in acidity) without breaking the cell, which made them easy to collect and study.

:::hook
"**Chlamy** has two tails and a red-orange eye." Two flagella for swimming, one eyespot for steering.
:::

#### Phototaxis and the eyespot

:::key
- Eyespot senses light direction and intensity → swims toward light (phototaxis)
:::

Chlamydomonas swims toward light so it can photosynthesize (make food from light). Moving in response to light is called **phototaxis** ("photo" = light, "taxis" = movement toward or away). It senses which way and how bright the light is with an **eyespot**, a small orange oval in the cell. The big question was: what protein in the eyespot actually feels the light?

### The discoveries, in order

:::key
- 2002 ChR1: H+ only
- 2003 ChR2: non-selective cation channel (Na+, K+, Ca2+) → can fire neurons
- ChR2 works in mammalian cells

*Skim:* Author lists and journal volumes: skip.
:::

The short version: ChR1 (2002) let protons through. ChR2 (2003) let ordinary positive ions through, and that's the one that can fire neurons.

**2002, Channelrhodopsin-1 (Nagel, Hegemann and others, Science).** They found a gene in Chlamydomonas that looked similar (**homologous**, meaning related by shared ancestry) to **bacteriorhodopsin**, a known light-powered proton pump from microbes. They made frog eggs produce it (*Xenopus laevis* oocytes, huge cells that are easy to inject and record electricity from), added all-trans retinal, and shone light. Light produced a current through a channel that only let **protons (H+)** through. They proposed these "channelrhodopsins" are what steer the alga toward light.

**2003, Channelrhodopsin-2 (Nagel and others, PNAS).** ChR2 turned out to be a broad, **non-selective cation channel**: it lets Na+, K+ and Ca2+ through. That's what made it so useful. Neurons fire by letting Na+ in, so a sodium door that opens with light can make a neuron fire. They also showed ChR2 folds and works in mammal cells (human embryonic kidney cells and hamster kidney cells), so an alga protein could work in animal membranes.

:::trap
ChR1 = proton (H+) channel. ChR2 = non-selective cation channel (Na+, K+, Ca2+). ChR2 is the one used to fire neurons.
:::

:::hook
"**1 = one ion (H+). 2 = lots of ions (Na+, K+, Ca2+).**" And 2 came second but is number one for neuroscience.
:::

| | ChR1 | ChR2 |
|---|---|---|
| Year, journal | 2002, Science | 2003, PNAS |
| Lets through | H+ only | Na+, K+, Ca2+ (non-selective cations) |
| Tested in | frog eggs | frog eggs and mammal kidney cells |
| Useful for firing neurons? | no | yes |

:::nancy
For ChR2 she writes: "a broad, non-selective cation channel that efficiently conducts both monovalent and divalent positive ions."

Plain version: it lets most plus ions through, both the single-charge ones (Na+, K+) and the double-charge one (Ca2+).
:::

### How channelrhodopsin-2 works

:::key
- Blue light ~470 nm
- Retinal flips all-trans → 13-cis (opposite of rod)
- It IS the channel: no G protein, very fast
:::

The short version: a 7-pass protein holding retinal. Blue light bends the retinal, the protein opens as a pore, ions flow.

ChR2 is a **7-transmembrane protein** (like a GPCR, it crosses the membrane seven times) with **all-trans-retinal** bolted on as its light catcher (chromophore). When it absorbs **blue light (about 470 nm)**, the retinal changes to **13-cis-retinal**. That shape change opens a pore through the protein, and cations flow through. In the dark, the retinal flips back and the channel closes.

{{slide:L7-6|Blue light flips all-trans retinal to 13-cis and the pore opens; in darkness it flips back.}}

{{fig:chr2}}

:::easy
Both-boxes trap: ChR2 looks like a rhodopsin (7 transmembrane helices, retinal) but it is an ion channel, not a GPCR. OptoXR is the optogenetic tool that is a GPCR.
:::

Compare it with the rod rhodopsin from Lecture 5:

| | Rod rhodopsin (L5) | Channelrhodopsin-2 (L7) |
|---|---|---|
| What it is | GPCR | ion channel (the protein itself is the pore) |
| Retinal before light | 11-cis (bent) | all-trans (straight) |
| Retinal after light | all-trans (straight) | 13-cis (bent) |
| What happens next | G protein (transducin), PDE, cGMP falls | ions flow straight through |
| Speed | slower (a cascade) | very fast (milliseconds) |
| Result on the cell | rod hyperpolarizes | neuron depolarizes and fires |

:::conn
This is the rhodopsin story from Lecture 5 run backwards and wired differently. Rod rhodopsin straightens retinal and starts a G protein chain. Channelrhodopsin bends retinal and is itself the door. No G protein and no second messenger, so it's very fast.
:::

:::hook
"**Rod straightens, ChR bends.**" Rod: 11-cis to all-trans. ChR2: all-trans to 13-cis. And "ChR2 = **Ch**annel, **R**apid, **2** blue." Blue light opens it, ions rush in, the neuron fires within milliseconds.
:::

:::nancy
She writes: "covalently linked to the chromophore all trans-retinal. Upon absorption of blue light changes to the 13-cis-retinal conformation."

Plain version: "chromophore" is the light-catching part. Watch the direction: in ChR2 it goes all-trans TO 13-cis, the reverse of the rod in Lecture 5 (11-cis to all-trans).
:::

:::exam
Her Q15 and Q16 are the two basic ChR2 facts, each surrounded by distractors borrowed from other proteins in the unit.

- What it is: a light-gated ion channel that opens with blue light (about 470 nm).
- What it does: cations, mainly Na+, rush in, the membrane depolarizes toward threshold, and the neuron fires.

How to clear the distractors fast. "G protein coupled receptor" describes rod rhodopsin or OptoXR. "Pump" describes halorhodopsin or bacteriorhodopsin. "Chloride rushes in" is halorhodopsin. "K+ in and hyperpolarize" doesn't happen with any of these tools. Wrong colors (UV, green, red, infrared) are out too, since ChR2 is the blue one.
:::

### 2005: the birth of optogenetics

:::key
- ChR2 in cultured neurons: one flash = one spike, millisecond precision
:::

The short version: put ChR2 in neurons in a dish, flash blue light, get one spike per flash.

Boyden, Zhang, Bamberg, Nagel and Deisseroth (Nature Neuroscience, 2005) put ChR2 into mammal neurons growing in a dish. Pulses of blue light opened the channels, positive ions flooded in, and the neurons fired action potentials with millisecond precision. On her recording: light off, no spikes; blue light on, one spike for every flash; light off, no spikes again.

{{slide:L7-8|A spike for every blue flash, none when the light is off. That one-to-one match is the whole point.}}

This gave neuroscientists a way to turn specific neurons on or off whenever they wanted. The gene can be put into any cell type, in animals with or without backbones, so researchers can test which neurons cause which behaviors.

:::hook
"**One flash, one spike.**" That one-to-one control is what made 2005 the birthday.
:::

### Getting it into a living animal

:::key
- Two hurdles: deliver the gene, deliver the light
- Harmless virus (lentivirus/AAV) + cell-type promoter
- Implanted fiber-optic cable; transgenic mice are another option
:::

:::she
Her slide lists two "massive technical hurdles" for moving from a dish into a freely moving animal, and how Deisseroth's lab solved both (2006-2007).
:::

The short version: problem 1 was getting the gene into the right cells, solved with a virus and a cell-type switch. Problem 2 was getting light deep into the brain, solved with a fiber-optic cable.

1. Getting the gene into the brain safely. They used modified, harmless viruses (**lentiviruses** or **adeno-associated viruses, AAV**) as delivery trucks for the gene. They also picked the **promoter**, the stretch of DNA in front of a gene that decides which cells read it. A promoter that's only active in one neuron type means only that neuron type makes ChR2, and the neighbors are left alone.
2. Getting light deep into the brain. Light can't get through skull and thick tissue. They implanted a thin, flexible **fiber-optic cable** (a cannula-coupled optical fiber) right into the target area, connected to a laser, so the mouse could still walk, eat and behave normally.

You can also skip the virus by breeding **transgenic mice**: mice that carry the light-sensitive channel gene in specific neurons from birth.

:::hook
"**Truck and flashlight.**" The virus is the delivery truck (with a promoter as the address label), the fiber is the flashlight you push into the brain.
:::

Her six-step recipe:

1. build the construct (promoter + opsin gene)
2. package it in a virus
3. inject it into the brain
4. implant the optical fiber
5. shine light of the right color
6. record the behavior

{{slide:L7-11|The recipe: construct, virus, injection, optical fiber, light, behavior.}}

:::nancy
She writes: "By altering the genetic code of the virus, they could dictate exactly which types of neurons would produce the light-sensitive protein."

Plain version: they picked a promoter (the gene's on-switch) that's only active in one neuron type. If asked how only certain neurons get ChR2, answer "cell-type-specific promoter."
:::

### Experiments she showed

:::key
- 2007: orexin/hypocretin neurons → sleeping mice wake
- SFO neurons → hydrated mice drink
- Aggression neurons → attack
- Control: no ChR2 + light = no effect
:::

The short version: flip on a group of neurons, and the mouse wakes up, drinks, or attacks.

| Experiment | Neurons targeted | What light did |
|---|---|---|
| First in a living animal (2007) | hypocretin (also called orexin) neurons in the hypothalamus, suspected to control sleep | blue light pulses while the mice slept made the neurons fire, and the mice woke up |
| Thirst | neurons in the **subfornical organ (SFO)** of the hypothalamus | mice drank lots of water even though they weren't thirsty; mice without ChR2 didn't |
| Aggression | neurons thought to control aggression | light on, mice attacked anything nearby; light off, they stopped |

More detail on the thirst experiment: ChR2 was tagged with **YFP** (yellow fluorescent protein, a glowing tag). The yellow glow showed which cells had it, and **patch-clamp recording** (a tiny glass pipette that measures one cell's electricity) showed that blue light made those cells fire.

{{slide:L7-13|The bar graph is the experiment in one picture: only ChR2-infected mice given light drank.}}

:::hook
"**Wake, Drink, Fight.**" Sleep neurons, thirst neurons, aggression neurons.
:::

:::trap
Look at the control in the thirst experiment: mice without ChR2 that got blue light didn't drink. That proves the light itself isn't the cause; the ChR2 in those neurons is. If she gives you an optogenetics experiment, check for this control.
:::

:::nancy
She writes "The First In Vivo Proof (2007)."

Plain version: "in vivo" means in a living animal, as opposed to "in culture" (in a dish).
:::

### The optogenetic toolbox

:::key
- ChR2: cations in → fire
- Halorhodopsin: pumps Cl- in → silence
- Bacteriorhodopsin: pumps H+ out → silence
- OptoXR: GPCR, controls second messengers

*Skim:* Red-shifted opsins (ReaChR): just know red goes deeper.
:::

The short version: some tools turn neurons on (let plus in), some turn them off (push minus in or plus out), and one controls G proteins instead of voltage.

| Tool | What it moves | Effect on the neuron |
|---|---|---|
| Channelrhodopsin-2 (ChR2) | lets cations in (it's a channel) | depolarizes, so it activates (fires) |
| Halorhodopsin (HR) | pumps Cl- into the cell (from archaebacteria) | hyperpolarizes, so it inhibits (silences) |
| Bacteriorhodopsin (BR) | pumps H+ out of the cell | hyperpolarizes, so it inhibits |
| OptoXR | a light-activated rhodopsin whose inside loops were swapped so it switches on a chosen Gα | controls second messengers (cAMP, IP3) instead of voltage |

Newer tools include **red-shifted** opsins such as **ReaChR** (opened by red light near 600 nm, which travels deeper into tissue than blue), and uses outside the brain (heart cells, muscle, stem cells).

{{slide:L7-15|ChR lets cations in, HR pumps Cl- in, BR/PR pumps H+ out, OptoXR talks to G proteins instead of moving ions.}}

{{fig:opto_tools}}

{{3d:opto|Shine blue light on ChR2 and watch the neuron fire; then light halorhodopsin and watch it go silent.}}

:::hook
**ChR2 = Charge in** (go). **HR = "Halo"** puts a Cl- halo inside and **Holds** the neuron quiet. **BR = "Bye" protons**, pumped out, also quiet. **OptoXR = "X-Ray into the G protein"**, skips the voltage and talks to Gα.
:::

:::trap
Channel vs pump. ChR2 is a channel: it opens a door and ions run downhill. HR and BR are pumps: they use light energy to push ions one way. A pump can move ions against their gradient; a channel can't.
:::

:::conn
Use the Lecture 6 rule to predict each tool. Minus coming in (Cl- via HR) makes the inside more negative. Plus going out (H+ via BR) does too. Both hyperpolarize. Plus coming in (ChR2) depolarizes. If you can do "plus in or minus out = up," you never need to memorize which tool excites and which silences.
:::

:::nancy
For OptoXR she writes: "intracellular domains of rhodopsin have been engineered to activate different Galpha proteins and thus controlling intracellular signaling."

Plain version: they swapped the inside loops so light switches on a G protein of their choice. That makes OptoXR the one optogenetic tool that is a GPCR.
:::

### Reading her questions on this lecture {#read-l7}

| If the question says... | She's testing... | How you'd get tricked |
|---|---|---|
| "channelrhodopsin-1" vs "-2" | ChR1 = H+; ChR2 = Na+, K+, Ca2+ | Mixing up which was useful for neurons |
| "is ChR2 a GPCR?" | No, it's the channel itself | Being fooled by 7 helices + retinal |
| "silence a neuron" | Halorhodopsin (Cl- in) or bacteriorhodopsin (H+ out) | Picking ChR2 |
| "two blanks: fire ___, silence ___" | Order | Right pair, wrong order (the MT1 laminin mistake) |
| "how did they get it into the brain" | Virus + cell-specific promoter; fiber optic for light | Saying "injected the protein" |
| "control group" in an experiment | Non-infected mice + light | Ignoring that light alone could cause the effect |
| "retinal isomer" | ChR2: all-trans to 13-cis; rod: 11-cis to all-trans | Using the rod direction for ChR2 |
| "what type of protein is ChR2" | Light-gated cation channel, blue light | Picking GPCR (7 helices and retinal fool you) or pump |
| "blue light hits a ChR2 neuron" | Na+ and other cations in, depolarize toward threshold | Picking Cl- in or K+ in (those are other tools or nothing) |

### Lecture 7 on one page

| Part | Plain-English job | Remember it by |
|---|---|---|
| Optogenetics | light + a gene = remote control for neurons | TV remote |
| Chlamydomonas | alga with two tails and an eyespot; IFT, ciliopathies | Chlamy's two tails |
| ChR1 vs ChR2 | H+ only vs Na+/K+/Ca2+ | 1 ion vs lots |
| ChR2 mechanism | blue 470 nm, all-trans to 13-cis, it's the pore | rod straightens, ChR bends |
| 2005 | one spike per flash in a dish | birthday of optogenetics |
| In animals | virus + promoter, fiber-optic cable | truck and flashlight |
| Experiments | orexin (wake), SFO (drink), aggression | Wake, Drink, Fight |
| Silencers | HR pumps Cl- in, BR pumps H+ out | Halo holds, Bye protons |
| OptoXR | light switches a chosen G protein | talks to Gα, not voltage |
