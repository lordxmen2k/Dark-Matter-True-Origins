#!/usr/bin/env python3
"""
Computed figures for "Dark Matter: Its True Origins, Whether We Have Already
Tapped It, and Why the Answer Matters".

This script owns the seven computed charts. The three schematic diagrams are
drawn by make_diagrams.py, which owns them; keeping one generator per
figure is the point.

Every curve that represents a published result is anchored to the published
number, and the anchors are named in the code beside the curve. Where a
curve is illustrative rather than measured -- the neutrino fog, the
candidate map -- the caption says so.

Output: vector PDF into ../figures/
"""
import math
import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

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

plt.rcParams.update({
    "figure.facecolor": BG,
    "axes.facecolor": BG,
    "savefig.facecolor": BG,
    "text.color": TXT,
    "axes.labelcolor": TXTDIM,
    "xtick.color": TXTDIM,
    "ytick.color": TXTDIM,
    "axes.edgecolor": EDGE,
    "grid.color": EDGE,
    "font.family": "DejaVu Sans",
    "font.size": 8,
    "axes.titlesize": 9,
    "axes.titleweight": "bold",
    "axes.titlecolor": TXT,
    "figure.dpi": 200,
    "pdf.fonttype": 42,
})

W = 4.6   # text width in inches


def save(fig, name):
    p = OUT / name
    fig.savefig(p, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    print("wrote", p)


# =====================================================================
# 1. The cosmic energy budget
# =====================================================================
def fig_budget():
    fig, ax = plt.subplots(figsize=(W, 2.05))
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.08, 1.16)
    ax.axis("off")

    de, dm, ba = 68.5, 26.8, 4.9
    ax.add_patch(Rectangle((0, 0.58), de, 0.30, facecolor=ACCENT,
                           edgecolor=BG, lw=1.2))
    ax.add_patch(Rectangle((de, 0.58), dm, 0.30, facecolor=AMBER,
                           edgecolor=BG, lw=1.2))
    ax.add_patch(Rectangle((de + dm, 0.58), ba, 0.30, facecolor=EDGE,
                           edgecolor=BG, lw=1.2))

    ax.text(de / 2, 0.73, "Dark energy\n68.5%", ha="center", va="center",
            fontsize=8.4, color=BG, weight="bold")
    ax.text(de + dm / 2, 0.73, "Dark matter\n26.8%", ha="center", va="center",
            fontsize=7.6, color=BG, weight="bold")
    ax.annotate("baryons 4.9%",
                xy=(de + dm + ba / 2, 0.90), xytext=(de + dm - 6.0, 1.06),
                fontsize=6.4, color=TXTDIM, ha="center",
                arrowprops=dict(arrowstyle="-", color=TXTDIM, lw=0.6))

    # the matter breakdown
    ax.text(0, 0.40, "Within matter (100%):", fontsize=7.4, color=TXTDIM,
            va="center")
    ax.add_patch(Rectangle((0, 0.14), 84.0, 0.20, facecolor=AMBER,
                           edgecolor=BG, lw=1.0))
    ax.add_patch(Rectangle((84.0, 0.14), 16.0, 0.20, facecolor=EDGE,
                           edgecolor=BG, lw=1.0))
    ax.text(42, 0.24, "dark matter  84%", ha="center", va="center",
            fontsize=7.4, color=BG, weight="bold")
    ax.text(92, 0.24, "baryons\n16%", ha="center", va="center",
            fontsize=5.6, color=TXT, weight="bold")

    ax.text(0, 0.02, "Planck 2018:  " + r"$\Omega_c h^2 = 0.1200 \pm 0.0012$"
            "     " + r"$\Omega_b h^2 = 0.0224 \pm 0.0001$",
            fontsize=7.2, color=TXTDIM, va="center")
    save(fig, "fig_budget.pdf")


