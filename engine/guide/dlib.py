"""Tiny SVG helper for theme-aware study diagrams.
All colours come from CSS classes defined in the page, so the same SVG works in light and dark."""
import html

class D:
    def __init__(self, name, w, h):
        self.name, self.w, self.h = name, w, h
        self.parts = []

    # primitives -------------------------------------------------------
    def raw(self, s):
        self.parts.append(s)

    def text(self, x, y, s, cls="t", anchor="middle", size=None, weight=None):
        lines = str(s).split("\n")
        st = []
        if size: st.append(f"font-size:{size}px")
        if weight: st.append(f"font-weight:{weight}")
        style = f' style="{";".join(st)}"' if st else ""
        lh = (size or 14) * 1.2
        y0 = y - (len(lines) - 1) * lh / 2
        for i, ln in enumerate(lines):
            self.parts.append(
                f'<text x="{x}" y="{y0 + i*lh:.1f}" class="{cls}" text-anchor="{anchor}" dominant-baseline="middle"{style}>{html.escape(ln)}</text>')

    def box(self, x, y, w, h, label="", cls="fT", rx=8, tcls="t", size=None, weight=None):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls} sk"/>')
        if label:
            self.text(x + w/2, y + h/2, label, tcls, size=size, weight=weight)

    def circle(self, cx, cy, r, label="", cls="fT", tcls="t", size=None):
        self.parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" class="{cls} sk"/>')
        if label:
            self.text(cx, cy, label, tcls, size=size)

    def ellipse(self, cx, cy, rx, ry, cls="fG"):
        self.parts.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" class="{cls} sk"/>')

    def line(self, x1, y1, x2, y2, cls="ln", dash=False):
        d = ' stroke-dasharray="5 4"' if dash else ""
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}"{d}/>')

    def arrow(self, x1, y1, x2, y2, cls="ar", dash=False, head="a"):
        d = ' stroke-dasharray="5 4"' if dash else ""
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}"{d} marker-end="url(#{self.name}-{head})"/>')

    def path(self, d, cls="ar", head="a", dash=False):
        m = f' marker-end="url(#{self.name}-{head})"' if head else ""
        dd = ' stroke-dasharray="5 4"' if dash else ""
        self.parts.append(f'<path d="{d}" class="{cls}" fill="none"{dd}{m}/>')

    def block(self, x1, y1, x2, y2, cls="arO"):
        """inhibition: line with flat bar end"""
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}" marker-end="url(#{self.name}-bar)"/>')

    def membrane(self, y, x0=10, x1=None, h=34, label="plasma membrane", lx=None):
        x1 = x1 if x1 is not None else self.w - 10
        self.parts.append(f'<rect x="{x0}" y="{y}" width="{x1-x0}" height="{h}" class="mem"/>')
        self.line(x0, y, x1, y, "memln"); self.line(x0, y + h, x1, y + h, "memln")
        if label:
            self.text(lx if lx else x1 - 6, y + h/2, label, "tm", anchor="end", size=12)

    def ion(self, cx, cy, label, cls="fA", r=11, size=11):
        self.circle(cx, cy, r, label, cls, size=size)

    def P(self, cx, cy):
        self.circle(cx, cy, 9, "P", "fO", size=11)

    def cross(self, cx, cy, s=9):
        self.parts.append(f'<path d="M{cx-s} {cy-s} L{cx+s} {cy+s} M{cx+s} {cy-s} L{cx-s} {cy+s}" class="xO"/>')

    def svg(self, title):
        n = self.name
        defs = (f'<defs>'
                f'<marker id="{n}-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" class="ahf"/></marker>'
                f'<marker id="{n}-o" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" class="ahfO"/></marker>'
                f'<marker id="{n}-t" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" class="ahfT"/></marker>'
                f'<marker id="{n}-bar" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M5 0 L5 10" class="barO"/></marker>'
                f'</defs>')
        return (f'<svg class="dg" viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{html.escape(title)}" xmlns="http://www.w3.org/2000/svg">'
                f'<title>{html.escape(title)}</title>{defs}' + "".join(self.parts) + '</svg>')
