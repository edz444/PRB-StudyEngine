## Practice, worked {#practice}

Her lab-quiz practice sheet, reworked in plain words. Try each before opening the answer. They also appear in each week's boss level.

### Her practice set {#practice-hers}

:::exam
How her lab quiz tests you:

- Calculations with your work shown (the hemocytometer seeding volume).
- 'Explain or sketch' a mechanism (transfection, myocardin, a droplet).
- 'Give 2-3 reasons' answers, where each reason needs a because.
- 'What do the data show vs mean' on a ddPCR plot: two separate answers.
:::

:::q
(Her Q1, L1) You count 87, 91, 83 and 85 cells in four 75 nL quadrants. What volume seeds 400,000 cells?
???
Average 86.5 per quadrant. 86.5 / 75 nL = 1.153 x 10^6 cells/mL. 400,000 / 1,153,333 = 0.347 mL, about 347 uL.
:::

:::q
(Her Q2, L3) Draw a myocardin-regulated gene with and without myocardin (practice Q1).
???
Both: SRF on the CArG box in the promoter, then the contractile coding region. Without myocardin: little or no transcription. With myocardin: myocardin bound to SRF, Pol II recruited, lots of mRNA, then contractile protein and differentiation.
:::

:::q
(Her Q3, L3) How does a transfection reaction get plasmid DNA into a7r5 cells (practice Q2b)?
???
Cationic lipid reagent wraps the negative plasmid into complexes that stick to the negative cell surface and are taken in by endocytosis; the DNA escapes to the cytoplasm and reaches the nucleus. Label the plasmid and your reagent names.
:::

:::q
(Her Q4, L3) What is the purpose of GFP in the transfection experiments (practice Q2d)?
???
A no-stain reporter that marks plasmid-expressing cells (green = also making myocardin), used for transfection efficiency and to pick transfected cells; pEGFP is the control.
:::

:::q
(Her Q5, L4) Why is it useful to run RNA on a gel if you can't see the mRNA (practice Q4d)?
???
Sharp 28S and 18S rRNA bands at about 2:1 with no smear mean no RNase degraded the sample, so mRNA should be intact too. The gel also shows genomic DNA contamination.
:::

:::q
(Her Q6, L4) Why not measure DNA by spectrophotometry after reverse transcription (practice Q4b)?
???
The tube still has RNA, primers and nucleotides, which all absorb at 260 nm, so the reading can't isolate your cDNA.
:::

:::q
(Her Q7, L5) Give three tips so images across conditions can be compared quantitatively (practice Q3a).
???
Identical exposure/gain/intensity per channel; set exposure so nothing saturates; choose fields without bias and take several per condition; save raw files.
:::

:::q
(Her Q8, L5) Rico's phalloidin cells show high red background. Suggest two mistakes (practice Q3b).
???
Not washing enough after phalloidin (unbound dye left behind); too much dye or too long a stain (non-specific binding). Also: cells dried out, or red gain set too high.
:::

:::q
(Her Q9, L6) Sketch a blue and a gray droplet at the start and end of ddPCR (practice Q5a).
???
Blue start: one target plus reagents, dye unbound (dim). Blue end: lots of dsDNA product, dye bound, bright. Gray start: reagents, no target. Gray end: no product, still dim.
:::

:::q
(Her Q10, L7) All of Rico's droplets are labelled blue. Why isn't that the result he wants (practice Q5c)?
???
No negative droplets means the reaction is saturated and Poisson can't count it (could be 3 or 300 copies per droplet). Dilute and rerun. It could also be a mis-set threshold or contamination.
:::

:::q
(Her Q11, L7) How could Rico tell which primer set was in which well (practice Q5b)?
???
Each primer set gives a characteristic positive amplitude (product length and efficiency), so match band heights to known runs, or run the products on a gel and match sizes.
:::


### Deeper cuts, predicted and harder {#practice-deep}

These are not from her sheet. They are harder questions in the same lab-quiz style, built to make you reason across techniques rather than recall one fact. Each also shows up in its week's boss level, after her real questions.

:::q
(Predicted deep cut, L1) You seed two 35 mm dishes from the same tube at 400,000 cells each. At day 7, one dish is confluent and the other is half empty, with no sign of infection. Give three reasons that are not a counting mistake.
???
The suspension was not fully resuspended, so one dish drew a denser draw and the other a thinner one. Cells settle in the tube between pipetting, so the second dish seeded fewer live cells. Dead cells were counted as live (no trypan blue), so one dish had fewer that actually attached. Edge or incubator effects (evaporation, uneven temperature, position) slowed one dish. The lesson: seeding by a hemocytometer count assumes the tube is uniform and every counted cell is alive.
:::

