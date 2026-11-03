## Lecture 6: synaptic signaling and neurons {#l6}

Textbook chapter 11, pages 653-674.

:::story
Chapter 2. Lecture 5 ended with ion channels and the cell as a battery sitting at -70 mV. Neurons use that battery to send a fast electrical pulse down a long wire (the action potential), then pass the message to the next cell with chemicals (neurotransmitters). Calcium comes back as the trigger, this time for releasing chemicals and squeezing muscle.

What you need from before: which ions are crowded inside vs outside (K+ inside, Na+ outside), and what opening a channel does to the voltage (end of Lecture 5).
:::

### The big picture in one paragraph

A neuron is a long electrical wire with a chemical messenger at the end. The message travels along the wire as a wave of sodium rushing in (the action potential). When the wave reaches the end, calcium rushes in and makes little bubbles of chemical (neurotransmitter) dump into a tiny gap. The chemical crosses the gap and opens channels on the next cell. If the next cell is a muscle, the same idea repeats: an electrical wave spreads, calcium is released, and calcium lets the muscle proteins grab each other and pull.

:::hook
The whole lecture in one line: **"Na+ runs the wire, Ca2+ sends the mail, Ca2+ moves the muscle."**
:::

### Three kinds of neurons

:::key
- Afferent (sensory) → CNS; efferent (motor) → out
- Interneurons: inside CNS, largest group
:::

The short version: some neurons bring news in, some send orders out, and most sit in the middle connecting them.

| Type | Direction | Job |
|---|---|---|
| Sensory (afferent) | toward the **CNS** (central nervous system: brain and spinal cord) | carry information from receptors in skin, eyes, ears |
| Motor (efferent) | away from the CNS | carry orders out to muscles and glands |
| Interneurons | inside the CNS | the biggest group; connect sensory to motor |

:::hook
**Afferent Arrives** at the CNS; **Efferent Exits** the CNS. A comes before E in the alphabet, the same order the signal travels.
:::

### Structure of a neuron

:::key
- Dendrites receive → cell body → axon → terminals (one way)

*Skim:* Axon length range: skim.
:::

The short version: antennae in, cable out.

- Cell body: holds the nucleus, the "headquarters."
- Dendrites: many short branches that receive signals, like antennae.
- Axon: one long cable that sends the signal. It can be under 1 mm or more than 1 m long (the ones from your spine to your toes).
- Axon terminals: branches at the end that pass the signal to the next cell.

Signals always travel one way: dendrites → cell body → axon → terminals.

:::hook
"**D**on't **C**ross **A**ny **T**racks": **D**endrites → **C**ell body → **A**xon → **T**erminals.
:::

### The action potential

:::key
- All-or-none, rapid, transient spike
- Depolarize → repolarize → brief hyperpolarize → rest

*Skim:* Exact mV values on the trace: roughly -60 to +50 is enough.
:::

The short version: a quick, full-size voltage spike that runs along the neuron. It's either fully on or not there at all.

An **action potential** is a fast, short electrical spike that travels along the membrane of "excitable" cells (neurons and muscle). It's **all-or-none**: it either fires at full size or doesn't fire. Think of a gun. Squeezing the trigger harder doesn't make a bigger bang. Once the trigger point (called **threshold**) is passed, you get the full spike.

On her recording, the spike goes like this:

| Phase | Voltage | What it means |
|---|---|---|
| Rest | about -60 mV | waiting |
| **Depolarization** | shoots up to about +50 mV | inside goes from negative to positive |
| **Repolarization** | falls back down | heading back to negative |
| **Hyperpolarization** (undershoot) | dips below rest | briefly even more negative than normal |
| Back to rest | about -60 mV | ready again |

The whole spike lasts only a few milliseconds.

{{slide:L6-5|The tall spikes last about 4 ms; notice the dip below the resting line right after each one.}}

{{fig:action_potential}}

:::hook
Picture a wave at a stadium: people stand up (depolarize), sit back down (repolarize), and for a second slouch lower than normal (hyperpolarize) before sitting normally.
:::

:::nancy
She writes: "a rapid, transient, all-or-none electrical activity propagated in the plasma membrane of excitable cells."

