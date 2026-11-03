from dlib import D
from diagrams_a import reg, gpcr, FIGS

def zig(d, x, y, cls="arB"):
    d.path(f"M{x} {y} L{x+10} {y+10} L{x+3} {y+15} L{x+14} {y+27} L{x+7} {y+32} L{x+20} {y+46}", cls, head="a")

def receptor(d, x, top, bot, cls="fT"):
    d.box(x - 7, top, 14, bot - top, "", cls, rx=5)

# ---------------- L7 -----------------
@reg("chr2", "Channelrhodopsin-2 dark vs blue light",
     "Blue light flips the retinal and opens the pore; cations flood in and the neuron fires.")
def _():
    d = D("chr2", 720, 310)
    d.box(10, 10, 340, 290, "", "panel", rx=12); d.box(370, 10, 340, 290, "", "panel", rx=12)
    d.text(180, 34, "Dark: closed", "t", size=15, weight=700)
    d.text(540, 34, "Blue light (about 470 nm): open", "t", size=15, weight=700)
    d.membrane(120, 20, 340, label=""); d.membrane(120, 380, 700, label="")
    d.box(158, 106, 22, 62, "", "fT", rx=5); d.box(180, 106, 22, 62, "", "fT", rx=5)
    d.text(180, 200, "all-trans retinal", "t", size=13)
    d.text(180, 255, "no ions cross;\nmembrane stays at rest", "tm", size=13)
    zig(d, 470, 50)
    d.box(518, 106, 22, 62, "", "fT", rx=5); d.box(560, 106, 22, 62, "", "fT", rx=5)
    d.text(470, 200, "13-cis retinal", "t", size=13)
    for i, (x, y) in enumerate([(530, 70), (560, 60), (590, 76)]):
        d.ion(x, y, ["Na+", "Ca", "Na+"][i], "fA", r=12, size=10)
    d.arrow(550, 92, 550, 200, "arT", head="t")
    d.text(620, 222, "cations in", "t", size=12)
    d.text(540, 262, "depolarization, so an\naction potential fires", "tT", size=13)
    return d

@reg("opto_tools", "The optogenetic toolbox",
     "Which way the charge moves decides the effect: cations in excite, Cl- in or H+ out silence.")
def _():
    d = D("tools", 720, 340)
    d.membrane(120, label="", h=40)
    d.text(14, 100, "outside", "tm", anchor="start", size=12)
    d.text(14, 186, "cytosol", "tm", anchor="start", size=12)
    # ChR2
    d.box(80, 112, 16, 56, "", "fT", rx=4); d.box(108, 112, 16, 56, "", "fT", rx=4)
    d.text(102, 44, "Na+ Ca2+", "t", size=12)
    d.arrow(102, 58, 102, 210, "arT", head="t")
    d.text(102, 262, "ChR2 (channel)\ncations flow in\nexcites: neuron fires", "t", size=12)
    # HR
    d.box(255, 112, 50, 56, "pump", "fA", rx=14, size=11)
    d.text(280, 44, "Cl-", "t", size=12)
    d.arrow(280, 58, 280, 210, "arO", head="o")
    d.text(280, 262, "Halorhodopsin (pump)\nCl- pumped in\nsilences", "t", size=12)
    # BR
    d.box(435, 112, 50, 56, "pump", "fA", rx=14, size=11)
    d.text(460, 222, "H+", "t", size=12)
    d.arrow(460, 208, 460, 58, "arO", head="o")
    d.text(460, 262, "Bacteriorhodopsin (pump)\nH+ pumped out\nsilences", "t", size=12)
    # OptoXR
    gpcr(d, 605, 120, h=40)
    d.box(605, 186, 60, 26, "Gα", "fG", size=12)
    d.arrow(635, 168, 635, 184)
    d.text(635, 262, "OptoXR (GPCR)\nchanges cAMP or IP3\n(no direct voltage change)", "t", size=12)
    for x in (130, 308, 488, 670):
        zig(d, x, 48)
    return d

# ---------------- L8 -----------------
@reg("rtk_activation", "RTK activation in three steps",
     "Pair up, cross-phosphorylate, then put out phosphotyrosine landing pads for SH2 proteins.")
