from dlib import D

FIGS = {}

def reg(name, title, caption):
    def deco(fn):
        d = fn()
        FIGS[name] = (d.svg(title), caption)
        return fn
    return deco

def gpcr(d, x, y, n=7, h=34):
    for i in range(n):
        d.box(x + i*10, y - 4, 6, h + 8, "", "fT", rx=3)

# ---------------- L5 -----------------
@reg("gcycle", "G protein on/off cycle",
     "The G protein is ON only while Gα holds GTP. Its own GTPase is the timer that ends the signal.")
def _():
    d = D("gcycle", 720, 380)
    d.box(30, 150, 190, 80, "1. OFF\nGα-GDP + Gβγ\n(trimer together)", "fG", size=13)
    d.box(265, 20, 190, 80, "2. Ligand binds GPCR\nreceptor pries\nGDP out of Gα", "fA", size=13)
    d.box(500, 150, 190, 80, "3. GTP jumps in\nGα-GTP and Gβγ\nsplit apart: ON", "fT", size=13)
    d.box(265, 280, 190, 80, "4. Gα hydrolyzes\nGTP to GDP + Pi\n(built-in timer)", "fO", size=13)
    d.path("M125 148 Q125 60 260 60")
    d.path("M458 60 Q595 60 595 145")
    d.path("M595 233 Q595 320 460 320")
    d.path("M262 320 Q125 320 125 235")
    d.text(360, 175, "Gα-GTP or Gβγ", "tT", size=14, weight=600)
    d.text(360, 200, "switches on the effector", "tT", size=14)
    return d

@reg("camp_cascade", "cAMP pathway across the membrane",
     "Two receptors feed one adenylyl cyclase: Gαs pushes it on, Gαi holds it back. PDE is the off switch for cAMP.")
def _():
    d = D("camp", 720, 440)
    d.membrane(110, label="")
    d.text(20, 80, "outside", "tm", anchor="start", size=12)
    d.text(20, 200, "cytosol", "tm", anchor="start", size=12)
    gpcr(d, 62, 110)
    d.circle(95, 72, 16, "", "fA")
    d.text(95, 30, "stimulatory hormone\n(epinephrine, glucagon)", "t", size=12)
    d.box(140, 152, 82, 32, "Gαs-GTP", "fT", size=13)
    d.arrow(100, 148, 138, 164)
    d.box(250, 104, 110, 46, "adenylyl\ncyclase", "fT", size=13)
    d.arrow(222, 166, 250, 146)
    gpcr(d, 482, 110)
    d.circle(515, 72, 16, "", "fG")
    d.text(515, 30, "inhibitory hormone\n(PGE1, adenosine)", "t", size=12)
    d.box(388, 152, 82, 32, "Gαi-GTP", "fG", size=13)
    d.arrow(515, 148, 472, 164)
    d.block(388, 166, 364, 146)
    d.arrow(305, 152, 305, 206)
    d.text(262, 180, "ATP", "tm", size=12)
    d.text(340, 180, "PPi", "tm", size=12)
    d.circle(305, 232, 26, "cAMP", "fT", size=13)
    d.arrow(333, 232, 386, 232, "arO", head="o")
    d.box(390, 214, 200, 36, "PDE: cAMP to 5'-AMP (off)", "fO", size=13)
    d.arrow(305, 260, 305, 288)
    d.box(225, 290, 160, 40, "PKA: cAMP frees C", "fT", size=13)
    d.box(15, 372, 210, 52, "glycogen synthase\nOFF (storage stops)", "fG", size=13)
    d.box(255, 372, 210, 52, "phosphorylase kinase\nON (glycogen breakdown)", "fT", size=13)
    d.box(495, 372, 210, 52, "CREB in nucleus\nturns on CRE genes", "fT", size=13)
    d.arrow(270, 332, 125, 370); d.arrow(305, 332, 360, 370); d.arrow(345, 332, 595, 370)
    return d

@reg("plc_pathway", "PLC-β pathway",
     "PLC-β cuts PIP2 in two. IP3 leaves to open the ER calcium store; DAG stays in the membrane and, with Ca2+, turns on PKC.")
