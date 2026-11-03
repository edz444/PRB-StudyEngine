from dlib import D
from diagrams_a import reg, gpcr, FIGS

def chrom(d, x, y, bad=False, cls="fT", h=58):
    d.box(x, y, 14, h, "", cls, rx=6)
    if bad: d.cross(x + 7, y + h/2, 6)

# ---------------- intro story map -----------------
@reg("storymap", "Seven chapters, one story",
     "Chapters 1 to 4 build the switches; chapters 5 to 7 break them. Arrows show which chapter each one leans on.")
def _():
    d = D("story", 720, 330)
    d.text(180, 22, "Build the switches", "tT", size=14, weight=700)
    d.text(540, 22, "Break the switches", "tO", size=14, weight=700)
    bx = {
        "1": (30, 44, "1. GPCRs (L5)\nG proteins, cAMP, Ca2+", "fT"),
        "2": (30, 138, "2. Synapses (L6)\naction potential, release", "fT"),
        "3": (30, 232, "3. Optogenetics (L7)\nlight-gated channels", "fT"),
        "4": (200, 138, "4. RTKs (L8)\nRas, MAPK, growth", "fT"),
        "5": (400, 44, "5. Cancer I (L9)\nwhat a tumor is", "fO"),
        "6": (400, 138, "6. Cancer II (L10)\ngas pedals (oncogenes)", "fO"),
        "7": (400, 232, "7. Cancer III (L11)\nbrakes, Wnt, TGFβ", "fO"),
    }
    for k, (x, y, t, c) in bx.items():
        d.box(x, y, 160, 62, t, c, size=12)
    d.arrow(110, 106, 110, 136); d.arrow(110, 200, 110, 230)
    d.arrow(190, 75, 220, 136)
    d.arrow(360, 169, 398, 169)
    d.arrow(480, 106, 480, 136); d.arrow(480, 200, 480, 230)
    d.path("M360 160 Q 380 90 398 80", "ar", head="a")
    d.box(590, 120, 120, 100, "end of the story:\nevery cancer gene\non one map", "fA", size=12)
    d.arrow(562, 263, 640, 222)
    d.text(285, 312, "Chapter 6 reuses parts from 1 and 4 (Ras, RTKs, PKC); chapter 7 adds Wnt and TGFβ.", "tm", size=12)
    return d

# ---------------- L11 -----------------
@reg("twohit", "Two hits for a tumor suppressor, one for an oncogene",
     "A stuck gas pedal needs one mutant copy. A brake only fails when both copies are lost, and an inherited first hit makes that far more likely.")
def _():
    d = D("twohit", 720, 330)
    d.box(10, 10, 220, 300, "", "panel", rx=12); d.box(250, 10, 460, 300, "", "panel", rx=12)
    d.text(120, 34, "Oncogene (gas pedal)", "t", size=14, weight=700)
    chrom(d, 90, 70, cls="fG"); chrom(d, 130, 70, bad=True, cls="fO")
    d.text(120, 160, "one gain-of-function\ncopy is enough", "t", size=13)
    d.text(120, 230, "dominant in the cell", "tO", size=13)
    d.text(480, 34, "Tumor suppressor (brake)", "t", size=14, weight=700)
    for i, (lab, h1, h2, res, rc) in enumerate([("normal cell", False, False, "brake works", "tT"),
                                                 ("one hit", True, False, "still works", "tT"),
                                                 ("two hits", True, True, "brake lost:\ntumor", "tO")]):
        x = 300 + i * 140
        d.text(x + 27, 62, lab, "tm", size=12)
        chrom(d, x + 6, 80, h1, "fO" if h1 else "fT"); chrom(d, x + 34, 80, h2, "fO" if h2 else "fT")
        d.text(x + 27, 166, res, rc, size=13)
        if i < 2: d.arrow(x + 64, 109, x + 128, 109)
    d.text(480, 222, "hereditary retinoblastoma: born with hit 1 in every cell,", "t", size=12)
    d.text(480, 242, "so hit 2 happens in many cells (tumors in both eyes)", "t", size=12)
    d.text(480, 270, "sporadic: two rare hits in one cell (about 1 in 30,000)", "tm", size=12)
    return d

@reg("methylation", "Promoter methylation silences a gene",
     "Methylating the Cs in a CpG island packs the chromatin tight and switches the gene off without changing its sequence.")