def _():
    d = D("rtk", 720, 330)
    d.membrane(120, label="")
    def rtk(x, ps=()):
        d.box(x - 13, 56, 26, 60, "", "fT", rx=8)
        d.line(x, 116, x, 154, "thick")
        d.box(x - 16, 156, 32, 44, "", "fT", rx=6)
        for (dx, dy) in ps:
            d.P(x + dx, dy)
    rtk(85); rtk(145)
    d.text(115, 245, "1. two inactive\nmonomers", "t", size=13)
    d.circle(345, 40, 10, "", "fA"); d.circle(375, 40, 10, "", "fA")
    rtk(345, [(-24, 170)]); rtk(375, [(24, 170)])
    d.path("M352 175 Q360 160 368 175", "arO", head="o"); d.path("M368 190 Q360 205 352 190", "arO", head="o")
    d.text(360, 245, "2. ligand makes a dimer;\nkinases phosphorylate\neach other's activation lip", "t", size=13)
    d.circle(595, 40, 10, "", "fA"); d.circle(625, 40, 10, "", "fA")
    rtk(595, [(-24, 170), (-24, 194)]); rtk(625, [(24, 170), (24, 194)])
    d.box(662, 214, 52, 26, "SH2", "fO", size=12)
    d.arrow(680, 214, 660, 200)
    d.text(600, 270, "3. more P-Tyr sites;\nSH2 proteins dock", "t", size=13)
    d.arrow(200, 180, 290, 180); d.arrow(440, 180, 530, 180)
    return d

@reg("ras_switch", "Ras GTPase switch",
     "GEF turns Ras on, GAP turns it off. RasD breaks the off side.")
def _():
    d = D("ras", 720, 300)
    d.box(50, 110, 190, 64, "Ras-GDP\nOFF", "fG", size=15)
    d.box(480, 110, 190, 64, "Ras-GTP\nON", "fT", size=15)
    d.path("M150 106 Q360 10 570 106", "arT", head="t")
    d.text(360, 40, "GEF (Sos) swaps GDP out, GTP in", "t", size=13)
    d.path("M570 180 Q360 276 150 180", "arO", head="o")
    d.text(360, 210, "GAP speeds GTP hydrolysis (+ Pi)", "t", size=13)
    d.cross(360, 230, 12)
    d.text(360, 275, "Glycine 12 mutation (RasD): GAP can't act, so Ras is stuck ON", "tO", size=13)
    return d

@reg("ras_mapk", "RTK to Ras to MAP kinase to c-fos",
     "GRB2 brings Sos to Ras at the membrane; Ras starts the Raf, MEK, ERK chain; ERK turns on c-fos in the nucleus.")
def _():
    d = D("mapk", 720, 500)
    d.membrane(90, label="")
    d.text(700, 70, "outside", "tm", anchor="end", size=12)
    d.circle(82, 40, 11, "", "fA"); d.circle(112, 40, 11, "", "fA")
    for x in (82, 112):
        d.box(x - 9, 52, 18, 36, "", "fT", rx=6); d.line(x, 88, x, 124, "thick"); d.box(x - 11, 126, 22, 44, "", "fT", rx=5)
    d.P(132, 160)
    d.box(146, 146, 64, 30, "GRB2", "fA", size=13)
    d.box(216, 146, 56, 30, "Sos", "fT", size=13)
    d.box(296, 126, 88, 32, "Ras-GTP", "fT", size=13)
    d.arrow(260, 146, 296, 142)
    d.text(120, 230, "GRB2: SH2 grabs\nthe P-Tyr; SH3\nholds Sos", "t", size=12)
    for i, (lab, y) in enumerate((("Raf (MAPKKK)", 210), ("MEK (MAPKK)", 270), ("ERK (MAPK)", 330))):
        d.box(270, y, 140, 34, lab, "fT", size=13)
    d.arrow(340, 160, 340, 208); d.arrow(340, 244, 340, 268); d.arrow(340, 304, 340, 328)
    d.text(120, 330, "each kinase\nphosphorylates\nthe next", "tm", size=12)
    d.box(440, 300, 270, 180, "", "fG", rx=26)
    d.text(575, 318, "nucleus", "tm", size=12)
    d.box(460, 350, 90, 32, "TCF", "fT", size=13); d.box(556, 350, 90, 32, "SRF", "fA", size=13)
    d.line(452, 396, 700, 396, "thick")
    d.text(600, 412, "SRE in the c-fos enhancer", "tm", size=12)
    d.text(575, 448, "c-fos ON (cell cycle moves)", "tT", size=13)
    d.arrow(410, 347, 470, 352)
    return d

@reg("r7_epistasis", "R7 induction genetics",
     "Active Ras rescues R7 in a sevenless mutant, so Ras sits downstream of the Sev receptor.")