# =====================================================================
# 2. Central density profiles: cusp, core, soliton
# =====================================================================
def fig_smallscale():
    fig, ax = plt.subplots(figsize=(W, 2.55))
    r = np.logspace(-1, 3, 600)          # parsec
    rs = 100.0                            # scale radius, parsec

    # NFW cusp: rho ~ 1/(r (r+rs)^2)
    nfw = 1.0 / (r * (r + rs) ** 2)
    nfw = nfw / nfw.max()

    # cored profile: flat inside, then r^-3
    core = np.where(r < 40, 1.0, (40.0 / r) ** 3)
    core = core / core.max()

    # soliton: 1/r^4 with a regularised core
    sol = 1.0 / (r ** 4 + (2.0 ** 4))
    sol = sol / sol.max()

    ax.loglog(r, nfw, color=ACCENT, lw=1.6, label="cusp  (collisionless particles)")
    ax.loglog(r, core, color=TXTDIM, lw=1.4, ls="--",
              label="core  (baryonic feedback)")
    ax.loglog(r, sol, color=AMBER, lw=1.6, label="soliton  (light field)")

    ax.axvspan(50, 400, color=ACCENT, alpha=0.07)
    ax.axvline(120, color=ACCENTDIM, lw=0.7, ls=":")
    ax.text(150, 2.6, "the discriminating\nregion", fontsize=6.6,
            color=ACCENTDIM, va="top")
    ax.annotate("MW soliton mass\n" + r"$\sim 10^{9}\,M_\odot$",
                xy=(30, sol[np.argmin(np.abs(r - 30))]), xytext=(0.35, 0.28),
                fontsize=6.4, color=AMBER,
                arrowprops=dict(arrowstyle="-", color=AMBER, lw=0.7))

    ax.set_xlabel("radius  r  [pc]")
    ax.set_ylabel(r"normalised density  $\rho(r)$")
    ax.set_title("Central density profiles of a dark matter halo")
    ax.set_xlim(0.1, 1000)
    ax.set_ylim(1e-4, 4)
    ax.grid(True, which="both", alpha=0.22, lw=0.4)
    ax.legend(fontsize=6.4, loc="lower left", frameon=False, labelcolor=TXT)
    save(fig, "fig_smallscale.pdf")


# =====================================================================
# 3. The direct-detection frontier and the neutrino fog
# =====================================================================
def _limit(m, m0, s0, slope_lo=0.62, slope_hi=0.10):
    """A smooth limit curve anchored at (m0, s0)."""
    lm = np.log10(m)
    l0 = np.log10(m0)
    out = np.where(lm <= l0,
                   np.log10(s0) + slope_lo * np.abs(l0 - lm) ** 1.5,
                   np.log10(s0) + slope_hi * (lm - l0))
    return 10.0 ** out


def fig_exclusions():
    fig, ax = plt.subplots(figsize=(W, 2.75))
    m = np.logspace(0.0, 4.0, 500)

    # published anchors
    lz = _limit(m, 40, 2.2e-48)
    xen = _limit(m, 30, 1.7e-47)
    pdx = _limit(m, 40, 3.0e-48)
    xlzd = _limit(m, 40, 3.0e-49)

    # The fog: schematic. Its exact shape depends on the target, the
    # exposure and the neutrino flux model; it is drawn here with a
    # minimum near 40 GeV, just above the current limit, and it rises
    # steeply towards lower masses.
    lf = np.log10(m)
    fog = np.where(lf < 1.602, -48.3 - 0.90 * (1.602 - lf),
                   -48.3 + 0.28 * (lf - 1.602))
    fog = 10.0 ** fog

    ax.fill_between(m, 1e-52, fog, color=AMBER, alpha=0.10)
    ax.plot(m, fog, color=AMBER, lw=1.2, ls="--")
    ax.text(1.2, 6e-50, "neutrino fog\n(schematic)", fontsize=6.4, color=AMBER)

    ax.plot(m, lz, color=ACCENT, lw=1.6, label="LZ, 4.2 t$\\cdot$yr")
    ax.plot(m, xen, color=TXT, lw=1.2, label="XENONnT, 3.1 t$\\cdot$yr")
    ax.plot(m, pdx, color=TXTDIM, lw=1.2, ls="-.", label="PandaX-4T, 1.54 t$\\cdot$yr")
    ax.plot(m, xlzd, color=ACCENTDIM, lw=1.3, ls=":", label="projected XLZD reach")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1, 1e4)
    ax.set_ylim(1e-52, 1e-44)
    ax.set_xlabel(r"mass  $m_\chi$  [GeV]")
    ax.set_ylabel(r"spin-independent cross section  $\sigma_{\rm SI}$  [cm$^2$]")
    ax.set_title("The exclusion frontier at the end of 2026")
    ax.grid(True, which="major", alpha=0.25, lw=0.4)
    ax.legend(fontsize=6.0, loc="lower left", frameon=False, labelcolor=TXT,
              ncol=2, handlelength=1.8, columnspacing=1.2)
    ax.text(2.2, 2.6e-45, "excluded", fontsize=6.6, color=TXTDIM, ha="center")
    save(fig, "fig_exclusions.pdf")