def _():
    d = D("plc", 720, 440)
    d.membrane(90, label="")
    d.text(700, 70, "outside", "tm", anchor="end", size=12)
    gpcr(d, 42, 90)
    d.circle(75, 62, 14, "", "fA")
    d.text(100, 40, "hormone (e.g. angiotensin)", "t", anchor="start", size=12)
    d.box(108, 136, 88, 32, "Gαq-GTP", "fT", size=13)
    d.arrow(82, 128, 108, 148)
    d.box(218, 128, 96, 40, "PLC-β\n(effector)", "fT", size=13)
    d.arrow(196, 152, 216, 150)
    d.box(340, 95, 64, 24, "PIP2", "fA", size=13)
    d.arrow(300, 128, 342, 120)
    d.text(318, 186, "cuts", "tm", size=12)
    d.box(452, 95, 64, 24, "DAG", "fA", size=13)
    d.arrow(404, 107, 450, 107)
    d.circle(372, 206, 24, "IP3", "fA", size=13)
    d.arrow(372, 121, 372, 180)
    d.box(250, 312, 330, 108, "", "fG", rx=30)
    d.text(415, 392, "ER lumen: the Ca2+ store", "tm", size=12)
    d.box(358, 300, 28, 26, "", "fT", rx=4)
    d.arrow(372, 232, 372, 296)
    d.text(470, 330, "IP3-gated Ca2+ channel", "t", size=12)
    for (x, y) in [(455, 250), (490, 268), (455, 282)]:
        d.ion(x, y, "Ca", "fO", r=12, size=10)
    d.path("M388 300 Q410 270 440 262")
    d.box(560, 128, 130, 40, "PKC active", "fT", size=13)
    d.arrow(516, 112, 580, 128)
    d.arrow(470, 245, 590, 170)
    d.box(560, 220, 150, 52, "calmodulin\nCaMKII and more", "fT", size=13)
    d.arrow(503, 266, 558, 250)
    d.text(130, 250, "IP3 floats away;\nDAG stays home\nin the membrane", "tT", size=13)
    return d

@reg("rod_dark_light", "Rod cell in dark vs light",
     "Light lowers cGMP, which closes the cation channels. The rod hyperpolarizes and releases less transmitter.")
def _():
    d = D("rod", 720, 380)
    d.box(10, 10, 340, 360, "", "panel", rx=12)
    d.box(370, 10, 340, 360, "", "panel", rx=12)
    d.text(180, 34, "In the dark", "t", size=15, weight=700)
    d.text(540, 34, "In the light", "t", size=15, weight=700)
    for (x, y) in [(110, 90), (140, 110), (175, 85), (210, 112), (245, 92), (130, 140), (230, 140), (180, 130)]:
        d.circle(x, y, 7, "", "fT")
    d.text(180, 62, "cGMP high", "tT", size=13)
    d.membrane(196, 20, 340, label="")
    d.box(160, 190, 16, 46, "", "fT", rx=3); d.box(196, 190, 16, 46, "", "fT", rx=3)
    d.circle(186, 180, 6, "", "fT")
    d.arrow(186, 290, 186, 156, "arT", head="t")
    d.text(262, 270, "Na+, Ca2+\nflow in", "t", size=12)
    d.text(180, 330, "about -30 mV (depolarized)\nconstant transmitter release", "t", size=13)
    d.path("M392 48 L404 60 L396 66 L410 80 L402 86 L418 100", "arB", head="a")
    d.text(400, 112, "photon", "tm", size=12)
    d.text(565, 72, "rhodopsin → transducin\n→ cGMP PDE", "t", size=13)
    for (x, y) in [(500, 135), (600, 128)]:
        d.circle(x, y, 7, "", "fT")
    d.text(560, 162, "cGMP low (broken down)", "tT", size=13)
    d.membrane(196, 380, 700, label="")
    d.box(529, 190, 16, 46, "", "fG", rx=3); d.box(545, 190, 16, 46, "", "fG", rx=3)
    d.arrow(545, 290, 545, 248, "arT", head="t", dash=True)
    d.cross(545, 268)
    d.text(630, 270, "channels\nclosed", "t", size=12)
    d.text(540, 330, "hyperpolarizes toward -70 mV\nless transmitter released", "t", size=13)
    return d

# ---------------- L6 -----------------
@reg("action_potential", "Action potential and channel states",
     "The rise is Na+ rushing in; the fall is Na+ channels inactivating while the slower K+ channels let K+ out.")
