#!/usr/bin/env python3
"""Prepare the cover plates and the legibility scrims.

Both plates are 6 x 9 in at 300 DPI (1800 x 2700 px), saved as JPEG so that
LaTeX embeds them as DCTDecode rather than as raw RGB. The front uses the
whole artwork; the back uses a different crop so it is not a repeat.

The scrim is the alpha ramp that keeps the cover type legible over the
artwork. It is baked into the plate here rather than drawn in the cover
document, so that the finished cover carries one raster image and vector
type, and no hundreds of vector rectangles.
"""
import pathlib

from PIL import Image, ImageEnhance

HERE = pathlib.Path(__file__).resolve().parent
FIG = HERE.parent / "figures"
SRC = FIG / "cover_art.jpg"
DPI = 300
W, H = 6 * DPI, 9 * DPI

FIG.mkdir(parents=True, exist_ok=True)

im = Image.open(SRC).convert("RGB")
# A mild lift before the scrim, so that the plate keeps its luminosity
# instead of being flattened to black by the legibility ramp.
im = ImageEnhance.Brightness(im).enhance(1.45)
im = ImageEnhance.Color(im).enhance(1.15)
w, h = im.size

# Alpha at the given height in inches from the foot of the page.
#
# The front keeps the gold band clear between about 3.1 and 4.2 inches,
# darkens the lower third so that the credits sit on ink, and lifts the
# upper region slightly so that the title block reads as part of the
# image rather than as type pasted onto it.
FRONT_STOPS = [(0.00, 0.90), (0.80, 0.88), (1.80, 0.86), (2.45, 0.78),
               (3.10, 0.40), (3.80, 0.12), (4.40, 0.02), (5.20, 0.05),
               (6.60, 0.10), (7.80, 0.14), (9.00, 0.16)]

# The back crop is mostly star field with the band entering at the foot,
# so it needs a lighter, flatter scrim.
BACK_STOPS = [(0.00, 0.88), (1.60, 0.80), (3.40, 0.60), (5.20, 0.44),
              (7.00, 0.36), (9.00, 0.34)]

INK = (0x0B, 0x0E, 0x1A)


def ramp(stops, y):
    """Alpha at height y (inches from the foot) for a list of (y, alpha) stops."""
    if y <= stops[0][0]:
        return stops[0][1]
    if y >= stops[-1][0]:
        return stops[-1][1]
    for (y0, a0), (y1, a1) in zip(stops[:-1], stops[1:]):
        if y0 <= y <= y1:
            return a0 + (a1 - a0) * (y - y0) / (y1 - y0)
    return stops[-1][1]


def scrim(plate, stops):
    """Bake the legibility ramp into the plate."""
    import numpy as np
    a = np.asarray(plate).astype("float32")
    h = a.shape[0]
    ys = (1.0 - np.arange(h) / h) * 9.0        # inches from the foot
    alphas = np.array([ramp(stops, float(y)) for y in ys], dtype="float32")
    alphas = alphas[:, None, None]
    ink = np.array(INK, dtype="float32")[None, None, :]
    out = a * (1.0 - alphas) + ink * alphas
    return Image.fromarray(out.clip(0, 255).astype("uint8"))


front = scrim(im.resize((W, H), Image.BICUBIC), FRONT_STOPS)
front.save(FIG / "cover_front_art.jpg", "JPEG", quality=86, optimize=True,
           progressive=True, subsampling=1)

back = im.crop((int(w * 0.00), int(h * 0.26), int(w * 0.66), int(h * 1.00)))
back = scrim(back.resize((W, H), Image.BICUBIC), BACK_STOPS)
back.save(FIG / "cover_back_art.jpg", "JPEG", quality=86, optimize=True,
          progressive=True, subsampling=1)

for p in (FIG / "cover_front_art.jpg", FIG / "cover_back_art.jpg"):
    print(f"wrote {p}  ({p.stat().st_size // 1024} KB)")