# =====================================================================
# 4. The 248 keV candidate: local significance and the look-elsewhere factor
# =====================================================================
def fig_event248():
    fig, axes = plt.subplots(1, 2, figsize=(W, 2.25))

    # (a) the null distribution of local significance
    ax = axes[0]
    z = np.linspace(0, 6, 800)
    pdf = np.exp(-0.5 * z ** 2) / math.sqrt(2 * math.pi)
    ax.plot(z, pdf, color=TXTDIM, lw=1.3)
    ax.fill_between(z, 0, pdf, where=(z >= 5), color=ACCENT, alpha=0.16)
    ax.axvline(5.0, color=ACCENT, lw=1.2, ls="--")
    ax.axvline(3.4, color=AMBER, lw=1.4)
    ax.text(3.4, 0.42, "  3.4$\\sigma$ local\n  (LZ candidate)", fontsize=6.2,
            color=AMBER, va="top")
    ax.text(5.0, 0.16, "5$\\sigma$\nthreshold", fontsize=6.2, color=ACCENT,
            ha="center")
    ax.set_xlabel("local significance")
    ax.set_ylabel("null density")
    ax.set_title("Discovery threshold", fontsize=8)
    ax.set_xlim(0, 6.2)
    ax.set_ylim(0, 0.45)
    ax.grid(True, alpha=0.22, lw=0.4)

    # (b) expected maximum local significance against the number of trials
    ax = axes[1]
    N = np.logspace(0, 3.6, 400)
    zmax = np.sqrt(2.0 * np.log(N))      # expected maximum of N Gaussians
    ax.plot(N, zmax, color=ACCENT, lw=1.5)
    ax.axvline(293, color=TXTDIM, lw=1.0, ls=":")
    ax.axhline(3.4, color=AMBER, lw=1.2)
    ax.plot([293], [math.sqrt(2 * math.log(293))], "o", color=AMBER, ms=4.5)
    ax.text(300, 2.55, "293 spectra\nsearched", fontsize=6.2, color=TXTDIM)
    ax.text(1.4, 3.52, "observed local significance 3.4$\\sigma$",
            fontsize=6.0, color=AMBER)
    ax.set_xscale("log")
    ax.set_xlabel("number of windows searched")
    ax.set_ylabel("expected maximum significance")
    ax.set_title("Look-elsewhere factor", fontsize=8)
    ax.set_xlim(1, 5e3)
    ax.set_ylim(0, 4.3)
    ax.grid(True, alpha=0.22, lw=0.4)

    fig.subplots_adjust(wspace=0.38)
    save(fig, "fig_event248.pdf")


