"""SVG diagrams for {{fig:name}} markers. Colours come from CSS classes (fT teal, fO orange, fA amber, fG grey)."""
from dlib import D

FIGS = {}

def reg(name, title, caption):
    def deco(fn):
        FIGS[name] = (fn().svg(title), caption)
        return fn
    return deco


@reg("pipeline", "The term in one picture", "Each box is a week's technique; each arrow sets up the next readout.")
def _():
    d = D("pipeline", 560, 420)
    d.box(10, 20, 160, 56, "Grow + count\ncells (W1)", "fT", size=13)
    d.box(200, 20, 160, 56, "See cells\nW2", "fT", size=13)
    d.box(390, 20, 160, 56, "Transfect\nW3-4", "fO", size=13)
    d.arrow(170, 48, 198, 48); d.arrow(360, 48, 388, 48)
    d.arrow(470, 76, 220, 120); d.arrow(470, 76, 470, 120)
    d.box(120, 124, 200, 56, "Fix, stain, image\nHoechst/GFP/actin (W6)", "fT", size=12)
    d.box(350, 124, 200, 56, "Extract RNA, cDNA\nspin column, RT (W5)", "fT", size=12)
    d.arrow(220, 180, 220, 214); d.arrow(450, 180, 450, 214)
    d.box(350, 218, 200, 52, "ddPCR\ncount transcripts (W7-8)", "fT", size=12)
    d.box(120, 218, 200, 120, "Structural readout\n% GFP-positive\n(transfection efficiency)\nActin: parallel fibres?", "fG", size=12)
    d.arrow(450, 270, 450, 300)
    d.box(350, 304, 200, 52, "Molecular readout\ntarget / housekeeping", "fG", size=12)
    return d


@reg("hemo", "The hemocytometer calculation", "Average, convert to cells per mL, then divide what you need by what you have.")
def _():
    d = D("hemo", 560, 170)
    d.box(10, 24, 160, 120, "1. Average\n\n87+91+83+85\n divide by 4\n\n= 86.5 /75 nL", "fT", size=13)
    d.arrow(170, 84, 192, 84)
    d.box(196, 24, 168, 120, "2. Concentration\n\n86.5 / 75 nL\nx 1,000,000\n\n= 1.153 x 10^6 /mL", "fT", size=13)
    d.arrow(364, 84, 386, 84)
    d.box(390, 24, 160, 120, "3. Volume\n\n400,000 cells\n/ 1.153e6 /mL\n\n= 347 uL", "fO", size=13)
    return d


@reg("myocd", "A gene with and without myocardin", "SRF is always on the CArG box; myocardin is the switch.")
def _():
    d = D("myocd", 560, 320)
    d.text(14, 20, "Without myocardin", "t", anchor="start", size=14, weight=700)
    d.line(14, 96, 300, 96, "ln"); d.box(70, 86, 60, 20, "CArG", "fA", size=11)
    d.ellipse(100, 70, 30, 16, "fG"); d.text(100, 70, "SRF", "t", size=12)
    d.box(210, 82, 150, 28, "contractile gene", "fT", size=12)
    d.text(300, 56, "little or no mRNA", "t", anchor="start", size=12)
    d.text(14, 150, "With myocardin", "t", anchor="start", size=14, weight=700)
    d.line(14, 236, 300, 236, "ln"); d.box(70, 226, 60, 20, "CArG", "fA", size=11)
    d.ellipse(100, 210, 30, 16, "fG"); d.text(100, 210, "SRF", "t", size=12)
    d.ellipse(150, 178, 46, 16, "fO"); d.text(150, 178, "Myocardin", "t", size=12)
    d.box(210, 222, 150, 28, "contractile gene", "fT", size=12)
    d.path("M300 236 q20 -10 40 0 t40 0 t40 0", "arO", head="o")
    d.text(470, 210, "lots of mRNA,\nmore protein", "t", size=12)
    return d


@reg("column", "The RNA spin column", "Until the elute step the RNA is stuck to the silica, so the flow-through is waste.")
def _():
    d = D("column", 560, 150)
    steps = [("Lyse", "break cells", "fG"), ("Bind", "RNA on silica", "fT"),
             ("Wash", "rinse junk", "fT"), ("Elute", "RNA out (KEEP)", "fO")]
    x = 10
    for i, (t, s, c) in enumerate(steps):
        d.box(x, 30, 120, 90, f"{t}\n\n{s}", c, size=13)
        if i < 3:
            d.arrow(x + 120, 75, x + 132, 75)
        x += 132
    return d


@reg("stain", "The staining order", "Permeabilize before phalloidin, because it cannot cross an intact membrane.")
def _():
    d = D("stain", 560, 230)
    d.box(10, 20, 110, 44, "Fix", "fT", size=13)
    d.arrow(65, 64, 65, 80)
    d.box(10, 84, 110, 40, "Wash", "fG", size=13)
    d.arrow(65, 124, 65, 140)
    d.box(10, 144, 110, 50, "Permeabilize", "fT", size=12)
    d.arrow(120, 169, 150, 169)
    d.box(154, 144, 120, 50, "Hoechst (blue)", "fT", size=12)
    d.arrow(274, 169, 300, 169)
    d.box(304, 144, 90, 50, "Wash", "fG", size=12)
    d.arrow(394, 169, 420, 169)
    d.box(424, 144, 126, 50, "Phalloidin (red)", "fO", size=12)
    d.text(300, 40, "Each wash removes unbound dye", "t", size=12)
    d.text(300, 60, "that would glow as background.", "t", size=12)
    return d


@reg("droplets", "One positive and one negative droplet", "At the end, only the droplet with target cDNA is bright.")
def _():
    d = D("droplets", 560, 260)
    d.text(150, 20, "Start of run", "t", size=13, weight=700)
    d.text(420, 20, "End of run", "t", size=13, weight=700)
    d.line(285, 36, 285, 250, "ln", dash=True)
    d.text(14, 90, "Positive", "t", anchor="start", size=13, weight=700)
    d.circle(170, 95, 46, "1 target\n+ reagents", "fG", size=11)
    d.circle(430, 95, 46, "lots of\nproduct", "fO", size=11)
    d.text(14, 205, "Negative", "t", anchor="start", size=13, weight=700)
    d.circle(170, 200, 38, "reagents\nonly", "fG", size=11)
    d.circle(430, 200, 38, "still dim", "fG", size=11)
    return d