def _():
    d = D("ap", 720, 420)
    y = lambda v: 50 + (50 - v) * 1.6667
    d.line(80, 40, 80, 290, "axis"); d.line(80, 290, 690, 290, "axis")
    for v in (50, 0, -70):
        d.line(75, y(v), 80, y(v), "axis"); d.text(70, y(v), f"{v:+d} mV" if v else "0 mV", "tm", anchor="end", size=12)
    d.line(80, y(-55), 690, y(-55), "ln", dash=True)
    d.text(690, y(-55) - 12, "threshold", "tm", anchor="end", size=12)
    d.text(385, 306, "time (a few milliseconds)", "tm", size=12)
    d.path("M80 250 L160 250 C175 250 182 238 190 225 C200 205 210 70 230 58 C245 50 270 150 300 220 C315 255 330 267 360 267 C390 267 410 252 440 250 L690 250", "curve", head=None)
    d.text(130, 105, "Na+ channels open,\nNa+ rushes in", "t", size=13)
    d.arrow(160, 128, 210, 140)
    d.text(470, 110, "Na+ channels inactivate;\ndelayed K+ channels open,\nK+ flows out", "t", size=13)
    d.arrow(395, 138, 290, 175)
    d.text(520, 200, "undershoot (hyperpolarization)", "t", size=13)
    d.arrow(450, 210, 368, 262)
    def bar(yb, segs, lab):
        d.text(70, yb + 11, lab, "t", anchor="end", size=13)
        for (a, b, t, c) in segs:
            d.box(a, yb, b - a, 22, t, c, rx=3, size=11)
    bar(330, [(80, 200, "closed", "fG"), (200, 238, "open", "fT"), (238, 420, "inactivated", "fO"), (420, 690, "closed", "fG")], "Na+")
    bar(370, [(80, 240, "closed", "fG"), (240, 430, "open", "fT"), (430, 690, "closed", "fG")], "K+")
    return d

@reg("na_states", "Three states of the voltage-gated Na+ channel",
     "Closed can open; inactivated cannot. The inactivation plug is why the spike can't run backwards.")
def _():
    d = D("na", 720, 350)
    d.membrane(90, 10, 710, h=60, label="")
    d.text(700, 70, "outside", "tm", anchor="end", size=12)
    d.text(700, 172, "cytosol", "tm", anchor="end", size=12)
    for c, st in ((120, "closed"), (360, "open"), (600, "inact")):
        d.box(c - 36, 80, 22, 82, "", "fT", rx=5); d.box(c + 14, 80, 22, 82, "", "fT", rx=5)
        if st == "closed":
            d.box(c - 14, 84, 28, 12, "", "fO", rx=3)
        if st == "open":
            d.ion(c, 52, "Na+", "fA", r=14, size=11)
            d.arrow(c, 68, c, 190, "arT", head="t")
        if st == "inact":
            d.line(c + 36, 160, c + 14, 172, "ln")
            d.circle(c, 172, 13, "", "fO")
        else:
            d.line(c + 36, 160, c + 50, 182, "ln")
            d.circle(c + 54, 192, 11, "", "fO")
    d.text(120, 240, "Closed\nat rest; ready to open", "t", size=13)
    d.text(360, 240, "Open\nNa+ rushes in (under 0.1 ms)", "t", size=13)
    d.text(600, 240, "Inactivated\nplug in the pore; can't open", "t", size=13)
    d.arrow(196, 120, 282, 120); d.text(239, 104, "depolarize", "tm", size=12)
    d.arrow(436, 120, 522, 120); d.text(479, 104, "about 1 ms", "tm", size=12)
    d.path("M600 272 Q360 320 130 274")
    d.text(360, 330, "repolarization resets it to closed (a few ms)", "tm", size=12)
    return d

@reg("synapse", "Chemical synapse step by step",
     "Calcium is the send button: nothing is released until the voltage-gated Ca2+ channels open.")