Plain version: a quick, short spike that's either full size or not there, which travels along neurons and muscle cells. "Transient" = short-lived. "Excitable cells" = neurons and muscle.
:::

#### Why Na+ rushes in

:::key
- Voltage-gated Na+ channels open → Na+ floods in
- Both gradients (concentration AND voltage) push Na+ in

*Skim:* The ΔG numbers: know both are negative and add up; exact values are low priority.
:::

:::she
"How is an action potential generated and propagated?" Her answer slide: opening of voltage-gated Na+ channels depolarizes the membrane, and the inward movement of Na+ is energetically very favorable.
:::

The short version: both forces push sodium in, so the moment a door opens, it floods in.

- Crowding pushes it in. There's 145 mM Na+ outside and only 12 mM inside.
- Charge pulls it in. The inside is -70 mV, and negative attracts positive.

She puts numbers on this using **free energy (ΔG)**, a measure of how much a process "wants" to happen. Negative ΔG means it happens on its own, like a ball rolling downhill. The crowding part gives ΔGc = -1.45 kcal/mol, the voltage part gives ΔGm = -1.61 kcal/mol, and together ΔG = -3.06 kcal/mol. Both negative, so both push inward. Open a door and Na+ pours in.

:::hook
Na+ coming in is a ball rolling down **two** hills at once (crowding and charge). Add the two hills: -1.45 + -1.61 = -3.06.
:::

:::nancy
She writes: "The inward movement of Na+ ions is energetically very favorable."

Plain version: Na+ rolls downhill into the cell on its own, because both the crowding and the charge push it in.
:::

#### The voltage-gated Na+ channel

:::key
- States: Closed (ready), Open, Inactivated (plugged, can't open)
- S4 helices = voltage sensors
- Inactivation = refractory period

*Skim:* 4 domains x 6 helices: recognize.
:::

The short version: a sodium door with a voltage sensor that opens it and a plug that shuts it a moment later.

The channel is one long protein folded into **four similar domains**, and each domain has **six helices** crossing the membrane. In each domain, the fourth helix (**S4**) is covered in positive charges and acts as the **voltage sensor**. Hanging in the cytosol there's also an **inactivation gate**, a "ball" on a floppy loop.

:::hook
"**4 rooms, 6 walls, wall 4 is the sensor.**"
:::

The channel has three states:

{{slide:L6-10|Closed, open, inactivated. Look for the inactivation segment plugging the pore in step 3.}}

1. **Closed** (at rest, -70 mV). The door is shut, but it's ready and can open.
2. Open. When the membrane depolarizes a bit, the positive S4 sensors get pushed outward (same charges repel), and the door opens in under 0.1 ms. Na+ rushes in. That depolarizes the next patch of membrane even more, which opens more channels. This self-feeding loop is called **positive feedback**.
3. Inactivated. Within about 0.5-1 ms, the inactivation ball swings in and plugs the pore from the inside. Now the channel can't open again, even if the voltage is still high. This "can't fire yet" window is the **refractory period**.

Only after the membrane goes back to negative do the S4 sensors move back and the plug pop out, resetting the channel to closed (this takes a few ms).

{{fig:na_states}}

{{3d:na|Watch the S4 sensors move, Na+ pour in, then the plug swing up from the cytosol.}}

:::hook
**Closed, Open, Inactivated = "COIN".** Closed is "ready," Inactivated is "on cooldown." Like a phone's camera flash: it can't fire again until it recharges.
:::

:::trap
Closed and inactivated are different. A closed channel CAN open if the membrane depolarizes. An inactivated channel CANNOT, no matter what. This difference is what makes the action potential travel in only one direction.
:::

#### How the resting potential comes back

:::key
- Na+ channels inactivate AND delayed K+ channels open
- Slow K+ channels cause the undershoot
:::

The short version: shut off the sodium, let potassium out.

Two things happen together to bring the voltage back down (repolarize):

1. The Na+ channels inactivate, so Na+ stops coming in.
2. Voltage-gated K+ channels open. They're also called **delayed K+ channels**, because they respond to depolarization more slowly than the Na+ channels do. K+ rushes out (it's crowded inside), carrying plus charge out and pulling the voltage back down. They stay open a little too long, which causes the brief dip below rest (the undershoot).