def _():
    d = D("meth", 720, 300)
    d.box(10, 10, 340, 280, "", "panel", rx=12); d.box(370, 10, 340, 280, "", "panel", rx=12)
    d.text(180, 34, "Active promoter", "t", size=15, weight=700)
    d.text(540, 34, "Silenced promoter", "t", size=15, weight=700)
    d.line(30, 120, 330, 120, "thick"); d.box(60, 108, 110, 24, "CpG island", "fA", rx=4, size=11)
    for x in (75, 100, 125, 150):
        d.text(x, 150, "C", "tT", size=13)
    d.text(115, 172, "unmethylated", "tT", size=12)
    d.box(190, 104, 120, 32, "gene ON", "fT", size=13)
    d.text(180, 230, "open chromatin,\ntranscription happens", "t", size=13)
    d.line(390, 120, 690, 120, "thick"); d.box(420, 108, 110, 24, "CpG island", "fA", rx=4, size=11)
    for x in (435, 460, 485, 510):
        d.text(x, 150, "C", "tO", size=13); d.circle(x, 172, 8, "", "fO"); d.text(x, 172, "M", "t", size=9)
    d.text(475, 196, "5-methylcytosine", "tO", size=12)
    d.box(550, 104, 120, 32, "gene OFF", "fG", size=13)
    d.text(540, 236, "DNA methyltransferase moves CH3\nfrom SAM onto C5 of cytosine;\nchromatin condenses", "t", size=12)
    return d

@reg("mutpattern", "Where mutations land: oncogene vs tumor suppressor",
     "Oncogene mutations stack up at a few hotspots; tumor suppressor mutations scatter along the whole gene and many cut it short.")
def _():
    d = D("mut", 720, 300)
    d.text(20, 40, "Oncogene", "t", anchor="start", size=14, weight=700)
    d.box(130, 92, 440, 16, "", "fT", rx=4); d.box(570, 92, 120, 16, "", "fO", rx=4)
    d.text(630, 122, "kinase domain", "tm", size=11)
    for x, n in ((330, 6), (650, 5)):
        for k in range(n):
            d.raw(f'<path d="M{x-5} {84-k*9} L{x+5} {84-k*9} L{x} {90-k*9} z" class="tri"/>')
    for x in (180, 250, 420):
        d.raw(f'<path d="M{x-5} 84 L{x+5} 84 L{x} 90 z" class="tri"/>')
    d.text(330, 22, "hotspot", "tO", size=12)
    d.text(20, 170, "Tumor\nsuppressor", "t", anchor="start", size=14, weight=700)
    d.box(130, 192, 560, 16, "", "fT", rx=4)
    import random
    random.seed(4)
    for k in range(26):
        x = 140 + k * 21 + random.randint(-4, 4)
        y = 214 + (k % 3) * 9
        d.raw(f'<path d="M{x-5} {y+6} L{x+5} {y+6} L{x} {y} z" class="triA"/>')
    for x in (170, 300, 460, 610):
        d.raw(f'<path d="M{x-5} 184 L{x+5} 184 L{x} 190 z" class="tri"/>')
    d.raw('<path d="M140 276 L150 276 L145 270 z" class="triA"/>'); d.text(158, 274, "truncating (early stop)", "tm", anchor="start", size=11)
    d.raw('<path d="M380 270 L390 270 L385 276 z" class="tri"/>'); d.text(398, 274, "missense (one amino acid swapped)", "tm", anchor="start", size=11)
    return d

@reg("wnt", "Canonical Wnt pathway off and on",
     "No Wnt: the destruction complex tags β-catenin for the proteasome. Wnt: the complex breaks up, β-catenin reaches TCF and turns on Myc.")
def _():
    d = D("wnt", 720, 420)
    d.box(10, 10, 340, 400, "", "panel", rx=12); d.box(370, 10, 340, 400, "", "panel", rx=12)
    d.text(180, 26, "No Wnt: OFF", "t", size=15, weight=700)
    d.text(540, 26, "Wnt present: ON", "t", size=15, weight=700)
    for x0, x1 in ((20, 340), (380, 700)):
        d.membrane(56, x0, x1, label="", h=28)
    gpcr(d, 70, 56, h=28); d.text(105, 102, "Frizzled", "tm", size=11)
    d.box(160, 48, 12, 44, "", "fG", rx=4); d.text(166, 102, "LRP", "tm", size=11)
    d.box(40, 126, 270, 70, "", "fO", rx=20)
    d.text(175, 142, "destruction complex", "t", size=12, weight=600)
    d.text(175, 164, "axin + APC + GSK-3 + CK1", "t", size=12)
    d.text(175, 182, "phosphorylate β-catenin", "t", size=12)
    d.circle(70, 230, 15, "β", "fA", size=13); d.P(84, 218)
    d.arrow(90, 236, 170, 252, "arO", head="o")
    d.box(172, 238, 140, 30, "ubiquitin, proteasome", "fG", size=11)
    d.box(40, 300, 280, 96, "", "fG", rx=20); d.text(180, 316, "nucleus", "tm", size=11)
    d.line(56, 370, 304, 370, "thick")
    d.box(80, 340, 60, 26, "TCF", "fT", size=12); d.box(142, 340, 82, 26, "Groucho", "fO", size=12)
    d.text(220, 386, "target genes OFF", "tO", size=12)
    d.circle(460, 45, 8, "", "fA"); d.text(474, 45, "Wnt binds Frizzled + LRP", "t", anchor="start", size=11)
    gpcr(d, 430, 56, h=28); d.box(520, 48, 12, 44, "", "fT", rx=4)
    d.box(420, 104, 110, 28, "Dishevelled", "fT", size=12)
    d.box(560, 104, 60, 28, "axin", "fA", size=12)
    d.arrow(530, 118, 558, 118)
    d.text(600, 148, "complex falls apart", "tm", size=12)
    for x in (430, 465, 500):
        d.circle(x, 200, 15, "β", "fA", size=13)
    d.text(570, 200, "β-catenin\nbuilds up", "tT", size=13)
    d.box(400, 300, 280, 96, "", "fG", rx=20); d.text(620, 316, "nucleus", "tm", size=11)
    d.arrow(465, 216, 465, 336, "arT", head="t")
    d.line(416, 370, 664, 370, "thick")
    d.box(440, 340, 60, 26, "TCF", "fT", size=12); d.circle(520, 352, 14, "β", "fA", size=12)
    d.text(600, 352, "Myc and other\ngenes ON", "tT", size=12)
    return d