def _():
    d = D("r7", 720, 340)
    cols = [(95, "wild type", True, True, False, "R7", "normal"),
            (275, "sev mutant", True, False, False, "cone", "no R7"),
            (455, "boss mutant", False, True, False, "cone", "no R7"),
            (635, "sev + RasD", True, False, True, "R7", "R7 rescued:\nRas is downstream")]
    for c, g, boss, sev, rasd, out, v in cols:
        d.text(c, 24, g, "t", size=14, weight=700)
        d.circle(c, 82, 24, "R8", "fG", size=13)
        d.circle(c, 150, 26, "", "fG")
        if boss: d.box(c - 10, 102, 20, 10, "", "fA", rx=2)
        else: d.cross(c, 108, 7)
        if sev: d.box(c - 10, 114, 20, 10, "", "fT", rx=2)
        else: d.cross(c, 120, 7)
        if rasd: d.box(c - 22, 142, 44, 18, "RasD", "fO", size=11)
        d.arrow(c, 178, c, 210)
        d.circle(c, 246, 32, "R7" if out == "R7" else "cone\ncell", "fT" if out == "R7" else "fG", size=13)
        d.text(c, 306, v, "tO" if rasd else "t", size=13)
    d.text(20, 130, "", "t")
    return d

@reg("ephrin_map", "Ephrin gradient sets the retinotopic map",
     "High-EphA axons are pushed away by high ephrinA, so posterior retina maps to anterior tectum.")
def _():
    d = D("eph", 720, 360)
    d.text(150, 40, "retina: EphA receptor", "t", size=13, weight=700)
    d.text(560, 40, "tectum: ephrinA ligand", "t", size=13, weight=700)
    for i in range(5):
        d.raw(f'<rect x="{40+i*44}" y="70" width="44" height="200" class="fTs" style="fill-opacity:{0.12+i*0.18:.2f}"/>')
        d.raw(f'<rect x="{450+i*44}" y="70" width="44" height="200" class="fOs" style="fill-opacity:{0.12+i*0.18:.2f}"/>')
    d.box(40, 70, 220, 200, "", "none", rx=0); d.box(450, 70, 220, 200, "", "none", rx=0)
    d.text(60, 290, "anterior\n(low EphA)", "tm", anchor="start", size=12)
    d.text(250, 290, "posterior\n(high EphA)", "tm", anchor="end", size=12)
    d.text(460, 290, "anterior\n(low ephrinA)", "tm", anchor="start", size=12)
    d.text(660, 290, "posterior\n(high ephrinA)", "tm", anchor="end", size=12)
    d.circle(70, 120, 9, "", "fT"); d.circle(230, 220, 9, "", "fT")
    d.path("M79 120 C 300 110, 450 120, 640 120", "arT", head="t")
    d.path("M239 220 C 330 220, 400 220, 490 220", "arO", head="bar")
    d.text(555, 205, "repelled", "tO", size=12)
    d.text(360, 335, "Anterior retina reaches posterior tectum; posterior retina stops in the front.", "t", size=13)
    return d

# ---------------- L9 -----------------
@reg("warburg", "Normal vs Warburg metabolism",
     "Tumor cells push most glucose through glycolysis to lactate and building blocks, even with oxygen around.")
def _():
    d = D("wb", 720, 330)
    d.box(10, 10, 340, 310, "", "panel", rx=12); d.box(370, 10, 340, 310, "", "panel", rx=12)
    d.text(180, 34, "Normal differentiated cell", "t", size=14, weight=700)
    d.text(540, 34, "Proliferating tumor cell", "t", size=14, weight=700)
    for cx, big in ((180, False), (540, True)):
        d.box(cx - 55, 54, 110, 30, "glucose", "fA", size=13)
        d.line(cx, 84, cx, 138, "arThick" if big else "ar")
        d.text(cx - 60, 110, "glycolysis", "tm", anchor="end", size=12)
        d.box(cx - 55, 140, 110, 30, "pyruvate", "fA", size=13)
    d.arrow(160, 170, 110, 214, "arThick"); d.box(30, 216, 150, 40, "oxidative\nphosphorylation", "fT", size=12)
    d.arrow(200, 170, 250, 214, "ar", dash=True); d.box(200, 216, 120, 40, "lactate", "fG", size=12)
    d.text(180, 290, "net: CO2, H2O, lots of ATP", "t", size=13)
    d.arrow(520, 170, 470, 214, "ar", dash=True); d.box(390, 216, 150, 40, "oxidative\nphosphorylation", "fG", size=12)
    d.arrow(560, 170, 610, 214, "arThick"); d.box(560, 216, 120, 40, "lactate", "fO", size=12)
    d.arrow(546, 110, 610, 110, "arThick"); d.box(612, 94, 92, 34, "building\nblocks", "fO", size=11)
    d.text(540, 290, "net: building blocks, NADPH", "t", size=13)
    return d

