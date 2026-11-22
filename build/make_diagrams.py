#!/usr/bin/env python3
"""
Diagram figures for "Dark Matter: Its True Origins, Whether We Have Already
Tapped It, and Why the Answer Matters", drawn at true print size.

The three diagram figures are laid out in INCH coordinates on a 4.6 x H inch
canvas, which is the exact text width of the 6 x 9 trim. They are therefore
included at \\textwidth with no scaling, so every label is at its stated
point size in the finished book.

The seven chart figures are computed and sized to the same text width; they
are owned by make_figures.py.
"""
import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)

BG = "#0B0E1A"
PANEL = "#151A2B"
EDGE = "#2B3450"
ACCENT = "#F0C36A"
ACCENTDIM = "#8E7738"
TXT = "#E8EAF0"
TXTDIM = "#98A0B0"
AMBER = "#7FA8D4"
RED = "#C9705A"

W = 4.6

plt.rcParams.update({
    "figure.facecolor": BG,
    "axes.facecolor": BG,
    "savefig.facecolor": BG,
    "text.color": TXT,
    "font.family": "DejaVu Sans",
    "font.size": 8,
    "figure.dpi": 200,
    "pdf.fonttype": 42,
})



def canvas(h):
    fig, ax = plt.subplots(figsize=(W, h))
    ax.set_xlim(0, W)
    ax.set_ylim(0, h)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    return fig, ax


def save(fig, name):
    p = OUT / name
    fig.savefig(p, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    print("wrote", p)


def box(ax, x, y, w, h, fc=PANEL, ec=EDGE, lw=0.7, r=0.03):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0,rounding_size=%f" % r,
                                facecolor=fc, edgecolor=ec, linewidth=lw))


def label(ax, x, y, s, size=6.6, color=TXT, weight="normal", ha="left",
          va="center"):
    ax.text(x, y, s, fontsize=size, color=color, ha=ha, va=va,
            weight=weight, linespacing=1.35)


# =====================================================================
# 1. The five handles on the missing mass
# =====================================================================
def fig_handles():
    H = 3.30
    fig, ax = canvas(H)

    rows = [
        ("Rotation curves", "the force on the stars in a disc"),
        ("Cluster dynamics", "the motion of member galaxies"),
        ("Gravitational lensing", "the bending of background light"),
        ("CMB acoustic peaks", "the oscillation of the fluid"),
        ("Baryon acoustic\noscillations", "the ruler in galaxy clustering"),
    ]
    top, bot = 2.34, 0.74
    step = (top - bot) / 4.0
    bh = 0.48

    for i, (name, route) in enumerate(rows):
        y = top - i * step
        box(ax, 0.04, y, 1.40, bh)
        label(ax, 0.13, y + bh / 2, name, size=6.2, color=ACCENT,
              weight="bold")
        label(ax, 1.54, y + bh / 2, route, size=6.3, color=TXTDIM)
        ax.plot([3.12, 3.24], [y + bh / 2, y + bh / 2], color=EDGE, lw=0.7)

    bx = 3.24
    ax.plot([bx, bx], [top + bh / 2, bot + bh / 2], color=ACCENT, lw=1.0)
    ax.plot([bx, bx + 0.10], [top + bh / 2, top + bh / 2], color=ACCENT, lw=1.0)
    ax.plot([bx, bx + 0.10], [bot + bh / 2, bot + bh / 2], color=ACCENT, lw=1.0)
    ax.plot([bx + 0.10, bx + 0.26], [top + bh / 2, top + bh / 2],
            color=ACCENT, lw=1.0)
    ax.plot([bx + 0.10, bx + 0.26], [bot + bh / 2, bot + bh / 2],
            color=ACCENT, lw=1.0)

    box(ax, bx + 0.26, 1.16, 0.98, 1.06, fc=PANEL, ec=ACCENT, lw=0.9)
    label(ax, bx + 0.75, 1.96, "all five", size=6.2, color=TXTDIM, ha="center")
    label(ax, bx + 0.75, 1.72, r"$\Omega_c h^2$", size=9.0, color=TXT,
          ha="center", weight="bold")
    label(ax, bx + 0.75, 1.48, "= 0.1200", size=7.0, color=ACCENT,
          ha="center")
    label(ax, bx + 0.75, 1.30, r"$\pm\,0.0012$", size=6.4, color=TXTDIM,
          ha="center")

    label(ax, 0.04, H - 0.16, "Five independent routes to the same number",
          size=8.2, color=TXT, weight="bold")
    label(ax, 0.04, 0.22,
          "Different instruments, different physics, different assumptions.",
          size=6.2, color=TXTDIM)
    save(fig, "fig_handles.pdf")


