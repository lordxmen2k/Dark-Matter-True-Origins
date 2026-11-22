# Build Notes

**Title:** Dark Matter
**Subtitle:** Its True Origins, Whether We Have Already Tapped It, and Why the Answer Matters
**Author:** Gerald Enrique Nelson Mc Kenzie
**Publisher / imprint:** Tico Internet LLC
**Edition:** 2026 First Edition
**Licence:** Apache License 2.0
**DOI:** 10.5281/zenodo.24435288 (single field, `source/preamble.tex`, `\bookDOI`)
**Facts current as of:** 22 November 2026

---

## Extent

| | |
|---|---|
| Trim size | 6 × 9 in (432 × 648 pt) |
| Pages | 168 (166 numbered + full-bleed front and back covers) |
| File size | 1.5 MB |
| Word count | 33,101 (body, front matter and back matter, excluding the cover artwork and the LaTeX control words) |
| Chapters | 28, in 6 parts |
| Figures | 10 (7 computed charts, 3 diagrams) |
| Tables | 9 |
| Key Takeaways boxes | 27 |
| Deeper-dive boxes | 1 |
| Index headwords | 38 |
| Glossary terms | 50 |
| Fonts embedded | Outfit, DejaVu Sans Mono, Fira Math — all subsets, all embedded, no Type 3 |
| PDF bookmarks | 172 outline entries matching the table of contents |
| Link annotations | 433 |

### Structure

| Part | Chapters | Content |
|---|---|---|
| I | 1–4 | The budget, the five handles on the missing mass, the Bullet Cluster, the small-scale structure |
| II | 5–10 | The candidates one at a time: WIMP, axion, ultralight fields, primordial black holes, the long tail, modified gravity |
| III | 11–16 | The 2026 frontier: the Solar System as a laboratory, the exclusion frontier and the neutrino fog, the 248 keV candidate, the anomaly record, the cosmological probes, the cosmological tensions |
| IV | 17–19 | The origins: the relic-density constraint, the production mechanisms, and which origin is true |
| V | 20–24 | The five senses of tapping: the framework, gravity, capture, harvesting, quantum devices and the particle |
| VI | 25–28 | The decision: the portfolio, the candidate-by-candidate criteria, what a discovery would prove, the roadmap to 2040 |

---

## Build

```sh
./build.sh
```

The script installs the book fonts into fontconfig, counts the words in the
manuscript, regenerates the seven computed charts and the three diagrams,
typesets with XeLaTeX, builds the index with `makeindex`, refreshes the
colophon with the page and word counts, and copies the result to
`output/Dark-Matter.pdf`.

The covers are built separately by `build/make_covers.sh`, which prepares the
300 DPI plates and then sets the cover typography in LaTeX over them.

### Toolchain

| | |
|---|---|
| Engine | XeLaTeX (fontspec, unicode-math, TikZ, pgfplots) |
| Text face | Outfit |
| Code face | DejaVu Sans Mono |
| Math face | Fira Math (single weight, from the system TeX Live tree) |
| Index | makeindex |
| Figures | matplotlib 3.10 (computed), hand-drawn inch-coordinate diagrams |
| Plates | Pillow 12 for the 300 DPI cover preparation |

### One generator per artefact

- `build/make_figures.py` owns the seven computed charts: the energy budget,
  the density profiles, the exclusion frontier, the 248 keV significance
  structure, the candidate landscape, the wind and the energy scales.
- `build/make_diagrams.py` owns the three diagrams: the five handles, the
  five detection channels and the roadmap.
- `build/make_cover_art.py` owns the two cover plates.

No artefact has two generators, so no stale copy can overwrite a good one.
Every figure is rendered and looked at before it is accepted; three rounds of
correction were needed on the candidate landscape, the wind and the cover
scrim.

---

## Verification

Run against the log of the final build:

| Gate | Result |
|---|---|
| LaTeX errors | 0 |
| LaTeX warnings (grep `Warning` alone, not a prefix) | 0 |
| Undefined references | 0 |
| Missing characters | 0 |
| Overfull boxes over 25 pt | 0 (no overfull box of any size) |
| Blank pages | 0 |
| Words outside the physical page | 0 |
| Fonts embedded | all, no Type 3 |
| Outline matches the contents | 172 entries |
| Figures inspected in place | 10 of 10 |

Underfull boxes remain (85, nearly all in narrow table cells). They are
a cosmetic consequence of fixed-width table columns with short last lines
and do not affect the printed result.

---

## Sources

Every identifier used in the book was resolved against the arXiv API, the
Crossref bibliographic query API or INSPIRE-HEP while the book was written,
and the resolved title was compared against the paper it was intended to
cite. `research/source_ledger.md` is the record of that process, including
the four errors it caught and the three claims it removed for want of a
primary source. The resolvers are in `research/scripts/`.

---

## Repository

`github.com/lordxmen2k/Dark-Matter-True-Origins` (private, branch `main`).
The DOI appears in seven places and must be changed together if it is ever
reassigned: `source/preamble.tex` (`\bookDOI`), the copyright page, the
colophon, the cover artwork, the README, `ZENODO_METADATA.md` and this file.

The cover artwork is generated, not photographed, and is committed as
`figures/cover_art.jpg` so that the cover can be rebuilt without a
generation service.