@reg("telomere", "Telomere shortening vs telomerase",
     "Without telomerase the caps shrink each division until the cell stops; cancer cells keep telomerase on.")
def _():
    d = D("tel", 720, 300)
    def row(y, caps, end, title):
        d.text(20, y - 26, title, "t", anchor="start", size=14, weight=700)
        for i, c in enumerate(caps):
            x = 30 + i * 150
            d.box(x + 18, y, 92, 18, "", "fG", rx=4)
            if c: d.box(x + 18 - c, y, c, 18, "", "fO", rx=3); d.box(x + 110, y, c, 18, "", "fO", rx=3)
            if i < len(caps) - 1: d.arrow(x + 132, y + 9, x + 160, y + 9)
        d.text(680, y + 9, end, "tT" if "keeps" in end else "tO", size=13)
    row(70, [18, 12, 6, 1], "stops\ndividing", "Normal somatic cell (little telomerase)")
    d.text(360, 115, "telomere caps (TTAGGG repeats) shrink every division", "tm", size=12)
    row(200, [18, 18, 18, 18], "keeps\ndividing", "Cancer cell (telomerase kept on)")
    d.text(360, 245, "telomerase adds TTAGGG back, so the count never runs out", "tm", size=12)
    return d

@reg("multihit", "Multi-hit colon cancer progression",
     "Each new mutation gives a bigger, more abnormal clone. The order is APC, K-ras, Smad4 (chromosome 18), p53.")
def _():
    d = D("mh", 720, 260)
    xs = [10, 155, 300, 445, 590]
    labs = ["normal\nepithelium", "small\npolyp", "benign\nadenoma", "larger\nadenoma", "carcinoma\n(invasive)"]
    cls = ["fG", "fA", "fA", "fA", "fO"]
    for x, l, c in zip(xs, labs, cls):
        d.box(x, 30, 120, 60, l, c, size=13)
    muts = ["lose APC\n(chr 5)", "activate K-ras\n(chr 12)", "lose Smad4\n(chr 18q, DCC region)", "lose p53\n(chr 17)"]
    for i, m in enumerate(muts):
        x = xs[i] + 120
        d.arrow(x + 2, 60, x + 23, 60)
        d.line(x + 12, 66, x + 12, 118, "ln", dash=True)
        d.text(x + 12, 142, m, "t", size=12)
    d.text(360, 210, "then more changes allow invasion and metastasis", "tm", size=13)
    d.text(360, 236, "one founder cell, years of accumulated hits", "tm", size=12)
    return d

@reg("metastasis", "Steps of metastasis",
     "Six hurdles in order. Very few cells clear all of them, yet metastasis causes about 90% of cancer deaths.")
def _():
    d = D("met", 720, 290)
    bx = [(10, 30, "1. lose cell-cell\nadhesion", "fA"), (255, 30, "2. break through\nthe basal lamina", "fA"),
          (500, 30, "3. enter a\nblood vessel", "fA"), (500, 150, "4. survive the trip\n(under 1 in 1000 do)", "fO"),
          (255, 150, "5. stick and exit\nin a new organ", "fA"), (10, 150, "6. grow: micrometastasis,\nthen a new tumor", "fO")]
    for x, y, t, c in bx:
        d.box(x, y, 210, 70, t, c, size=13)
    d.arrow(220, 65, 253, 65); d.arrow(465, 65, 498, 65); d.arrow(605, 100, 605, 148)
    d.arrow(500, 185, 467, 185); d.arrow(255, 185, 222, 185)
    d.text(360, 262, "Let go, break out, hop on, hop off, settle in.", "tT", size=13)
    return d

@reg("hif", "HIF with and without oxygen",
     "Oxygen marks HIF for destruction through VHL. Without oxygen, or without VHL, HIF turns on VEGF.")