# =====================================================================
# 5. The candidate mass landscape
# =====================================================================
def fig_candidates():
    fig = plt.figure(figsize=(W, 3.4))
    ax = fig.add_axes([0.10, 0.47, 0.87, 0.44])

    ax.axvspan(0.5, 4.0, color=RED, alpha=0.12, zorder=0)
    ax.text(2.25, 3.58, "excluded for the standard coupling",
            fontsize=5.6, color=RED, ha="center")

    items = [
        (3, -25.0, -19.5, "1", ACCENT),
        (3, -15.0, -11.0, "2", ACCENT),
        (2, -12.0, -6.0, "3", TXTDIM),
        (2, -5.0, -0.3, "4", TXTDIM),
        (1, -4.0, -0.6, "5", AMBER),
        (1, 0.5, 4.0, "6", RED),
        (0, -6.0, 3.0, "7", TXTDIM),
        (0, 6.0, 21.0, "8", TXTDIM),
    ]
    for y, a, b, num, col in items:
        ax.add_patch(Rectangle((a, y - 0.19), b - a, 0.38, facecolor=col,
                               edgecolor=BG, lw=0.8, alpha=0.9, zorder=3))
        ax.text((a + b) / 2, y, num, fontsize=7.0, color=BG, weight="bold",
                ha="center", va="center", zorder=4)

    ax.set_xlim(-25.0, 23.0)
    ax.set_ylim(-0.55, 3.85)
    ax.set_yticks([])
    ax.set_xticks(range(-24, 25, 4))
    ax.set_xticklabels([r"$10^{%d}$" % k for k in range(-24, 25, 4)],
                       fontsize=6.4)
    ax.set_xlabel(r"mass  $m$  [eV]", fontsize=7.2, labelpad=2)
    ax.grid(True, axis="x", alpha=0.18, lw=0.4, zorder=0)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.tick_params(axis="x", length=2, labelsize=6.4, pad=2)

    legend = [
        ("1", "ultralight field", "constrained", ACCENT),
        ("2", "QCD axion", "open", ACCENT),
        ("3", "sterile neutrino", "narrow window", TXTDIM),
        ("4", "SIMP", "constrained", TXTDIM),
        ("5", "light WIMP", "open", AMBER),
        ("6", "thermal relic", "excluded", RED),
        ("7", "freeze-in", "open", TXTDIM),
        ("8", "superheavy", "open", TXTDIM),
    ]
    for i, (num, name, status, col) in enumerate(legend):
        column = 0 if i < 4 else 1
        row = i % 4
        x = 0.02 + column * 0.505
        y = 0.375 - row * 0.058
        fig.text(x, y, num, fontsize=6.4, color=BG, weight="bold",
                 va="center",
                 bbox=dict(boxstyle="square,pad=0.16", fc=col, ec="none"))
        fig.text(x + 0.030, y, name, fontsize=6.3, color=TXT, weight="bold",
                 va="center")
        fig.text(x + 0.215, y, status, fontsize=6.1, color=col, va="center")

    fig.text(0.02, 0.025,
             "Primordial black holes are not on this axis: their masses are quoted in solar "
             "masses, and the surviving windows lie near $10^{-16}$ to $10^{-11}\\,M_\\odot$.",
             fontsize=5.7, color=TXTDIM)
    save(fig, "fig_candidates.pdf")