{{slide:L6-13|The bars under the graph show the delay: Na+ channels open first, the K+ channels open later and stay open longer.}}

:::hook
"**Sodium first, potassium late.**" Na+ is the sprinter who starts the spike, K+ is the slowpoke who ends it and overshoots the finish line.
:::

### Why action potentials only travel forward

:::key
- Channels behind the spike are INACTIVATED, so it can't go back
- Channels ahead are closed (ready) and fire

*Skim:* PET scan slide: just the link that active brain areas and tumors both use lots of glucose.
:::

:::she
"How is an action potential propagated unidirectionally??"
:::

The short version: the patch behind the spike is on cooldown, so the spike can only move forward.

When one patch of axon depolarizes, the Na+ that came in spreads sideways inside the axon and nudges the patches on both sides. But:

- The patch **ahead** has Na+ channels that are **closed** (ready), so they open and fire.
- The patch **behind** has Na+ channels that are **inactivated** (on cooldown), so they can't fire.

So the spike can only move into fresh territory.

{{slide:L6-15|Inactivated channels (left of the open ones) block the backward path, so the wave only moves right.}}

In her figure, three electrodes (V1, V2, V3) along the axon record the same spike at 0, 1 and 2 ms. Same size, just later.

:::hook
Like a line of dominoes that need a few seconds to be stood back up. The wave can only travel toward dominoes still standing.
:::

:::conn
The PET scan slide (seeing, thinking and hearing light up visual cortex, prefrontal cortex and auditory cortex) is the big-picture version. A PET scan tracks radioactive glucose, and brain regions firing lots of action potentials burn more glucose. Remember this for Lecture 9: cancer cells also gobble glucose (the Warburg effect), and the same PET trick finds tumors.
:::

{{slide:L6-16|Different tasks light up different cortex areas because firing neurons burn more glucose.}}

:::nancy
She asks: "How is an action potential propagated unidirectionally??"

Plain version: "Why does the spike only go one way?" The answer she wants is the inactivated Na+ channels behind the spike, not myelin.
:::

### Myelin and saltatory conduction

:::key
- Myelin insulates; Na+ channels packed at nodes of Ranvier
- Spike jumps node to node (saltatory) = much faster
- Schwann cells = PNS, oligodendrocytes = CNS
- MS = CNS myelin; Guillain-Barré = PNS gangliosides, after infection
:::

The short version: myelin is insulation that lets the signal hop between gaps, which makes it much faster.

Many axons in animals with backbones are wrapped in a **myelin sheath**: many layers of membrane wound around the axon by **glial cells** (support cells), like electrical tape wrapped around a wire. Myelin insulates, so very little current leaks out.

| | Who makes myelin |
|---|---|
| **PNS** (peripheral nervous system: nerves outside the brain and spinal cord) | Schwann cells |
| **CNS** (brain and spinal cord) | oligodendrocytes |

:::hook
"**S**chwann = **S**ide (peripheral). **O**ligodendrocyte = **O**nly in the brain and spinal cord."
:::

The sheath has small gaps about every 1 mm called **nodes of Ranvier**. The voltage-gated Na+ channels are packed into these nodes. The current zips quickly under the insulated stretches and only has to be rebuilt at each node, so the action potential "jumps" from node to node. This is **saltatory conduction**, from the Latin for "to leap."

{{slide:L6-18|Na+ enters only at the nodes; the micrograph shows a node of Ranvier between two myelin segments.}}

Result: a myelinated axon conducts much faster than an unmyelinated axon of the same size. Her slide leaves the two speeds blank for you to fill in. Textbook ballpark: around 1 m/s for a thin unmyelinated axon, up to about 100 m/s for a myelinated one.

{{fig:myelin}}

{{3d:axon|Race the spike on a myelinated vs unmyelinated axon, then slow it down to see why it only goes forward.}}

:::hook
Myelin turns the action potential from a walker into a hopscotch player. Skip the insulated squares, land only on the nodes. "**Salt**atory" sounds like "**salt**o" (a flip or jump).
:::

