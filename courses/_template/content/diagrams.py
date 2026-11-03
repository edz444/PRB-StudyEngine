"""SVG diagrams for {{fig:name}} markers. Colors come from CSS classes (fT teal, fO orange, fA amber, fG grey), so they work in light and dark."""
from dlib import D

FIGS = {}

def reg(name, title, caption):
    def deco(fn):
        FIGS[name] = (fn().svg(title), caption)
        return fn
    return deco

@reg("wall", "The membrane as a wall with doors", "Small greasy molecules slip through the wall; ions need a protein door.")
def _():
    d = D("wall", 600, 220)
    d.membrane(110, label="membrane")
    d.box(250, 92, 60, 54, "door", "fT", size=13)
    d.text(120, 40, "oxygen slips through", "t", size=14)
    d.arrow(120, 55, 120, 165)
    d.text(420, 40, "Na+ needs the door", "t", size=14)
    d.arrow(380, 55, 300, 100)
    return d