def _():
    d = D("hif", 720, 360)
    d.box(10, 10, 340, 290, "", "panel", rx=12); d.box(370, 10, 340, 290, "", "panel", rx=12)
    d.text(180, 34, "High O2", "t", size=15, weight=700)
    d.text(540, 34, "Low O2 (hypoxia)", "t", size=15, weight=700)
    steps = [("HIF", "fA"), ("HIF-OH (hydroxylated)", "fA"), ("VHL E3 ligase adds ubiquitin", "fO"), ("proteasome: HIF destroyed", "fG")]
    for i, (t, c) in enumerate(steps):
        d.box(50, 56 + i * 60, 260, 38, t, c, size=13)
        if i: d.arrow(180, 56 + i * 60 - 22, 180, 56 + i * 60 - 2)
    steps2 = [("HIF stable", "fA"), ("enters nucleus", "fA"), ("VEGF gene ON", "fT"), ("new blood vessels", "fT")]
    for i, (t, c) in enumerate(steps2):
        d.box(410, 56 + i * 60, 260, 38, t, c, size=13)
        if i: d.arrow(540, 56 + i * 60 - 22, 540, 56 + i * 60 - 2)
    d.text(360, 330, "VHL lost: HIF escapes destruction even with O2, so VEGF stays on (blood-vessel tumors).", "tO", size=13)
    return d

# ---------------- L10 -----------------
@reg("venn", "Mutagens vs carcinogens",
     "The overlap is genotoxic carcinogens. Each circle also has members that don't belong to the other.")
def _():
    d = D("venn", 720, 330)
    d.raw('<circle cx="285" cy="175" r="135" class="vT sk"/>')
    d.raw('<circle cx="435" cy="175" r="135" class="vO sk"/>')
    d.text(200, 22, "mutagens (change DNA)", "tT", size=14, weight=700)
    d.text(520, 22, "carcinogens (cause cancer)", "tO", size=14, weight=700)
    d.text(225, 175, "Ames positive,\nbut repaired or\nkept out of\nanimal cells", "t", size=12)
    d.text(360, 175, "genotoxic\ncarcinogens:\naflatoxin,\nbenzo[a]pyrene,\nradiation", "t", size=12, weight=600)
    d.text(497, 175, "non-genotoxic:\nasbestos,\nphorbol esters\n(TPA)", "t", size=12)
    return d

@reg("onco_mechanisms", "Four ways to make an oncogene",
     "Ask whether the result is an abnormal hyperactive protein or too much of a normal one.")
def _():
    d = D("onc", 720, 320)
    cs = [90, 270, 450, 630]
    titles = ["point mutation or\ndeletion in coding", "regulatory\nmutation", "gene\namplification", "chromosome\nrearrangement"]
    for c, t in zip(cs, titles):
        d.box(c - 82, 16, 164, 46, t, "fG", size=12)
    # 1
    d.box(30, 100, 120, 18, "", "fA", rx=3); d.cross(95, 109, 6)
    # 2
    d.box(200, 100, 30, 18, "", "fO", rx=3); d.box(230, 100, 100, 18, "", "fA", rx=3)
    d.text(215, 132, "promoter", "tm", size=11)
    for k in range(4):
        d.line(230, 150 + k * 10, 330, 150 + k * 10, "thinT")
    # 3
    for k in range(4):
        d.box(400, 92 + k * 22, 100, 16, "", "fA", rx=3)
    # 4
    d.box(560, 100, 60, 18, "", "fG", rx=3); d.box(620, 100, 60, 18, "", "fO", rx=3)
    d.text(630, 136, "two genes fused", "tm", size=11)
    res = [("abnormal protein,\nhyperactive", "fO"), ("normal protein,\nfar too much", "fA"),
           ("normal protein,\nfar too much", "fA"), ("hyperactive fusion\nor overproduced", "fO")]
    for c, (t, k) in zip(cs, res):
        d.arrow(c, 196, c, 226)
        d.box(c - 82, 228, 164, 50, t, k, size=12)
    d.text(360, 304, "Examples: RasD (1), HER2 amplification (3), Bcr-Abl fusion (4)", "tm", size=12)
    return d

@reg("src", "c-Src self-lock vs oncogenic Src",
     "P-Tyr527 tucked into Src's own SH2 domain keeps the kinase shut. Remove Tyr527 and the lock is gone.")