:::she
Human Perspective on demyelination diseases. Multiple sclerosis: the immune system attacks myelin in the CNS (brain and spinal cord); symptoms include muscle weakness, balance, speech and vision problems; cause unknown and doesn't seem hereditary. Guillain-Barré syndrome: the immune system attacks gangliosides that are enriched in PNS myelin, often after fighting an infection; causes paralysis and is one of the leading causes of non-trauma paralysis worldwide.
:::

| | Multiple sclerosis (MS) | Guillain-Barré syndrome |
|---|---|---|
| Where | CNS (brain, spinal cord) | PNS (body nerves) |
| What's attacked | myelin | gangliosides (a glycolipid) in PNS myelin |
| Trigger | unknown, not clearly inherited | often after an infection |
| Result | weakness, balance, speech, vision problems | paralysis |

:::trap
MS = CNS. Guillain-Barré = PNS. Easy marks if you keep them straight. Both are the immune system attacking myelin.
:::

:::hook
"**M**S = **M**ain office (brain, spinal cord). **G**uillain-Barré = **G**oes out to the body."
:::

:::nancy
Two things on these slides read harder than they are. Her myelin slide leaves the two speeds blank ("velocity... non-myelinated axon -" and "myelinated axon -"), so fill them from class. And for Guillain-Barré she writes the host "mounts an immune response to a foreign pathogen and instead the immune system attacks gangliosides."

Plain version of that: you fight off an infection, and the immune system gets confused and attacks the insulation on your body's nerves.
:::

### The synapse

:::key
- Released by exocytosis into the cleft
- Bind ligand-gated channels (fast) or GPCRs (slow)
- Removed quickly

*Skim:* Which amino acid each transmitter comes from: low priority.
:::

The short version: a synapse is a tiny gap between two cells. The first cell spits chemicals into the gap, and the second cell catches them.

A **synapse** is the contact point where a neuron passes its signal to the next cell.

- The sending side is **presynaptic** ("before the synapse").
- The receiving side is **postsynaptic** ("after the synapse").
- The tiny gap between them is the **synaptic cleft**.

Three facts from her slide:

1. Neurotransmitters leave the presynaptic cell by **exocytosis**: little bubbles (vesicles) merge with the membrane and dump their contents out into the cleft.
2. They bind either **ligand-gated ion channels** on the postsynaptic cell (fast) or **GPCRs** (slower).
3. They're removed quickly after release, so the signal is short.

Most neurotransmitters are made from amino acids:

| Neurotransmitter | Made from |
|---|---|
| acetylcholine, glycine, glutamate | on her list; glycine and glutamate are amino acids themselves |
| dopamine, norepinephrine, epinephrine | tyrosine |
| serotonin | tryptophan |
| histamine | histidine |
| GABA | glutamate |

:::hook
"**Ty**rosine **Ty**pes the 'catecholamines' (dopamine, norepinephrine, epinephrine). **Try**ptophan gives you the happy one (serotonin). **Hist**idine gives **hist**amine. GABA comes from **G**lutamate."
:::

#### Release, step by step

:::key
- Vesicles loaded by H+ antiporter (V-type pump makes the H+ gradient)
- AP opens VOLTAGE-gated Ca2+ channels; Ca2+ binds synaptotagmin
- SNAREs fuse the vesicle; botulinum cuts SNAREs
- Recycled by endocytosis (dynamin; shibire flies)
:::

The short version: load the bubble, park it, wait for calcium, pop it, recycle it, clean up.

1. Load. A pump (V-class H+ pump) spends ATP to fill the vesicle with H+ (protons). Then an **H+ antiporter** lets one H+ out in exchange for pulling one neurotransmitter in. ("Antiporter" means two things move in opposite directions through one protein.) So the proton gradient, not ATP directly, powers the loading.
2. Park (dock). Loaded vesicles move to the "active zone" and dock at the membrane. **SNARE** proteins on the vesicle (v-SNAREs, like **VAMP**) twist together with SNAREs on the cell membrane, pulling the two close. A calcium-sensing protein called **synaptotagmin** holds them back from merging yet.
3. Trigger. The action potential reaches the end of the axon and opens **voltage-gated Ca2+ channels**. Ca2+ rushes in and binds synaptotagmin.
4. Pop (fusion). The vesicle merges with the membrane and neurotransmitter spills into the cleft.
5. Recycle. The vesicle membrane gets pulled back into the cell by **endocytosis** (a coat protein called clathrin shapes it, and a protein called **dynamin** pinches it off), then gets refilled.
6. Clean up. The neurotransmitter is cleared from the cleft by **reuptake transporters** (pumps powered by the Na+ gradient that pull it back into the neuron) or broken down by enzymes.

