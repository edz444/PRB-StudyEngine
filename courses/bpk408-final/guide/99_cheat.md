## One-glance cheat sheet {#cheat}

### Numbers to know

| Thing | Number |
|---|---|
| Hemocytometer square | 6.25 nL |
| Quadrant | 12 squares = 75 nL |
| Cells/mL from a quadrant count | average count ÷ 75 nL × 10⁶ (or × 13,333) |
| 1 mL | 1,000 µL = 1,000,000 nL |
| Hoechst 33342 | ex ~350 nm, em ~461 nm, blue, binds dsDNA |
| WGA | ex ~495 nm, em ~519 nm, green, binds membrane carbohydrates |
| Zoe blue channel | ex 355/40, em 433/36 |
| Zoe green channel | ex 480/17, em 517/23 |
| Zoe red channel | ex 556/20, em 615/61 |
| Pixel values on the Zoe | 0 to 255 (255 = saturated) |
| Pure RNA A260/A280 | about 2.0 |
| Intact RNA gel | 28S : 18S about 2 : 1, no smear |
| RT temperatures | anneal ~25 °C, extend 46 °C |
| PCR after 30 cycles | 2³⁰ = 1,073,741,824 copies per template |
| ddPCR loading | 20 µL reaction (middle row), 70 µL oil (bottom row) |

### Formulas

Cells/mL = average quadrant count ÷ 75 nL × 1,000,000

Volume to seed = cells wanted ÷ cells/mL

Doubling time = t × ln(2) ÷ ln(N_final ÷ N_start)

Transfection efficiency = GFP-positive cells ÷ total Hoechst nuclei × 100

Normalized expression = target copies ÷ housekeeping copies (same sample)

Poisson (concept only): average copies per droplet = −ln(fraction of negative droplets)

### Who's who

| Name | What it is |
|---|---|
| A7r5 | rat aortic smooth muscle cells (VSMCs), embryonic, fibroblast-like, transfectable |
| Myocardin (MYOCD) | transcriptional coactivator; binds SRF on CArG boxes; switches on contractile genes |
| SRF | serum response factor; the DNA-binding partner |
| pMYOCD-IRES-GFP | plasmid making myocardin and GFP from one mRNA |
| pEGFP | GFP-only control plasmid |
| DM, GM | the dish conditions named on the slides (GM is growth medium) |
| Housekeeping genes | GAPDH, rTbp1, β-actin1 |
| Contractile genes | α-SMA, SM22α, CNN (calponin), MHC |
| Hoechst | blue, DNA, nucleus, total cell count |
| GFP | green, natural fluorescence, transfected cells |
| Phalloidin | red, F-actin, cytoskeleton shape |

### Exam traps in one list

1. Average all quadrant counts before converting, and check nL to mL.
2. Emission is always at a longer wavelength than excitation.
3. Myocardin binds SRF, not DNA.
4. GFP is natural fluorescence, not a stain.
5. Phalloidin needs permeabilization; Hoechst comes before phalloidin in our protocol, with washes between.
6. Saturated pixels (255) are lost data; slightly underexpose.
7. Same imaging settings across conditions, or the comparison is invalid.
8. In a spin column, RNA is on the silica until elution. Keep the final flow-through.
9. A260 after RT is meaningless because RNA, primers and nucleotides absorb too.
10. You infer mRNA integrity from rRNA bands.
11. End-point PCR isn't quantitative because of the plateau.
12. ddPCR brightness reflects product length and efficiency, not starting copy number.
13. All-positive ddPCR is saturated and can't be quantified. Dilute.
14. Normalize to a housekeeping gene that stays steady across conditions.
15. "What do the data show" and "what do the data mean" are two different answers.