def _():
    d = D("src", 720, 310)
    d.box(10, 10, 340, 290, "", "panel", rx=12); d.box(370, 10, 340, 290, "", "panel", rx=12)
    d.text(180, 34, "c-Src: OFF", "t", size=15, weight=700)
    d.text(540, 34, "v-Src or Tyr527 mutant: ON", "t", size=15, weight=700)
    d.circle(70, 110, 24, "SH3", "fG", size=12); d.circle(115, 165, 24, "SH2", "fG", size=12)
    d.box(160, 80, 130, 100, "kinase\n(clamped shut)", "fG", size=13)
    d.path("M290 160 C 320 200, 250 225, 150 200", "ln", head=None)
    d.P(146, 194)
    d.text(220, 230, "tail P-Tyr527 bound\nto its own SH2", "t", size=12)
    d.box(40, 250, 70, 30, "Csk", "fO", size=12)
    d.arrow(80, 250, 138, 204, "arO", head="o")
    d.text(195, 266, "Csk adds the P", "tm", size=12)
    d.circle(430, 110, 24, "SH3", "fG", size=12); d.circle(475, 165, 24, "SH2", "fG", size=12)
    d.box(520, 80, 130, 100, "kinase\nopen", "fT", size=13)
    d.line(650, 160, 672, 172, "ln"); d.cross(680, 178, 7)
    d.text(600, 222, "Tyr527 deleted or mutated", "tO", size=12)
    d.text(540, 262, "phosphorylates targets nonstop", "tT", size=13)
    return d

@reg("bcrabl", "Philadelphia chromosome and Bcr-Abl",
     "The 9;22 swap fuses bcr to abl. The fusion kinase never turns off, and Gleevec plugs its ATP pocket.")
def _():
    d = D("ba", 720, 330)
    d.text(30, 40, "chr 9", "t", anchor="start", size=13)
    d.box(80, 30, 220, 22, "", "fG", rx=8); d.box(240, 30, 60, 22, "abl", "fO", rx=4, size=11)
    d.text(30, 100, "chr 22", "t", anchor="start", size=13)
    d.box(80, 90, 170, 22, "", "fG", rx=8); d.box(150, 90, 60, 22, "bcr", "fA", rx=4, size=11)
    d.line(240, 22, 240, 60, "lnO"); d.line(210, 82, 210, 120, "lnO")
    d.arrow(310, 72, 400, 72)
    d.text(355, 52, "swap", "tm", size=12)
    d.box(410, 60, 70, 22, "", "fG", rx=8); d.box(480, 60, 50, 22, "bcr", "fA", rx=3, size=11); d.box(530, 60, 70, 22, "abl", "fO", rx=3, size=11)
    d.text(505, 110, "Philadelphia chromosome (short 22)", "t", size=12)
    d.arrow(505, 124, 505, 158)
    d.box(405, 160, 200, 50, "Bcr-Abl fusion kinase\nalways ON", "fO", size=13)
    d.arrow(505, 210, 505, 244)
    d.box(405, 246, 200, 50, "phosphorylates JAK2,\nSTAT5: CML", "fA", size=13)
    d.box(625, 165, 85, 40, "Gleevec", "fT", size=13)
    d.block(625, 185, 607, 185, "arT")
    d.text(170, 200, "every leukemic cell has the\nsame breakpoint, so they all\ncame from one cell", "tm", size=12)
    return d

@reg("jakstat", "JAK-STAT pathway",
     "The receptor brings the binding, the attached JAK brings the kinase, and STATs carry the message straight to DNA.")
def _():
    d = D("js", 720, 420)
    d.membrane(90, label="")
    d.text(700, 70, "outside", "tm", anchor="end", size=12)
    d.circle(330, 40, 14, "", "fA")
    for x in (305, 355):
        d.box(x - 9, 56, 18, 140, "", "fT", rx=6)
    d.box(250, 150, 46, 30, "JAK", "fO", size=12); d.box(364, 150, 46, 30, "JAK", "fO", size=12)
    d.path("M296 158 Q330 140 362 158", "arO", head="o")
    d.P(305, 206); d.P(355, 206)
    d.box(200, 214, 70, 30, "STAT", "fA", size=12)
    d.arrow(270, 222, 294, 210)
    d.box(390, 250, 110, 34, "STAT dimer", "fA", size=12)
    d.P(388, 250); d.P(502, 250)
    d.arrow(445, 284, 520, 318)
    d.box(470, 300, 240, 110, "", "fG", rx=24)
    d.text(590, 318, "nucleus", "tm", size=12)
    d.line(490, 370, 700, 370, "thick")
    d.text(590, 392, "target genes ON", "tT", size=13)
    d.text(20, 300, "1. cytokine pairs two receptors\n2. JAKs phosphorylate each other\n    and the receptor tails\n3. STAT SH2 docks on a P-Tyr\n4. JAK phosphorylates STAT\n5. STAT dimer enters the nucleus", "t", anchor="start", size=12)
    return d