# =====================================================================
# 2. The detection channels
# =====================================================================
def fig_channels():
    H = 3.30
    fig, ax = canvas(H)

    cx, cy, r = 2.30, 1.55, 0.42
    ax.add_patch(Circle((cx, cy), r, facecolor=PANEL, edgecolor=ACCENT,
                        lw=1.0))
    label(ax, cx, cy + 0.08, "dark", size=7.0, color=ACCENT, ha="center",
          weight="bold")
    label(ax, cx, cy - 0.10, "matter", size=7.0, color=ACCENT, ha="center",
          weight="bold")

    channels = [
        (1.30, 2.40, "Direct detection", "nuclear and electron recoils\nin a cryogenic target", ACCENT),
        (3.30, 2.40, "Indirect detection", "annihilation products:\ngamma rays, positrons, neutrinos", AMBER),
        (0.95, 1.55, "Cosmology", "CMB peaks, BAO,\nlarge-scale structure", ACCENT),
        (3.65, 1.55, "Astrophysics", "rotation curves, lensing,\ndwarf dynamics", AMBER),
        (2.30, 0.42, "Laboratory field", "quantum devices,\naxion conversion", ACCENT),
    ]
    bw, bh = 1.78, 0.70
    for x, y, name, route, col in channels:
        box(ax, x - bw / 2, y - bh / 2, bw, bh, ec=col, lw=0.8)
        label(ax, x, y + 0.20, name, size=6.8, color=col, ha="center",
              weight="bold")
        label(ax, x, y - 0.11, route, size=5.6, color=TXTDIM, ha="center")
        ax.add_patch(FancyArrowPatch((x, y), (cx, cy),
                                     arrowstyle="-", color=EDGE, lw=0.7,
                                     shrinkA=0, shrinkB=r + 0.02,
                                     connectionstyle="arc3,rad=0"))

    label(ax, 0.04, H - 0.16, "The five ways dark matter is looked for",
          size=8.2, color=TXT, weight="bold")
    label(ax, 0.04, 0.06,
          "Each channel has a different bottleneck; no single one covers the space.",
          size=5.9, color=TXTDIM)
    save(fig, "fig_channels.pdf")


# =====================================================================
# 3. The roadmap to 2040
# =====================================================================
def fig_roadmap():
    H = 3.62
    fig, ax = canvas(H)

    x0, x1 = 0.92, 4.50
    years = [2027, 2030, 2035, 2040]

    def xpos(year):
        return x0 + (year - 2027) / 13.0 * (x1 - x0)

    ax.plot([x0, x1], [2.92, 2.92], color=EDGE, lw=0.9)
    for yr in years:
        ax.plot([xpos(yr), xpos(yr)], [2.86, 2.98], color=EDGE, lw=0.9)
        label(ax, xpos(yr), 3.08, str(yr), size=6.4, color=TXTDIM, ha="center")

    phases = [
        (2027, 2032, "next generation", ACCENT),
        (2032, 2036, "diversification", AMBER),
        (2036, 2040, "the decision", ACCENT),
    ]
    for a, b, name, col in phases:
        ax.add_patch(Rectangle((xpos(a), 2.58), xpos(b) - xpos(a), 0.17,
                               facecolor=col, edgecolor="none", alpha=0.88))
        label(ax, (xpos(a) + xpos(b)) / 2, 2.665, name, size=5.8, color=BG,
              ha="center", weight="bold")

    rows = [
        ("Detectors", [
            (2027, 2032, "XLZD,\nDarkSide-20k", ACCENT),
            (2032, 2037, "light targets,\nelectron recoils", AMBER),
            (2037, 2040, "beyond\nthe fog", ACCENT),
        ]),
        ("The sky", [
            (2027, 2032, "DESI, Euclid,\nRubin", ACCENT),
            (2032, 2037, "dwarf census,\nhalo profiles", AMBER),
            (2037, 2040, "structure\nresolved", ACCENT),
        ]),
        ("Early universe", [
            (2027, 2032, "primordial\nspectrum", ACCENT),
            (2032, 2038, "spectral\ndistortions", AMBER),
            (2038, 2040, "thermal\nhistory", ACCENT),
        ]),
        ("Devices", [
            (2028, 2033, "quantum\nsensors", AMBER),
            (2033, 2038, "directional\ndetection", AMBER),
            (2038, 2040, "field\nmeasurement", ACCENT),
        ]),
    ]

    y = 2.22
    for name, items in rows:
        label(ax, 0.04, y + 0.14, name, size=6.6, color=TXT, weight="bold")
        for a, b, txt, col in items:
            ax.add_patch(FancyBboxPatch((xpos(a), y - 0.04),
                                        xpos(b) - xpos(a), 0.40,
                                        boxstyle="round,pad=0,rounding_size=0.04",
                                        facecolor=PANEL, edgecolor=col,
                                        linewidth=0.8))
            label(ax, (xpos(a) + xpos(b)) / 2, y + 0.16, txt, size=5.2,
                  color=col, ha="center")
        y -= 0.52

    xd = xpos(2036)
    ax.plot([xd, xd], [0.44, 2.92], color=ACCENT, lw=0.9, ls=":")
    label(ax, xd - 0.08, 0.32, "the decision point", size=6.2, color=ACCENT,
          ha="right")

    label(ax, 0.04, H - 0.14, "The schedule, 2027 to 2040", size=8.2,
          color=TXT, weight="bold")
    label(ax, 0.04, 0.08,
          "Kill conditions are attached to every branch; the reserve for unexplored "
          "candidates is not shown.",
          size=5.8, color=TXTDIM)
    save(fig, "fig_roadmap.pdf")


if __name__ == "__main__":
    fig_handles()
    fig_channels()
    fig_roadmap()
    print("diagrams done")