{{slide:L6-23|The numbered cycle: import, move to active zone, dock, Ca2+-triggered fusion. Botulinum toxin blocks at the SNARE step.}}

{{fig:synapse}}

{{3d:syn|Ca2+ in, vesicles fuse, transmitter crosses, receptors open. Try botulinum toxin.}}

:::hook
**Ca2+ is the "send" button.** The message (vesicle) is typed and loaded, but nothing goes out until calcium hits send. SNAREs are the zipper that pulls the envelope to the mailbox.
:::

Two ways her figure breaks this cycle:

| Breaker | What it breaks | Result |
|---|---|---|
| **Botulinum toxin** | cuts SNARE proteins | vesicles can't fuse, no neurotransmitter released, paralysis |
| **shibire** mutation (fruit flies) | breaks dynamin | vesicles can't be recycled; flies become paralyzed when warm |

:::hook
"**Botox Breaks the zipper**" (SNAREs). "**Shibire**" sounds like "shivering" and the flies freeze up when warm because their recycling stops.
:::

:::trap
The Ca2+ channel at the nerve ending is voltage-gated (opened by the action potential), not ligand-gated. And the vesicle is loaded by an H+ antiporter, not by ATP directly.
:::

#### Excitatory vs inhibitory

:::key
- Excitatory: cation channels, Na+/Ca2+ in, depolarize
- Inhibitory (GABA, glycine): K+ out or Cl- in, harder to fire
:::

The short version: excitatory signals push the next cell toward firing, inhibitory ones hold it back.

| | Excitatory | Inhibitory |
|---|---|---|
| Examples | acetylcholine (at muscle), glutamate (in brain) | GABA, glycine |
| Channel opened | **cation channels** (cations = positive ions) | **K+ or Cl- channels** |
| Ion flow | Na+ and Ca2+ flow in | K+ flows out, or Cl- flows in |
| Effect on the voltage | depolarizes, moves toward **threshold** (the firing point) | keeps it at rest or more negative |
| Next cell | more likely to fire | less likely to fire |

:::hook
Excitatory = "plus charges come in, the cell gets excited." Inhibitory = "plus goes out or minus comes in, the cell calms down." **GABA = "Gotta Always Be Asleep."**
:::

### The neuromuscular junction (NMJ)

:::key
- NMJ receptor = nicotinic: a 5-subunit cation channel, needs 2 ACh
- Heart receptor = muscarinic GPCR; same ACh, opposite effect
:::

The short version: the synapse between a nerve and a muscle, using acetylcholine and a channel-type receptor.

The **neuromuscular junction (NMJ)** is the synapse between a motor neuron and a skeletal muscle cell. The neurotransmitter is **acetylcholine (ACh)**. The ACh receptor on the muscle is a **nicotinic acetylcholine receptor**: a channel made of five subunits in a ring around a central pore. Two ACh molecules must bind (one on each of the two α subunits) to open it. When open, it lets cations through.

:::trap
At the NMJ, the ACh receptor is a ligand-gated ion channel (nicotinic). In the heart (Lecture 5), the ACh receptor is a GPCR (muscarinic). Same neurotransmitter, two different receptor types, opposite effects: skeletal muscle contracts, the heart slows down.
:::

| | Nicotinic ACh receptor | Muscarinic ACh receptor |
|---|---|---|
| Where | skeletal muscle (NMJ) | heart |
| Type | ion channel (5 subunits, 2 ACh needed) | GPCR (Gi, Gβγ opens K+) |
| Effect | depolarize, contract | hyperpolarize, slow down |
| Speed | fast | slower |

