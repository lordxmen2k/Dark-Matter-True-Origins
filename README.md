# Dark Matter: Its True Origins, Whether We Have Already Tapped It, and Why the Answer Matters

Gerald Enrique Nelson Mc Kenzie — Tico Internet LLC
2026 First Edition · Apache License 2.0 · DOI 10.5281/zenodo.24435288

A bleeding-edge assessment of where dark matter physics stands as of late 2026, what the
evidence actually supports, and what should be built, funded and decided next.

## Contents

```
source/          the LaTeX manuscript
  preamble.tex   identity, design tokens, page furniture
  frontmatter.tex, body.tex, backmatter.tex
  chapters/      ch01.tex .. chNN.tex
figures/         cover_front, cover_back, and the book's figures
build/           figure, cover, index and repair scripts
research/        source ledger, corrections log, research log,
                 literature verification, and the identifier-resolution scripts
output/          the finished PDF
```

## Building

```sh
./build.sh
```

Requires XeLaTeX, `makeindex`, Python 3 with matplotlib and Pillow, and the fonts in
`fonts/`.

## The research materials

`research/source_ledger.md` is the evidentiary record behind the book: every source
relied on, with its identifier, what it supports, and its verification status. The
identifiers in it were resolved against the arXiv API, the Crossref bibliographic query
API and INSPIRE-HEP, and each resolved title was compared with the intended paper.

## Licence

Apache License 2.0. The complete text is at
<https://www.apache.org/licenses/LICENSE-2.0>.