:::q
(Predicted deep cut, L1) Your four quadrant counts are 210, 8, 190 and 205. What do you do before calculating, and what density do you report?
???
Do not average the 8 in blindly. It is an outlier, almost certainly a quadrant that did not fill or had a bubble. Recount if you can, or drop it and use the three agreeing quadrants (about 202). 202 / 75 nL = 2.7 x 10^6 cells/mL. The point is to sanity-check your replicates, not to trust the arithmetic over your eyes.
:::

:::q
(Predicted deep cut, L1) Why count cells in suspension before seeding instead of imaging the attached dish and counting there?
???
In suspension the cells are separate and sit in a known volume, so density is defined and you can seed an exact number. Attached cells overlap, spread by different amounts and represent no known volume, so you cannot turn a dish image into an absolute concentration. The hemocytometer gives you a number you can actually seed with.
:::

:::q
(Predicted deep cut, L2) A dye excites at 488 nm and emits at 510 nm. Your Zoe has only the blue (excite 355, collect 433) and green (excite 480, collect 517) channels loaded. Which channel, and what goes wrong if you pick blue?
???
Use green: 480 excites near the dye's 488, and 517 collects near its 510. Blue would try to excite at 355, which barely excites this dye, and collect at 433, which is below the 510 emission, so you would see almost nothing or only bleed-through. You have to match both filters, not just one.
:::

:::q
(Predicted deep cut, L2) Hoechst and WGA are both on the cells. In the green channel you see the membrane but also faint nuclei. Give two reasons.
???
Bleed-through: Hoechst's emission has a tail that reaches into the green collection band, or the green excitation light slightly excites Hoechst. WGA can also bind sugar groups on the nuclear envelope, putting real signal near the nucleus. Single-stain controls and tighter settings tell you which it is. Channels are never perfectly clean.
:::

:::q
(Predicted deep cut, L2) You image three conditions to compare brightness. Which change makes the comparison invalid? A. Using the same exposure for all three. B. Setting exposure on the brightest condition first. C. Raising the gain for only the dim condition so you can see it. D. Collecting every channel before moving the stage.
???
C. Changing gain or exposure for one condition means brightness no longer reflects the cells, so you cannot compare across conditions. The other three are exactly what keeps the comparison fair.
:::

:::q
(Predicted deep cut, L3) A labmate transfects pMYOCD-IRES-GFP and sees bright green cells, but ddPCR shows no rise in alpha-SMA. Give three explanations.
???
Green only proves the plasmid is expressed, not that myocardin worked. The IRES may make GFP well while myocardin is made poorly or misfolds. It may be too early, since the downstream genes need time to transcribe and the RNA to build up. Or the cells lack a cofactor myocardin needs, or the ddPCR primers/normalization are off. GFP is a transfection marker, not proof of the myocardin effect.
:::

:::q
(Predicted deep cut, L3) Why is pEGFP (GFP only) a better control than untransfected cells for judging myocardin's effect on actin?
???
pEGFP cells go through the same transfection stress and make a foreign protein, just without myocardin. So any actin change in pMyo above pEGFP is from myocardin itself. Untransfected cells never felt the reagent, the endocytosis or the load of expressing a foreign protein, so they would not separate those effects from myocardin's.
:::

:::q
(Predicted deep cut, L3) Transfected plasmid is lost as cells divide. Why read out after a few days, and what would change if the gene integrated into the genome?
???
Transient expression climbs then fades, so you measure in the window while it is high, a few days in. If the plasmid integrated into a chromosome it would be copied with the genome and passed to every daughter cell, so expression would persist and you could select a stable line and read out much later.
:::

:::q
(Predicted deep cut, L4) Your A260/A280 is 2.0 but the gel shows a smear with faint 28S and 18S bands. Is the RNA good? What does each test actually tell you?
???
No. A260/A280 checks purity, mainly protein contamination, and 2.0 says it is clean. It says nothing about whether the RNA is intact. The smear with weak rRNA bands means the RNA is degraded. You need both tests: the ratio for contamination, the gel for integrity. Clean but chopped up is still unusable.
:::

:::q
(Predicted deep cut, L4) You skip shearing the genomic DNA, and later a no-RT control still gives an alpha-SMA ddPCR signal. Explain.
???
Without reverse transcriptase there is no cDNA, so any signal cannot come from mRNA. It is leftover genomic DNA being amplified, because the alpha-SMA gene exists in the genome. That is why you shear or remove DNA and run a no-RT control: it catches genomic contamination masquerading as expression.
:::