:::hook
"**N**icotinic = **N**MJ, **N**ow (fast channel). **M**uscarinic = **M**ellow heart (slow GPCR)."
:::

:::nancy
She writes "transmitted gated cation channel."

Plain version: that's a typo for transmitter-gated, which means the same as ligand-gated: a channel that opens when the neurotransmitter binds.
:::

#### Five channels from nerve to contraction

:::key
- Order: nerve Ca2+ → nicotinic AChR → muscle Na+ → T-tubule Ca2+ sensor → SR Ca2+ release
- The big Ca2+ rise comes from the SR
:::

:::easy
Both-boxes trap: acetylcholine excites skeletal muscle (nicotinic channel) and slows the heart (muscarinic GPCR). If a question asks whether ACh is excitatory or inhibitory, the answer depends on the receptor.
:::

The short version: calcium in the nerve, sodium in the muscle, then the muscle's calcium tank opens.

Her slide says the trip from nerve to contraction uses five different ion channels. In order:

1. Nerve: voltage-gated Ca2+ channels in the motor neuron ending open when the action potential arrives. Ca2+ triggers ACh release.
2. Muscle surface: ACh-gated cation channels (nicotinic receptors) open. Na+ flows in and that patch of muscle membrane depolarizes.
3. Muscle surface: voltage-gated Na+ channels open and fire an action potential that spreads over the muscle surface and down into the **T tubules** (tunnels of membrane that dive deep into the muscle fiber so the signal reaches the middle).
4. T tubule: voltage-gated Ca2+ channels sense the depolarization and change shape. They work here mainly as voltage sensors.
5. Calcium tank: Ca2+-release channels of the **sarcoplasmic reticulum** (SR, the muscle's version of the ER, its calcium storage tank) are pulled open by that shape change. Ca2+ floods the cytosol.

{{slide:L6-30|Five channels in numbered order, from the nerve terminal Ca2+ channel to the SR Ca2+-release channel.}}

{{fig:nmj_chain}}

{{lab:nmj|nerve to muscle (botulinum, curare, sarin)}}

:::hook
Order of the five: "**Ca, ACh, Na, Ca, Ca**." Read it as "**Call A Nurse, Call Charlie**." One calcium door in the nerve, then ACh and Na+ on the muscle surface, then two calcium doors inside the muscle.
:::

:::she
"How does an increase in intracellular Ca2+ result in contraction of a muscle cell??" She put this question on two slides in a row.
:::

:::nancy
She writes: "the opening of acetylcholine-gated cation channels leads to an influx of Ca2+ in the muscle cell (involves 5 different ion channels)."

Plain version: this makes it sound like the ACh channel itself lets the calcium in. It mainly lets Na+ in. The big Ca2+ rise comes from the SR at the end of the five-channel chain. Read her sentence as "opening the ACh channel starts a chain that ends with Ca2+ flooding the muscle."
:::

#### Sarcomeres and the sliding filament model

:::key
- Myosin pulls actin; Z disks move closer
- Filaments stay the SAME length

*Skim:* The muscle-to-myofibril hierarchy: recognize.
:::

The short version: muscle is built from repeating units where two kinds of fibers overlap. Contraction is the fibers sliding past each other, not shrinking.

How a muscle is built, from big to small:

muscle → bundle of long **muscle fibers** (each one cell with many nuclei) → each fiber is packed with **myofibrils** → each myofibril is a chain of repeating units called **sarcomeres**

A sarcomere runs from one **Z disk** to the next. Thin filaments made of **actin** are anchored to the Z disks. Thick filaments made of **myosin** sit in the middle and overlap with the actin.

In the **sliding filament model**, the myosin heads grab actin and pull the thin filaments toward the middle of the sarcomere, using ATP for energy. The filaments themselves don't get shorter. They slide past each other, and the Z disks get pulled closer together.

{{slide:L6-33|Relaxed vs contracted: the filaments keep their length, the Z disks move closer.}}

:::hook
Think of two hands with fingers interlaced. Push them together and the hands (Z disks) get closer, but your fingers (filaments) stay the same length. Myosin is the **M**otor in the **M**iddle; actin is the rope it pulls.
:::

#### The role of Ca2+

:::key
- Ca2+ binds TROPONIN, which moves TROPOMYOSIN
- That uncovers myosin-binding sites on actin
- Ca2+ pumped back into SR = relax
:::

The short version: at rest, a rope blocks myosin from grabbing actin. Calcium moves the rope.

Two control proteins wrap along each actin filament:

- Tropomyosin: a long rod that lies over the spots where myosin wants to grab actin. At rest, it blocks them.
- Troponin: a small complex sitting on tropomyosin. This is the part that senses calcium.

When Ca2+ rises, it binds **troponin**. Troponin changes shape and drags tropomyosin to a new position, uncovering the grab spots on actin. Myosin grabs on and the muscle contracts. When Ca2+ is pumped back into the SR, tropomyosin slides back over the spots and the muscle relaxes.

{{slide:L6-34|In the 3D reconstruction, tropomyosin (TM) slides over once Ca2+ is added, uncovering the myosin-binding sites.}}

{{3d:sarc|Ca2+ binds troponin, tropomyosin rolls aside, myosin pulls, Z disks close in while the filaments keep their length.}}

:::hook
Tropomyosin is a "Do Not Touch" rope over the actin. Ca2+ talks to the security guard (troponin), and the guard moves the rope. "**Ca2+ talks to TropoNIN, TropoMYOSIN moves.**" Calcium never touches the rope directly.
:::

:::conn
Ca2+ is the trigger twice in the same story: it releases neurotransmitter at the nerve ending, and it uncovers actin in the muscle. In Lecture 5, calcium was released from the ER by IP3. Here it's released from the SR by voltage-sensing channels in the T tubule. Different door, same calcium-vault idea.
:::

### Drugs and toxins at the synapse

:::key
- Cocaine (dopamine) and SSRIs (serotonin) block reuptake → longer signal
- Sarin blocks acetylcholinesterase → too much ACh
- Curare blocks the muscle ACh receptor → paralysis
- Valium helps GABA open Cl- channels → hyperpolarize, fire less
:::

:::she
Human Perspective: neurotransmitters, their transporters, and transmitter-gated channels are targets of many drugs.
:::

The short version: drugs either block cleanup (signal lasts longer), block the receptor (no signal), or boost the receptor.

| Drug | What it targets | What happens |
|---|---|---|
| Cocaine | dopamine transporter (reuptake) | dopamine stays in the gap longer, signal lasts longer |
| Prozac and other **SSRIs** (selective serotonin reuptake inhibitors) | serotonin reuptake | serotonin stays longer; used as antidepressants |
| Sarin (nerve gas) | **acetylcholinesterase**, the enzyme that breaks down ACh in the gap | ACh builds up, muscles can't stop being stimulated; very deadly |
| Curare (South American plant extract) | ACh receptors on muscle | blocks them, paralysis |
| Valium (diazepam) and other benzodiazepines | GABA receptor (a Cl- channel) | helps GABA work, neuron fires less |

How Valium works, in plain words: it's a **positive allosteric modulator** of the GABA receptor. "Allosteric" means it binds somewhere other than GABA's own spot and changes the receptor's shape; "positive" means the shape change helps. GABA binds better, more Cl- flows in, the neuron gets more negative (hyperpolarizes), the gap between rest and threshold gets bigger, and firing becomes less likely. That's the calming effect.

:::hook
"**Cocaine and Prozac Clog the vacuum** (reuptake). **Sarin Stops the cleaner** (esterase). **Curare Covers the lock** (receptor). **Valium Volumes up GABA.**"
:::

:::trap
Sarin and curare both hit the NMJ but in opposite directions. Sarin blocks the cleanup enzyme, so there's too much ACh signaling. Curare blocks the receptor, so there's no ACh signaling. Ask: does the drug block the receptor or block the off switch?
:::

:::nancy
For Valium she writes: "positive allosteric modulators... increases the total conduction of chloride ions... As a result, the difference between resting potential and threshold potential is increased."

Plain version: Valium binds a different spot on the GABA receptor and helps GABA work, more Cl- comes in, and the neuron ends up further from its firing point.
:::

### How to figure it out: what does opening this channel do to the membrane? {#howto-membrane}

How to spot it: a question names an ion channel, a drug that opens or blocks one, or a change in ion levels, and asks about voltage, firing, or excitability.

Steps:

1. Which ion? Remember where it's crowded: Na+, Ca2+ and Cl- are high outside, K+ is high inside.
2. Which way does it flow when the door opens? Na+ and Ca2+ flow in. K+ flows out. Cl- usually flows in (smell neurons are the exception, because they keep Cl- high inside).
3. What charge moves which way?
   - Plus coming in, or minus going out → inside more positive → **depolarization** (more likely to fire).
   - Plus going out, or minus coming in → inside more negative → **hyperpolarization** (less likely to fire).
4. Next consequence: more or less neurotransmitter, more or fewer action potentials, faster or slower heart.

:::hook
"**Plus in or minus out = up. Plus out or minus in = down.**"
:::

Practice:

- Valium strengthens GABA receptor Cl- channels. Cl- (negative) comes in, the inside gets more negative, hyperpolarization, the neuron fires less. Calming.
- Light closes cGMP-gated cation channels in a rod. Fewer plus ions come in, hyperpolarization, less neurotransmitter.
- The muscarinic receptor in the heart opens K+ channels via Gβγ. K+ (positive) leaves, hyperpolarization, slower heartbeat.
- A toxin holds voltage-gated Na+ channels in the inactivated state. No action potentials can fire, so paralysis. (Inactivated can't open.)
- A drug blocks the delayed K+ channels. Repolarization slows, so the action potential lasts longer and the cell takes longer to recover.
- Channelrhodopsin (Lecture 7) opens and lets Na+, K+ and Ca2+ through. Net effect: mainly Na+ in, so depolarization and firing.

### Reading her questions on this lecture {#read-l6}

| If the question says... | She's testing... | How you'd get tricked |
|---|---|---|
| "refractory" or "cannot fire again" | Na+ channel inactivated | Calling it closed |
| "why does the AP move one way" | Inactivated channels behind the spike | Answering "myelin" |
| "myelin damage in brain" vs "in peripheral nerves" | MS (CNS) vs Guillain-Barré (PNS) | Swapping them |
| "triggers transmitter release" | Voltage-gated Ca2+ channels, synaptotagmin | Saying Na+ or a ligand-gated channel |
| "blocks acetylcholinesterase" | Too much ACh (sarin) | Mixing up with curare (blocks receptor) |
| "inhibitory neurotransmitter" | K+ out or Cl- in | Saying "closes Na+ channels" |
| "Ca2+ binds..." in muscle | Troponin, which moves tropomyosin | Saying Ca2+ binds tropomyosin or myosin |
| "five channels" at the NMJ | The exact order nerve to SR | Skipping the T-tubule voltage sensor |
| "Valium" | Helps GABA open Cl- channels, hyperpolarizes | Saying it blocks GABA |

### Lecture 6 on one page

| Part | Plain-English job | Remember it by |
|---|---|---|
| Action potential | all-or-none voltage spike | a gun, not a dimmer |
| Na+ channel | door with sensor (S4) and plug | COIN: Closed, Open, Inactivated |
| K+ channel | delayed door that ends the spike | sodium first, potassium late |
| One-way travel | the patch behind is on cooldown | dominoes being reset |
| Myelin | insulation, hop between nodes | hopscotch, Schwann = side |
| MS vs Guillain-Barré | CNS vs PNS myelin attack | Main office vs Goes out |
| Synapse release | Ca2+ in, synaptotagmin, SNAREs zip | calcium is the send button |
| Botulinum / shibire | cuts SNAREs / breaks dynamin | Botox breaks the zipper |
| NMJ | nicotinic channel, 5 channels to contraction | Call A Nurse, Call Charlie |
| Sarcomere | filaments slide, Z disks close in | interlaced fingers |
| Ca2+ in muscle | binds troponin, tropomyosin moves | talks to the guard, not the rope |
| Drugs | reuptake / esterase / receptor / boost | clog, stop, cover, volume up |