def _():
    d = D("syn", 720, 430)
    d.box(170, 10, 380, 170, "", "fG", rx=50)
    d.text(360, 32, "presynaptic terminal", "tm", size=12)
    d.box(150, 250, 420, 160, "", "fG", rx=20)
    d.text(360, 390, "postsynaptic cell", "tm", size=12)
    d.text(640, 215, "synaptic cleft", "tm", size=12)
    for (x, y) in [(300, 85), (345, 62), (395, 90), (330, 128), (445, 112)]:
        d.circle(x, y, 17, "", "fT")
        d.circle(x - 4, y - 3, 3, "", "fA"); d.circle(x + 5, y + 4, 3, "", "fA")
    d.circle(372, 170, 15, "", "fT")
    for (x, y) in [(350, 205), (372, 218), (395, 207), (360, 232), (390, 236)]:
        d.circle(x, y, 4, "", "fA")
    d.box(200, 165, 22, 30, "", "fT", rx=3)
    d.ion(211, 228, "Ca", "fO", r=12, size=10)
    d.arrow(211, 214, 211, 152, "arT", head="t")
    d.box(495, 165, 22, 30, "", "fO", rx=3)
    d.arrow(445, 222, 497, 188, "arO", head="o")
    for x in (330, 360, 390):
        d.box(x - 8, 242, 16, 22, "", "fT", rx=3)
    d.text(80, 48, "1. action potential\narrives", "t", size=12)
    d.arrow(120, 72, 178, 92)
    d.text(80, 150, "2. Ca2+ channels\nopen, Ca2+ in", "t", size=12)
    d.arrow(132, 166, 196, 178)
    d.text(640, 60, "3. vesicle fuses\n(SNAREs +\nsynaptotagmin)", "t", size=12)
    d.arrow(592, 82, 392, 160)
    d.text(640, 150, "5. reuptake\ntransporter", "t", size=12)
    d.arrow(596, 160, 520, 176)
    d.text(360, 305, "4. transmitter binds receptors\n(ion channels or GPCRs)", "t", size=13)
    return d

@reg("myelin", "Saltatory vs continuous conduction",
     "Myelin insulates the axon so the spike only has to regenerate at the nodes of Ranvier.")
def _():
    d = D("my", 720, 330)
    d.text(360, 22, "Myelinated: the spike jumps from node to node", "t", size=14, weight=700)
    d.box(20, 92, 680, 24, "", "fG", rx=10)
    for a, b in ((40, 190), (210, 360), (380, 530), (550, 700)):
        d.box(a, 78, b - a, 52, "", "fA", rx=18)
    for c in (200, 370, 540):
        d.box(c - 5, 84, 10, 8, "", "fT", rx=2); d.box(c - 5, 116, 10, 8, "", "fT", rx=2)
    d.path("M200 72 Q285 30 368 72", "arT", head="t"); d.path("M370 72 Q455 30 538 72", "arT", head="t")
    d.text(200, 158, "node of Ranvier\n(Na+ channels here)", "t", size=12)
    d.line(200, 140, 200, 126, "ln")
    d.text(455, 152, "myelin sheath (insulation)", "t", size=12)
    d.text(360, 208, "Unmyelinated: every patch must fire in turn", "t", size=14, weight=700)
    d.box(20, 248, 680, 24, "", "fG", rx=10)
    for x in range(40, 660, 44):
        d.path(f"M{x} 244 Q{x+20} 228 {x+40} 244", "arT", head="t")
    d.text(360, 300, "many small steps, much slower", "tm", size=12)
    return d

@reg("nmj_chain", "Five channels from nerve to contraction",
     "Five channels open in a fixed order, and the last one floods the muscle cytosol with Ca2+.")
def _():
    d = D("nmj", 720, 290)
    bx = [(10, 30, "1. Voltage-gated Ca2+\nchannel (nerve terminal)\nACh is released", "fT"),
          (255, 30, "2. Nicotinic ACh receptor\n(cation channel)\nNa+ in, muscle depolarizes", "fT"),
          (500, 30, "3. Voltage-gated Na+\nchannels: muscle AP\nspreads into T tubules", "fT"),
          (500, 150, "4. T-tubule Ca2+ channel\nsenses the voltage\nand changes shape", "fA"),
          (255, 150, "5. SR Ca2+-release\nchannel opens:\nCa2+ floods cytosol", "fA"),
          (10, 150, "Ca2+ binds troponin,\ntropomyosin moves,\nmyosin grabs actin", "fO")]
    for x, y, t, c in bx:
        d.box(x, y, 210, 76, t, c, size=13)
    d.arrow(220, 68, 253, 68); d.arrow(465, 68, 498, 68); d.arrow(605, 106, 605, 148)
    d.arrow(500, 188, 467, 188); d.arrow(255, 188, 222, 188)
    d.text(360, 262, "Contraction ends when Ca2+ is pumped back into the SR.", "tm", size=13)
    return d