:::q
(Predicted deep cut, L4) How does using poly-T primer for reverse transcription change what you can detect, compared with random primers?
???
Poly-T only primes RNA with a poly-A tail, so you copy mRNA and miss rRNA and tRNA, and you bias toward the 3' end. Random primers prime everywhere and along the whole length, so they copy all RNA types. If your target is a mature mRNA, poly-T enriches it; if you need full-length coverage or non-polyA RNA, you want random primers.
:::

:::q
(Predicted deep cut, L5) Same exposure, and pMyo actin looks dimmer than pEGFP. Before concluding myocardin lowers actin, what must you rule out?
???
Everything that changes brightness that is not actin amount: fewer or flatter cells in that field, different cell density, a slightly off focus plane, uneven staining or washing, bleaching between captures, and different transfection efficiency. You need matched fields and a per-cell measure, not one image, before you blame myocardin.
:::

:::q
(Predicted deep cut, L5) You permeabilize too harshly (long, strong detergent). How could that corrupt both your actin image and your transfection-efficiency count?
???
Over-permeabilizing extracts soluble protein and can wash cytoplasmic GFP out of the cells and pull apart F-actin. The phalloidin signal dims, so morphology looks wrong, and the GFP dims, so transfected cells read as GFP-negative and your transfection efficiency comes out too low. One protocol slip damages two readouts at once.
:::

:::q
(Predicted deep cut, L5) Why can a saturated (255) GFP image make transfection efficiency look too high?
???
Saturated pixels bloom, spreading bright signal into neighbouring pixels, and raise the background so that dim or autofluorescent cells cross your positive threshold. Borderline cells get counted as green. Set exposure so nothing clips at 255, and set the threshold against a no-GFP control dish.
:::

:::q
(Predicted deep cut, L6) GAPDH reads 1500, 1400 and 1600 copies in DM, pMyo and pEGFP. Alpha-SMA reads 100, 260 and 150. Which condition raised alpha-SMA most, and by how much over the control?
???
Normalize to GAPDH: DM 100/1500 = 0.067, pMyo 260/1400 = 0.186, pEGFP 150/1600 = 0.094. pMyo is highest. Against the right control, pEGFP, it is 0.186 / 0.094, about 2-fold. The raw 260 looks big, but you only trust it after normalizing and comparing to pEGFP, not DM.
:::

:::q
(Predicted deep cut, L6) Why is ddPCR better than endpoint PCR for showing a 2-fold difference, and why might qPCR give a different number than ddPCR?
???
Endpoint PCR plateaus, so a 2-fold difference at the start looks identical at the end. ddPCR counts absolute molecules, so a real 2-fold shows up as twice the positive droplets. qPCR is relative and leans on a standard curve and amplification efficiency, so inefficiency or primer differences move its numbers, while ddPCR's droplet counting barely cares about efficiency. They can disagree on the exact value.
:::

:::q
(Predicted deep cut, L6) Every droplet in a reaction is positive. Which is NOT a valid next step? A. Dilute the cDNA and run it again. B. Check the threshold is not sitting inside the negative band. C. Report the concentration from the positive fraction. D. Suspect contamination or primer-dimer.
???
C. With no negative droplets the Poisson math cannot give a concentration, so reporting one is wrong. Diluting, checking the threshold and suspecting contamination are all sensible.
:::

:::q
(Predicted deep cut, L7) Two wells for the same gene: well A separates cleanly, well B has heavy rain and you have to drag the threshold. Which number do you trust, and how do you fix B?
???
Trust A. Clean bands mean the positive and negative calls are confident, so the count is solid. B's rain makes the split ambiguous, so its number is shaky. Fix B by optimizing the annealing temperature, cleaning up or redesigning the primers, diluting the template, or simply rerunning it.
:::

:::q
(Predicted deep cut, L7) Normalized to beta-actin, myocardin looks like it did nothing; normalized to GAPDH, alpha-SMA looks doubled. Which do you believe?
???
Believe GAPDH. Beta-actin is itself an actin and can rise with myocardin's contractile program, so it is not steady here and normalizing to it hides the real change. GAPDH is more likely flat across conditions. Confirm by checking that each housekeeping gene's raw copies really are steady across DM, pMyo and pEGFP before you pick one.
:::

:::q
(Predicted deep cut, L7) Why does "all droplets positive" break the math while "all droplets negative" does not?
???
The count uses the fraction of negative droplets: copies per droplet equals minus the natural log of that fraction. All-negative means zero target, a real and valid zero. All-positive means the negative fraction is zero, and ln(0) is undefined, so no concentration can be computed. The reaction is saturated and must be diluted and rerun.
:::