# =====================================================================
# 6. The dark matter wind and the velocity sensitivity of capture
# =====================================================================
def fig_wind():
    fig, axes = plt.subplots(1, 2, figsize=(W, 2.2))

    # (a) speed distribution of the halo, with the Sun's motion marked
    ax = axes[0]
    v = np.linspace(0, 700, 800)
    sigma = 220.0
    f = v ** 2 * np.exp(-3 * v ** 2 / (4 * sigma ** 2))
    f = f / np.trapezoid(f, v)
    ax.plot(v, f, color=ACCENT, lw=1.5, label="halo speed distribution")
    ax.fill_between(v, 0, f, color=ACCENT, alpha=0.12)
    ax.axvline(232, color=AMBER, lw=1.2, ls="--",
               label="Sun's orbital speed, 232")
    ax.axvline(300, color=TXT, lw=1.0, ls=":",
               label="net wind, $\\sim$300")
    ax.set_xlabel("speed  [km s$^{-1}$]")
    ax.set_ylabel("probability density")
    ax.set_title("The wind", fontsize=8, pad=9)
    ax.set_xlim(0, 700)
    ax.set_ylim(0, 0.0040)
    ax.grid(True, alpha=0.22, lw=0.4)
    ax.legend(fontsize=5.6, loc="upper left", bbox_to_anchor=(0.02, 0.99),
              frameon=False, labelcolor=TXT, handlelength=1.6)

    # (b) production rate against the threshold velocity
    #
    # The cross section for a gravitational scattering through more than 90
    # degrees scales as v^-4, and the halo speed distribution contributes a
    # factor v^2, so the integrand is v^-2 exp(-a v^2) and the rate is
    # dominated by the slowest particles that can be scattered in at all.
    ax = axes[1]
    from math import erfc
    v0 = np.logspace(np.log10(18), np.log10(160), 400)

    def rate(sig, thr):
        a = 3.0 / (4.0 * sig ** 2)
        return (np.exp(-a * thr ** 2) / thr
                - 0.5 * np.sqrt(np.pi * a) * np.vectorize(erfc)(np.sqrt(a) * thr))

    for sig, c in ((180.0, AMBER), (220.0, ACCENT), (260.0, TXTDIM)):
        r = rate(sig, v0) / rate(220.0, np.array([42.0]))[0]
        ax.plot(v0, r, color=c, lw=1.5,
                label=("$\\sigma$ = %d" % sig) if sig in (180.0, 260.0)
                else "$\\sigma$ = 220")
    ax.axvline(42, color=TXTDIM, lw=0.9, ls=":")
    ax.text(45, 2.6, "escape speed\nat 1 AU", fontsize=6.0, color=TXTDIM)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("threshold speed  [km s$^{-1}$]")
    ax.set_ylabel("relative production rate")
    ax.set_title("Threshold sensitivity", fontsize=8)
    ax.set_xlim(18, 160)
    ax.set_ylim(0.15, 4.0)
    ax.set_xticks([20, 30, 50, 80, 120])
    ax.set_xticklabels(["20", "30", "50", "80", "120"])
    ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())
    ax.grid(True, which="both", alpha=0.22, lw=0.4)
    ax.legend(fontsize=5.8, loc="lower left", frameon=False, labelcolor=TXT,
              handlelength=1.4)

    fig.subplots_adjust(wspace=0.40)
    save(fig, "fig_wind.pdf")


# =====================================================================
# 7. The energy scale comparison
# =====================================================================
def fig_energy():
    fig, ax = plt.subplots(figsize=(W, 2.35))
    items = [
        ("ADMX cavity, quantum limit", 1e-22, RED),
        ("personal consumption", 1e3, TXTDIM),
        ("world electricity", 3e16, TXTDIM),
        ("global primary energy", 6e20, TXTDIM),
        ("formal ALP conversion, $10^{-15}$ eV", 1.3e24, AMBER),
        ("solar luminosity", 3.8e26, ACCENT),
    ]
    y = np.arange(len(items))[::-1]
    xmin, xmax = -26.5, 27.4
    for (lab, val, col), yy in zip(items, y):
        ax.barh(yy, np.log10(val) - xmin, left=xmin, height=0.46, color=col,
                alpha=0.30, edgecolor="none")
        ax.plot([np.log10(val)], [yy], "o", color=col, ms=5.5)
        ax.text(np.log10(val) - 0.5, yy, lab, ha="right", va="center",
                fontsize=6.5, color=TXT)
    ax.set_yticks([])
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(-0.7, len(items) - 0.3)
    ax.set_xlabel(r"power  [W]      ($\log_{10}$ scale)")
    ax.set_title("Energy scales: dark matter and everything else", fontsize=8.2)
    ax.grid(True, axis="x", alpha=0.2, lw=0.4)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    save(fig, "fig_energy.pdf")


if __name__ == "__main__":
    fig_budget()
    fig_smallscale()
    fig_exclusions()
    fig_event248()
    fig_candidates()
    fig_wind()
    fig_energy()
    print("computed figures done")