@reg("tgfdual", "TGFβ switches sides as a tumor progresses",
     "Early on, TGFβ blocks growth (a brake). Late tumors stop responding to the brake but use TGFβ to invade and hide.")
def _():
    d = D("dual", 720, 260)
    d.raw('<path d="M40 70 L680 150 L680 70 Z" class="fTsolid"/>')
    d.raw('<path d="M40 150 L680 150 L680 70 Z" class="fOsolid"/>')
    d.text(60, 50, "normal epithelium", "t", anchor="start", size=13, weight=600)
    d.text(680, 50, "invasive, metastatic cancer", "t", anchor="end", size=13, weight=600)
    d.text(170, 96, "response to TGFβ", "tT", size=12)
    d.text(560, 136, "TGFβ made and activated", "tO", size=12)
    d.arrow(40, 170, 680, 170)
    d.text(160, 200, "tumor suppressor:\ngrowth inhibition, apoptosis,\ngenome stability", "tT", size=12)
    d.text(560, 200, "pro-oncogenic:\nEMT, invasion, survival,\nimmune suppression, angiogenesis", "tO", size=12)
    return d

@reg("smad", "TGFβ signaling from receptor to DNA",
     "Type II activates type I, type I phosphorylates Smad2/3, which joins Smad4 and enters the nucleus once its NLS is uncovered.")
def _():
    d = D("smad", 720, 430)
    d.membrane(80, label="")
    d.text(700, 60, "outside", "tm", anchor="end", size=12)
    d.circle(300, 36, 11, "", "fA"); d.circle(322, 36, 11, "", "fA")
    d.text(380, 36, "TGFβ dimer", "t", anchor="start", size=12)
    for x, lab in ((250, "II"), (370, "I")):
        d.box(x - 10, 50, 20, 70, "", "fT", rx=6)
        d.box(x - 24, 124, 48, 32, lab, "fT", size=13)
    d.text(166, 140, "type II", "tm", size=12); d.text(456, 140, "type I", "tm", size=12)
    d.path("M276 144 Q311 124 344 144", "arO", head="o")
    d.P(352, 166)
    d.text(311, 104, "", "t")
    d.text(560, 128, "Ser/Thr kinases\n(not tyrosine)", "tO", size=12)
    d.box(390, 196, 100, 30, "Smad2/3", "fA", size=12); d.P(496, 196)
    d.arrow(372, 158, 410, 194)
    d.box(390, 240, 100, 30, "Smad2/3", "fA", size=12); d.P(496, 240)
    d.box(500, 240, 80, 30, "Smad4", "fO", size=12)
    d.arrow(440, 226, 440, 238)
    d.text(160, 230, "phosphate uncovers\nthe NLS (MH1 domain),\nimportin carries it in", "t", size=12)
    d.box(380, 300, 330, 120, "", "fG", rx=24); d.text(545, 316, "nucleus", "tm", size=12)
    d.arrow(480, 272, 480, 340)
    d.line(400, 390, 690, 390, "thick")
    d.box(420, 350, 150, 30, "Smads + partner TF", "fA", size=12)
    d.text(580, 408, "p15 (stop dividing), PAI-1", "tT", size=12)
    d.text(160, 330, "lost in cancer:\nreceptors, or Smad4\n(chr 18q, DPC)", "tO", size=12)
    return d
